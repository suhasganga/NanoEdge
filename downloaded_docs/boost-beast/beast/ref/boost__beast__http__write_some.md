#### [http::write\_some](boost__beast__http__write_some.html "http::write_some")

Write part of a message to a stream using a serializer.

```programlisting
template<
    class SyncWriteStream,
    bool isRequest,
    class Body,
    class Fields>
std::size_t
write_some(
    SyncWriteStream& stream,
    serializer< isRequest, Body, Fields >& sr);
  » more...

template<
    class SyncWriteStream,
    bool isRequest,
    class Body,
    class Fields>
std::size_t
write_some(
    SyncWriteStream& stream,
    serializer< isRequest, Body, Fields >& sr,
    error_code& ec);
  » more...
```