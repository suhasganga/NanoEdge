#### [buffers\_range\_ref](boost__beast__buffers_range_ref.html "buffers_range_ref")

Returns an iterable range representing a buffer sequence.

##### [Synopsis](boost__beast__buffers_range_ref.html#beast.ref.boost__beast__buffers_range_ref.synopsis)

Defined in header `<boost/beast/core/buffers_range.hpp>`

```programlisting
template<
    class BufferSequence>
implementation-defined
buffers_range_ref(
    BufferSequence const& buffers);
```

##### [Description](boost__beast__buffers_range_ref.html#beast.ref.boost__beast__buffers_range_ref.description)

This function returns an iterable range representing the passed buffer sequence.
The values obtained when iterating the range will be `net::const_buffer`,
unless the underlying buffer sequence is a *MutableBufferSequence*,
in which case the value obtained when iterating will be a `net::mutable_buffer`.

##### [Example](boost__beast__buffers_range_ref.html#beast.ref.boost__beast__buffers_range_ref.example)

The following function returns the total number of bytes in the specified
buffer sequence. A reference to the original buffers is maintained for the
lifetime of the range object:

```programlisting
template < class BufferSequence>
std::size_t buffer_sequence_size_ref (BufferSequence const & buffers)
{
    std::size_t size = 0;
    for ( auto const buffer : buffers_range_ref (buffers))
        size += buffer.size();
    return size;
}
```

##### [Parameters](boost__beast__buffers_range_ref.html#beast.ref.boost__beast__buffers_range_ref.parameters)

| Name | Description |
| --- | --- |
| `buffers` | The buffer sequence to adapt into a range. The range returned from this function will maintain a reference to these buffers. The application is responsible for ensuring that the lifetime of the referenced buffers extends until the range object is destroyed. |

##### [Return Value](boost__beast__buffers_range_ref.html#beast.ref.boost__beast__buffers_range_ref.return_value)

An object of unspecified type which meets the requirements of *ConstBufferSequence*.
If `buffers` is a mutable buffer
sequence, the returned object will also meet the requirements of *MutableBufferSequence*.

##### [See Also](boost__beast__buffers_range_ref.html#beast.ref.boost__beast__buffers_range_ref.see_also)

[`buffers_range`](boost__beast__buffers_range.html "buffers_range")