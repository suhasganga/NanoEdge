#### [http::message\_generator](boost__beast__http__message_generator.html "http::message_generator")

Type-erased buffers generator for [`http::message`](boost__beast__http__message.html "http::message") .

##### [Synopsis](boost__beast__http__message_generator.html#beast.ref.boost__beast__http__message_generator.synopsis)

Defined in header `<boost/beast/http/message_generator.hpp>`

```programlisting
class message_generator
```

##### [Types](boost__beast__http__message_generator.html#beast.ref.boost__beast__http__message_generator.types)

| Name | Description |
| --- | --- |
| **[const\_buffers\_type](boost__beast__http__message_generator/const_buffers_type.html "http::message_generator::const_buffers_type")** |  |

##### [Member Functions](boost__beast__http__message_generator.html#beast.ref.boost__beast__http__message_generator.member_functions)

| Name | Description |
| --- | --- |
| **[consume](boost__beast__http__message_generator/consume.html "http::message_generator::consume")** | `BuffersGenerator` |
| **[is\_done](boost__beast__http__message_generator/is_done.html "http::message_generator::is_done")** | `BuffersGenerator` |
| **[keep\_alive](boost__beast__http__message_generator/keep_alive.html "http::message_generator::keep_alive")** | Returns the result of `m.keep_alive()` on the underlying message. |
| **[message\_generator](boost__beast__http__message_generator/message_generator.html "http::message_generator::message_generator") [constructor]** |  |
| **[prepare](boost__beast__http__message_generator/prepare.html "http::message_generator::prepare")** | `BuffersGenerator` |

##### [Description](boost__beast__http__message_generator.html#beast.ref.boost__beast__http__message_generator.description)

Implements the BuffersGenerator concept for any concrete instance of the
 [`http::message`](boost__beast__http__message.html "http::message") 
template.

[`http::message_generator`](boost__beast__http__message_generator.html "http::message_generator")  takes ownership
of a message on construction, erasing the concrete type from the interface.

This makes it practical for use in server applications to implement request
handling:

```programlisting
template < class Body, class Fields>
http::message_generator handle_request(
    string_view doc_root,
    http::request<Body, Fields>&& request);
```

The [`beast::write`](boost__beast__write.html "write")
and [`beast::async_write`](boost__beast__async_write.html "async_write")
operations are provided for BuffersGenerator. The [`http::message::keep_alive`](boost__beast__http__message/keep_alive.html "http::message::keep_alive")  property is made available
for use after writing the message.