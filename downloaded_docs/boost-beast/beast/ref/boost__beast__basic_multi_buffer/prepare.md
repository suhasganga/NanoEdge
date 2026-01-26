##### [basic\_multi\_buffer::prepare](prepare.html "basic_multi_buffer::prepare")

Returns a mutable buffer sequence representing writable bytes.

###### [Synopsis](prepare.html#beast.ref.boost__beast__basic_multi_buffer.prepare.synopsis)

```programlisting
mutable_buffers_type
prepare(
    size_type n);
```

###### [Description](prepare.html#beast.ref.boost__beast__basic_multi_buffer.prepare.description)

Returns a mutable buffer sequence representing the writable bytes containing
exactly `n` bytes of storage.
Memory may be reallocated as needed.

All buffer sequences previously obtained using [`prepare`](prepare.html "basic_multi_buffer::prepare") are invalidated. Buffer
sequences previously obtained using [`data`](data.html "basic_multi_buffer::data") remain valid.

###### [Parameters](prepare.html#beast.ref.boost__beast__basic_multi_buffer.prepare.parameters)

| Name | Description |
| --- | --- |
| `n` | The desired number of bytes in the returned buffer sequence. |

###### [Exceptions](prepare.html#beast.ref.boost__beast__basic_multi_buffer.prepare.exceptions)

| Type | Thrown On |
| --- | --- |
| `std::length_error` | if [`size()`](size.html "basic_multi_buffer::size") + n exceeds [`max_size()`](max_size.html "basic_multi_buffer::max_size"). |

###### [Exception Safety](prepare.html#beast.ref.boost__beast__basic_multi_buffer.prepare.exception_safety)

Strong guarantee.