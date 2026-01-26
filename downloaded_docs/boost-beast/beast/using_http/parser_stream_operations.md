### [Parser Stream Operations](parser_stream_operations.html "Parser Stream Operations")

Non-trivial algorithms need to do more than receive entire messages at once,
such as:

* Receive the header first and body later.
* Receive a large body using a fixed-size buffer.
* Receive a message incrementally: bounded work in each I/O cycle.
* Defer the commitment to a [*Body*](../concepts/Body.html "Body")
  type until after reading the header.

These types of operations require callers to manage the lifetime of associated
state, by constructing a class derived from [`basic_parser`](../ref/boost__beast__http__basic_parser.html "http::basic_parser"). Beast comes with the
derived instance [`parser`](../ref/boost__beast__http__parser.html "http::parser") which creates complete [`message`](../ref/boost__beast__http__message.html "http::message")
objects using the [`basic_fields`](../ref/boost__beast__http__basic_fields.html "http::basic_fields") Fields container.

**Table 1.23. Parser**

| Name | Description |
| --- | --- |
| [`parser`](../ref/boost__beast__http__parser.html "http::parser") | ```programlisting /// An HTTP/1 parser for producing a message. template<     bool isRequest,                         // `true` to parse an HTTP request     class Body,                             // The Body type for the resulting message     class Allocator = std::allocator<char>> // The type of allocator for the header class parser     : public basic_parser<...>; ``` |
| [`request_parser`](../ref/boost__beast__http__request_parser.html "http::request_parser") | ```programlisting /// An HTTP/1 parser for producing a request message. template<class Body, class Allocator = std::allocator<char>> using request_parser = parser<true, Body, Allocator>; ``` |
| [`response_parser`](../ref/boost__beast__http__response_parser.html "http::response_parser") | ```programlisting /// An HTTP/1 parser for producing a response message. template<class Body, class Allocator = std::allocator<char>> using response_parser = parser<false, Body, Allocator>; ``` |

  

|  |  |
| --- | --- |
| [Note] | Note |
| The [`basic_parser`](../ref/boost__beast__http__basic_parser.html "http::basic_parser") and classes derived from it handle octet streams serialized in the HTTP/1 format described in [rfc7230](https://tools.ietf.org/html/rfc7230). |

The stream operations which work on parsers are:

**Table 1.24. Parser Stream Operations**

| Name | Description |
| --- | --- |
| [**read**](../ref/boost__beast__http__read/overload1.html "http::read (1 of 4 overloads)") | Read everything into a parser from a [*SyncReadStream*](../../../../../../doc/html/boost_asio/reference/SyncReadStream.html). |
| [**async\_read**](../ref/boost__beast__http__async_read/overload1.html "http::async_read (1 of 2 overloads)") | Read everything into a parser asynchronously from an [*AsyncReadStream*](../../../../../../doc/html/boost_asio/reference/AsyncReadStream.html). |
| [**read\_header**](../ref/boost__beast__http__read_header/overload1.html "http::read_header (1 of 2 overloads)") | Read only the header octets into a parser from a [*SyncReadStream*](../../../../../../doc/html/boost_asio/reference/SyncReadStream.html). |
| [**async\_read\_header**](../ref/boost__beast__http__async_read_header.html "http::async_read_header") | Read only the header octets into a parser asynchronously from an [*AsyncReadStream*](../../../../../../doc/html/boost_asio/reference/AsyncReadStream.html). |
| [**read\_some**](../ref/boost__beast__http__read_some/overload1.html "http::read_some (1 of 2 overloads)") | Read some octets into a parser from a [*SyncReadStream*](../../../../../../doc/html/boost_asio/reference/SyncReadStream.html). |
| [**async\_read\_some**](../ref/boost__beast__http__async_read_some.html "http::async_read_some") | Read some octets into a parser asynchronously from an [*AsyncReadStream*](../../../../../../doc/html/boost_asio/reference/AsyncReadStream.html). |

  

As with message stream operations, parser stream operations require a persisted
[*DynamicBuffer*](../concepts/DynamicBuffer.html "DynamicBuffer")
for holding unused octets from the stream. The basic parser implementation
is optimized for the case where this dynamic buffer stores its input sequence
in a single contiguous memory buffer. It is advised to use an instance of
[`flat_buffer`](../ref/boost__beast__flat_buffer.html "flat_buffer"),
[`flat_static_buffer`](../ref/boost__beast__flat_static_buffer.html "flat_static_buffer"), or [`flat_static_buffer_base`](../ref/boost__beast__flat_static_buffer_base.html "flat_static_buffer_base") for this
purpose, although a user defined instance of [*DynamicBuffer*](../concepts/DynamicBuffer.html "DynamicBuffer")
which produces input sequences of length one is also suitable.

The parser contains a message constructed internally. Arguments passed to
the parser's constructor are forwarded into the message container. The caller
can access the message inside the parser by calling [`parser::get`](../ref/boost__beast__http__parser/get.html "http::parser::get"). If the `Fields`
and `Body` types are **MoveConstructible**, the caller can take ownership of
the message by calling [`parser::release`](../ref/boost__beast__http__parser/release.html "http::parser::release"). In this example we read
an HTTP response with a string body using a parser, then print the response:

```programlisting
template<class SyncReadStream>
void
print_response(SyncReadStream& stream)
{
    static_assert(is_sync_read_stream<SyncReadStream>::value,
        "SyncReadStream type requirements not met");

    // Declare a parser for an HTTP response
    response_parser<string_body> parser;

    // Read the entire message
    read(stream, parser);

    // Now print the message
    std::cout << parser.get() << std::endl;
}
```