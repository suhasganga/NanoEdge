##### [http::basic\_parser::on\_body\_impl](on_body_impl.html "http::basic_parser::on_body_impl")

Called each time additional data is received representing the content body.

###### [Synopsis](on_body_impl.html#beast.ref.boost__beast__http__basic_parser.on_body_impl.synopsis)

```programlisting
std::size_t
on_body_impl(
    string_view body,
    error_code& ec);
```

###### [Description](on_body_impl.html#beast.ref.boost__beast__http__basic_parser.on_body_impl.description)

This virtual function is invoked for each piece of the body which is received
while parsing of a message. This function is only used when no chunked
transfer encoding is present.

###### [Parameters](on_body_impl.html#beast.ref.boost__beast__http__basic_parser.on_body_impl.parameters)

| Name | Description |
| --- | --- |
| `body` | A string holding the additional body contents. This may contain nulls or unprintable characters. |
| `ec` | An output parameter which the function may set to indicate an error. The error will be clear before this function is invoked. |

###### [See Also](on_body_impl.html#beast.ref.boost__beast__http__basic_parser.on_body_impl.see_also)

[`on_chunk_body_impl`](on_chunk_body_impl.html "http::basic_parser::on_chunk_body_impl")