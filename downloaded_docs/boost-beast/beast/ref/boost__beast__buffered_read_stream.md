#### [buffered\_read\_stream](boost__beast__buffered_read_stream.html "buffered_read_stream")

A *Stream* with attached *DynamicBuffer*
to buffer reads.

##### [Synopsis](boost__beast__buffered_read_stream.html#beast.ref.boost__beast__buffered_read_stream.synopsis)

Defined in header `<boost/beast/core/buffered_read_stream.hpp>`

```programlisting
template<
    class Stream,
    class DynamicBuffer>
class buffered_read_stream
```

##### [Types](boost__beast__buffered_read_stream.html#beast.ref.boost__beast__buffered_read_stream.types)

| Name | Description |
| --- | --- |
| **[buffer\_type](boost__beast__buffered_read_stream/buffer_type.html "buffered_read_stream::buffer_type")** | The type of the internal buffer. |
| **[executor\_type](boost__beast__buffered_read_stream/executor_type.html "buffered_read_stream::executor_type")** |  |
| **[next\_layer\_type](boost__beast__buffered_read_stream/next_layer_type.html "buffered_read_stream::next_layer_type")** | The type of the next layer. |

##### [Member Functions](boost__beast__buffered_read_stream.html#beast.ref.boost__beast__buffered_read_stream.member_functions)

| Name | Description |
| --- | --- |
| **[async\_read\_some](boost__beast__buffered_read_stream/async_read_some.html "buffered_read_stream::async_read_some")** | Start an asynchronous read. |
| **[async\_write\_some](boost__beast__buffered_read_stream/async_write_some.html "buffered_read_stream::async_write_some")** | Start an asynchronous write. |
| **[buffer](boost__beast__buffered_read_stream/buffer.html "buffered_read_stream::buffer")** | Access the internal buffer. |
| **[buffered\_read\_stream](boost__beast__buffered_read_stream/buffered_read_stream.html "buffered_read_stream::buffered_read_stream") [constructor]** | Move constructor.  — Construct the wrapping stream. |
| **[capacity](boost__beast__buffered_read_stream/capacity.html "buffered_read_stream::capacity")** | Set the maximum buffer size. |
| **[get\_executor](boost__beast__buffered_read_stream/get_executor.html "buffered_read_stream::get_executor")** | Get the executor associated with the object. |
| **[next\_layer](boost__beast__buffered_read_stream/next_layer.html "buffered_read_stream::next_layer")** | Get a reference to the next layer.  — Get a const reference to the next layer. |
| **[operator=](boost__beast__buffered_read_stream/operator_eq_.html "buffered_read_stream::operator=")** | Move assignment. |
| **[read\_some](boost__beast__buffered_read_stream/read_some.html "buffered_read_stream::read_some")** | Read some data from the stream. |
| **[write\_some](boost__beast__buffered_read_stream/write_some.html "buffered_read_stream::write_some")** | Write some data to the stream. |

##### [Description](boost__beast__buffered_read_stream.html#beast.ref.boost__beast__buffered_read_stream.description)

This wraps a *Stream* implementation so that calls to
write are passed through to the underlying stream, while calls to read will
first consume the input sequence stored in a *DynamicBuffer*
which is part of the object.

The use-case for this class is different than that of the `net::buffered_read_stream`.
It is designed to facilitate the use of `net::read_until`,
and to allow buffers acquired during detection of handshakes to be made transparently
available to callers. A hypothetical implementation of the buffered version
of `net::ssl::stream::async_handshake`
could make use of this wrapper.

Uses:

* Transparently leave untouched input acquired in calls to `net::read_until` behind for subsequent callers.
* "Preload" a stream with handshake input data acquired from
  other sources.

Example:

```programlisting
// Process the next HTTP header on the stream,
// leaving excess bytes behind for the next call.
//
template < class Stream, class DynamicBuffer>
void process_http_message(
    buffered_read_stream<Stream, DynamicBuffer>& stream)
{
    // Read up to and including the end of the HTTP
    // header, leaving the sequence in the stream's
    // buffer. read_until may read past the end of the
    // headers; the return value will include only the
    // part up to the end of the delimiter.
    //
    std::size_t bytes_transferred =
        net::read_until(
            stream.next_layer(), stream.buffer(), "\r\n\r\n" );

    // Use buffers_prefix() to limit the input
    // sequence to only the data up to and including
    // the trailing "\r\n\r\n".
    //
    auto header_buffers = buffers_prefix(
        bytes_transferred, stream.buffer().data());

    ...

    // Discard the portion of the input corresponding
    // to the HTTP headers.
    //
    stream.buffer().consume(bytes_transferred);

    // Everything we read from the stream
    // is part of the content-body.
}
```

##### [Template Parameters](boost__beast__buffered_read_stream.html#beast.ref.boost__beast__buffered_read_stream.template_parameters)

| Type | Description |
| --- | --- |
| `Stream` | The type of stream to wrap. |
| `DynamicBuffer` | The type of stream buffer to use. |