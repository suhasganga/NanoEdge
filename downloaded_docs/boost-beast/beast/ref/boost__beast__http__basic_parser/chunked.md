##### [http::basic\_parser::chunked](chunked.html "http::basic_parser::chunked")

Returns `true` if the last value
for Transfer-Encoding is "chunked".

###### [Synopsis](chunked.html#beast.ref.boost__beast__http__basic_parser.chunked.synopsis)

```programlisting
bool
chunked() const;
```

###### [Remarks](chunked.html#beast.ref.boost__beast__http__basic_parser.chunked.remarks)

The return value is undefined unless [`is_header_done`](is_header_done.html "http::basic_parser::is_header_done") would return `true`.