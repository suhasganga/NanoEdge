###### [buffered\_read\_stream::buffer (1 of 2 overloads)](overload1.html "buffered_read_stream::buffer (1 of 2 overloads)")

Access the internal buffer.

###### [Synopsis](overload1.html#beast.ref.boost__beast__buffered_read_stream.buffer.overload1.synopsis)

```programlisting
DynamicBuffer&
buffer();
```

###### [Description](overload1.html#beast.ref.boost__beast__buffered_read_stream.buffer.overload1.description)

The internal buffer is returned. It is possible for the caller to break
invariants with this function. For example, by causing the internal buffer
size to increase beyond the caller defined maximum.