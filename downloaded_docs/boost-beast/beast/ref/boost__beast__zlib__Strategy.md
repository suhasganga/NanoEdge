#### [zlib::Strategy](boost__beast__zlib__Strategy.html "zlib::Strategy")

Compression strategy.

##### [Synopsis](boost__beast__zlib__Strategy.html#beast.ref.boost__beast__zlib__Strategy.synopsis)

Defined in header `<boost/beast/zlib/zlib.hpp>`

```programlisting
enum Strategy
```

##### [Values](boost__beast__zlib__Strategy.html#beast.ref.boost__beast__zlib__Strategy.values)

| Name | Description |
| --- | --- |
| `normal` | Default strategy.  This is suitable for general purpose compression, and works well in the majority of cases. |
| `filtered` | Filtered strategy.  This strategy should be used when the data be compressed is produced by a filter or predictor. |
| `huffman` | Huffman-only strategy.  This strategy only performs Huffman encoding, without doing any string matching. |
| `rle` | Run Length Encoding strategy.  This strategy limits match distances to one, making it equivalent to run length encoding. This can give better performance for things like PNG image data. |
| `fixed` | Fixed table strategy.  This strategy prevents the use of dynamic Huffman codes, allowing for a simpler decoder for special applications. |

##### [Description](boost__beast__zlib__Strategy.html#beast.ref.boost__beast__zlib__Strategy.description)

These are used when compressing streams.