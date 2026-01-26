#### [http::validate\_list](boost__beast__http__validate_list.html "http::validate_list")

Returns `true` if a parsed list
is parsed without errors.

##### [Synopsis](boost__beast__http__validate_list.html#beast.ref.boost__beast__http__validate_list.synopsis)

Defined in header `<boost/beast/http/rfc7230.hpp>`

```programlisting
template<
    class Policy>
bool
validate_list(
    detail::basic_parsed_list< Policy > const& list);
```

##### [Description](boost__beast__http__validate_list.html#beast.ref.boost__beast__http__validate_list.description)

This function iterates a single pass through a parsed list and returns `true` if there were no parsing errors, else
returns `false`.