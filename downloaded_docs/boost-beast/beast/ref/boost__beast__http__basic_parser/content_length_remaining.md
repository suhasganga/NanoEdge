##### [http::basic\_parser::content\_length\_remaining](content_length_remaining.html "http::basic_parser::content_length_remaining")

Returns the remaining content length if known.

###### [Synopsis](content_length_remaining.html#beast.ref.boost__beast__http__basic_parser.content_length_remaining.synopsis)

```programlisting
boost::optional< std::uint64_t >
content_length_remaining() const;
```

###### [Description](content_length_remaining.html#beast.ref.boost__beast__http__basic_parser.content_length_remaining.description)

If the message header specifies a Content-Length, the return value will
be the number of bytes remaining in the payload body have not yet been
parsed.

###### [Remarks](content_length_remaining.html#beast.ref.boost__beast__http__basic_parser.content_length_remaining.remarks)

The return value is undefined unless [`is_header_done`](is_header_done.html "http::basic_parser::is_header_done") would return `true`.