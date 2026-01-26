On this page

This page describes the available operators to assist with performing pattern
matching. For operators using regular expressions (`regex` in the syntax),
QuestDB uses
[Java regular expression implementation](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/regex/Pattern.html).

VARCHAR and STRING data types

QuestDB supports two types of string data: `VARCHAR` and `STRING`. Most users
should use `VARCHAR` as it is more efficient. See
[VARCHAR vs STRING](/docs/query/datatypes/overview/#varchar-and-string-considerations)
for more information.

Functions described in this page work with both types.

## ~ (match) and !~ (does not match)[​](#-match-and--does-not-match "Direct link to ~ (match) and !~ (does not match)")

* `(string) ~ (regex)` - returns true if the `string` value matches a regular
  expression, `regex`, otherwise returns false (case sensitive match).
* `(string) !~ (regex)` - returns true if the `string` value fails to match a
  regular expression, `regex`, otherwise returns false (case sensitive match).

### Arguments[​](#arguments "Direct link to Arguments")

* `string` is an expression that evaluates to the `string` data type.
* `regex` is any regular expression pattern.

### Return value[​](#return-value "Direct link to Return value")

Return value type is `boolean`.

## LIKE/ILIKE[​](#likeilike "Direct link to LIKE/ILIKE")

* `(string) LIKE (pattern)` - returns true if the `string` value matches
  `pattern`, otherwise returns false (case sensitive match).
* `(string) ILIKE (pattern)` - returns true if the `string` value matches
  `pattern`, otherwise returns false (case insensitive match).

### Arguments[​](#arguments-1 "Direct link to Arguments")

* `string` is an expression that evaluates to the `string` data type.
* `pattern` is a pattern which can contain wildcards like `_` and `%`.

### Return value[​](#return-value-1 "Direct link to Return value")

Return value type is `boolean`.

### Description[​](#description "Direct link to Description")

If the pattern doesn't contain wildcards, then the pattern represents the string
itself.

The wildcards which can be used in pattern are interpreted as follows:

* `_` - matches any single character.
* `%` - matches any sequence of zero or more characters.

Wildcards can be used as follows:

```prism-code
SELECT 'quest' LIKE 'quest' ;  
-- Returns true  
SELECT 'quest' LIKE 'ques_';  
-- Returns true  
SELECT 'quest' LIKE 'que%';  
-- Returns true  
SELECT 'quest' LIKE '_ues_';  
-- Returns true  
SELECT 'quest' LIKE 'q_'  
-- Returns false
```

`ILIKE` performs a case insensitive match as follows:

```prism-code
SELECT 'quest' ILIKE 'QUEST';  
-- Returns true  
SELECT 'qUeSt' ILIKE 'QUEST';  
-- Returns true  
SELECT 'quest' ILIKE 'QUE%';  
-- Returns true  
SELECT 'QUEST' ILIKE '_ues_';  
-- Returns true
```

### Examples[​](#examples "Direct link to Examples")

#### LIKE[​](#like "Direct link to LIKE")

```prism-code
SELECT * FROM trades  
WHERE symbol LIKE '%-USDT'  
LATEST ON timestamp PARTITION BY symbol;
```

| symbol | side | price | amount | timestamp |
| --- | --- | --- | --- | --- |
| ETH-USDT | sell | 1348.13 | 3.22455108 | 2022-10-04T15:25:58.834362Z |
| BTC-USDT | sell | 20082.08 | 0.16591219 | 2022-10-04T15:25:59.742552Z |

#### ILIKE[​](#ilike "Direct link to ILIKE")

```prism-code
SELECT * FROM trades  
WHERE symbol ILIKE '%-usdt'  
LATEST ON timestamp PARTITION BY symbol;
```

| symbol | side | price | amount | timestamp |
| --- | --- | --- | --- | --- |
| ETH-USDT | sell | 1348.13 | 3.22455108 | 2022-10-04T15:25:58.834362Z |
| BTC-USDT | sell | 20082.08 | 0.16591219 | 2022-10-04T15:25:59.742552Z |

## regexp\_replace[​](#regexp_replace "Direct link to regexp_replace")

`regexp_replace (string1, regex , string2 )` - provides substitution of new text
for substrings that match regular expression patterns.

### Arguments:[​](#arguments-2 "Direct link to Arguments:")

* `string1` is a source `string` value to be manipulated.
* `regex` is a regular expression pattern.
* `string2` is any `string` value to replace part or the whole of the source
  value.

### Return value[​](#return-value-2 "Direct link to Return value")

Return value type is `string`. The source string is returned unchanged if there
is no match to the pattern. If there is a match, the source string is returned
with the replacement string substituted for the matching substring.

### Examples:[​](#examples-1 "Direct link to Examples:")

Example description - regexp\_replace

```prism-code
SELECT regexp_replace('MYSQL is a great database', '^(\S*)', 'QuestDB');
```

```prism-code
QuestDB is a great database
```