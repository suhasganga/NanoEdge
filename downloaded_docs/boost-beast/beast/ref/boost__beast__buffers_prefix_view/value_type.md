##### [buffers\_prefix\_view::value\_type](value_type.html "buffers_prefix_view::value_type")

The type for each element in the list of buffers.

###### [Synopsis](value_type.html#beast.ref.boost__beast__buffers_prefix_view.value_type.synopsis)

```programlisting
using value_type = see-below;
```

###### [Description](value_type.html#beast.ref.boost__beast__buffers_prefix_view.value_type.description)

If the type `BufferSequence`
meets the requirements of *MutableBufferSequence*, then
[`value_type`](value_type.html "buffers_prefix_view::value_type") is `net::mutable_buffer`.
Otherwise, [`value_type`](value_type.html "buffers_prefix_view::value_type") is `net::const_buffer`.

###### [See Also](value_type.html#beast.ref.boost__beast__buffers_prefix_view.value_type.see_also)

[`buffers_type`](../boost__beast__buffers_type.html "buffers_type")