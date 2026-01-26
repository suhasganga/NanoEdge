###### [websocket::stream::read\_size\_hint (2 of 2 overloads)](overload2.html "websocket::stream::read_size_hint (2 of 2 overloads)")

Returns a suggested maximum buffer size for the next call to read.

###### [Synopsis](overload2.html#beast.ref.boost__beast__websocket__stream.read_size_hint.overload2.synopsis)

```programlisting
template<
    class DynamicBuffer>
std::size_t
read_size_hint(
    DynamicBuffer& buffer) const;
```

###### [Description](overload2.html#beast.ref.boost__beast__websocket__stream.read_size_hint.overload2.description)

This function returns a reasonable upper limit on the number of bytes
for the size of the buffer passed in the next call to read. The number
is determined by the state of the current frame and whether or not the
permessage-deflate extension is enabled.

###### [Parameters](overload2.html#beast.ref.boost__beast__websocket__stream.read_size_hint.overload2.parameters)

| Name | Description |
| --- | --- |
| `buffer` | The buffer which will be used for reading. The implementation will query the buffer to obtain the optimum size of a subsequent call to `buffer.prepare` based on the state of the current frame, if any. |