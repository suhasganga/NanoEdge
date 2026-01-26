On this page

QuestDB's query optimizer automatically selects execution plans for SQL queries
based on heuristics. While the default execution strategy should be the fastest
for most scenarios, you can use hints to select a specific strategy that may
better suit your data's characteristics. SQL hints influence the execution
strategy of queries without changing their semantics.

## Hint Syntax[​](#hint-syntax "Direct link to Hint Syntax")

In QuestDB, you specify SQL hints in block comments with a plus sign after the
opening comment marker. You must place the hint immediately after the `SELECT`
keyword:

SQL hint syntax

```prism-code
SELECT /*+ HINT_NAME(parameter1 parameter2) */ columns FROM table;
```

Only block comment hints (`/*+ HINT */`) are supported, not line comment hints
(`--+ HINT`).

Hints are designed to be a safe optimization mechanism:

* without hints, QuestDB uses default optimization strategies
* QuestDB silently ignores unknown hints and those that don't apply to a query
* QuestDB silently ignores any syntax errors in a hint block

---

## Temporal JOIN hints[​](#temporal-join-hints "Direct link to Temporal JOIN hints")

A significant factor in choosing the optimal algorithm for a
[temporal join](/docs/query/sql/asof-join/) (ASOF and LT) is the pattern in
which the rows of the left-hand dataset are matched to the rows of the
right-hand dataset. When there's no additional join condition, only the implied
matching on timesatmp, the situation is simple: we search for a timestamp in a
dataset which is already sorted by timestamp. We can use binary search, or
linear search if the search space is small enough.

When there is an additional JOIN condition, as in
`left ASOF JOIN right ON (condition)`, the matching row can be anywhere in the
past from the row that matches by timestamp. For this, we need a more
sophisticated algorithm.

Our optimized algorithms assume the JOIN condition matches additional columns by
equality. Basically, there's a join key that must match on both sides. An even
narrower common case we optimize more aggressively for is matching on a *symbol
column* on both sides.

We distinguish these two cases:

### 1. Localized matching[​](#1-localized-matching "Direct link to 1. Localized matching")

In this case, when scanning the right-hand table backward from the timestamp of
the left-hand row, we find a match much sooner than reaching the timestamp of
the previous left-hand row. We end up scanning only a small subset of the
right-hand rows. In the diagram, we show the scanned portions of the right-hand
dataset in red.

The best way to perform this join is the straightforward one: first locate the
right-hand row that matches by timestamp (marked with the dotted line), then
scan backward to find the row satisfying additional join conditions.

![Diagram showing localized row matching](/docs/images/docs/concepts/asof-join-sparse.svg)

### 2. Distant matching[​](#2-distant-matching "Direct link to 2. Distant matching")

In this case, the matching row is in the more distant past, earlier than the
previous left-hand row. The scanning ranges now ovelap, and we end up scanning
almost the entire right-hand dataset. If we do a separate scan for each
left-hand row, we'll end up going over the same rows many times. In the diagram,
this shows up as more intensely red regions in the right-hand table.

The best way in this case is to scan the entire red region once, collect the
join keys in a hashtable, and match up with the left-hand rows as needed.

![Diagram showing distant row matching](/docs/images/docs/concepts/asof-join-dense.svg)

## ASOF JOIN algorithms[​](#asof-join-algorithms "Direct link to ASOF JOIN algorithms")

QuestDB implements several algorithms to deal with keyed joins.

* *Fast* algorithm is the best for localized row matching
* *Dense* algorithm is the best for distant row matching

In a real scenario, you may not have such a clear-cut situation. If your join
pattern is mostly localized, but with some distant matching, the *Memoized*
algorithm may help. It remembers where the previous match was for a given join
key, and can avoid rescanning to find it.

When you use a WHERE clause on the right-hand dataset, and if it's highly
selective (passing through a small fraction of rows), the *Light* algorithm may
be the best. It is the only one that allows QuestDB to use its parallelized
filtering to quickly identify the filtered subset.

The default algorithm is *Fast*, and you can enable others through query hints.

### List of hints[​](#list-of-hints "Direct link to List of hints")

### `asof_dense(l r)`[​](#asof_densel-r "Direct link to asof_densel-r")

This hint enables the [Dense](#dense-algo) algorithm, the best choice (when it's
available) for the case of distant row matching.

Applying the query hint for the Dense algorithm

```prism-code
SELECT /*+ asof_dense(orders md) */  
    orders.timestamp, orders.symbol, orders.price  
FROM orders  
ASOF JOIN (md) ON (symbol);
```

### `asof_linear(l r)`[​](#asof_linearl-r "Direct link to asof_linearl-r")

info

This hint applies to `LT` joins as well.

