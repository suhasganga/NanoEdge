On this page

## `||` Concat[​](#-concat "Direct link to -concat")

`||` concatenates strings, similar to [concat()](/docs/query/functions/text/#concat).

#### Example[​](#example "Direct link to Example")

```prism-code
SELECT 'a' || 'b'
```

| concat |
| --- |
| ab |

## `~` Regex match[​](#-regex-match "Direct link to -regex-match")

Performs a regular-expression match on a string.

#### Example[​](#example-1 "Direct link to Example")

```prism-code
SELECT address FROM (SELECT 'abc@foo.com' as address) WHERE address ~ '@foo.com'
```

| address |
| --- |
| [abc@foo.com](mailto:abc@foo.com) |

## `!~` Regex doesn't match[​](#-regex-doesnt-match "Direct link to -regex-doesnt-match")

The inverse of the `~` regex matching operator.

```prism-code
SELECT address FROM (SELECT 'abc@foo.com' as address) WHERE address !~ '@bah.com'
```

| address |
| --- |
| [abc@foo.com](mailto:abc@foo.com) |

## `LIKE`[​](#like "Direct link to like")

`LIKE` performs a case-sensitive match, based on a pattern.

The `%` wildcard represents 0, 1 or n characters.

The `_` wildcard represents a single character.

#### Example[​](#example-2 "Direct link to Example")

```prism-code
SELECT 'abc' LIKE '%c', 'abc' LIKE 'a_c'
```

| column | column1 |
| --- | --- |
| true | true |

## `ILIKE`[​](#ilike "Direct link to ilike")

`ILIKE` is the same as `LIKE`, but performs a case insensitive match,

#### Example[​](#example-3 "Direct link to Example")

```prism-code
SELECT 'abC' LIKE '%c', 'abC' ILIKE '%c'
```

| column | column1 |
| --- | --- |
| false | true |