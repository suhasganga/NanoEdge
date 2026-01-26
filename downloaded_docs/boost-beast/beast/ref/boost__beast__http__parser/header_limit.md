##### [http::parser::header\_limit](header_limit.html "http::parser::header_limit")

(Inherited from [`http::basic_parser`](../boost__beast__http__basic_parser.html "http::basic_parser"))

Set a limit on the total size of the header.

###### [Synopsis](header_limit.html#beast.ref.boost__beast__http__parser.header_limit.synopsis)

```programlisting
void
header_limit(
    std::uint32_t v);
```

###### [Description](header_limit.html#beast.ref.boost__beast__http__parser.header_limit.description)

This function sets the maximum allowed size of the header including all
field name, value, and delimiter characters and also including the CRLF
sequences in the serialized input. If the end of the header is not found
within the limit of the header size, the error [`error::header_limit`](../boost__beast__http__error.html "http::error") is returned by [`put`](put.html "http::parser::put").

Setting the limit after any header octets have been parsed results in undefined
behavior.