This enables the [Light](#light-algo) algorithm, similar to Dense but simpler.
It is more generic and selected automatically in queries where the Dense algo
isn't applicable. Its downside is that it must scan the entire history in
the RHS table, up to the most recent LHS timestamp.

There's a case where the Light algo is at an advantage even when the Dense algo
is also available: when the right-hand side is a subquery with a WHERE clause
that is highly selective, passing through a small number of rows. QuestDB has
parallelized filtering support, which cannot be used with the other algorithms.

Applying the query hint for the Light algorithm

```prism-code
SELECT /*+ asof_linear(orders md) */  
  orders.ts, orders.price, md.md_ts, md.bid, md.ask  
FROM orders  
ASOF JOIN (  
  SELECT ts as md_ts, bid, ask FROM market_data  
  WHERE state = 'INVALID' -- Highly selective filter  
) md;
```

### `asof_memoized(l r)`[​](#asof_memoizedl-r "Direct link to asof_memoizedl-r")

This hint enables [Memoized](#memoized-algo), a variant of the
[Fast](#fast-algo) algorithm. It works for queries that join on a symbol column,
as in `left ASOF JOIN right ON (symbol)`. It helps when there's a mix of
localized and distant matches by reusing the results of earlier backward scans.

Appling the query hint for the Memoized algorithm

```prism-code
SELECT /*+ asof_memoized(orders md) */  
    orders.timestamp, orders.symbol, orders.price  
FROM orders  
ASOF JOIN (md) ON (symbol);
```

---

### Check the Execution Plan[​](#check-the-execution-plan "Direct link to Check the Execution Plan")

You can verify how QuestDB executes your query by examining its execution plan
with the `EXPLAIN` statement.

#### Default Execution Plan (Binary Search)[​](#default-execution-plan-binary-search "Direct link to Default Execution Plan (Binary Search)")

Without any hints, a filtered `ASOF JOIN` will use the Fast algorithm.

Observing the default execution plan[Demo this query](https://demo.questdb.io/?query=EXPLAIN%20SELECT%20%20*%0AFROM%20core_price%0AASOF%20JOIN%20market_data%0AON%20symbol%0AWHERE%20bids%5B1%2C1%5D%3D107.03%20--%20Highly%20selective%20filter%0A%3B&executeQuery=true)

```prism-code
EXPLAIN SELECT  *  
FROM core_price  
ASOF JOIN market_data  
ON symbol  
WHERE bids[1,1]=107.03 -- Highly selective filter  
;
```

The execution plan will show a `Filtered AsOf Join Fast` operator,
confirming the binary search strategy is being used.

```prism-code
SelectedRecord  
    Filter filter: market_data.bids[1,1]=107.03  
        AsOf Join Fast  
          condition: market_data.symbol=core_price.symbol  
            PageFrame  
                Row forward scan  
                Frame forward scan on: core_price  
            PageFrame  
                Row forward scan  
                Frame forward scan on: market_data
```

#### Hinted Execution Plan (Full Scan)[​](#hinted-execution-plan-full-scan "Direct link to Hinted Execution Plan (Full Scan)")

When you use the `asof_linear` hint, the plan changes.

Observing execution plan with asof\_linear query hint[Demo this query](https://demo.questdb.io/?query=EXPLAIN%20SELECT%20%2F*%2B%20asof_linear(core_price%20market_data)%20*%2F%0A%20%20*%0AFROM%20core_price%0AASOF%20JOIN%20market_data%0AON%20symbol%0AWHERE%20bids%5B1%2C1%5D%3D107.03%20--%20Highly%20selective%20filter%0A%3B&executeQuery=true)

```prism-code
EXPLAIN SELECT /*+ asof_linear(core_price market_data) */  
  *  
FROM core_price  
ASOF JOIN market_data  
ON symbol  
WHERE bids[1,1]=107.03 -- Highly selective filter  
;
```

The execution plan will now show the `AsOf Join Light` operator and a separate,
preceding filtering step on the joined table.

```prism-code
SelectedRecord  
    Filter filter: market_data.bids[1,1]=107.03  
        AsOf Join Light  
          condition: market_data.symbol=core_price.symbol  
            PageFrame  
                Row forward scan  
                Frame forward scan on: core_price  
            PageFrame  
                Row forward scan  
                Frame forward scan on: market_data
```

---

### Algorithms compared on an example[​](#algorithms-compared-on-an-example "Direct link to Algorithms compared on an example")

Let's use the diagram below to explain the key differences among algorithms. It
shows two tables, LHS and RHS. We show the rows aligned on timestamp, so there
are gaps in the LHS column. These gaps don't represent any LHS rows, it is just
the way we visualize the two tables.

The example assumes a JOIN condition on a symbol column. We show the values of
that column in the table:

```prism-code
row | LHS | RHS  
----|-----|----  
 1  |     | G  
 2  |     | C  
 3  |     | G  
 4  |     | A  
 5  |     | F  
 6  |   A | B  
 7  |     | D  
 8  |     | B  
 9  |   C | G  
10  |     | F  
11  |     | D  
12  |   B | E  
13  |     | D  
14  |     | C  
15  |   A | B
```

Since the match for each LHS row occurs in the RHS table at a time earlier than
the previous LHS row, the join pattern is "distant matching".

#### Light algo[​](#light-algo "Direct link to Light algo")

Light algo uses a forward-only scan of the RHS table. When matching the first
RHS symbol (row 6, symbol A), it starts from RHS row 1, and proceeds all the way
to row 6, collecting all the symbols into a hashtable. When done, it looks up
symbol A in the hashtable and finds the prevailing RHS row is row 4. When
matching the next RHS symbol (row 9, symbol C), it resumes the forward scan,
touching rows 7, 8 and 9. Then it looks up symbol C, and finds the prevailing
row is row 2.

#### Fast algo[​](#fast-algo "Direct link to Fast algo")

Fast algo uses binary search over RHS timestamps to zero in on row 6 as the most
recent row not newer than the first LHS row. Then it scans backward: rows 6, 5,
4, and there it finds the matching symbol A. When matching the next LHS symbol
(row 9, symbol C), it uses binary search to zero in on RHS row 9, then scans all
the way back to row 2, where it finds symbol C.

When matching symbol A in row LHS row 15, it uses binary search to zero in or
RHS row 15, then scans backward, again all the way back to row 4.

There's also an optimization that avoids the fixed cost of binary search by
first searching linearly for the matching timestamp in the RHS row, for a
smallish number of steps. This doesn't affect the backward search for the
symbol.

#### Memoized algo[​](#memoized-algo "Direct link to Memoized algo")

The Memoized algo is a variant of the Fast algo. It uses the exact same
linear/binary search to find the matching timestamp in the RHS, and then uses
the same backward search for the symbol. However, it memorizes for each symbol
where it started the backward search, and where it found it.

In our example, this means it handles the first LHS row (6) exactly the same
way, scanning backward to row 4. But when it encounters the same symbol A in row
15, it scans backward only until reaching row 6, and then directly uses the
remembered result of the previous scan, and matches up with row 4.

#### Dense algo[​](#dense-algo "Direct link to Dense algo")

The Dense algo starts like the Fast algo, performing a binary search to zero in
on RHS row 6 and searching backward to find symbol A in row 4 of RHS. From then
on, it behaves more like the Light algo.

To match up LHS row 9 (symbol C), it first does a linear scan forward from row 6
to row 9 (exactly like the Light algo). Since it didn't find C in this scan, it
resumes the backward scan, touching rows 3 and 2, and there it finds the symbol
C.

At LHS row 12 (symbol B), it resumes the forward scan, touching rows 10, 11, and
12. Then it finds symbol B in the hashtable, getting row 8 as the prevailing
row. No backward scan nedeed here.

At LHS row 15 (symbol A), it resumes the forward scan, touching rows 13, 14, and
15. Then it looks up symbol A in the hashtable of the forward scan, finding
nothing. Then it looks up symbol A in the hashtable of the backward scan, and
finds it there. The prevailing row is number 4. Again, no backward search was
needed.

#### Discussion[​](#discussion "Direct link to Discussion")

As expected for distant matching, the Fast and Memoized algos had to touch the
most rows. Especially, when matching row 15, Fast algo had to scan backward to
row 4, and Memoized did only slighly better, scanning until row 6.

Light algo had to initially scan all the history (rows 1 to 6), but from then
on, it only needed to touch the additional rows that came into scope as the LHS
timestamp was moving on.

Dense algo had the same advantage as Light, but it didn't have to scan all the
history. It scanned only as far back into history as needed to find the most
recent occurence of a symbol not yet seen in the forward scan.

### RAM considerations[​](#ram-considerations "Direct link to RAM considerations")

The Fast algorithm is the only one that doesn't use any RAM to store the results
of scanning. It is purely search-based, giving it an additional advantage when
your symbol set is high-cardinality.

---

## Deprecated hints[​](#deprecated-hints "Direct link to Deprecated hints")

* `avoid_asof_binary_search`
  + superseded by `asof_linear`
* `avoid_lt_binary_search`
  + superseded by `asof_linear`
* `asof_linear_search`
  + superseded by `asof_linear`
* `asof_index_search`
  + superseded by `asof_index`
* `asof_memoized_search`
  + superseded by `asof_memoized`