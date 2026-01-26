##### [zlib::deflate\_stream::pending](pending.html "zlib::deflate_stream::pending")

Return bits pending in the output.

###### [Synopsis](pending.html#beast.ref.boost__beast__zlib__deflate_stream.pending.synopsis)

```programlisting
void
pending(
    unsigned* value,
    int* bits);
```

###### [Description](pending.html#beast.ref.boost__beast__zlib__deflate_stream.pending.description)

This function returns the number of bytes and bits of output that have
been generated, but not yet provided in the available output. The bytes
not provided would be due to the available output space having being consumed.
The number of bits of output not provided are between 0 and 7, where they
await more bits to join them in order to fill out a full byte. If pending
or bits are `nullptr`, then
those values are not set.

###### [Return Value](pending.html#beast.ref.boost__beast__zlib__deflate_stream.pending.return_value)

`Z_OK` if success, or `Z_STREAM_ERROR` if the source stream state
was inconsistent.