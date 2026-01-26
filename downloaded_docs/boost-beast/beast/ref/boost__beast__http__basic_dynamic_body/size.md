##### [http::basic\_dynamic\_body::size](size.html "http::basic_dynamic_body::size")

Returns the payload size of the body.

###### [Synopsis](size.html#beast.ref.boost__beast__http__basic_dynamic_body.size.synopsis)

```programlisting
static
std::uint64_t
size(
    value_type const& v);
```

###### [Description](size.html#beast.ref.boost__beast__http__basic_dynamic_body.size.description)

When this body is used with [`message::prepare_payload`](../boost__beast__http__message/prepare_payload.html "http::message::prepare_payload"), the Content-Length
will be set to the payload size, and any chunked Transfer-Encoding will
be removed.