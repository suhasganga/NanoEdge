##### [zlib::deflate\_stream::upper\_bound](upper_bound.html "zlib::deflate_stream::upper_bound")

Returns the upper limit on the size of a compressed block.

###### [Synopsis](upper_bound.html#beast.ref.boost__beast__zlib__deflate_stream.upper_bound.synopsis)

```programlisting
std::size_t
upper_bound(
    std::size_t sourceLen) const;
```

###### [Description](upper_bound.html#beast.ref.boost__beast__zlib__deflate_stream.upper_bound.description)

This function makes a conservative estimate of the maximum number of bytes
needed to store the result of compressing a block of data based on the
current compression level and strategy.

###### [Parameters](upper_bound.html#beast.ref.boost__beast__zlib__deflate_stream.upper_bound.parameters)

| Name | Description |
| --- | --- |
| `sourceLen` | The size of the uncompressed data. |

###### [Return Value](upper_bound.html#beast.ref.boost__beast__zlib__deflate_stream.upper_bound.return_value)

The maximum number of resulting compressed bytes.