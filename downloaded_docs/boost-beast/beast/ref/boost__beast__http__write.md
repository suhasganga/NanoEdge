#### [http::write](boost__beast__http__write.html "http::write")

Write a complete message to a stream using a serializer.

```programlisting
template<
    class SyncWriteStream,
    bool isRequest,
    class Body,
    class Fields>
std::size_t
write(
    SyncWriteStream& stream,
    serializer< isRequest, Body, Fields >& sr);
  » more...

template<
    class SyncWriteStream,
    bool isRequest,
    class Body,
    class Fields>
std::size_t
write(
    SyncWriteStream& stream,
    serializer< isRequest, Body, Fields >& sr,
    error_code& ec);
  » more...
```

Write a complete message to a stream.

```programlisting
template<
    class SyncWriteStream,
    bool isRequest,
    class Body,
    class Fields>
std::size_t
write(
    SyncWriteStream& stream,
    message< isRequest, Body, Fields >& msg);
  » more...

template<
    class SyncWriteStream,
    bool isRequest,
    class Body,
    class Fields>
std::size_t
write(
    SyncWriteStream& stream,
    message< isRequest, Body, Fields > const& msg);
  » more...

template<
    class SyncWriteStream,
    bool isRequest,
    class Body,
    class Fields>
std::size_t
write(
    SyncWriteStream& stream,
    message< isRequest, Body, Fields >& msg,
    error_code& ec);
  » more...

template<
    class SyncWriteStream,
    bool isRequest,
    class Body,
    class Fields>
std::size_t
write(
    SyncWriteStream& stream,
    message< isRequest, Body, Fields > const& msg,
    error_code& ec);
  » more...
```