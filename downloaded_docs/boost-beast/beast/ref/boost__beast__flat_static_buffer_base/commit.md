##### [flat\_static\_buffer\_base::commit](commit.html "flat_static_buffer_base::commit")

Append writable bytes to the readable bytes.

###### [Synopsis](commit.html#beast.ref.boost__beast__flat_static_buffer_base.commit.synopsis)

```programlisting
void
commit(
    std::size_t n);
```

###### [Description](commit.html#beast.ref.boost__beast__flat_static_buffer_base.commit.description)

Appends n bytes from the start of the writable bytes to the end of the
readable bytes. The remainder of the writable bytes are discarded. If n
is greater than the number of writable bytes, all writable bytes are appended
to the readable bytes.

All buffers sequences previously obtained using [`data`](data.html "flat_static_buffer_base::data") or [`prepare`](prepare.html "flat_static_buffer_base::prepare") are invalidated.

###### [Parameters](commit.html#beast.ref.boost__beast__flat_static_buffer_base.commit.parameters)

| Name | Description |
| --- | --- |
| `n` | The number of bytes to append. If this number is greater than the number of writable bytes, all writable bytes are appended. |

###### [Exception Safety](commit.html#beast.ref.boost__beast__flat_static_buffer_base.commit.exception_safety)

No-throw guarantee.