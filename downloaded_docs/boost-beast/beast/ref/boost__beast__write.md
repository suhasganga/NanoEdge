#### [write](boost__beast__write.html "write")

Write all output from a BuffersGenerator to a stream.

```programlisting
template<
    class SyncWriteStream,
    class BuffersGenerator>
std::size_t
write(
    SyncWriteStream& stream,
    BuffersGenerator&& generator,
    beast::error_code& ec);
  » more...

template<
    class SyncWriteStream,
    class BuffersGenerator>
std::size_t
write(
    SyncWriteStream& stream,
    BuffersGenerator&& generator);
  » more...
```