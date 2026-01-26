#### [http::response\_parser](boost__beast__http__response_parser.html "http::response_parser")

An HTTP/1 parser for producing a response message.

##### [Synopsis](boost__beast__http__response_parser.html#beast.ref.boost__beast__http__response_parser.synopsis)

Defined in header `<boost/beast/http/parser.hpp>`

```programlisting
template<
    class Body,
    class Allocator = std::allocator<char>>
using response_parser = parser< false, Body, Allocator >;
```

##### [Types](boost__beast__http__response_parser.html#beast.ref.boost__beast__http__response_parser.types)

| Name | Description |
| --- | --- |
| **[is\_request](boost__beast__http__parser/is_request.html "http::parser::is_request")** | `true` if this parser parses requests, `false` for responses. |
| **[value\_type](boost__beast__http__parser/value_type.html "http::parser::value_type")** | The type of message returned by the parser. |

##### [Member Functions](boost__beast__http__response_parser.html#beast.ref.boost__beast__http__response_parser.member_functions)

| Name | Description |
| --- | --- |
| **[body\_limit](boost__beast__http__parser/body_limit.html "http::parser::body_limit")** | Set the limit on the payload body. |
| **[chunked](boost__beast__http__parser/chunked.html "http::parser::chunked")** | Returns `true` if the last value for Transfer-Encoding is "chunked". |
| **[content\_length](boost__beast__http__parser/content_length.html "http::parser::content_length")** | Returns the optional value of Content-Length if known. |
| **[content\_length\_remaining](boost__beast__http__parser/content_length_remaining.html "http::parser::content_length_remaining")** | Returns the remaining content length if known. |
| **[eager](boost__beast__http__parser/eager.html "http::parser::eager")** | Returns `true` if the eager parse option is set.  — Set the eager parse option. |
| **[get](boost__beast__http__parser/get.html "http::parser::get")** | Returns the parsed message. |
| **[got\_some](boost__beast__http__parser/got_some.html "http::parser::got_some")** | Returns `true` if the parser has received at least one byte of input. |
| **[header\_limit](boost__beast__http__parser/header_limit.html "http::parser::header_limit")** | Set a limit on the total size of the header. |
| **[is\_done](boost__beast__http__parser/is_done.html "http::parser::is_done")** | Returns `true` if the message is complete. |
| **[is\_header\_done](boost__beast__http__parser/is_header_done.html "http::parser::is_header_done")** | Returns `true` if a the parser has produced the full header. |
| **[keep\_alive](boost__beast__http__parser/keep_alive.html "http::parser::keep_alive")** | Returns `true` if the message has keep-alive connection semantics. |
| **[merge\_all\_trailers](boost__beast__http__parser/merge_all_trailers.html "http::parser::merge_all_trailers")** | Returns `true` if the parser is allowed to merge all trailer fields.  — Set whether the parser is allowed to merge all trailer fields. |
| **[need\_eof](boost__beast__http__parser/need_eof.html "http::parser::need_eof")** | Returns `true` if the message semantics require an end of file. |
| **[on\_chunk\_body](boost__beast__http__parser/on_chunk_body.html "http::parser::on_chunk_body")** | Set a callback to be invoked on chunk body data. |
| **[on\_chunk\_header](boost__beast__http__parser/on_chunk_header.html "http::parser::on_chunk_header")** | Set a callback to be invoked on each chunk header. |
| **[operator=](boost__beast__http__parser/operator_eq_.html "http::parser::operator=")** | Assignment (disallowed) |
| **[parser](boost__beast__http__parser/parser.html "http::parser::parser")** | Constructor (disallowed)  — Constructor.  — Construct a parser from another parser, changing the Body type. |
| **[put](boost__beast__http__parser/put.html "http::parser::put")** | Write a buffer sequence to the parser. |
| **[put\_eof](boost__beast__http__parser/put_eof.html "http::parser::put_eof")** | Inform the parser that the end of stream was reached. |
| **[release](boost__beast__http__parser/release.html "http::parser::release")** | Returns ownership of the parsed message. |
| **[skip](boost__beast__http__parser/skip.html "http::parser::skip")** | Returns `true` if the skip parse option is set.  — Set the skip parse option. |
| **[upgrade](boost__beast__http__parser/upgrade.html "http::parser::upgrade")** | Returns `true` if the message is an upgrade message. |
| **[~parser](boost__beast__http__parser/_dtor_parser.html "http::parser::~parser") [destructor]** | Destructor. |

This class uses the basic HTTP/1 wire format parser to convert a series of
octets into a [`message`](boost__beast__http__message.html "http::message") using the [`basic_fields`](boost__beast__http__basic_fields.html "http::basic_fields") container to represent
the fields.

##### [Template Parameters](boost__beast__http__response_parser.html#beast.ref.boost__beast__http__response_parser.template_parameters)

| Type | Description |
| --- | --- |
| `isRequest` | Indicates whether a request or response will be parsed. |
| `Body` | The type used to represent the body. This must meet the requirements of *Body*. |
| `Allocator` | The type of allocator used with the [`basic_fields`](boost__beast__http__basic_fields.html "http::basic_fields") container. |

##### [Remarks](boost__beast__http__response_parser.html#beast.ref.boost__beast__http__response_parser.remarks)

A new instance of the parser is required for each message.