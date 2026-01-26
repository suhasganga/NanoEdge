##### [http::basic\_chunk\_extensions::parse](parse.html "http::basic_chunk_extensions::parse")

Parse a set of chunk extensions.

###### [Synopsis](parse.html#beast.ref.boost__beast__http__basic_chunk_extensions.parse.synopsis)

```programlisting
void
parse(
    string_view s,
    error_code& ec);
```

###### [Description](parse.html#beast.ref.boost__beast__http__basic_chunk_extensions.parse.description)

Any previous extensions will be cleared