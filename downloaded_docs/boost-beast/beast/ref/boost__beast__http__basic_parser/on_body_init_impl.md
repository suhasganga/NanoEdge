##### [http::basic\_parser::on\_body\_init\_impl](on_body_init_impl.html "http::basic_parser::on_body_init_impl")

Called once before the body is processed.

###### [Synopsis](on_body_init_impl.html#beast.ref.boost__beast__http__basic_parser.on_body_init_impl.synopsis)

```programlisting
void
on_body_init_impl(
    boost::optional< std::uint64_t > const& content_length,
    error_code& ec);
```

###### [Description](on_body_init_impl.html#beast.ref.boost__beast__http__basic_parser.on_body_init_impl.description)

This virtual function is invoked once, before the content body is processed
(but after the complete header is received).

###### [Parameters](on_body_init_impl.html#beast.ref.boost__beast__http__basic_parser.on_body_init_impl.parameters)

| Name | Description |
| --- | --- |
| `content_length` | A value representing the content length in bytes if the length is known (this can include a zero length). Otherwise, the value will be `boost::none`. |
| `ec` | An output parameter which the function may set to indicate an error. The error will be clear before this function is invoked. |