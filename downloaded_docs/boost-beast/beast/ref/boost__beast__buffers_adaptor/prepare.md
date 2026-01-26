##### [buffers\_adaptor::prepare](prepare.html "buffers_adaptor::prepare")

Returns a mutable buffer sequence representing writable bytes.

###### [Synopsis](prepare.html#beast.ref.boost__beast__buffers_adaptor.prepare.synopsis)

```programlisting
mutable_buffers_type
prepare(
    std::size_t n);
```

###### [Description](prepare.html#beast.ref.boost__beast__buffers_adaptor.prepare.description)

Returns a mutable buffer sequence representing the writable bytes containing
exactly `n` bytes of storage.
This function does not allocate memory. Instead, the storage comes from
the underlying mutable buffer sequence.

All buffer sequences previously obtained using [`prepare`](prepare.html "buffers_adaptor::prepare") are invalidated. Buffer
sequences previously obtained using [`data`](data.html "buffers_adaptor::data") remain valid.

###### [Parameters](prepare.html#beast.ref.boost__beast__buffers_adaptor.prepare.parameters)

| Name | Description |
| --- | --- |
| `n` | The desired number of bytes in the returned buffer sequence. |

###### [Exceptions](prepare.html#beast.ref.boost__beast__buffers_adaptor.prepare.exceptions)

| Type | Thrown On |
| --- | --- |
| `std::length_error` | if [`size()`](size.html "buffers_adaptor::size") + n exceeds [`max_size()`](max_size.html "buffers_adaptor::max_size"). |

###### [Exception Safety](prepare.html#beast.ref.boost__beast__buffers_adaptor.prepare.exception_safety)

Strong guarantee.