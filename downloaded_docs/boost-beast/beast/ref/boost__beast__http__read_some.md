#### [http::read\_some](boost__beast__http__read_some.html "http::read_some")

Read part of a message from a stream using a parser.

```programlisting
template<
    class SyncReadStream,
    class DynamicBuffer,
    bool isRequest>
std::size_t
read_some(
    SyncReadStream& stream,
    DynamicBuffer& buffer,
    basic_parser< isRequest >& parser);
  » more...

template<
    class SyncReadStream,
    class DynamicBuffer,
    bool isRequest>
std::size_t
read_some(
    SyncReadStream& stream,
    DynamicBuffer& buffer,
    basic_parser< isRequest >& parser,
    error_code& ec);
  » more...
```