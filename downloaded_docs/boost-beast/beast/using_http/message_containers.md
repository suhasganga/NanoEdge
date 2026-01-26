### [Message Containers](message_containers.html "Message Containers")

Beast provides a single class template [`message`](../ref/boost__beast__http__message.html "http::message") and some aliases which model
HTTP/1 and [HTTP/2](https://tools.ietf.org/html/rfc7540)
messages:

**Table 1.16. Message**

| Name | Description |
| --- | --- |
| [`message`](../ref/boost__beast__http__message.html "http::message") | ```programlisting /// An HTTP message template<     bool isRequest,             // `true` for requests, `false` for responses     class Body,                 // Controls the container and algorithms used for the body     class Fields = fields>      // The type of container to store the fields class message; ``` |
| [`request`](../ref/boost__beast__http__request.html "http::request") | ```programlisting /// A typical HTTP request template<class Body, class Fields = fields> using request = message<true, Body, Fields>; ``` |
| [`response`](../ref/boost__beast__http__response.html "http::response") | ```programlisting /// A typical HTTP response template<class Body, class Fields = fields> using response = message<false, Body, Fields>; ``` |

  

The container offers value semantics including move and copy if supported
by [*Body*](../concepts/Body.html "Body") and
[*Fields*](../concepts/Fields.html "Fields").
User defined template function parameters can accept any message, or can
use partial specialization to accept just requests or responses. The default
[`fields`](../ref/boost__beast__http__fields.html "http::fields")
is a provided associative container using the standard allocator and supporting
modification and inspection of fields. As per [rfc7230](https://tools.ietf.org/html/rfc7230),
a non-case-sensitive comparison is used for field names. User defined types
for fields are possible. The `Body`
type determines the type of the container used to represent the body as well
as the algorithms for transferring buffers to and from the container. The
library comes with a collection of common body types. As with fields, user
defined body types are possible.

Sometimes it is desired to only work with a header. Beast provides a single
class template [`header`](../ref/boost__beast__http__header.html "http::header") and some aliases to model
HTTP/1 and HTTP/2 headers:

**Table 1.17. Header**

| Name | Description |
| --- | --- |
| [`header`](../ref/boost__beast__http__header.html "http::header") | ```programlisting /// An HTTP header template<     bool isRequest,             // `true` for requests, `false` for responses     class Fields = fields>      // The type of container to store the fields class header; ``` |
| [`request_header`](../ref/boost__beast__http__request_header.html "http::request_header") | ```programlisting /// A typical HTTP request header template<class Fields> using request_header = header<true, Fields>; ``` |
| [`response_header`](../ref/boost__beast__http__response_header.html "http::response_header") | ```programlisting /// A typical HTTP response header template<class Fields> using response_header = header<false, Fields>; ``` |

  

Requests and responses share the version, fields, and body but have a few
members unique to the type. This is implemented by declaring the header classes
as partial specializations of `isRequest`.
[`message`](../ref/boost__beast__http__message.html "http::message")
is derived from [`header`](../ref/boost__beast__http__header.html "http::header"); a message may be passed
as an argument to a function taking a suitably typed header as a parameter.
Additionally, `header` is publicly
derived from `Fields`; a message
inherits all the member functions of `Fields`.
This diagram shows the inheritance relationship between header and message,
along with some of the notable differences in members in each partial specialization:

![](../images/message.png)

##### [Body Types](message_containers.html#beast.using_http.message_containers.body)

Beast defines the [*Body*](../concepts/Body.html "Body")
concept, which determines both the type of the [`message::body`](../ref/boost__beast__http__message/body.html "http::message::body") member (as seen in the diagram
above) and may also include algorithms for transferring buffers in and out.
These algorithms are used during parsing and serialization. Users may define
their own body types which meet the requirements, or use the ones that come
with the library:

| Name | Description |
| --- | --- |
| [`buffer_body`](../ref/boost__beast__http__buffer_body.html "http::buffer_body") | A body whose [`value_type`](../ref/boost__beast__http__buffer_body__value_type.html "http::buffer_body::value_type") holds a raw pointer and size to a caller-provided buffer. This allows for serialization of body data coming from external sources, and incremental parsing of message body content using a fixed size buffer. |
| [`dynamic_body`](../ref/boost__beast__http__dynamic_body.html "http::dynamic_body")  [`basic_dynamic_body`](../ref/boost__beast__http__basic_dynamic_body.html "http::basic_dynamic_body") | A body whose `value_type` is a [*DynamicBuffer*](../concepts/DynamicBuffer.html "DynamicBuffer"). It inherits the insertion complexity of the underlying choice of dynamic buffer. Messages with this body type may be serialized and parsed. |
| [`empty_body`](../ref/boost__beast__http__empty_body.html "http::empty_body") | A special body with an empty `value_type` indicating that the message has no body. Messages with this body may be serialized and parsed; however, body octets received while parsing a message with this body will generate a unique error. |
| [`file_body`](../ref/boost__beast__http__file_body.html "http::file_body")  [`basic_file_body`](../ref/boost__beast__http__basic_file_body.html "http::basic_file_body") | This body is represented by a file opened for either reading or writing. Messages with this body may be serialized and parsed. HTTP algorithms will use the open file for reading and writing, for streaming and incremental sends and receives. |
| [`span_body`](../ref/boost__beast__http__span_body.html "http::span_body") | A body whose `value_type` is a [`span`](../../../../../../libs/core/doc/html/core/span.html), a non-owning reference to a single linear buffer of bytes. Messages with this body type may be serialized and parsed. |
| [`string_body`](../ref/boost__beast__http__string_body.html "http::string_body")  [`basic_string_body`](../ref/boost__beast__http__basic_string_body.html "http::basic_string_body") | A body whose `value_type` is `std::basic_string` or `std::string`. Insertion complexity is amortized constant time, while capacity grows geometrically. Messages with this body type may be serialized and parsed. This is the type of body used in the examples. |
| [`vector_body`](../ref/boost__beast__http__vector_body.html "http::vector_body") | A body whose `value_type` is `std::vector`. Insertion complexity is amortized constant time, while capacity grows geometrically. Messages with this body type may be serialized and parsed. |

##### [Usage](message_containers.html#beast.using_http.message_containers.usage)

These examples show how to create and fill in request and response objects:
Here we build an [HTTP
GET](https://tools.ietf.org/html/rfc7231#section-4.3.1) request with an empty message body:

**Table 1.18. Create Request**

| Statements | Serialized Result |
| --- | --- |
| ```programlisting request<empty_body> req; req.version(11);   // HTTP/1.1 req.method(verb::get); req.target("/index.htm"); req.set(field::accept, "text/html"); req.set(field::user_agent, "Beast"); ``` | ```programlisting GET /index.htm HTTP/1.1\r\n Accept: text/html\r\n User-Agent: Beast\r\n \r\n ``` |

  

In this code we create an HTTP response with a status code indicating success.
This message has a body with a non-zero length. The function [`message::prepare_payload`](../ref/boost__beast__http__message/prepare_payload.html "http::message::prepare_payload") automatically sets
the Content-Length or Transfer-Encoding field depending on the content and
type of the `body` member.
Use of this function is optional; these fields may also be set explicitly.

**Table 1.19. Create Response**

| Statements | Serialized Result |
| --- | --- |
| ```programlisting response<string_body> res; res.version(11);   // HTTP/1.1 res.result(status::ok); res.set(field::server, "Beast"); res.body() = "Hello, world!"; res.prepare_payload(); ``` | ```programlisting HTTP/1.1 200 OK\r\n Server: Beast\r\n Content-Length: 13\r\n \r\n Hello, world! ``` |

  

The implementation will automatically fill in the obsolete [reason-phrase](https://tools.ietf.org/html/rfc7230#section-3.1.2)
from the status code when serializing a message. Or it may be set directly
using [`header::reason`](../ref/boost__beast__http__header/reason/overload2.html "http::header::reason (2 of 2 overloads)").