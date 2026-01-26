##### [zlib::deflate\_stream::clear](clear.html "zlib::deflate_stream::clear")

Clear the stream.

###### [Synopsis](clear.html#beast.ref.boost__beast__zlib__deflate_stream.clear.synopsis)

```programlisting
void
clear();
```

###### [Description](clear.html#beast.ref.boost__beast__zlib__deflate_stream.clear.description)

This function resets the stream and frees all dynamically allocated internal
buffers. The compression settings are left unchanged.

###### [Remarks](clear.html#beast.ref.boost__beast__zlib__deflate_stream.clear.remarks)

Any unprocessed input or pending output from previous calls are discarded.