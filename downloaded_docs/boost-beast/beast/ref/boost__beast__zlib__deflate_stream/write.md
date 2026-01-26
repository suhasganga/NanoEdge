##### [zlib::deflate\_stream::write](write.html "zlib::deflate_stream::write")

Compress input and write output.

###### [Synopsis](write.html#beast.ref.boost__beast__zlib__deflate_stream.write.synopsis)

```programlisting
void
write(
    z_params& zs,
    Flush flush,
    error_code& ec);
```

###### [Description](write.html#beast.ref.boost__beast__zlib__deflate_stream.write.description)

This function compresses as much data as possible, and stops when the input
buffer becomes empty or the output buffer becomes full. It may introduce
some output latency (reading input without producing any output) except
when forced to flush.

In each call, one or both of these actions are performed:

* Compress more input starting at `zs.next_in`
  and update `zs.next_in` and `zs.avail_in`
  accordingly. If not all input can be processed (because there is not
  enough room in the output buffer), `zs.next_in`
  and `zs.avail_in` are updated and processing
  will resume at this point for the next call.
* Provide more output starting at `zs.next_out`
  and update `zs.next_out` and `zs.avail_out`
  accordingly. This action is forced if the parameter flush is not [`Flush::none`](../boost__beast__zlib__Flush.html "zlib::Flush").
  Forcing flush frequently degrades the compression ratio, so this parameter
  should be set only when necessary (in interactive applications). Some
  output may be provided even if flush is not set.

Before the call, the application must ensure that at least one of the actions
is possible, by providing more input and/or consuming more output, and
updating `zs.avail_in` or `zs.avail_out`
accordingly; `zs.avail_out` should never be zero before
the call. The application can consume the compressed output when it wants,
for example when the output buffer is full (`zs.avail_out
== 0`),
or after each call of `write`.
If `write` returns no error
with zero `zs.avail_out`, it must be called again after
making room in the output buffer because there might be more output pending.

Normally the parameter flush is set to [`Flush::none`](../boost__beast__zlib__Flush.html "zlib::Flush"), which allows deflate to
decide how much data to accumulate before producing output, in order to
maximize compression.

If the parameter flush is set to [`Flush::sync`](../boost__beast__zlib__Flush.html "zlib::Flush"), all pending output is flushed
to the output buffer and the output is aligned on a byte boundary, so that
the decompressor can get all input data available so far. In particular
`zs.avail_in` is zero after the call if enough
output space has been provided before the call. Flushing may degrade compression
for some compression algorithms and so it should be used only when necessary.
This completes the current deflate block and follows it with an empty stored
block that is three bits plus filler bits to the next byte, followed by
the four bytes `{ 0x00, 0x00 0xff
0xff }`.

If flush is set to [`Flush::partial`](../boost__beast__zlib__Flush.html "zlib::Flush"), all pending output is
flushed to the output buffer, but the output is not aligned to a byte boundary.
All of the input data so far will be available to the decompressor, as
for Z\_SYNC\_FLUSH. This completes the current deflate block and follows
it with an empty fixed codes block that is 10 bits long. This assures that
enough bytes are output in order for the decompressor to finish the block
before the empty fixed code block.

If flush is set to [`Flush::block`](../boost__beast__zlib__Flush.html "zlib::Flush"), a deflate block is completed
and emitted, as for [`Flush::sync`](../boost__beast__zlib__Flush.html "zlib::Flush"), but the output is not aligned
on a byte boundary, and up to seven bits of the current block are held
to be written as the next byte after the next deflate block is completed.
In this case, the decompressor may not be provided enough bits at this
point in order to complete decompression of the data provided so far to
the compressor. It may need to wait for the next block to be emitted. This
is for advanced applications that need to control the emission of deflate
blocks.

If flush is set to [`Flush::full`](../boost__beast__zlib__Flush.html "zlib::Flush"), all output is flushed as
with [`Flush::sync`](../boost__beast__zlib__Flush.html "zlib::Flush"), and the compression state
is reset so that decompression can restart from this point if previous
compressed data has been damaged or if random access is desired. Using
[`Flush::full`](../boost__beast__zlib__Flush.html "zlib::Flush")
too often can seriously degrade compression.

If `write` returns with
`zs.avail_out ==
0`, this function must be called again
with the same value of the flush parameter and more output space (updated
`zs.avail_out`), until the flush is complete
(`write` returns with non-zero
`zs.avail_out`). In the case of a [`Flush::full`](../boost__beast__zlib__Flush.html "zlib::Flush")or [`Flush::sync`](../boost__beast__zlib__Flush.html "zlib::Flush"), make sure that `zs.avail_out`
is greater than six to avoid repeated flush markers due to `zs.avail_out
== 0`
on return.

If the parameter flush is set to [`Flush::finish`](../boost__beast__zlib__Flush.html "zlib::Flush"), pending input is processed,
pending output is flushed and deflate returns the error [`error::end_of_stream`](../boost__beast__zlib__error.html "zlib::error") if there was enough
output space; if deflate returns with no error, this function must be called
again with [`Flush::finish`](../boost__beast__zlib__Flush.html "zlib::Flush") and more output space (updated
`zs.avail_out`) but no more input data, until
it returns the error [`error::end_of_stream`](../boost__beast__zlib__error.html "zlib::error") or another error.
After `write` has returned
the [`error::end_of_stream`](../boost__beast__zlib__error.html "zlib::error")
error, the only possible operations on the stream are to reset or destroy.

[`Flush::finish`](../boost__beast__zlib__Flush.html "zlib::Flush")
can be used immediately after initialization if all the compression is
to be done in a single step. In this case, `zs.avail_out`
must be at least value returned by `upper_bound`
(see below). Then `write`
is guaranteed to return the [`error::end_of_stream`](../boost__beast__zlib__error.html "zlib::error") error. If not enough
output space is provided, deflate will not return [`error::end_of_stream`](../boost__beast__zlib__error.html "zlib::error"), and it must be
called again as described above.

`write` returns no error
if some progress has been made (more input processed or more output produced),
[`error::end_of_stream`](../boost__beast__zlib__error.html "zlib::error")
if all input has been consumed and all output has been produced (only when
flush is set to [`Flush::finish`](../boost__beast__zlib__Flush.html "zlib::Flush")), [`error::stream_error`](../boost__beast__zlib__error.html "zlib::error") if the stream state
was inconsistent (for example if `zs.next_in`
or `zs.next_out` was `nullptr`),
[`error::need_buffers`](../boost__beast__zlib__error.html "zlib::error")
if no progress is possible (for example `zs.avail_in`
or `zs.avail_out` was zero). Note that [`error::need_buffers`](../boost__beast__zlib__error.html "zlib::error")
is not fatal, and `write`
can be called again with more input and more output space to continue compressing.