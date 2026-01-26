##### [buffers\_adaptor::commit](commit.html "buffers_adaptor::commit")

Append writable bytes to the readable bytes.

###### [Synopsis](commit.html#beast.ref.boost__beast__buffers_adaptor.commit.synopsis)

```programlisting
void
commit(
    std::size_t n);
```

###### [Description](commit.html#beast.ref.boost__beast__buffers_adaptor.commit.description)

Appends n bytes from the start of the writable bytes to the end of the
readable bytes. The remainder of the writable bytes are discarded. If n
is greater than the number of writable bytes, all writable bytes are appended
to the readable bytes.

All buffer sequences previously obtained using [`prepare`](prepare.html "buffers_adaptor::prepare") are invalidated. Buffer
sequences previously obtained using [`data`](data.html "buffers_adaptor::data") remain valid.

###### [Parameters](commit.html#beast.ref.boost__beast__buffers_adaptor.commit.parameters)

| Name | Description |
| --- | --- |
| `n` | The number of bytes to append. If this number is greater than the number of writable bytes, all writable bytes are appended. |

###### [Exception Safety](commit.html#beast.ref.boost__beast__buffers_adaptor.commit.exception_safety)

No-throw guarantee.