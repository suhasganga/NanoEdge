##### [static\_buffer::consume](consume.html "static_buffer::consume")

Remove bytes from beginning of the readable bytes.

###### [Synopsis](consume.html#beast.ref.boost__beast__static_buffer.consume.synopsis)

```programlisting
void
consume(
    std::size_t n);
```

###### [Description](consume.html#beast.ref.boost__beast__static_buffer.consume.description)

Removes n bytes from the beginning of the readable bytes.

All buffers sequences previously obtained using [`data`](data.html "static_buffer::data") or [`prepare`](prepare.html "static_buffer::prepare") are invalidated.

###### [Parameters](consume.html#beast.ref.boost__beast__static_buffer.consume.parameters)

| Name | Description |
| --- | --- |
| `n` | The number of bytes to remove. If this number is greater than the number of readable bytes, all readable bytes are removed. |

###### [Exception Safety](consume.html#beast.ref.boost__beast__static_buffer.consume.exception_safety)

No-throw guarantee.