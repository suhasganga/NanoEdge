#### [buffers\_range](boost__beast__buffers_range.html "buffers_range")

Returns an iterable range representing a buffer sequence.

##### [Synopsis](boost__beast__buffers_range.html#beast.ref.boost__beast__buffers_range.synopsis)

Defined in header `<boost/beast/core/buffers_range.hpp>`

```programlisting
template<
    class BufferSequence>
implementation-defined
buffers_range(
    BufferSequence const& buffers);
```

##### [Description](boost__beast__buffers_range.html#beast.ref.boost__beast__buffers_range.description)

This function returns an iterable range representing the passed buffer sequence.
The values obtained when iterating the range will be `net::const_buffer`,
unless the underlying buffer sequence is a *MutableBufferSequence*,
in which case the value obtained when iterating will be a `net::mutable_buffer`.

##### [Example](boost__beast__buffers_range.html#beast.ref.boost__beast__buffers_range.example)

The following function returns the total number of bytes in the specified
buffer sequence. A copy of the buffer sequence is maintained for the lifetime
of the range object:

```programlisting
template < class BufferSequence>
std::size_t buffer_sequence_size (BufferSequence const & buffers)
{
    std::size_t size = 0;
    for ( auto const buffer : buffers_range (buffers))
        size += buffer.size();
    return size;
}
```

##### [Parameters](boost__beast__buffers_range.html#beast.ref.boost__beast__buffers_range.parameters)

| Name | Description |
| --- | --- |
| `buffers` | The buffer sequence to adapt into a range. The range object returned from this function will contain a copy of the passed buffer sequence. |

##### [Return Value](boost__beast__buffers_range.html#beast.ref.boost__beast__buffers_range.return_value)

An object of unspecified type which meets the requirements of *ConstBufferSequence*.
If `buffers` is a mutable buffer
sequence, the returned object will also meet the requirements of *MutableBufferSequence*.

##### [See Also](boost__beast__buffers_range.html#beast.ref.boost__beast__buffers_range.see_also)

[`buffers_range_ref`](boost__beast__buffers_range_ref.html "buffers_range_ref")