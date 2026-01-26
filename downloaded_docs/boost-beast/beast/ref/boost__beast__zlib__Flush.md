#### [zlib::Flush](boost__beast__zlib__Flush.html "zlib::Flush")

[`Flush`](boost__beast__zlib__Flush.html "zlib::Flush")
option.

##### [Synopsis](boost__beast__zlib__Flush.html#beast.ref.boost__beast__zlib__Flush.synopsis)

Defined in header `<boost/beast/zlib/zlib.hpp>`

```programlisting
enum Flush
```

##### [Values](boost__beast__zlib__Flush.html#beast.ref.boost__beast__zlib__Flush.values)

| Name | Description |
| --- | --- |
| `none` | No policy. |
| `block` | [`Flush`](boost__beast__zlib__Flush.html "zlib::Flush") all pending output on a bit boundary and hold up to seven bits. |
| `partial` | [`Flush`](boost__beast__zlib__Flush.html "zlib::Flush") all pending output on a bit boundary. |
| `sync` | [`Flush`](boost__beast__zlib__Flush.html "zlib::Flush") all pending output on a byte boundary. |
| `full` | [`Flush`](boost__beast__zlib__Flush.html "zlib::Flush") all pending output on a byte boundary and reset state. |
| `finish` | Compress the input left in a single step. |
| `trees` | [`Flush`](boost__beast__zlib__Flush.html "zlib::Flush") output as in [`Flush::block`](boost__beast__zlib__Flush.html "zlib::Flush") or at the end of each deflate block header. |

##### [Description](boost__beast__zlib__Flush.html#beast.ref.boost__beast__zlib__Flush.description)

The allowed flush values for the [`deflate_stream::write`](boost__beast__zlib__deflate_stream/write.html "zlib::deflate_stream::write") and [`inflate_stream::write`](boost__beast__zlib__inflate_stream/write.html "zlib::inflate_stream::write") functions.

Please refer to [`deflate_stream::write`](boost__beast__zlib__deflate_stream/write.html "zlib::deflate_stream::write") and [`inflate_stream::write`](boost__beast__zlib__inflate_stream/write.html "zlib::inflate_stream::write") for details.

##### [See Also](boost__beast__zlib__Flush.html#beast.ref.boost__beast__zlib__Flush.see_also)

[`deflate_stream::write`](boost__beast__zlib__deflate_stream/write.html "zlib::deflate_stream::write"), [`inflate_stream::write`](boost__beast__zlib__inflate_stream/write.html "zlib::inflate_stream::write")