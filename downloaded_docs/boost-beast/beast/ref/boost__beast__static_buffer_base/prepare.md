##### [static\_buffer\_base::prepare](prepare.html "static_buffer_base::prepare")

Returns a mutable buffer sequence representing writable bytes.

###### [Synopsis](prepare.html#beast.ref.boost__beast__static_buffer_base.prepare.synopsis)

```programlisting
mutable_buffers_type
prepare(
    std::size_t n);
```

###### [Description](prepare.html#beast.ref.boost__beast__static_buffer_base.prepare.description)

Returns a mutable buffer sequence representing the writable bytes containing
exactly `n` bytes of storage.

All buffers sequences previously obtained using [`data`](data.html "static_buffer_base::data") or [`prepare`](prepare.html "static_buffer_base::prepare") may be invalidated.

###### [Parameters](prepare.html#beast.ref.boost__beast__static_buffer_base.prepare.parameters)

| Name | Description |
| --- | --- |
| `n` | The desired number of bytes in the returned buffer sequence. |

###### [Exceptions](prepare.html#beast.ref.boost__beast__static_buffer_base.prepare.exceptions)

| Type | Thrown On |
| --- | --- |
| `std::length_error` | if [`size()`](size.html "static_buffer_base::size") + n exceeds [`max_size()`](max_size.html "static_buffer_base::max_size"). |

###### [Exception Safety](prepare.html#beast.ref.boost__beast__static_buffer_base.prepare.exception_safety)

Strong guarantee.