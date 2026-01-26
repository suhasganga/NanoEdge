#### [http::error](boost__beast__http__error.html "http::error")

Error codes returned from HTTP algorithms and operations.

##### [Synopsis](boost__beast__http__error.html#beast.ref.boost__beast__http__error.synopsis)

Defined in header `<boost/beast/http/error.hpp>`

```programlisting
enum error
```

##### [Values](boost__beast__http__error.html#beast.ref.boost__beast__http__error.values)

| Name | Description |
| --- | --- |
| `end_of_stream` | The end of the stream was reached.  This error is returned when attempting to read HTTP data, and the stream returns the error `net::error::eof` before any octets corresponding to a new HTTP message have been received. |
| `partial_message` | The incoming message is incomplete.  This happens when the end of stream is reached during parsing and some octets have been received, but not the entire message. |
| `need_more` | Additional buffers are required.  This error is returned during parsing when additional octets are needed. The caller should append more data to the existing buffer and retry the parse operation. |
| `unexpected_body` | An unexpected body was encountered during parsing.  This error is returned when attempting to parse body octets into a message container which has the [`empty_body`](boost__beast__http__empty_body.html "http::empty_body") body type.  See Also  [`empty_body`](boost__beast__http__empty_body.html "http::empty_body") |
| `need_buffer` | Additional buffers are required.  This error is returned under the following conditions:  * During serialization when using [`buffer_body`](boost__beast__http__buffer_body.html "http::buffer_body"). The caller   should update the body to point to a new buffer or indicate   that there are no more octets in the body.  * During parsing when using [`buffer_body`](boost__beast__http__buffer_body.html "http::buffer_body"). The caller   should update the body to point to a new storage area to receive   additional body octets. |
| `end_of_chunk` | The end of a chunk was reached. |
| `buffer_overflow` | Buffer maximum exceeded.  This error is returned when reading HTTP content into a dynamic buffer, and the operation would exceed the maximum size of the buffer. |
| `header_limit` | Header limit exceeded.  The parser detected an incoming message header which exceeded a configured limit. |
| `body_limit` | Body limit exceeded.  The parser detected an incoming message body which exceeded a configured limit. |
| `bad_alloc` | A memory allocation failed.  When [`basic_fields`](boost__beast__http__basic_fields.html "http::basic_fields") throws std::bad\_alloc, it is converted into this error by [`parser`](boost__beast__http__parser.html "http::parser"). |
| `bad_line_ending` | The line ending was malformed. |
| `bad_method` | The method is invalid. |
| `bad_target` | The request-target is invalid. |
| `bad_version` | The HTTP-version is invalid. |
| `bad_status` | The status-code is invalid. |
| `bad_reason` | The reason-phrase is invalid. |
| `bad_field` | The field name is invalid. |
| `bad_value` | The field value is invalid. |
| `bad_content_length` | The Content-Length is invalid. |
| `bad_transfer_encoding` | The Transfer-Encoding is invalid. |
| `bad_chunk` | The chunk syntax is invalid. |
| `bad_chunk_extension` | The chunk extension is invalid. |
| `bad_obs_fold` | An obs-fold exceeded an internal limit. |
| `multiple_content_length` | The response contains multiple and conflicting Content-Length. |
| `stale_parser` | The parser is stale.  This happens when attempting to re-use a parser that has already completed parsing a message. Programs must construct a new parser for each message. This can be easily done by storing the parser in an boost or std::optional container. |
| `short_read` | The message body is shorter than expected.  This error is returned by [`file_body`](boost__beast__http__file_body.html "http::file_body") when an unexpected unexpected end-of-file condition is encountered while trying to read from the file. |
| `header_field_name_too_large` | Header field name exceeds [`basic_fields::max_name_size`](boost__beast__http__basic_fields/max_name_size.html "http::basic_fields::max_name_size"). |
| `header_field_value_too_large` | Header field value exceeds [`basic_fields::max_value_size`](boost__beast__http__basic_fields/max_value_size.html "http::basic_fields::max_value_size"). |