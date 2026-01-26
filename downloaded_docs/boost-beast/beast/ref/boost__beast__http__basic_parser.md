#### [http::basic\_parser](boost__beast__http__basic_parser.html "http::basic_parser")

A parser for decoding HTTP/1 wire format messages.

##### [Synopsis](boost__beast__http__basic_parser.html#beast.ref.boost__beast__http__basic_parser.synopsis)

Defined in header `<boost/beast/http/basic_parser.hpp>`

```programlisting
template<
    bool isRequest>
class basic_parser
```

##### [Types](boost__beast__http__basic_parser.html#beast.ref.boost__beast__http__basic_parser.types)

| Name | Description |
| --- | --- |
| **[is\_request](boost__beast__http__basic_parser/is_request.html "http::basic_parser::is_request")** | `true` if this parser parses requests, `false` for responses. |

##### [Member Functions](boost__beast__http__basic_parser.html#beast.ref.boost__beast__http__basic_parser.member_functions)

| Name | Description |
| --- | --- |
| **[basic\_parser](boost__beast__http__basic_parser/basic_parser.html "http::basic_parser::basic_parser") [constructor]** | Copy constructor. |
| **[body\_limit](boost__beast__http__basic_parser/body_limit.html "http::basic_parser::body_limit")** | Set the limit on the payload body. |
| **[chunked](boost__beast__http__basic_parser/chunked.html "http::basic_parser::chunked")** | Returns `true` if the last value for Transfer-Encoding is "chunked". |
| **[content\_length](boost__beast__http__basic_parser/content_length.html "http::basic_parser::content_length")** | Returns the optional value of Content-Length if known. |
| **[content\_length\_remaining](boost__beast__http__basic_parser/content_length_remaining.html "http::basic_parser::content_length_remaining")** | Returns the remaining content length if known. |
| **[eager](boost__beast__http__basic_parser/eager.html "http::basic_parser::eager")** | Returns `true` if the eager parse option is set.  — Set the eager parse option. |
| **[got\_some](boost__beast__http__basic_parser/got_some.html "http::basic_parser::got_some")** | Returns `true` if the parser has received at least one byte of input. |
| **[header\_limit](boost__beast__http__basic_parser/header_limit.html "http::basic_parser::header_limit")** | Set a limit on the total size of the header. |
| **[is\_done](boost__beast__http__basic_parser/is_done.html "http::basic_parser::is_done")** | Returns `true` if the message is complete. |
| **[is\_header\_done](boost__beast__http__basic_parser/is_header_done.html "http::basic_parser::is_header_done")** | Returns `true` if a the parser has produced the full header. |
| **[keep\_alive](boost__beast__http__basic_parser/keep_alive.html "http::basic_parser::keep_alive")** | Returns `true` if the message has keep-alive connection semantics. |
| **[need\_eof](boost__beast__http__basic_parser/need_eof.html "http::basic_parser::need_eof")** | Returns `true` if the message semantics require an end of file. |
| **[operator=](boost__beast__http__basic_parser/operator_eq_.html "http::basic_parser::operator=")** | Copy assignment. |
| **[put](boost__beast__http__basic_parser/put.html "http::basic_parser::put")** | Write a buffer sequence to the parser. |
| **[put\_eof](boost__beast__http__basic_parser/put_eof.html "http::basic_parser::put_eof")** | Inform the parser that the end of stream was reached. |
| **[skip](boost__beast__http__basic_parser/skip.html "http::basic_parser::skip")** | Returns `true` if the skip parse option is set.  — Set the skip parse option. |
| **[upgrade](boost__beast__http__basic_parser/upgrade.html "http::basic_parser::upgrade")** | Returns `true` if the message is an upgrade message. |
| **[~basic\_parser](boost__beast__http__basic_parser/_dtor_basic_parser.html "http::basic_parser::~basic_parser") [destructor]** | Destructor. |

##### [Protected Member Functions](boost__beast__http__basic_parser.html#beast.ref.boost__beast__http__basic_parser.protected_member_functions)

