##### [http::basic\_parser::keep\_alive](keep_alive.html "http::basic_parser::keep_alive")

Returns `true` if the message
has keep-alive connection semantics.

###### [Synopsis](keep_alive.html#beast.ref.boost__beast__http__basic_parser.keep_alive.synopsis)

```programlisting
bool
keep_alive() const;
```

###### [Description](keep_alive.html#beast.ref.boost__beast__http__basic_parser.keep_alive.description)

This function always returns `false`
if [`need_eof`](need_eof.html "http::basic_parser::need_eof") would return `false`.

###### [Remarks](keep_alive.html#beast.ref.boost__beast__http__basic_parser.keep_alive.remarks)

The return value is undefined unless [`is_header_done`](is_header_done.html "http::basic_parser::is_header_done") would return `true`.