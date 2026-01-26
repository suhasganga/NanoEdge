#### [buffers\_front](boost__beast__buffers_front.html "buffers_front")

Returns the first buffer in a buffer sequence.

##### [Synopsis](boost__beast__buffers_front.html#beast.ref.boost__beast__buffers_front.synopsis)

Defined in header `<boost/beast/core/buffers_prefix.hpp>`

```programlisting
template<
    class BufferSequence>
buffers_type< BufferSequence >
buffers_front(
    BufferSequence const& buffers);
```

##### [Description](boost__beast__buffers_front.html#beast.ref.boost__beast__buffers_front.description)

This returns the first buffer in the buffer sequence. If the buffer sequence
is an empty range, the returned buffer will have a zero buffer size.

##### [Parameters](boost__beast__buffers_front.html#beast.ref.boost__beast__buffers_front.parameters)

| Name | Description |
| --- | --- |
| `buffers` | The buffer sequence. If the sequence is mutable, the returned buffer sequence will also be mutable. Otherwise, the returned buffer sequence will be constant. |