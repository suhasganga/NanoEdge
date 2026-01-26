On this page

This page describes the available operators to assist with performing bitwise
operations on numeric values.

## `~` NOT[​](#-not "Direct link to -not")

`~` is a unary operation that performs bitwise negation on each bit. Bits that
are 0 become 1, and those that are 1 become 0. Expects a value of `long` or
`int` type.

#### Examples[​](#examples "Direct link to Examples")

```prism-code
SELECT ~1024
```

| column |
| --- |
| -1025 |

## `&` AND[​](#-and "Direct link to -and")

`&` is a binary operation that takes two equal-length binary representations and
performs the bitwise AND operation on each pair of the corresponding bits.
Expects values of `long` or `int` type.

#### Examples[​](#examples-1 "Direct link to Examples")

```prism-code
SELECT 5 & 3
```

| column |
| --- |
| 1 |

## `^` XOR[​](#-xor "Direct link to -xor")

`^` is a binary operation that takes two bit patterns of equal length and
performs the bitwise exclusive OR (XOR) operation on each pair of corresponding
bits. Expects a value of `long` or `int` type.

#### Examples[​](#examples-2 "Direct link to Examples")

```prism-code
SELECT 5 ^ 3
```

| column |
| --- |
| 6 |

## `|` OR[​](#-or "Direct link to -or")

`|` is a binary operation that takes two bit patterns of equal length and
performs the logical inclusive OR operation on each pair of corresponding bits.
Expects a value of `long` or `int` type.

#### Examples[​](#examples-3 "Direct link to Examples")

```prism-code
SELECT 5 | 3
```

| column |
| --- |
| 7 |