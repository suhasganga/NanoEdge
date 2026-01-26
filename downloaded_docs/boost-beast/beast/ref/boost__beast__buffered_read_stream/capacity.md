##### [buffered\_read\_stream::capacity](capacity.html "buffered_read_stream::capacity")

Set the maximum buffer size.

###### [Synopsis](capacity.html#beast.ref.boost__beast__buffered_read_stream.capacity.synopsis)

```programlisting
void
capacity(
    std::size_t size);
```

###### [Description](capacity.html#beast.ref.boost__beast__buffered_read_stream.capacity.description)

This changes the maximum size of the internal buffer used to hold read
data. No bytes are discarded by this call. If the buffer size is set to
zero, no more data will be buffered.

Thread safety: The caller is responsible for making sure the call is made
from the same implicit or explicit strand.

###### [Parameters](capacity.html#beast.ref.boost__beast__buffered_read_stream.capacity.parameters)

| Name | Description |
| --- | --- |
| `size` | The number of bytes in the read buffer. |

###### [Remarks](capacity.html#beast.ref.boost__beast__buffered_read_stream.capacity.remarks)

This is a soft limit. If the new maximum size is smaller than the amount
of data in the buffer, no bytes are discarded.