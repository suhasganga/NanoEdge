###### [zlib::deflate\_stream::reset (2 of 2 overloads)](overload2.html "zlib::deflate_stream::reset (2 of 2 overloads)")

Reset the stream without deallocating memory.

###### [Synopsis](overload2.html#beast.ref.boost__beast__zlib__deflate_stream.reset.overload2.synopsis)

```programlisting
void
reset();
```

###### [Description](overload2.html#beast.ref.boost__beast__zlib__deflate_stream.reset.overload2.description)

This function performs the equivalent of calling `clear`
followed by `reset` with
the same compression settings, without deallocating the internal buffers.

###### [Remarks](overload2.html#beast.ref.boost__beast__zlib__deflate_stream.reset.overload2.remarks)

Any unprocessed input or pending output from previous calls are discarded.