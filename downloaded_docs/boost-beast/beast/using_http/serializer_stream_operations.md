### [Serializer Stream Operations](serializer_stream_operations.html "Serializer Stream Operations")

Non-trivial algorithms need to do more than send entire messages at once,
such as:

* Send the header first, and the body later.
* Send a message incrementally: bounded work in each I/O cycle.
* Use a series of caller-provided buffers to represent the body.

These tasks may be performed by using the serializer stream interfaces. To
use these interfaces, first construct an appropriate serializer from the
message to be sent:

**Table 1.21. Serializer**

| Name | Description |
| --- | --- |
| [`serializer`](../ref/boost__beast__http__serializer.html "http::serializer") | ```programlisting /// Provides buffer oriented HTTP message serialization functionality. template<     bool isRequest,     class Body,     class Fields = fields > class serializer; ``` |
| [`request_serializer`](../ref/boost__beast__http__request_serializer.html "http::request_serializer") | ```programlisting /// A serializer for HTTP/1 requests template<     class Body,     class Fields = fields > using request_serializer = serializer<true, Body, Fields>; ``` |
| [`response_serializer`](../ref/boost__beast__http__response_serializer.html "http::response_serializer") | ```programlisting /// A serializer for HTTP/1 responses template<     class Body,     class Fields = fields > using response_serializer = serializer<false, Body, Fields>; ``` |

  

The choices for template types must match the message passed on construction.
This code creates an HTTP response and the corresponding serializer:

```programlisting
response<string_body> res;

response_serializer<string_body> sr{res};
```

The stream operations which work on serializers are:

**Table 1.22. Serializer Stream Operations**

| Name | Description |
| --- | --- |
| [**write**](../ref/boost__beast__http__write/overload1.html "http::write (1 of 6 overloads)") | Send everything in a [`serializer`](../ref/boost__beast__http__serializer.html "http::serializer") to a [*SyncWriteStream*](../../../../../../doc/html/boost_asio/reference/SyncWriteStream.html). |
| [**async\_write**](../ref/boost__beast__http__async_write/overload1.html "http::async_write (1 of 3 overloads)") | Send everything in a [`serializer`](../ref/boost__beast__http__serializer.html "http::serializer") asynchronously to an [*AsyncWriteStream*](../../../../../../doc/html/boost_asio/reference/AsyncWriteStream.html). |
| [**write\_header**](../ref/boost__beast__http__write_header/overload1.html "http::write_header (1 of 2 overloads)") | Send only the header from a [`serializer`](../ref/boost__beast__http__serializer.html "http::serializer") to a [*SyncWriteStream*](../../../../../../doc/html/boost_asio/reference/SyncWriteStream.html). |
| [**async\_write\_header**](../ref/boost__beast__http__async_write_header.html "http::async_write_header") | Send only the header from a [`serializer`](../ref/boost__beast__http__serializer.html "http::serializer") asynchronously to an [*AsyncWriteStream*](../../../../../../doc/html/boost_asio/reference/AsyncWriteStream.html). |
| [**write\_some**](../ref/boost__beast__http__write_some/overload1.html "http::write_some (1 of 2 overloads)") | Send part of a [`serializer`](../ref/boost__beast__http__serializer.html "http::serializer") to a [*SyncWriteStream*](../../../../../../doc/html/boost_asio/reference/SyncWriteStream.html). |
| [**async\_write\_some**](../ref/boost__beast__http__async_write_some.html "http::async_write_some") | Send part of a [`serializer`](../ref/boost__beast__http__serializer.html "http::serializer") asynchronously to an [*AsyncWriteStream*](../../../../../../doc/html/boost_asio/reference/AsyncWriteStream.html). |

  

Here is an example of using a serializer to send a message on a stream synchronously.
This performs the same operation as calling `write(stream, m)`:

```programlisting
/** Send a message to a stream synchronously.

    @param stream The stream to write to. This type must support
    the <em>SyncWriteStream</em> concept.

    @param m The message to send. The Body type must support
    the <em>BodyWriter</em> concept.
*/
template<
    class SyncWriteStream,
    bool isRequest, class Body, class Fields>
void
send(
    SyncWriteStream& stream,
    message<isRequest, Body, Fields> const& m)
{
    // Check the template types
    static_assert(is_sync_write_stream<SyncWriteStream>::value,
        "SyncWriteStream type requirements not met");
    static_assert(is_body_writer<Body>::value,
        "BodyWriter type requirements not met");

    // Create the instance of serializer for the message
    serializer<isRequest, Body, Fields> sr{m};

    // Loop until the serializer is finished
    do
    {
        // This call guarantees it will make some
        // forward progress, or otherwise return an error.
        write_some(stream, sr);
    }
    while(! sr.is_done());
}
```