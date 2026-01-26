##### [http::empty\_body::size](size.html "http::empty_body::size")

Returns the payload size of the body.

###### [Synopsis](size.html#beast.ref.boost__beast__http__empty_body.size.synopsis)

```programlisting
static
std::uint64_t
size(
    value_type);
```

###### [Description](size.html#beast.ref.boost__beast__http__empty_body.size.description)

When this body is used with [`message::prepare_payload`](../boost__beast__http__message/prepare_payload.html "http::message::prepare_payload"), the Content-Length
will be set to the payload size, and any chunked Transfer-Encoding will
be removed.