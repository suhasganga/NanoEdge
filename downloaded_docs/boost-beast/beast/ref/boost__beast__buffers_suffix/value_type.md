##### [buffers\_suffix::value\_type](value_type.html "buffers_suffix::value_type")

The type for each element in the list of buffers.

###### [Synopsis](value_type.html#beast.ref.boost__beast__buffers_suffix.value_type.synopsis)

```programlisting
using value_type = see-below;
```

###### [Description](value_type.html#beast.ref.boost__beast__buffers_suffix.value_type.description)

If *BufferSequence* meets the requirements of *MutableBufferSequence*,
then this type will be `net::mutable_buffer`,
otherwise this type will be `net::const_buffer`.