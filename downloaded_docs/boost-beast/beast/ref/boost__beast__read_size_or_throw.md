#### [read\_size\_or\_throw](boost__beast__read_size_or_throw.html "read_size_or_throw")

Returns a natural read size or throw if the buffer is full.

##### [Synopsis](boost__beast__read_size_or_throw.html#beast.ref.boost__beast__read_size_or_throw.synopsis)

Defined in header `<boost/beast/core/read_size.hpp>`

```programlisting
template<
    class DynamicBuffer>
std::size_t
read_size_or_throw(
    DynamicBuffer& buffer,
    std::size_t max_size);
```

##### [Description](boost__beast__read_size_or_throw.html#beast.ref.boost__beast__read_size_or_throw.description)

This function inspects the capacity, size, and maximum size of the dynamic
buffer. Then it computes a natural read size given the passed-in upper limit.
It favors a read size that does not require a reallocation, subject to a
reasonable minimum to avoid tiny reads.

##### [Parameters](boost__beast__read_size_or_throw.html#beast.ref.boost__beast__read_size_or_throw.parameters)

| Name | Description |
| --- | --- |
| `buffer` | The dynamic buffer to inspect. |
| `max_size` | An upper limit on the returned value. |

##### [Exceptions](boost__beast__read_size_or_throw.html#beast.ref.boost__beast__read_size_or_throw.exceptions)

| Type | Thrown On |
| --- | --- |
| `std::length_error` | if `max_size > 0` and the buffer is full. |