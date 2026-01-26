#### [buffers\_prefix](boost__beast__buffers_prefix.html "buffers_prefix")

Returns a prefix of a constant or mutable buffer sequence.

##### [Synopsis](boost__beast__buffers_prefix.html#beast.ref.boost__beast__buffers_prefix.synopsis)

Defined in header `<boost/beast/core/buffers_prefix.hpp>`

```programlisting
template<
    class BufferSequence>
buffers_prefix_view< BufferSequence >
buffers_prefix(
    std::size_t size,
    BufferSequence const& buffers);
```

##### [Description](boost__beast__buffers_prefix.html#beast.ref.boost__beast__buffers_prefix.description)

The returned buffer sequence points to the same memory as the passed buffer
sequence, but with a size that is equal to or smaller. No memory allocations
are performed; the resulting sequence is calculated as a lazy range.

##### [Parameters](boost__beast__buffers_prefix.html#beast.ref.boost__beast__buffers_prefix.parameters)

| Name | Description |
| --- | --- |
| `size` | The maximum size of the returned buffer sequence in bytes. If this is greater than or equal to the size of the passed buffer sequence, the result will have the same size as the original buffer sequence. |
| `buffers` | An object whose type meets the requirements of *BufferSequence*. The returned value will maintain a copy of the passed buffers for its lifetime; however, ownership of the underlying memory is not transferred. |

##### [Return Value](boost__beast__buffers_prefix.html#beast.ref.boost__beast__buffers_prefix.return_value)

A constant buffer sequence that represents the prefix of the original buffer
sequence. If the original buffer sequence also meets the requirements of
*MutableBufferSequence*, then the returned value will
also be a mutable buffer sequence.