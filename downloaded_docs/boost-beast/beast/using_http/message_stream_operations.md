### [Message Stream Operations](message_stream_operations.html "Message Stream Operations")

Beast provides synchronous and asynchronous algorithms to parse and serialize
HTTP/1 wire format messages on streams. These functions form the message-oriented
stream interface:

**Table 1.20. Message Stream Operations**

| Name | Description |
| --- | --- |
| [**read**](../ref/boost__beast__http__read/overload3.html "http::read (3 of 4 overloads)") | Read a [`message`](../ref/boost__beast__http__message.html "http::message") from a [*SyncReadStream*](../../../../../../doc/html/boost_asio/reference/SyncReadStream.html). |
| [**async\_read**](../ref/boost__beast__http__async_read/overload2.html "http::async_read (2 of 2 overloads)") | Read a [`message`](../ref/boost__beast__http__message.html "http::message") from an [*AsyncReadStream*](../../../../../../doc/html/boost_asio/reference/AsyncReadStream.html). |
| [**write**](../ref/boost__beast__http__write/overload1.html "http::write (1 of 6 overloads)") | Write a [`message`](../ref/boost__beast__http__message.html "http::message") to a [*SyncWriteStream*](../../../../../../doc/html/boost_asio/reference/SyncWriteStream.html). |
| [**async\_write**](../ref/boost__beast__http__async_write.html "http::async_write") | Write a [`message`](../ref/boost__beast__http__message.html "http::message") to an [*AsyncWriteStream*](../../../../../../doc/html/boost_asio/reference/AsyncWriteStream.html). |

  

All synchronous stream operations come in two varieties. One which throws
an exception upon error, and another which accepts as the last parameter
an argument of type [`error_code&`](../ref/boost__beast__error_code.html "error_code").
If an error occurs this argument will be set to contain the error code.

##### [Reading](message_stream_operations.html#beast.using_http.message_stream_operations.reading)

Because a serialized header is not length-prefixed, algorithms which parse
messages from a stream may read past the end of a message for efficiency.
To hold this surplus data, all stream read operations use a passed-in [*DynamicBuffer*](../concepts/DynamicBuffer.html "DynamicBuffer")
which must be persisted between calls until the end of stream is reached
or the stream object is destroyed. Each read operation may consume bytes
remaining in the buffer, and leave behind new bytes. In this example we declare
the buffer and a message variable, then read a complete HTTP request synchronously:

```programlisting
flat_buffer buffer;         // (The parser is optimized for flat buffers)
request<string_body> req;
read(sock, buffer, req);
```

This example uses [`flat_buffer`](../ref/boost__beast__flat_buffer.html "flat_buffer"). Beast's [`basic_parser`](../ref/boost__beast__http__basic_parser.html "http::basic_parser") is optimized for structured
HTTP data located in a single contiguous (*flat*) memory
buffer. When not using a flat buffer the implementation may perform an additional
memory allocations to restructure the input into a single buffer for parsing.

|  |  |
| --- | --- |
| [Tip] | Tip |
| Other Implementations of [*DynamicBuffer*](../concepts/DynamicBuffer.html "DynamicBuffer") may avoid parser memory allocation by always returning buffer sequences of length one. |

Messages may also be read asynchronously. When performing asynchronous stream
read operations the stream, buffer, and message variables must remain valid
until the operation has completed. Beast asynchronous initiation functions
use Asio's completion handler model. This call reads a message asynchronously
and reports the error code upon completion. The handler is called with the
error, set to any that occurs, and the number of bytes parsed. This number
may be used to measure the relative amount of work performed, or it may be
ignored as this example shows.

```programlisting
flat_buffer buffer;
response<string_body> res;
async_read(sock, buffer, res,
    [&](error_code ec, std::size_t bytes_transferred)
    {
        boost::ignore_unused(bytes_transferred);
        std::cerr << ec.message() << std::endl;
    });
```

If a read stream algorithm cannot complete its operation without exceeding
the maximum specified size of the dynamic buffer provided, the error [`buffer_overflow`](../ref/boost__beast__http__error.html "http::error")
is returned. This is one technique which may be used to impose a limit on
the maximum size of an HTTP message header for protection from buffer overflow
attacks. The following code will print the error message:

```programlisting
// This buffer's max size is too small for much of anything
flat_buffer buffer{10};

// Try to read a request
error_code ec;
request<string_body> req;
read(sock, buffer, req, ec);
if(ec == http::error::buffer_overflow)
    std::cerr << "Buffer limit exceeded!" << std::endl;
```

##### [Writing](message_stream_operations.html#beast.using_http.message_stream_operations.writing)

A set of free functions allow serialization of an entire HTTP message to
a stream. This example constructs and sends an HTTP response:

```programlisting
response<string_body> res;
res.version(11);
res.result(status::ok);
res.set(field::server, "Beast");
res.body() = "Hello, world!";
res.prepare_payload();

error_code ec;
write(sock, res, ec);
```

The asynchronous version could be used instead:

```programlisting
async_write(sock, res,
    [&](error_code ec, std::size_t bytes_transferred)
    {
        boost::ignore_unused(bytes_transferred);
        if(ec)
            std::cerr << ec.message() << std::endl;
    });
```

The completion handler is called with the number of bytes written to the
stream, which includes protocol specific data such as the delimiters in the
header and line endings. The number may be used to measure the amount of
data transferred, or it may be ignored as in the example.