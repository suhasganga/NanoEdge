#### [buffers\_suffix](boost__beast__buffers_suffix.html "buffers_suffix")

Adaptor to progressively trim the front of a *BufferSequence*.

##### [Synopsis](boost__beast__buffers_suffix.html#beast.ref.boost__beast__buffers_suffix.synopsis)

Defined in header `<boost/beast/core/buffers_suffix.hpp>`

```programlisting
template<
    class BufferSequence>
class buffers_suffix
```

##### [Types](boost__beast__buffers_suffix.html#beast.ref.boost__beast__buffers_suffix.types)

| Name | Description |
| --- | --- |
| **[const\_iterator](boost__beast__buffers_suffix/const_iterator.html "buffers_suffix::const_iterator")** | A bidirectional iterator type that may be used to read elements. |
| **[value\_type](boost__beast__buffers_suffix/value_type.html "buffers_suffix::value_type")** | The type for each element in the list of buffers. |

##### [Member Functions](boost__beast__buffers_suffix.html#beast.ref.boost__beast__buffers_suffix.member_functions)

| Name | Description |
| --- | --- |
| **[begin](boost__beast__buffers_suffix/begin.html "buffers_suffix::begin")** | Get a bidirectional iterator to the first element. |
| **[buffers\_suffix](boost__beast__buffers_suffix/buffers_suffix.html "buffers_suffix::buffers_suffix") [constructor]** | Constructor.  — Copy Constructor. |
| **[consume](boost__beast__buffers_suffix/consume.html "buffers_suffix::consume")** | Remove bytes from the beginning of the sequence. |
| **[end](boost__beast__buffers_suffix/end.html "buffers_suffix::end")** | Get a bidirectional iterator to one past the last element. |
| **[operator=](boost__beast__buffers_suffix/operator_eq_.html "buffers_suffix::operator=")** | Copy Assignment. |

##### [Description](boost__beast__buffers_suffix.html#beast.ref.boost__beast__buffers_suffix.description)

This adaptor wraps a buffer sequence to create a new sequence which may be
incrementally consumed. Bytes consumed are removed from the front of the
buffer. The underlying memory is not changed, instead the adaptor efficiently
iterates through a subset of the buffers wrapped.

The wrapped buffer is not modified, a copy is made instead. Ownership of
the underlying memory is not transferred, the application is still responsible
for managing its lifetime.

##### [Template Parameters](boost__beast__buffers_suffix.html#beast.ref.boost__beast__buffers_suffix.template_parameters)

| Type | Description |
| --- | --- |
| `BufferSequence` | The buffer sequence to wrap. |

##### [Example](boost__beast__buffers_suffix.html#beast.ref.boost__beast__buffers_suffix.example)

This function writes the entire contents of a buffer sequence to the specified
stream.

```programlisting
template < class SyncWriteStream, class ConstBufferSequence>
void send(SyncWriteStream& stream, ConstBufferSequence const & buffers)
{
    buffers_suffix<ConstBufferSequence> bs{buffers};
    while (buffer_bytes(bs) > 0)
        bs.consume(stream.write_some(bs));
}
```