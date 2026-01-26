#### [zlib::deflate\_upper\_bound](boost__beast__zlib__deflate_upper_bound.html "zlib::deflate_upper_bound")

Returns the upper limit on the size of a compressed block.

##### [Synopsis](boost__beast__zlib__deflate_upper_bound.html#beast.ref.boost__beast__zlib__deflate_upper_bound.synopsis)

Defined in header `<boost/beast/zlib/deflate_stream.hpp>`

```programlisting
std::size_t
deflate_upper_bound(
    std::size_t bytes);
```

##### [Description](boost__beast__zlib__deflate_upper_bound.html#beast.ref.boost__beast__zlib__deflate_upper_bound.description)

This function makes a conservative estimate of the maximum number of bytes
needed to store the result of compressing a block of data.

##### [Parameters](boost__beast__zlib__deflate_upper_bound.html#beast.ref.boost__beast__zlib__deflate_upper_bound.parameters)

| Name | Description |
| --- | --- |
| `bytes` | The size of the uncompressed data. |

##### [Return Value](boost__beast__zlib__deflate_upper_bound.html#beast.ref.boost__beast__zlib__deflate_upper_bound.return_value)

The maximum number of resulting compressed bytes.