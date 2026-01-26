##### [zlib::inflate\_stream::write](write.html "zlib::inflate_stream::write")

Decompress input and produce output.

###### [Synopsis](write.html#beast.ref.boost__beast__zlib__inflate_stream.write.synopsis)

```programlisting
void
write(
    z_params& zs,
    Flush flush,
    error_code& ec);
```

###### [Description](write.html#beast.ref.boost__beast__zlib__inflate_stream.write.description)

This function decompresses as much data as possible, and stops when the
input buffer becomes empty or the output buffer becomes full. It may introduce
some output latency (reading input without producing any output) except
when forced to flush.

One or both of the following actions are performed:

* Decompress more input starting at `zs.next_in`
  and update `zs.next_in` and `zs.avail_in`
  accordingly. If not all input can be processed (because there is not
  enough room in the output buffer), `zs.next_in`
  is updated and processing will resume at this point for the next call.
* Provide more output starting at `zs.next_out`
  and update `zs.next_out` and `zs.avail_out`
  accordingly. `write`
  provides as much output as possible, until there is no more input data
  or no more space in the output buffer (see below about the flush parameter).

Before the call, the application should ensure that at least one of the
actions is possible, by providing more input and/or consuming more output,
and updating the values in `zs`
accordingly. The application can consume the uncompressed output when it
wants, for example when the output buffer is full (`zs.avail_out
== 0`),
or after each call. If `write`
returns no error and with zero `zs.avail_out`,
it must be called again after making room in the output buffer because
there might be more output pending.

The flush parameter may be [`Flush::none`](../boost__beast__zlib__Flush.html "zlib::Flush"), [`Flush::sync`](../boost__beast__zlib__Flush.html "zlib::Flush"), [`Flush::finish`](../boost__beast__zlib__Flush.html "zlib::Flush"), [`Flush::block`](../boost__beast__zlib__Flush.html "zlib::Flush"), or [`Flush::trees`](../boost__beast__zlib__Flush.html "zlib::Flush"). [`Flush::sync`](../boost__beast__zlib__Flush.html "zlib::Flush") requests to flush as much
output as possible to the output buffer. [`Flush::block`](../boost__beast__zlib__Flush.html "zlib::Flush") requests to stop if and
when it gets to the next deflate block boundary. When decoding the zlib
or gzip format, this will cause `write`
to return immediately after the header and before the first block. When
doing a raw inflate, `write`
will go ahead and process the first block, and will return when it gets
to the end of that block, or when it runs out of data.

The [`Flush::block`](../boost__beast__zlib__Flush.html "zlib::Flush")
option assists in appending to or combining deflate streams. Also to assist
in this, on return `write`
will set `zs.data_type` to the number of unused bits
in the last byte taken from `zs.next_in`,
plus 64 if `write` is currently
decoding the last block in the deflate stream, plus 128 if `write` returned immediately after decoding
an end-of-block code or decoding the complete header up to just before
the first byte of the deflate stream. The end-of-block will not be indicated
until all of the uncompressed data from that block has been written to
`zs.next_out`. The number of unused bits may
in general be greater than seven, except when bit 7 of `zs.data_type`
is set, in which case the number of unused bits will be less than eight.
`zs.data_type` is set as noted here every
time `write` returns for
all flush options, and so can be used to determine the amount of currently
consumed input in bits.

The [`Flush::trees`](../boost__beast__zlib__Flush.html "zlib::Flush")
option behaves as [`Flush::block`](../boost__beast__zlib__Flush.html "zlib::Flush") does, but it also returns
when the end of each deflate block header is reached, before any actual
data in that block is decoded. This allows the caller to determine the
length of the deflate block header for later use in random access within
a deflate block. 256 is added to the value of `zs.data_type`
when `write` returns immediately
after reaching the end of the deflate block header.

`write` should normally be
called until it returns [`error::end_of_stream`](../boost__beast__zlib__error.html "zlib::error") or another error.
However if all decompression is to be performed in a single step (a single
call of `write`), the parameter
flush should be set to [`Flush::finish`](../boost__beast__zlib__Flush.html "zlib::Flush"). In this case all pending
input is processed and all pending output is flushed; `zs.avail_out`
must be large enough to hold all of the uncompressed data for the operation
to complete. (The size of the uncompressed data may have been saved by
the compressor for this purpose.) The use of [`Flush::finish`](../boost__beast__zlib__Flush.html "zlib::Flush") is not required to perform
an inflation in one step. However it may be used to inform inflate that
a faster approach can be used for the single call. [`Flush::finish`](../boost__beast__zlib__Flush.html "zlib::Flush") also informs inflate to
not maintain a sliding window if the stream completes, which reduces inflate's
memory footprint. If the stream does not complete, either because not all
of the stream is provided or not enough output space is provided, then
a sliding window will be allocated and `write`
can be called again to continue the operation as if [`Flush::none`](../boost__beast__zlib__Flush.html "zlib::Flush") had been used.

In this implementation, `write`
always flushes as much output as possible to the output buffer, and always
uses the faster approach on the first call. So the effects of the flush
parameter in this implementation are on the return value of `write` as noted below, when `write` returns early when [`Flush::block`](../boost__beast__zlib__Flush.html "zlib::Flush") or [`Flush::trees`](../boost__beast__zlib__Flush.html "zlib::Flush") is used, and when `write` avoids the allocation of memory
for a sliding window when [`Flush::finish`](../boost__beast__zlib__Flush.html "zlib::Flush") is used.

If a preset dictionary is needed after this call, `write`
sets `zs.adler` to the Adler-32 checksum of the
dictionary chosen by the compressor and returns `error::need_dictionary`;
otherwise it sets `zs.adler` to the Adler-32 checksum of all
output produced so far (that is, `zs.total_out
bytes`) and returns no error,
[`error::end_of_stream`](../boost__beast__zlib__error.html "zlib::error"),
or an error code as described below. At the end of the stream, `write` checks that its computed adler32
checksum is equal to that saved by the compressor and returns [`error::end_of_stream`](../boost__beast__zlib__error.html "zlib::error") only if the checksum
is correct.

This function returns no error if some progress has been made (more input
processed or more output produced), [`error::end_of_stream`](../boost__beast__zlib__error.html "zlib::error") if the end of the
compressed data has been reached and all uncompressed output has been produced,
`error::need_dictionary` if a preset dictionary
is needed at this point, `error::invalid_data`
if the input data was corrupted (input stream not conforming to the zlib
format or incorrect check value), [`error::stream_error`](../boost__beast__zlib__error.html "zlib::error") if the stream structure
was inconsistent (for example if `zs.next_in`
or `zs.next_out` was null), [`error::need_buffers`](../boost__beast__zlib__error.html "zlib::error") if no progress is
possible or if there was not enough room in the output buffer when [`Flush::finish`](../boost__beast__zlib__Flush.html "zlib::Flush")
is used. Note that [`error::need_buffers`](../boost__beast__zlib__error.html "zlib::error") is not fatal, and
`write` can be called again
with more input and more output space to continue decompressing.