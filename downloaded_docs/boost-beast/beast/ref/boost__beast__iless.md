#### [iless](boost__beast__iless.html "iless")

A case-insensitive less predicate for strings.

##### [Synopsis](boost__beast__iless.html#beast.ref.boost__beast__iless.synopsis)

Defined in header `<boost/beast/core/string.hpp>`

```programlisting
struct iless
```

##### [Types](boost__beast__iless.html#beast.ref.boost__beast__iless.types)

| Name | Description |
| --- | --- |
| **[is\_transparent](boost__beast__iless/is_transparent.html "iless::is_transparent")** |  |

##### [Member Functions](boost__beast__iless.html#beast.ref.boost__beast__iless.member_functions)

| Name | Description |
| --- | --- |
| **[operator()](boost__beast__iless/operator_lp__rp_.html "iless::operator()")** |  |

##### [Description](boost__beast__iless.html#beast.ref.boost__beast__iless.description)

The case-comparison operation is defined only for low-ASCII characters.

As of C++14, containers using this class as the `Compare`
type will take part in heterogeneous lookup if the search term is implicitly
convertible to [`string_view`](boost__beast__string_view.html "string_view").