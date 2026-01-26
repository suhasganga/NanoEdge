## [HTTP](using_http.html "HTTP")

|  |  |
| --- | --- |
| [Warning] | Warning |
| Higher level functions such as Basic Authentication, mime/multipart encoding, cookies, automatic handling of redirects, gzipped transfer encodings, caching, or proxying (to name a few) are not directly provided, but nothing stops users from creating these features using Beast's HTTP message types. |

This library offers programmers simple and performant models of HTTP messages
and their associated operations including synchronous, asynchronous, and buffer-oriented
parsing and serialization of messages in the HTTP/1 wire format using [Boost.Asio](../../../../../libs/asio/index.html). Specifically, the library
provides:

Message Containers
:   Complete HTTP messages are modeled using the [`message`](ref/boost__beast__http__message.html "http::message") class, with possible
    user customizations.

Stream Reading
:   The functions [`read`](ref/boost__beast__http__read.html "http::read"), [`read_header`](ref/boost__beast__http__read_header.html "http::read_header"), [`read_some`](ref/boost__beast__http__read_some.html "http::read_some"), [`async_read`](ref/boost__beast__http__async_read.html "http::async_read"), [`async_read_header`](ref/boost__beast__http__async_read_header.html "http::async_read_header"), and [`async_read_some`](ref/boost__beast__http__async_read_some.html "http::async_read_some") read HTTP/1
    message data from a [stream](concepts/streams.html "Streams").

Stream Writing
:   The functions [`write`](ref/boost__beast__http__write.html "http::write"), [`write_header`](ref/boost__beast__http__write_header.html "http::write_header"), [`write_some`](ref/boost__beast__http__write_some.html "http::write_some"), [`async_write`](ref/boost__beast__http__async_write.html "http::async_write"), [`async_write_header`](ref/boost__beast__http__async_write_header.html "http::async_write_header"), and [`async_write_some`](ref/boost__beast__http__async_write_some.html "http::async_write_some") write HTTP/1
    message data to a [stream](concepts/streams.html "Streams").

