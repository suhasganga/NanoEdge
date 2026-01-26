##### [zlib::deflate\_stream::prime](prime.html "zlib::deflate_stream::prime")

Insert bits into the compressed output stream.

###### [Synopsis](prime.html#beast.ref.boost__beast__zlib__deflate_stream.prime.synopsis)

```programlisting
void
prime(
    int bits,
    int value,
    error_code& ec);
```

###### [Description](prime.html#beast.ref.boost__beast__zlib__deflate_stream.prime.description)

This function inserts bits in the deflate output stream. The intent is
that this function is used to start off the deflate output with the bits
leftover from a previous deflate stream when appending to it. As such,
this function can only be used for raw deflate, and must be used before
the first `write` call after
an initialization. `bits`
must be less than or equal to 16, and that many of the least significant
bits of `value` will be inserted
in the output.

###### [Return Value](prime.html#beast.ref.boost__beast__zlib__deflate_stream.prime.return_value)

[`error::need_buffers`](../boost__beast__zlib__error.html "zlib::error")
if there was not enough room in the internal buffer to insert the bits.