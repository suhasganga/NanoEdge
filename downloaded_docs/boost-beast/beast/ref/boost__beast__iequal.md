#### [iequal](boost__beast__iequal.html "iequal")

A case-insensitive equality predicate for strings.

##### [Synopsis](boost__beast__iequal.html#beast.ref.boost__beast__iequal.synopsis)

Defined in header `<boost/beast/core/string.hpp>`

```programlisting
struct iequal
```

##### [Types](boost__beast__iequal.html#beast.ref.boost__beast__iequal.types)

| Name | Description |
| --- | --- |
| **[is\_transparent](boost__beast__iequal/is_transparent.html "iequal::is_transparent")** |  |

##### [Member Functions](boost__beast__iequal.html#beast.ref.boost__beast__iequal.member_functions)

| Name | Description |
| --- | --- |
| **[operator()](boost__beast__iequal/operator_lp__rp_.html "iequal::operator()")** |  |

##### [Description](boost__beast__iequal.html#beast.ref.boost__beast__iequal.description)

The case-comparison operation is defined only for low-ASCII characters.

As of C++14, containers using this class as the `Compare`
type will take part in heterogeneous lookup if the search term is implicitly
convertible to [`string_view`](boost__beast__string_view.html "string_view").