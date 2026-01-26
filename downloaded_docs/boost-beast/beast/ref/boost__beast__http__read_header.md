#### [http::read\_header](boost__beast__http__read_header.html "http::read_header")

Read a complete message header from a stream using a parser.

```programlisting
template<
    class SyncReadStream,
    class DynamicBuffer,
    bool isRequest>
std::size_t
read_header(
    SyncReadStream& stream,
    DynamicBuffer& buffer,
    basic_parser< isRequest >& parser);
  » more...

template<
    class SyncReadStream,
    class DynamicBuffer,
    bool isRequest>
std::size_t
read_header(
    SyncReadStream& stream,
    DynamicBuffer& buffer,
    basic_parser< isRequest >& parser,
    error_code& ec);
  » more...
```