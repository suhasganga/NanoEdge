#### [zlib::deflate\_stream](boost__beast__zlib__deflate_stream.html "zlib::deflate_stream")

Raw deflate compressor.

##### [Synopsis](boost__beast__zlib__deflate_stream.html#beast.ref.boost__beast__zlib__deflate_stream.synopsis)

Defined in header `<boost/beast/zlib/deflate_stream.hpp>`

```programlisting
class deflate_stream
```

##### [Member Functions](boost__beast__zlib__deflate_stream.html#beast.ref.boost__beast__zlib__deflate_stream.member_functions)

| Name | Description |
| --- | --- |
| **[clear](boost__beast__zlib__deflate_stream/clear.html "zlib::deflate_stream::clear")** | Clear the stream. |
| **[deflate\_stream](boost__beast__zlib__deflate_stream/deflate_stream.html "zlib::deflate_stream::deflate_stream") [constructor]** | Construct a default deflate stream. |
| **[params](boost__beast__zlib__deflate_stream/params.html "zlib::deflate_stream::params")** | Update the compression level and strategy. |
| **[pending](boost__beast__zlib__deflate_stream/pending.html "zlib::deflate_stream::pending")** | Return bits pending in the output. |
| **[prime](boost__beast__zlib__deflate_stream/prime.html "zlib::deflate_stream::prime")** | Insert bits into the compressed output stream. |
| **[reset](boost__beast__zlib__deflate_stream/reset.html "zlib::deflate_stream::reset")** | Reset the stream and compression settings.  — Reset the stream without deallocating memory. |
| **[tune](boost__beast__zlib__deflate_stream/tune.html "zlib::deflate_stream::tune")** | Fine tune internal compression parameters. |
| **[upper\_bound](boost__beast__zlib__deflate_stream/upper_bound.html "zlib::deflate_stream::upper_bound")** | Returns the upper limit on the size of a compressed block. |
| **[write](boost__beast__zlib__deflate_stream/write.html "zlib::deflate_stream::write")** | Compress input and write output. |

##### [Description](boost__beast__zlib__deflate_stream.html#beast.ref.boost__beast__zlib__deflate_stream.description)

This is a port of zlib's "deflate" functionality to C++.