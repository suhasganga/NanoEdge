##### [static\_buffer::prepare](prepare.html "static_buffer::prepare")

Returns a mutable buffer sequence representing writable bytes.

###### [Synopsis](prepare.html#beast.ref.boost__beast__static_buffer.prepare.synopsis)

```programlisting
mutable_buffers_type
prepare(
    std::size_t n);
```

###### [Description](prepare.html#beast.ref.boost__beast__static_buffer.prepare.description)

Returns a mutable buffer sequence representing the writable bytes containing
exactly `n` bytes of storage.

All buffers sequences previously obtained using [`data`](data.html "static_buffer::data") or [`prepare`](prepare.html "static_buffer::prepare") may be invalidated.

###### [Parameters](prepare.html#beast.ref.boost__beast__static_buffer.prepare.parameters)

| Name | Description |
| --- | --- |
| `n` | The desired number of bytes in the returned buffer sequence. |

###### [Exceptions](prepare.html#beast.ref.boost__beast__static_buffer.prepare.exceptions)

| Type | Thrown On |
| --- | --- |
| `std::length_error` | if [`size()`](size.html "static_buffer::size") + n exceeds [`max_size()`](../boost__beast__static_buffer_base/max_size.html "static_buffer_base::max_size"). |

###### [Exception Safety](prepare.html#beast.ref.boost__beast__static_buffer.prepare.exception_safety)

Strong guarantee.