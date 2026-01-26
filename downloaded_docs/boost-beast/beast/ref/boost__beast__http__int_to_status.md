#### [http::int\_to\_status](boost__beast__http__int_to_status.html "http::int_to_status")

Converts the integer to a known status-code.

##### [Synopsis](boost__beast__http__int_to_status.html#beast.ref.boost__beast__http__int_to_status.synopsis)

Defined in header `<boost/beast/http/status.hpp>`

```programlisting
status
int_to_status(
    unsigned v);
```

##### [Description](boost__beast__http__int_to_status.html#beast.ref.boost__beast__http__int_to_status.description)

If the integer does not match a known status code, [`status::unknown`](boost__beast__http__status.html "http::status") is returned.