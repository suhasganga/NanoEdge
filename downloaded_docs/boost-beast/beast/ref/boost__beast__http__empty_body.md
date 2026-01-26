#### [http::empty\_body](boost__beast__http__empty_body.html "http::empty_body")

An empty *Body*

##### [Synopsis](boost__beast__http__empty_body.html#beast.ref.boost__beast__http__empty_body.synopsis)

Defined in header `<boost/beast/http/empty_body.hpp>`

```programlisting
struct empty_body
```

##### [Types](boost__beast__http__empty_body.html#beast.ref.boost__beast__http__empty_body.types)

| Name | Description |
| --- | --- |
| **[reader](boost__beast__http__empty_body/reader.html "http::empty_body::reader")** | The algorithm for parsing the body. |
| **[value\_type](boost__beast__http__empty_body__value_type.html "http::empty_body::value_type")** | The type of container used for the body. |
| **[writer](boost__beast__http__empty_body/writer.html "http::empty_body::writer")** | The algorithm for serializing the body. |

##### [Static Member Functions](boost__beast__http__empty_body.html#beast.ref.boost__beast__http__empty_body.static_member_functions)

| Name | Description |
| --- | --- |
| **[size](boost__beast__http__empty_body/size.html "http::empty_body::size")** | Returns the payload size of the body. |

##### [Description](boost__beast__http__empty_body.html#beast.ref.boost__beast__http__empty_body.description)

This body is used to represent messages which do not have a message body.
If this body is used with a parser, and the parser encounters octets corresponding
to a message body, the parser will fail with the error [`http::unexpected_body`](boost__beast__http__error.html "http::error") .

The Content-Length of this body is always 0.