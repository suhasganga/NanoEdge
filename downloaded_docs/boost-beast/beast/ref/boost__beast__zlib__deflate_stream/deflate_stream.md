##### [zlib::deflate\_stream::deflate\_stream](deflate_stream.html "zlib::deflate_stream::deflate_stream")

Construct a default deflate stream.

###### [Synopsis](deflate_stream.html#beast.ref.boost__beast__zlib__deflate_stream.deflate_stream.synopsis)

```programlisting
deflate_stream();
```

###### [Description](deflate_stream.html#beast.ref.boost__beast__zlib__deflate_stream.deflate_stream.description)

Upon construction, the stream settings will be set to these default values:

* `level =
  6`
* `windowBits =
  15`
* `memLevel =
  8`
* strategy = [`Strategy::normal`](../boost__beast__zlib__Strategy.html "zlib::Strategy")

Although the stream is ready to be used immediately after construction,
any required internal buffers are not dynamically allocated until needed.