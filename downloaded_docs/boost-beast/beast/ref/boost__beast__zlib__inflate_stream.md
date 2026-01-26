#### [zlib::inflate\_stream](boost__beast__zlib__inflate_stream.html "zlib::inflate_stream")

Raw deflate stream decompressor.

##### [Synopsis](boost__beast__zlib__inflate_stream.html#beast.ref.boost__beast__zlib__inflate_stream.synopsis)

Defined in header `<boost/beast/zlib/inflate_stream.hpp>`

```programlisting
class inflate_stream
```

##### [Member Functions](boost__beast__zlib__inflate_stream.html#beast.ref.boost__beast__zlib__inflate_stream.member_functions)

| Name | Description |
| --- | --- |
| **[clear](boost__beast__zlib__inflate_stream/clear.html "zlib::inflate_stream::clear")** | Put the stream in a newly constructed state. |
| **[inflate\_stream](boost__beast__zlib__inflate_stream/inflate_stream.html "zlib::inflate_stream::inflate_stream") [constructor]** | Construct a raw deflate decompression stream. |
| **[reset](boost__beast__zlib__inflate_stream/reset.html "zlib::inflate_stream::reset")** | Reset the stream. |
| **[write](boost__beast__zlib__inflate_stream/write.html "zlib::inflate_stream::write")** | Decompress input and produce output. |

##### [Description](boost__beast__zlib__inflate_stream.html#beast.ref.boost__beast__zlib__inflate_stream.description)

This implements a raw deflate stream decompressor. The deflate protocol is
a compression protocol described in "DEFLATE Compressed Data Format
Specification version 1.3" located here: <https://tools.ietf.org/html/rfc1951>

The implementation is a refactored port to C++ of ZLib's "inflate".
A more detailed description of ZLib is at <http://zlib.net/>.

Compression can be done in a single step if the buffers are large enough
(for example if an input file is memory mapped), or can be done by repeated
calls of the compression function. In the latter case, the application must
provide more input and/or consume the output (providing more output space)
before each call.