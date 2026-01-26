##### [http::serializer::consume](consume.html "http::serializer::consume")

Consume buffer octets in the serialization.

###### [Synopsis](consume.html#beast.ref.boost__beast__http__serializer.consume.synopsis)

```programlisting
void
consume(
    std::size_t n);
```

###### [Description](consume.html#beast.ref.boost__beast__http__serializer.consume.description)

This function should be called after one or more octets contained in the
buffers provided in the prior call to [`next`](next.html "http::serializer::next") have been used.

After a call to [`consume`](consume.html "http::serializer::consume"), callers should check
the return value of [`is_done`](is_done.html "http::serializer::is_done") to determine if the entire
message has been serialized.

###### [Parameters](consume.html#beast.ref.boost__beast__http__serializer.consume.parameters)

| Name | Description |
| --- | --- |
| `n` | The number of octets to consume. This number must be greater than zero and no greater than the number of octets in the buffers provided in the prior call to [`next`](next.html "http::serializer::next"). |