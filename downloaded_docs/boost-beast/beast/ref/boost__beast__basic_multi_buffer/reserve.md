##### [basic\_multi\_buffer::reserve](reserve.html "basic_multi_buffer::reserve")

Guarantee a minimum capacity.

###### [Synopsis](reserve.html#beast.ref.boost__beast__basic_multi_buffer.reserve.synopsis)

```programlisting
void
reserve(
    std::size_t n);
```

###### [Description](reserve.html#beast.ref.boost__beast__basic_multi_buffer.reserve.description)

This function adjusts the internal storage (if necessary) to guarantee
space for at least `n` bytes.

Buffer sequences previously obtained using [`data`](data.html "basic_multi_buffer::data") remain valid, while buffer
sequences previously obtained using [`prepare`](prepare.html "basic_multi_buffer::prepare") become invalid.

###### [Parameters](reserve.html#beast.ref.boost__beast__basic_multi_buffer.reserve.parameters)

| Name | Description |
| --- | --- |
| `n` | The minimum number of byte for the new capacity. If this value is greater than the maximum size, then the maximum size will be adjusted upwards to this value. |

###### [Exceptions](reserve.html#beast.ref.boost__beast__basic_multi_buffer.reserve.exceptions)

| Type | Thrown On |
| --- | --- |
| `std::length_error` | if n is larger than the maximum allocation size of the allocator. |

###### [Exception Safety](reserve.html#beast.ref.boost__beast__basic_multi_buffer.reserve.exception_safety)

Strong guarantee.