#### [buffers\_type](boost__beast__buffers_type.html "buffers_type")

Type alias for the underlying buffer type of a list of buffer sequence types.

##### [Synopsis](boost__beast__buffers_type.html#beast.ref.boost__beast__buffers_type.synopsis)

Defined in header `<boost/beast/core/buffer_traits.hpp>`

```programlisting
template<
    class... BufferSequence>
using buffers_type = see-below;
```

##### [Description](boost__beast__buffers_type.html#beast.ref.boost__beast__buffers_type.description)

This metafunction is used to determine the underlying buffer type for a list
of buffer sequence. The equivalent type of the alias will vary depending
on the template type argument:

* If every type in the list is a *MutableBufferSequence*,
  the resulting type alias will be `net::mutable_buffer`,
  otherwise
* The resulting type alias will be `net::const_buffer`.

##### [Example](boost__beast__buffers_type.html#beast.ref.boost__beast__buffers_type.example)

The following code returns the first buffer in a buffer sequence, or generates
a compilation error if the argument is not a buffer sequence:

```programlisting
template < class BufferSequence>
buffers_type <BufferSequence>
buffers_front (BufferSequence const & buffers)
{
    static_assert (
        net::is_const_buffer_sequence<BufferSequence>::value,
        "BufferSequence type requirements not met" );
    auto const first = net::buffer_sequence_begin (buffers);
    if (first == net::buffer_sequence_end (buffers))
        return {};
    return *first;
}
```

##### [Template Parameters](boost__beast__buffers_type.html#beast.ref.boost__beast__buffers_type.template_parameters)

| Type | Description |
| --- | --- |
| `BufferSequence` | A list of zero or more types to check. If this list is empty, the resulting type alias will be `net::mutable_buffer`. |