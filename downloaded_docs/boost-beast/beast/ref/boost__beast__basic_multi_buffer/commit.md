##### [basic\_multi\_buffer::commit](commit.html "basic_multi_buffer::commit")

Append writable bytes to the readable bytes.

###### [Synopsis](commit.html#beast.ref.boost__beast__basic_multi_buffer.commit.synopsis)

```programlisting
void
commit(
    size_type n);
```

###### [Description](commit.html#beast.ref.boost__beast__basic_multi_buffer.commit.description)

Appends n bytes from the start of the writable bytes to the end of the
readable bytes. The remainder of the writable bytes are discarded. If n
is greater than the number of writable bytes, all writable bytes are appended
to the readable bytes.

All buffer sequences previously obtained using [`prepare`](prepare.html "basic_multi_buffer::prepare") are invalidated. Buffer
sequences previously obtained using [`data`](data.html "basic_multi_buffer::data") remain valid.

###### [Parameters](commit.html#beast.ref.boost__beast__basic_multi_buffer.commit.parameters)

| Name | Description |
| --- | --- |
| `n` | The number of bytes to append. If this number is greater than the number of writable bytes, all writable bytes are appended. |

###### [Exception Safety](commit.html#beast.ref.boost__beast__basic_multi_buffer.commit.exception_safety)

No-throw guarantee.