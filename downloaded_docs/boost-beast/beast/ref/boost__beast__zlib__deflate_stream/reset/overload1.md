###### [zlib::deflate\_stream::reset (1 of 2 overloads)](overload1.html "zlib::deflate_stream::reset (1 of 2 overloads)")

Reset the stream and compression settings.

###### [Synopsis](overload1.html#beast.ref.boost__beast__zlib__deflate_stream.reset.overload1.synopsis)

```programlisting
void
reset(
    int level,
    int windowBits,
    int memLevel,
    Strategy strategy);
```

###### [Description](overload1.html#beast.ref.boost__beast__zlib__deflate_stream.reset.overload1.description)

This function initializes the stream to the specified compression settings.

Although the stream is ready to be used immediately after a reset, any
required internal buffers are not dynamically allocated until needed.

###### [Parameters](overload1.html#beast.ref.boost__beast__zlib__deflate_stream.reset.overload1.parameters)

| Name | Description |
| --- | --- |
| `level` | Compression level from 0 to 9. |
| `windowBits` | The base two logarithm of the window size, or the history buffer. It should be in the range 9..15. |
| `memLevel` | How much memory should be allocated for the internal compression state, with level from from 1 to 9. |
| `strategy` | [`Strategy`](../../boost__beast__zlib__Strategy.html "zlib::Strategy") to tune the compression algorithm. |

###### [Remarks](overload1.html#beast.ref.boost__beast__zlib__deflate_stream.reset.overload1.remarks)

Any unprocessed input or pending output from previous calls are discarded.