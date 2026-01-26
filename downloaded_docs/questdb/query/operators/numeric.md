On this page

These operations work for any numeric types. Also, addition and multiplication
work for N-dimensional arrays. The result will be an array where each element is
the result of applying the operation to the elements at the same coordinates in
the operand arrays.

## `*` Multiply[​](#-multiply "Direct link to -multiply")

`*` is a binary operation to multiply two numbers together.

#### Example[​](#example "Direct link to Example")

```prism-code
SELECT 5 + 2
```

| column |
| --- |
| 7 |

## `/` Divide[​](#-divide "Direct link to -divide")

`/` is a binary operation to divide two numbers.

#### Example[​](#example-1 "Direct link to Example")

```prism-code
SELECT 5 / 2, 5.0 / 2.0
```

| column | column1 |
| --- | --- |
| 2 | 2.5 |

## `%` Modulo[​](#-modulo "Direct link to -modulo")

`%` performs a modulo operation, returning the remainder of a division.

#### Example[​](#example-2 "Direct link to Example")

```prism-code
SELECT 5 % 2
```

| column |
| --- |
| 1 |

## `+` Add[​](#-add "Direct link to -add")

`+` performs an addition operation, for two numbers.

#### Example[​](#example-3 "Direct link to Example")

```prism-code
SELECT 5 + 2
```

| column |
| --- |
| 7 |

## `-` Subtract[​](#--subtract "Direct link to --subtract")

`-` performs a subtraction operation, for two numbers.

#### Example[​](#example-4 "Direct link to Example")

```prism-code
SELECT 5 - 2
```

| column |
| --- |
| 3 |

## `-` Negate[​](#--negate "Direct link to --negate")

`-` can also be used for unary negation.

#### Example[​](#example-5 "Direct link to Example")

```prism-code
SELECT -5
```

| column |
| --- |
| -5 |