##### [basic\_flat\_buffer::prepare](prepare.html "basic_flat_buffer::prepare")

Returns a mutable buffer sequence representing writable bytes.

###### [Synopsis](prepare.html#beast.ref.boost__beast__basic_flat_buffer.prepare.synopsis)

```programlisting
mutable_buffers_type
prepare(
    std::size_t n);
```

###### [Description](prepare.html#beast.ref.boost__beast__basic_flat_buffer.prepare.description)

Returns a mutable buffer sequence representing the writable bytes containing
exactly `n` bytes of storage.
Memory may be reallocated as needed.

All buffers sequences previously obtained using [`data`](data.html "basic_flat_buffer::data") or [`prepare`](prepare.html "basic_flat_buffer::prepare") become invalid.

###### [Parameters](prepare.html#beast.ref.boost__beast__basic_flat_buffer.prepare.parameters)

| Name | Description |
| --- | --- |
| `n` | The desired number of bytes in the returned buffer sequence. |

###### [Exceptions](prepare.html#beast.ref.boost__beast__basic_flat_buffer.prepare.exceptions)

| Type | Thrown On |
| --- | --- |
| `std::length_error` | if [`size()`](size.html "basic_flat_buffer::size") + n exceeds either [`max_size()`](max_size.html "basic_flat_buffer::max_size") or the allocator's maximum allocation size. |

###### [Exception Safety](prepare.html#beast.ref.boost__beast__basic_flat_buffer.prepare.exception_safety)

Strong guarantee.