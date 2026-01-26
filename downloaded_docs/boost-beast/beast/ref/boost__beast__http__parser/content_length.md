##### [http::parser::content\_length](content_length.html "http::parser::content_length")

(Inherited from [`http::basic_parser`](../boost__beast__http__basic_parser.html "http::basic_parser"))

Returns the optional value of Content-Length if known.

###### [Synopsis](content_length.html#beast.ref.boost__beast__http__parser.content_length.synopsis)

```programlisting
boost::optional< std::uint64_t >
content_length() const;
```

###### [Remarks](content_length.html#beast.ref.boost__beast__http__parser.content_length.remarks)

The return value is undefined unless [`is_header_done`](is_header_done.html "http::parser::is_header_done") would return `true`.