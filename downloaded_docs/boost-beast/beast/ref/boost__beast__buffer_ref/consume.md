##### [buffer\_ref::consume](consume.html "buffer_ref::consume")

Remove `n` bytes from the
readable byte sequence.

###### [Synopsis](consume.html#beast.ref.boost__beast__buffer_ref.consume.synopsis)

```programlisting
void
consume(
    std::size_t n);
```

###### [Description](consume.html#beast.ref.boost__beast__buffer_ref.consume.description)

**DynamicBuffer\_v1:**Removes `n` characters from the beginning of the
input sequence.

###### [Remarks](consume.html#beast.ref.boost__beast__buffer_ref.consume.remarks)

If `n` is greater than the
size of the input sequence, the entire input sequence is consumed and no
error is issued.