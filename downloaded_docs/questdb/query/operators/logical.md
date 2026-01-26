On this page

## `OR` Logical OR[​](#or-logical-or "Direct link to or-logical-or")

`OR` represents a logical OR operation, which takes two predicates and filters for either one being true.

#### Examples[​](#examples "Direct link to Examples")

```prism-code
SELECT * FROM (SELECT 5 AS a, 10 AS b) WHERE A = 5 OR B = 2
```

| a | b |
| --- | --- |
| 5 | 10 |

```prism-code
SELECT * FROM (SELECT 5 AS a, 10 AS b) WHERE A = 3 OR B = 2
```

| a | b |
| --- | --- |

## `AND` Logical AND[​](#and-logical-and "Direct link to and-logical-and")

`AND` represents a logical AND operation, which takes two predicates and filters for both being true.

#### Examples[​](#examples-1 "Direct link to Examples")

```prism-code
SELECT * FROM (SELECT 5 AS a, 10 AS b) WHERE A = 5 AND B = 2
```

| a | b |
| --- | --- |

```prism-code
SELECT * FROM (SELECT 5 AS a, 10 AS b) WHERE A = 5 AND B = 10
```

| a | b |
| --- | --- |
| 5 | 10 |

## `NOT` Logical NOT[​](#not-logical-not "Direct link to not-logical-not")

`NOT` inverts the boolean value. This can be combined with other operators to create their inverse operations, i.e `NOT IN`, `NOT WITHIN`.

#### Example[​](#example "Direct link to Example")

```prism-code
SELECT NOT TRUE
```

| column |
| --- |
| false |