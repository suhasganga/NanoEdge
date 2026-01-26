##### [zlib::deflate\_stream::params](params.html "zlib::deflate_stream::params")

Update the compression level and strategy.

###### [Synopsis](params.html#beast.ref.boost__beast__zlib__deflate_stream.params.synopsis)

```programlisting
void
params(
    z_params& zs,
    int level,
    Strategy strategy,
    error_code& ec);
```

###### [Description](params.html#beast.ref.boost__beast__zlib__deflate_stream.params.description)

This function dynamically updates the compression level and compression
strategy. The interpretation of level and strategy is as in [`reset`](reset.html "zlib::deflate_stream::reset"). This can be used to switch
between compression and straight copy of the input data, or to switch to
a different kind of input data requiring a different strategy. If the compression
level is changed, the input available so far is compressed with the old
level (and may be flushed); the new level will take effect only at the
next call of [`write`](write.html "zlib::deflate_stream::write").

Before the call of `params`,
the stream state must be set as for a call of [`write`](write.html "zlib::deflate_stream::write"), since the currently available
input may have to be compressed and flushed. In particular, `zs.avail_out`
must be non-zero.

###### [Return Value](params.html#beast.ref.boost__beast__zlib__deflate_stream.params.return_value)

`Z_OK` if success, `Z_STREAM_ERROR` if the source stream state
was inconsistent or if a parameter was invalid, [`error::need_buffers`](../boost__beast__zlib__error.html "zlib::error") if `zs.avail_out`
was zero.