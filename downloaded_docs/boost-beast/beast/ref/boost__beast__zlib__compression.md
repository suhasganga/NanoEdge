#### [zlib::compression](boost__beast__zlib__compression.html "zlib::compression")

Compression levels.

##### [Synopsis](boost__beast__zlib__compression.html#beast.ref.boost__beast__zlib__compression.synopsis)

Defined in header `<boost/beast/zlib/zlib.hpp>`

```programlisting
enum compression
```

##### [Values](boost__beast__zlib__compression.html#beast.ref.boost__beast__zlib__compression.values)

| Name | Description |
| --- | --- |
| `none` |  |
| `best_speed` |  |
| `best_size` |  |
| `default_size` |  |

##### [Description](boost__beast__zlib__compression.html#beast.ref.boost__beast__zlib__compression.description)

The compression levels go from 0 and 9: 1 gives best speed, 9 gives best
compression.

Compression level 0 gives no compression at all. The input data is simply
copied a block at a time.

A compression level 6 is usually a default compromise between speed and compression.