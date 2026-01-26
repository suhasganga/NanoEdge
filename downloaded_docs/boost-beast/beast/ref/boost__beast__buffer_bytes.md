#### [buffer\_bytes](boost__beast__buffer_bytes.html "buffer_bytes")

Return the total number of bytes in a buffer or buffer sequence.

##### [Synopsis](boost__beast__buffer_bytes.html#beast.ref.boost__beast__buffer_bytes.synopsis)

Defined in header `<boost/beast/core/buffer_traits.hpp>`

```programlisting
template<
    class BufferSequence>
std::size_t
buffer_bytes(
    BufferSequence const& buffers);
```

##### [Description](boost__beast__buffer_bytes.html#beast.ref.boost__beast__buffer_bytes.description)

This function returns the total number of bytes in a buffer, buffer sequence,
or object convertible to a buffer. Specifically it may be passed:

* A *ConstBufferSequence* or *MutableBufferSequence*
* A `net::const_buffer` or `net::mutable_buffer`
* An object convertible to `net::const_buffer`

This function is designed as an easier-to-use replacement for `net::buffer_size`.
It recognizes customization points found through argument-dependent lookup.
The call `beast::buffer_bytes(b)` is equivalent
to performing:

```programlisting
using net::buffer_size;
return buffer_size(b);
```

In addition this handles types which are convertible to `net::const_buffer`;
these are not handled by `net::buffer_size`.

##### [Parameters](boost__beast__buffer_bytes.html#beast.ref.boost__beast__buffer_bytes.parameters)

| Name | Description |
| --- | --- |
| `buffers` | The buffer or buffer sequence to calculate the size of. |

##### [Return Value](boost__beast__buffer_bytes.html#beast.ref.boost__beast__buffer_bytes.return_value)

The total number of bytes in the buffer or sequence.