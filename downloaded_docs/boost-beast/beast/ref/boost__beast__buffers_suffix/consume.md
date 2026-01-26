##### [buffers\_suffix::consume](consume.html "buffers_suffix::consume")

Remove bytes from the beginning of the sequence.

###### [Synopsis](consume.html#beast.ref.boost__beast__buffers_suffix.consume.synopsis)

```programlisting
void
consume(
    std::size_t amount);
```

###### [Parameters](consume.html#beast.ref.boost__beast__buffers_suffix.consume.parameters)

| Name | Description |
| --- | --- |
| `amount` | The number of bytes to remove. If this is larger than the number of bytes remaining, all the bytes remaining are removed. |