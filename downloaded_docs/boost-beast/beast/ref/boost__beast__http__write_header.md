#### [http::write\_header](boost__beast__http__write_header.html "http::write_header")

Write a header to a stream using a serializer.

```programlisting
template<
    class SyncWriteStream,
    bool isRequest,
    class Body,
    class Fields>
std::size_t
write_header(
    SyncWriteStream& stream,
    serializer< isRequest, Body, Fields >& sr);
  » more...

template<
    class SyncWriteStream,
    bool isRequest,
    class Body,
    class Fields>
std::size_t
write_header(
    SyncWriteStream& stream,
    serializer< isRequest, Body, Fields >& sr,
    error_code& ec);
  » more...
```