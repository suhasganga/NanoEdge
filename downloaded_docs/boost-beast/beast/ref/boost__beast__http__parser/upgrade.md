##### [http::parser::upgrade](upgrade.html "http::parser::upgrade")

(Inherited from [`http::basic_parser`](../boost__beast__http__basic_parser.html "http::basic_parser"))

Returns `true` if the message
is an upgrade message.

###### [Synopsis](upgrade.html#beast.ref.boost__beast__http__parser.upgrade.synopsis)

```programlisting
bool
upgrade() const;
```

###### [Remarks](upgrade.html#beast.ref.boost__beast__http__parser.upgrade.remarks)

The return value is undefined unless [`is_header_done`](is_header_done.html "http::parser::is_header_done") would return `true`.