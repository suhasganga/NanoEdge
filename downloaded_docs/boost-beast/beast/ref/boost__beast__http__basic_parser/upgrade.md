##### [http::basic\_parser::upgrade](upgrade.html "http::basic_parser::upgrade")

Returns `true` if the message
is an upgrade message.

###### [Synopsis](upgrade.html#beast.ref.boost__beast__http__basic_parser.upgrade.synopsis)

```programlisting
bool
upgrade() const;
```

###### [Remarks](upgrade.html#beast.ref.boost__beast__http__basic_parser.upgrade.remarks)

The return value is undefined unless [`is_header_done`](is_header_done.html "http::basic_parser::is_header_done") would return `true`.