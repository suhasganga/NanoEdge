###### [websocket::stream::read\_size\_hint (1 of 2 overloads)](overload1.html "websocket::stream::read_size_hint (1 of 2 overloads)")

Returns a suggested maximum buffer size for the next call to read.

###### [Synopsis](overload1.html#beast.ref.boost__beast__websocket__stream.read_size_hint.overload1.synopsis)

```programlisting
std::size_t
read_size_hint(
    std::size_t initial_size = +tcp_frame_size) const;
```

###### [Description](overload1.html#beast.ref.boost__beast__websocket__stream.read_size_hint.overload1.description)

This function returns a reasonable upper limit on the number of bytes
for the size of the buffer passed in the next call to read. The number
is determined by the state of the current frame and whether or not the
permessage-deflate extension is enabled.

###### [Parameters](overload1.html#beast.ref.boost__beast__websocket__stream.read_size_hint.overload1.parameters)

| Name | Description |
| --- | --- |
| `initial_size` | A non-zero size representing the caller's desired buffer size for when there is no information which may be used to calculate a more specific value. For example, when reading the first frame header of a message. |