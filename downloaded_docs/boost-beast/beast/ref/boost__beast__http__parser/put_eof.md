##### [http::parser::put\_eof](put_eof.html "http::parser::put_eof")

(Inherited from [`http::basic_parser`](../boost__beast__http__basic_parser.html "http::basic_parser"))

Inform the parser that the end of stream was reached.

###### [Synopsis](put_eof.html#beast.ref.boost__beast__http__parser.put_eof.synopsis)

```programlisting
void
put_eof(
    error_code& ec);
```

###### [Description](put_eof.html#beast.ref.boost__beast__http__parser.put_eof.description)

In certain cases, HTTP needs to know where the end of the stream is. For
example, sometimes servers send responses without Content-Length and expect
the client to consume input (for the body) until EOF. Callbacks and errors
will still be processed as usual.

This is typically called when a read from the underlying stream object
sets the error code to `net::error::eof`.

###### [Remarks](put_eof.html#beast.ref.boost__beast__http__parser.put_eof.remarks)

Only valid after parsing a complete header.

###### [Parameters](put_eof.html#beast.ref.boost__beast__http__parser.put_eof.parameters)

| Name | Description |
| --- | --- |
| `ec` | Set to the error, if any occurred. |