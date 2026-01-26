##### [buffer\_ref::commit](commit.html "buffer_ref::commit")

Move bytes from the output sequence to the input sequence.

###### [Synopsis](commit.html#beast.ref.boost__beast__buffer_ref.commit.synopsis)

```programlisting
void
commit(
    std::size_t n);
```

###### [Description](commit.html#beast.ref.boost__beast__buffer_ref.commit.description)

###### [Parameters](commit.html#beast.ref.boost__beast__buffer_ref.commit.parameters)

| Name | Description |
| --- | --- |
| `n` | The number of bytes to append from the start of the output sequence to the end of the input sequence. The remainder of the output sequence is discarded. |

Requires a preceding call `prepare(x)`
where `x >=
n`, and no intervening operations
that modify the input or output sequence.

###### [Remarks](commit.html#beast.ref.boost__beast__buffer_ref.commit.remarks)

If `n` is greater than the
size of the output sequence, the entire output sequence is moved to the
input sequence and no error is issued.