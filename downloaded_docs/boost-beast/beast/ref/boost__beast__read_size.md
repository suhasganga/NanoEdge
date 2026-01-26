#### [read\_size](boost__beast__read_size.html "read_size")

Returns a natural read size.

##### [Synopsis](boost__beast__read_size.html#beast.ref.boost__beast__read_size.synopsis)

Defined in header `<boost/beast/core/read_size.hpp>`

```programlisting
template<
    class DynamicBuffer>
std::size_t
read_size(
    DynamicBuffer& buffer,
    std::size_t max_size);
```

##### [Description](boost__beast__read_size.html#beast.ref.boost__beast__read_size.description)

This function inspects the capacity, size, and maximum size of the dynamic
buffer. Then it computes a natural read size given the passed-in upper limit.
It favors a read size that does not require a reallocation, subject to a
reasonable minimum to avoid tiny reads.

##### [Parameters](boost__beast__read_size.html#beast.ref.boost__beast__read_size.parameters)

| Name | Description |
| --- | --- |
| `buffer` | The dynamic buffer to inspect. |
| `max_size` | An upper limit on the returned value. |

##### [Remarks](boost__beast__read_size.html#beast.ref.boost__beast__read_size.remarks)

If the buffer is already at its maximum size, zero is returned.