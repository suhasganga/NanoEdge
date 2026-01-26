##### [http::basic\_parser::on\_chunk\_body\_impl](on_chunk_body_impl.html "http::basic_parser::on_chunk_body_impl")

Called each time additional data is received representing part of a body
chunk.

###### [Synopsis](on_chunk_body_impl.html#beast.ref.boost__beast__http__basic_parser.on_chunk_body_impl.synopsis)

```programlisting
std::size_t
on_chunk_body_impl(
    std::uint64_t remain,
    string_view body,
    error_code& ec);
```

###### [Description](on_chunk_body_impl.html#beast.ref.boost__beast__http__basic_parser.on_chunk_body_impl.description)

This virtual function is invoked for each piece of the body which is received
while parsing of a message. This function is only used when no chunked
transfer encoding is present.

###### [Parameters](on_chunk_body_impl.html#beast.ref.boost__beast__http__basic_parser.on_chunk_body_impl.parameters)

| Name | Description |
| --- | --- |
| `remain` | The number of bytes remaining in this chunk. This includes the contents of passed `body`. If this value is zero, then this represents the final chunk. |
| `body` | A string holding the additional body contents. This may contain nulls or unprintable characters. |
| `ec` | An output parameter which the function may set to indicate an error. The error will be clear before this function is invoked. |

###### [Return Value](on_chunk_body_impl.html#beast.ref.boost__beast__http__basic_parser.on_chunk_body_impl.return_value)

This function should return the number of bytes actually consumed from
the `body` value. Any bytes
that are not consumed on this call will be presented in a subsequent call.

###### [See Also](on_chunk_body_impl.html#beast.ref.boost__beast__http__basic_parser.on_chunk_body_impl.see_also)

[`on_body_impl`](on_body_impl.html "http::basic_parser::on_body_impl")