| Name | Description |
| --- | --- |
| **[basic\_parser](boost__beast__http__basic_parser/basic_parser.html "http::basic_parser::basic_parser") [constructor]** | Default constructor.  — Move constructor. |
| **[on\_body\_impl](boost__beast__http__basic_parser/on_body_impl.html "http::basic_parser::on_body_impl")** | Called each time additional data is received representing the content body. |
| **[on\_body\_init\_impl](boost__beast__http__basic_parser/on_body_init_impl.html "http::basic_parser::on_body_init_impl")** | Called once before the body is processed. |
| **[on\_chunk\_body\_impl](boost__beast__http__basic_parser/on_chunk_body_impl.html "http::basic_parser::on_chunk_body_impl")** | Called each time additional data is received representing part of a body chunk. |
| **[on\_chunk\_header\_impl](boost__beast__http__basic_parser/on_chunk_header_impl.html "http::basic_parser::on_chunk_header_impl")** | Called each time a new chunk header of a chunk encoded body is received. |
| **[on\_field\_impl](boost__beast__http__basic_parser/on_field_impl.html "http::basic_parser::on_field_impl")** | Called once for each complete field in the HTTP header. |
| **[on\_finish\_impl](boost__beast__http__basic_parser/on_finish_impl.html "http::basic_parser::on_finish_impl")** | Called once when the complete message is received. |
| **[on\_header\_impl](boost__beast__http__basic_parser/on_header_impl.html "http::basic_parser::on_header_impl")** | Called once after the complete HTTP header is received. |
| **[on\_request\_impl](boost__beast__http__basic_parser/on_request_impl.html "http::basic_parser::on_request_impl")** | Called after receiving the request-line. |
| **[on\_response\_impl](boost__beast__http__basic_parser/on_response_impl.html "http::basic_parser::on_response_impl")** | Called after receiving the status-line. |
| **[on\_trailer\_field\_impl](boost__beast__http__basic_parser/on_trailer_field_impl.html "http::basic_parser::on_trailer_field_impl")** | Called once for each complete field in the HTTP trailer header. |
| **[operator=](boost__beast__http__basic_parser/operator_eq_.html "http::basic_parser::operator=")** | Move assignment. |

##### [Description](boost__beast__http__basic_parser.html#beast.ref.boost__beast__http__basic_parser.description)

This parser is designed to efficiently parse messages in the HTTP/1 wire
format. It allocates no memory when input is presented as a single contiguous
buffer, and uses minimal state. It will handle chunked encoding and it understands
the semantics of the Connection, Content-Length, and Upgrade fields. The
parser is optimized for the case where the input buffer sequence consists
of a single contiguous buffer. The [`beast::basic_flat_buffer`](boost__beast__basic_flat_buffer.html "basic_flat_buffer") class is provided,
which guarantees that the input sequence of the stream buffer will be represented
by exactly one contiguous buffer. To ensure the optimum performance of the
parser, use [`beast::basic_flat_buffer`](boost__beast__basic_flat_buffer.html "basic_flat_buffer") with HTTP algorithms
such as [`read`](boost__beast__http__read.html "http::read"), [`read_some`](boost__beast__http__read_some.html "http::read_some"), [`async_read`](boost__beast__http__async_read.html "http::async_read"), and [`async_read_some`](boost__beast__http__async_read_some.html "http::async_read_some"). Alternatively,
the caller may use custom techniques to ensure that the structured portion
of the HTTP message (header or chunk header) is contained in a linear buffer.

The interface to the parser uses virtual member functions. To use this class,
derive your type from [`basic_parser`](boost__beast__http__basic_parser.html "http::basic_parser"). When bytes are presented,
the implementation will make a series of zero or more calls to virtual functions,
which the derived class must implement.

Every virtual function must be provided by the derived class, or else a compilation
error will be generated. The implementation will make sure that `ec` is clear before each virtual function
is invoked. If a virtual function sets an error, it is propagated out of
the parser to the caller.

##### [Template Parameters](boost__beast__http__basic_parser.html#beast.ref.boost__beast__http__basic_parser.template_parameters)

| Type | Description |
| --- | --- |
| `isRequest` | A `bool` indicating whether the parser will be presented with request or response message. |

##### [Remarks](boost__beast__http__basic_parser.html#beast.ref.boost__beast__http__basic_parser.remarks)

If the parser encounters a field value with obs-fold longer than 4 kilobytes
in length, an error is generated.