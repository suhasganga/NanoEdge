##### [http::basic\_parser::on\_header\_impl](on_header_impl.html "http::basic_parser::on_header_impl")

Called once after the complete HTTP header is received.

###### [Synopsis](on_header_impl.html#beast.ref.boost__beast__http__basic_parser.on_header_impl.synopsis)

```programlisting
void
on_header_impl(
    error_code& ec);
```

###### [Description](on_header_impl.html#beast.ref.boost__beast__http__basic_parser.on_header_impl.description)

This virtual function is invoked once, after the complete HTTP header is
received while parsing a message.

###### [Parameters](on_header_impl.html#beast.ref.boost__beast__http__basic_parser.on_header_impl.parameters)

| Name | Description |
| --- | --- |
| `ec` | An output parameter which the function may set to indicate an error. The error will be clear before this function is invoked. |