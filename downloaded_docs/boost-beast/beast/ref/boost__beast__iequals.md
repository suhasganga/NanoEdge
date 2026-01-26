#### [iequals](boost__beast__iequals.html "iequals")

Returns `true` if two strings
are equal, using a case-insensitive comparison.

##### [Synopsis](boost__beast__iequals.html#beast.ref.boost__beast__iequals.synopsis)

Defined in header `<boost/beast/core/string.hpp>`

```programlisting
bool
iequals(
    beast::string_view lhs,
    beast::string_view rhs);
```

##### [Description](boost__beast__iequals.html#beast.ref.boost__beast__iequals.description)

The case-comparison operation is defined only for low-ASCII characters.

##### [Parameters](boost__beast__iequals.html#beast.ref.boost__beast__iequals.parameters)

| Name | Description |
| --- | --- |
| `lhs` | The string on the left side of the equality |
| `rhs` | The string on the right side of the equality |