Serialization
:   The [`serializer`](ref/boost__beast__http__serializer.html "http::serializer") produces a series
    of octet buffers conforming to the [rfc7230](https://tools.ietf.org/html/rfc7230)
    wire representation of a [`message`](ref/boost__beast__http__message.html "http::message").

Parsing
:   The [`parser`](ref/boost__beast__http__parser.html "http::parser") attempts to convert a
    series of octet buffers into a [`message`](ref/boost__beast__http__message.html "http::message").

Interfaces for operating on HTTP messages are structured into several layers.
The highest level provides ease of use, while lower levels provide progressively
more control, options, and flexibility. At the lowest level customization points
are provided, where user defined types can replace parts of the implementation.
The layers are arranged thusly:

| Level | Read/Write What | Description |
| --- | --- | --- |
| **6** | [`message`](ref/boost__beast__http__message.html "http::message") | At the highest level, these free functions send or receive a complete HTTP message in one call. They are designed for ease of use: [`read`](ref/boost__beast__http__read/overload4.html "http::read (4 of 4 overloads)"), [`write`](ref/boost__beast__http__write/overload4.html "http::write (4 of 6 overloads)"), [`async_read`](ref/boost__beast__http__async_read/overload2.html "http::async_read (2 of 2 overloads)"), and [`async_write`](ref/boost__beast__http__async_write/overload2.html "http::async_write (2 of 3 overloads)"). |
| **5** | [`parser`](ref/boost__beast__http__parser.html "http::parser"), [`serializer`](ref/boost__beast__http__serializer.html "http::serializer") | For more control, callers may take responsibility for managing the required [`parser`](ref/boost__beast__http__parser.html "http::parser") or [`serializer`](ref/boost__beast__http__serializer.html "http::serializer") transient state objects. This allows additional configuration such as limiting the number of bytes for message components during parsing, or regulating the size of buffers emitted during output. These functions send or receive complete messages using a serializer or parser: [`read`](ref/boost__beast__http__read/overload2.html "http::read (2 of 4 overloads)"), [`write`](ref/boost__beast__http__write/overload2.html "http::write (2 of 6 overloads)"), [`async_read`](ref/boost__beast__http__async_read/overload1.html "http::async_read (1 of 2 overloads)"), and [`async_write`](ref/boost__beast__http__async_write/overload1.html "http::async_write (1 of 3 overloads)"). |
| **4** | [`header`](ref/boost__beast__http__header.html "http::header") | Sometimes it is necessary to first send or receive the HTTP header. For example, to read the header and take action before continuing to read the body. These functions use a [`parser`](ref/boost__beast__http__parser.html "http::parser") or [`serializer`](ref/boost__beast__http__serializer.html "http::serializer") to read or write the header: [`read_header`](ref/boost__beast__http__read_header/overload2.html "http::read_header (2 of 2 overloads)"), [`write_header`](ref/boost__beast__http__write_header/overload2.html "http::write_header (2 of 2 overloads)"), [`async_read_header`](ref/boost__beast__http__async_read_header.html "http::async_read_header"), and [`async_write_header`](ref/boost__beast__http__async_write_header.html "http::async_write_header"). |
| **3** | partial [`message`](ref/boost__beast__http__message.html "http::message") | All of the stream operations at higher levels thus far have operated on a complete header or message. At this level it is possible to send and receive messages incrementally. This allows resource constrained implementations to perform work bounded on storage, or allows better control when setting timeouts for example. These functions read or write bounded amounts of data and return the number of bytes transacted: [`read_some`](ref/boost__beast__http__read_some/overload2.html "http::read_some (2 of 2 overloads)"), [`write_some`](ref/boost__beast__http__write_some/overload2.html "http::write_some (2 of 2 overloads)"), [`async_read_some`](ref/boost__beast__http__async_read_some.html "http::async_read_some"), and [`async_write_some`](ref/boost__beast__http__async_write_some.html "http::async_write_some"). |
| **2** | [*chunked-body*](https://tools.ietf.org/html/rfc7230#section-4.1) | Until now parse and serialize operations apply or remove the chunked transfer coding as needed for message payloads whose size is not known ahead of time. For some domain specific niches, it is necessary to assume direct control over incoming or outgoing chunks in a chunk encoded message payload. For parsing this is achieved by setting hooks using the functions [`on_chunk_header`](ref/boost__beast__http__parser/on_chunk_header.html "http::parser::on_chunk_header") and/or [`on_chunk_body`](ref/boost__beast__http__parser/on_chunk_body.html "http::parser::on_chunk_body"). For serializing callers may first emit the header, and then use these buffer sequence adapters to control the contents of each chunk including [*chunk extensions*](https://tools.ietf.org/html/rfc7230#section-4.1.1) and the [*trailer-part*](https://tools.ietf.org/html/rfc7230#section-4.1.2): [`chunk_body`](ref/boost__beast__http__chunk_body.html "http::chunk_body"), [`chunk_crlf`](ref/boost__beast__http__chunk_crlf.html "http::chunk_crlf"), [`chunk_header`](ref/boost__beast__http__chunk_header.html "http::chunk_header"), and [`chunk_last`](ref/boost__beast__http__chunk_last.html "http::chunk_last"). |
| **1** | buffers | For ultimate control, the use of library stream algorithms may be bypassed entirely and instead work directly with buffers by calling members of [`parser`](ref/boost__beast__http__parser.html "http::parser") or [`serializer`](ref/boost__beast__http__serializer.html "http::serializer"). |
| **0** | *user-defined* | In addition to the typical customization points of [*Stream*](concepts/streams.html "Streams") and [*DynamicBuffer*](concepts/DynamicBuffer.html "DynamicBuffer"), user-defined types may replace parts of the library implementation at the lowest level. The customization points include [*Fields*](concepts/Fields.html "Fields") for creating a container to store HTTP fields, [*Body*](concepts/Body.html "Body") for defining containers and algorithms used for HTTP message payloads, and user-defined subclasses of [`basic_parser`](ref/boost__beast__http__basic_parser.html "http::basic_parser") for implementing custom message representation strategies. |

|  |  |
| --- | --- |
| [Note] | Note |
| This documentation assumes some familiarity with [Boost.Asio](../../../../../libs/asio/index.html) and the HTTP protocol specification described in [rfc7230](https://tools.ietf.org/html/rfc7230). Sample code and identifiers mentioned in this section is written as if these declarations are in effect:   ```programlisting #include <boost/beast/http.hpp> using namespace boost::beast::http; ``` |