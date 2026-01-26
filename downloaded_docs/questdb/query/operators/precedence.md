On this page

The following tables provide information about which operators are available, and their corresponding precedences.

For IPv4 operators, this list is not comprehensive, and users should refer directly to the [IPv4](/docs/query/operators/ipv4/) documentation itself.

## Pre-8.0 notice[​](#pre-80-notice "Direct link to Pre-8.0 notice")

In QuestDB 8.0.0, operator precedence is aligned closer to other SQL implementations.

If upgrading from 8.0, review your queries for any relevant changes.

If you are unable to migrate straight away, set the `cairo.sql.legacy.operator.precedence` config option to `true` in `server.conf`.

This is a temporary flag which will be removed in succeeding versions of QuestDB.

Legacy precedence, if set, is:

1. `.`, `::`
2. (none)
3. `*`, `/`, `%`, `+`, `-`
4. `<<`, `>>`, `<<=`, `>>=`
5. `||`
6. `<`, `>`, `<=`, `>=
7. `=`, `~`, `!=`, `<>`, `!~`, `IN`, `BETWEEN`, `LIKE`, `ILIKE`, `WITHIN`
8. `&`
9. `^`
10. `|`
11. `AND`, `OR`, `NOT`

See the next section for the current precedence.

### Current[​](#current "Direct link to Current")

| operator | name | precedence | description |
| --- | --- | --- | --- |
| [`.`](/docs/query/operators/misc/#-prefix) | prefix | 1 | prefix field with table name |
| [`::`](/docs/query/operators/misc/#-cast) | cast | 2 | postgres style type casting |
| [`-`](/docs/query/operators/numeric/#--negate) | negate | 3 | unary negation of a number |
| [`~`](/docs/query/operators/bitwise/#-not) | complement | 3 | unary complement of a number |
| [`*`](/docs/query/operators/numeric/#-multiply) | multiply | 4 | multiply two numbers |
| [`/`](/docs/query/operators/numeric/#-divide) | divide | 4 | divide two numbers |
| [`%`](/docs/query/operators/numeric/#-modulo) | modulo | 4 | take the modulo of two numbers |
| [`+`](/docs/query/operators/numeric/#-add) | add | 5 | add two numbers |
| [`-`](/docs/query/operators/numeric/#--subtract) | subtract | 5 | subtract two numbers |
| [`<<`](/docs/query/operators/ipv4/#-left-strict-ip-address-contained-by) | left IPv4 contains strict | 6 |  |
| [`>>`](/docs/query/operators/ipv4/#-right-strict-ip-address-contained-by) | right IPv4 contains strict | 6 |  |
| [`<<=`](/docs/query/operators/ipv4/#-left-ip-address-contained-by-or-equal) | left IPv4 contains or equal | 6 |  |
| [`<<=`](/docs/query/operators/ipv4/#-right-ip-address-contained-by-or-equal) | right IPv4 contains or equal | 6 |  |
| [`||`](/docs/query/operators/text/#-concat) | concat | 7 | concatenate strings |
| [`&`](/docs/query/operators/bitwise/#-and) | bitwise and | 8 | bitwise AND of two numbers |
| [`^`](/docs/query/operators/bitwise/#-xor) | bitwise xor | 9 | bitwise XOR of two numbers |
| [`|`](/docs/query/operators/bitwise/#-or) | bitwise or | 10 | bitwise OR of two numbers |
| [`IN`](/docs/query/operators/date-time/#in-timerange) | in | 11 | check if value in list or range |
| [`BETWEEN`](/docs/query/operators/date-time/#between-value1-and-value2) | between | 11 | check if timestamp in range |
| [`WITHIN`](/docs/query/operators/spatial/#within) | within geohash | 11 | prefix matches geohash |
| [`<`](/docs/query/operators/comparison/#-lesser-than) | lesser than | 12 | lt comparison |
| [`<=`](/docs/query/operators/comparison/#-lesser-than-or-equal-to) | lesser than or equal to | 12 | leq comparison |
| [`>`](/docs/query/operators/comparison/#-greater-than) | greater than | 12 | gt comparison |
| [`>=`](/docs/query/operators/comparison/#-greater-than-or-equal-to) | greater than or equal to | 12 | geq comparison |
| [`=`](/docs/query/operators/comparison/#-equals) | equals | 13 | eq comparison |
| [`~`](/docs/query/operators/text/#-regex-match) | regex match | 13 | regex pattern match |
| [`!=`](/docs/query/operators/comparison/#-or--not-equals) | not equals | 13 | neq comparison |
| [`<>`](/docs/query/operators/comparison/#-or--not-equals) | not equals | 13 | neq comparison |
| [`!~`](/docs/query/operators/text/#-regex-doesnt-match) | regex does not match | 13 | regex pattern does not match |
| [`LIKE`](/docs/query/operators/text/#like) | match string | 13 | pattern matching |
| [`ILIKE`](/docs/query/operators/text/#ilike) | match string without case | 13 | case insensitive pattern matching |
| [`NOT`](/docs/query/operators/logical/#not-logical-not) | logical not | 14 | logical NOT of two numbers |
| [`AND`](/docs/query/operators/logical/#and-logical-and) | logical and | 15 | logical AND of two numbers |
| [`OR`](/docs/query/operators/logical/#or-logical-or) | logical or | 16 | logical OR of two numbers |