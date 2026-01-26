#### [buffers\_iterator\_type](boost__beast__buffers_iterator_type.html "buffers_iterator_type")

Type alias for the iterator type of a buffer sequence type.

##### [Synopsis](boost__beast__buffers_iterator_type.html#beast.ref.boost__beast__buffers_iterator_type.synopsis)

Defined in header `<boost/beast/core/buffer_traits.hpp>`

```programlisting
template<
    class BufferSequence>
using buffers_iterator_type = see-below;
```

##### [Description](boost__beast__buffers_iterator_type.html#beast.ref.boost__beast__buffers_iterator_type.description)

This metafunction is used to determine the type of iterator used by a particular
buffer sequence.

##### [Template Parameters](boost__beast__buffers_iterator_type.html#beast.ref.boost__beast__buffers_iterator_type.template_parameters)

| Type | Description |
| --- | --- |
| `T` | The buffer sequence type to use. The resulting type alias will be equal to the iterator type used by the buffer sequence. |