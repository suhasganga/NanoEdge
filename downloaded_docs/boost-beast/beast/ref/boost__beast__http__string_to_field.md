#### [http::string\_to\_field](boost__beast__http__string_to_field.html "http::string_to_field")

Attempt to convert a string to a field enum.

##### [Synopsis](boost__beast__http__string_to_field.html#beast.ref.boost__beast__http__string_to_field.synopsis)

Defined in header `<boost/beast/http/field.hpp>`

```programlisting
field
string_to_field(
    string_view s);
```

##### [Description](boost__beast__http__string_to_field.html#beast.ref.boost__beast__http__string_to_field.description)

The string comparison is case-insensitive.

##### [Return Value](boost__beast__http__string_to_field.html#beast.ref.boost__beast__http__string_to_field.return_value)

The corresponding field, or [`field::unknown`](boost__beast__http__field.html "http::field") if no known field matches.