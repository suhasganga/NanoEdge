### [Protocol Primer](protocol_primer.html "Protocol Primer")

The HTTP protocol defines the [client
and server roles](https://tools.ietf.org/html/rfc7230#section-2.1): clients send requests and servers send back responses.
When a client and server have established a connection, the client sends
a series of requests while the server sends back at least one response for
each received request in the order those requests were received.

A request or response is an [HTTP
message](https://tools.ietf.org/html/rfc7230#section-3) (referred to hereafter as "message") having two
parts: a header with structured metadata and an optional variable-length
body holding arbitrary data. A serialized header is one or more text lines
where each line ends in a carriage return followed by linefeed (`"\r\n"`). An empty line marks the
end of the header. The first line in the header is called the *start-line*.
The contents of the start line contents are different for requests and responses.

Every message contains a set of zero or more field name/value pairs, collectively
called "fields". The names and values are represented using text
strings with various requirements. A serialized field contains the field
name, then a colon followed by a space (`":
"`), and finally the field value with a trailing CRLF.

##### [Requests](protocol_primer.html#beast.using_http.protocol_primer.requests)

Clients send requests, which contain a [method](https://tools.ietf.org/html/rfc7230#section-3.1.1)
and [request-target](https://tools.ietf.org/html/rfc7230#section-5.3),
and [HTTP-version](https://tools.ietf.org/html/rfc7230#section-2.6).
The method identifies the operation to be performed while the target identifies
the object on the server to which the operation applies. The version is almost
always 1.1, but older programs sometimes use 1.0.

| Serialized Request | Description |
| --- | --- |
| ```table-programlisting GET / HTTP/1.1\r\n User-Agent: Beast\r\n \r\n ``` | This request has a method of "GET", a target of "/", and indicates HTTP version 1.1. It contains a single field called "User-Agent" whose value is "Beast". There is no message body. |

##### [Responses](protocol_primer.html#beast.using_http.protocol_primer.responses)

Servers send responses, which contain a [status-code](https://tools.ietf.org/html/rfc7231#section-6),
[reason-phrase](https://tools.ietf.org/html/rfc7230#section-3.1.2),
and [HTTP-version](https://tools.ietf.org/html/rfc7230#section-2.6).
The reason phrase is [obsolete](https://tools.ietf.org/html/rfc7230#section-3.1.2):
clients SHOULD ignore the reason-phrase content. Here is a response which
includes a body. The special [Content-Length](https://tools.ietf.org/html/rfc7230#section-3.3.2)
field informs the remote host of the size of the body which follows.

| Serialized Response | Description |
| --- | --- |
| ```table-programlisting HTTP/1.1 200 OK\r\n Server: Beast\r\n Content-Length: 13\r\n \r\n Hello, world! ``` | This response has a [200 status code](https://tools.ietf.org/html/rfc7231#section-6) meaning the operation requested completed successfully. The obsolete reason phrase is "OK". It specifies HTTP version 1.1, and contains a body 13 octets in size with the text "Hello, world!". |

##### [Body](protocol_primer.html#beast.using_http.protocol_primer.body)

Messages may optionally carry a body. The size of the message body is determined
by the semantics of the message and the special fields Content-Length and
Transfer-Encoding. [rfc7230
section 3.3](https://tools.ietf.org/html/rfc7230#section-3.3) provides a comprehensive description for how the body
length is determined.

##### [Special Fields](protocol_primer.html#beast.using_http.protocol_primer.special_fields)

Certain fields appearing in messages are special. The library understands
these fields when performing serialization and parsing, taking automatic
action as needed when the fields are parsed in a message and also setting
the fields if the caller requests it.

**Table 1.15. Special Fields**

| Field | Description |
| --- | --- |
| [**`Connection`**](https://tools.ietf.org/html/rfc7230#section-6.1)  [**`Proxy-Connection`**](https://tools.ietf.org/html/rfc7230#appendix-A.1.2) | This field allows the sender to indicate desired control options for the current connection. Common values include "close", "keep-alive", and "upgrade". |
| [**`Content-Length`**](https://tools.ietf.org/html/rfc7230#section-3.3.2) | When present, this field informs the recipient about the exact size in bytes of the body which follows the message header. |
| [**`Transfer-Encoding`**](https://tools.ietf.org/html/rfc7230#section-3.3.1) | This optional field lists the names of the sequence of transfer codings that have been (or will be) applied to the content payload to form the message body.  Beast understands the "chunked" coding scheme when it is the last (outermost) applied coding. The library will automatically apply chunked encoding when the content length is not known ahead of time during serialization, and the library will automatically remove chunked encoding from parsed messages when present. |
| [**`Upgrade`**](https://tools.ietf.org/html/rfc7230#section-6.7) | The Upgrade header field provides a mechanism to transition from HTTP/1.1 to another protocol on the same connection. For example, it is the mechanism used by WebSocket's initial HTTP handshake to establish a WebSocket connection. |