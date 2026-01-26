#### [websocket::request\_type](boost__beast__websocket__request_type.html "websocket::request_type")

The type of object holding HTTP Upgrade requests.

##### [Synopsis](boost__beast__websocket__request_type.html#beast.ref.boost__beast__websocket__request_type.synopsis)

Defined in header `<boost/beast/websocket/rfc6455.hpp>`

```programlisting
using request_type = http::request< http::empty_body >;
```

##### [Types](boost__beast__websocket__request_type.html#beast.ref.boost__beast__websocket__request_type.types)

| Name | Description |
| --- | --- |
| **[reader](boost__beast__http__empty_body/reader.html "http::empty_body::reader")** | The algorithm for parsing the body. |
| **[value\_type](boost__beast__http__empty_body__value_type.html "http::empty_body::value_type")** | The type of container used for the body. |
| **[writer](boost__beast__http__empty_body/writer.html "http::empty_body::writer")** | The algorithm for serializing the body. |

##### [Static Member Functions](boost__beast__websocket__request_type.html#beast.ref.boost__beast__websocket__request_type.static_member_functions)

| Name | Description |
| --- | --- |
| **[size](boost__beast__http__empty_body/size.html "http::empty_body::size")** | Returns the payload size of the body. |

This body is used to represent messages which do not have a message body.
If this body is used with a parser, and the parser encounters octets corresponding
to a message body, the parser will fail with the error [`http::unexpected_body`](boost__beast__http__error.html "http::error") .

The Content-Length of this body is always 0.