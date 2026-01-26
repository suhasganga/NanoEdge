##### [buffers\_adaptor::consume](consume.html "buffers_adaptor::consume")

Remove bytes from beginning of the readable bytes.

###### [Synopsis](consume.html#beast.ref.boost__beast__buffers_adaptor.consume.synopsis)

```programlisting
void
consume(
    std::size_t n);
```

###### [Description](consume.html#beast.ref.boost__beast__buffers_adaptor.consume.description)

Removes n bytes from the beginning of the readable bytes.

All buffers sequences previously obtained using [`data`](data.html "buffers_adaptor::data") or [`prepare`](prepare.html "buffers_adaptor::prepare") are invalidated.

###### [Parameters](consume.html#beast.ref.boost__beast__buffers_adaptor.consume.parameters)

| Name | Description |
| --- | --- |
| `n` | The number of bytes to remove. If this number is greater than the number of readable bytes, all readable bytes are removed. |

###### [Exception Safety](consume.html#beast.ref.boost__beast__buffers_adaptor.consume.exception_safety)

No-throw guarantee.