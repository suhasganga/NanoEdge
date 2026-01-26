#### [http::icy\_stream](boost__beast__http__icy_stream.html "http::icy_stream")

Stream wrapper to process Shoutcast HTTP responses.

##### [Synopsis](boost__beast__http__icy_stream.html#beast.ref.boost__beast__http__icy_stream.synopsis)

Defined in header `<boost/beast/_experimental/http/icy_stream.hpp>`

```programlisting
template<
    class NextLayer>
class icy_stream
```

##### [Types](boost__beast__http__icy_stream.html#beast.ref.boost__beast__http__icy_stream.types)

| Name | Description |
| --- | --- |
| **[executor\_type](boost__beast__http__icy_stream/executor_type.html "http::icy_stream::executor_type")** | The type of the executor associated with the object. |
| **[next\_layer\_type](boost__beast__http__icy_stream/next_layer_type.html "http::icy_stream::next_layer_type")** | The type of the next layer. |

##### [Member Functions](boost__beast__http__icy_stream.html#beast.ref.boost__beast__http__icy_stream.member_functions)

| Name | Description |
| --- | --- |
| **[async\_read\_some](boost__beast__http__icy_stream/async_read_some.html "http::icy_stream::async_read_some")** | Start an asynchronous read. |
| **[async\_write\_some](boost__beast__http__icy_stream/async_write_some.html "http::icy_stream::async_write_some")** | Start an asynchronous write. |
| **[get\_executor](boost__beast__http__icy_stream/get_executor.html "http::icy_stream::get_executor")** | Get the executor associated with the object. |
| **[icy\_stream](boost__beast__http__icy_stream/icy_stream.html "http::icy_stream::icy_stream") [constructor]** | — Constructor. |
| **[next\_layer](boost__beast__http__icy_stream/next_layer.html "http::icy_stream::next_layer")** | Get a reference to the next layer. |
| **[operator=](boost__beast__http__icy_stream/operator_eq_.html "http::icy_stream::operator=")** |  |
| **[read\_some](boost__beast__http__icy_stream/read_some.html "http::icy_stream::read_some")** | Read some data from the stream. |
| **[write\_some](boost__beast__http__icy_stream/write_some.html "http::icy_stream::write_some")** | Write some data to the stream. |
| **[~icy\_stream](boost__beast__http__icy_stream/_dtor_icy_stream.html "http::icy_stream::~icy_stream") [destructor]** | Destructor. |

##### [Description](boost__beast__http__icy_stream.html#beast.ref.boost__beast__http__icy_stream.description)

This wrapper replaces the word "ICY" in the first HTTP response
received on the connection, with "HTTP/1.1". This allows the Beast
parser to be used with Shoutcast servers, which send a non-standard HTTP
message as the response.

For asynchronous operations, the application must ensure that they are are
all performed within the same implicit or explicit strand.

##### [Thread Safety](boost__beast__http__icy_stream.html#beast.ref.boost__beast__http__icy_stream.thread_safety)

*Distinct**objects:*Safe.

*Shared**objects:*Unsafe. The application
must also ensure that all asynchronous operations are performed within the
same implicit or explicit strand.

##### [Example](boost__beast__http__icy_stream.html#beast.ref.boost__beast__http__icy_stream.example)

To use the [`icy_stream`](boost__beast__http__icy_stream.html "http::icy_stream") template with an [`tcp_stream`](boost__beast__tcp_stream.html "tcp_stream")
you would write:

```programlisting
http::icy_stream<tcp_stream> is(ioc);
```

##### [Template Parameters](boost__beast__http__icy_stream.html#beast.ref.boost__beast__http__icy_stream.template_parameters)

| Type | Description |
| --- | --- |
| `NextLayer` | The type representing the next layer, to which data will be read and written during operations. For synchronous operations, the type must support the *SyncStream* concept. For asynchronous operations, the type must support the *AsyncStream* concept. |

##### [Remarks](boost__beast__http__icy_stream.html#beast.ref.boost__beast__http__icy_stream.remarks)

A stream object must not be moved or destroyed while there are pending asynchronous
operations associated with it.