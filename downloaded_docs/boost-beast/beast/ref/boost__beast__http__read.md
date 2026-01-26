#### [http::read](boost__beast__http__read.html "http::read")

Read a complete message from a stream using a parser.

```programlisting
template<
    class SyncReadStream,
    class DynamicBuffer,
    bool isRequest>
std::size_t
read(
    SyncReadStream& stream,
    DynamicBuffer& buffer,
    basic_parser< isRequest >& parser);
  » more...

template<
    class SyncReadStream,
    class DynamicBuffer,
    bool isRequest>
std::size_t
read(
    SyncReadStream& stream,
    DynamicBuffer& buffer,
    basic_parser< isRequest >& parser,
    error_code& ec);
  » more...
```

Read a complete message from a stream.

```programlisting
template<
    class SyncReadStream,
    class DynamicBuffer,
    bool isRequest,
    class Body,
    class Allocator>
std::size_t
read(
    SyncReadStream& stream,
    DynamicBuffer& buffer,
    message< isRequest, Body, basic_fields< Allocator > >& msg);
  » more...

template<
    class SyncReadStream,
    class DynamicBuffer,
    bool isRequest,
    class Body,
    class Allocator>
std::size_t
read(
    SyncReadStream& stream,
    DynamicBuffer& buffer,
    message< isRequest, Body, basic_fields< Allocator > >& msg,
    error_code& ec);
  » more...
```