##### [http::parser::chunked](chunked.html "http::parser::chunked")

(Inherited from [`http::basic_parser`](../boost__beast__http__basic_parser.html "http::basic_parser"))

Returns `true` if the last value
for Transfer-Encoding is "chunked".

###### [Synopsis](chunked.html#beast.ref.boost__beast__http__parser.chunked.synopsis)

```programlisting
bool
chunked() const;
```

###### [Remarks](chunked.html#beast.ref.boost__beast__http__parser.chunked.remarks)

The return value is undefined unless [`is_header_done`](is_header_done.html "http::parser::is_header_done") would return `true`.