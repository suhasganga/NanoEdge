### [Send Child Process Output 💡](send_child_process_output.html "Send Child Process Output 💡")

Sometimes it is necessary to send a message whose body is not conveniently
described by a single container. For example, when implementing an HTTP relay
function a robust implementation needs to present body buffers individually
as they become available from the downstream host. These buffers should be
fixed in size, otherwise creating the unnecessary and inefficient burden
of reading the complete message body before forwarding it to the upstream
host.

To enable these use-cases, the body type [`buffer_body`](../ref/boost__beast__http__buffer_body.html "http::buffer_body") is provided. This body
uses a caller-provided pointer and size instead of an owned container. To
use this body, instantiate an instance of the serializer and fill in the
pointer and size fields before calling a stream write function.

This example reads from a child process and sends the output back in an HTTP
response. The output of the process is sent as it becomes available:

```programlisting
/** Send the output of a child process as an HTTP response.

    The output of the child process comes from a @b SyncReadStream. Data
    will be sent continuously as it is produced, without the requirement
    that the entire process output is buffered before being sent. The
    response will use the chunked transfer encoding.

    @param input A stream to read the child process output from.

    @param output A stream to write the HTTP response to.

    @param ec Set to the error, if any occurred.
*/
template<
    class SyncReadStream,
    class SyncWriteStream>
void
send_cgi_response(
    SyncReadStream& input,
    SyncWriteStream& output,
    error_code& ec)
{
    static_assert(is_sync_read_stream<SyncReadStream>::value,
        "SyncReadStream requirements not met");

    static_assert(is_sync_write_stream<SyncWriteStream>::value,
        "SyncWriteStream requirements not met");

    // Set up the response. We use the buffer_body type,
    // allowing serialization to use manually provided buffers.
    response<buffer_body> res;

    res.result(status::ok);
    res.version(11);
    res.set(field::server, "Beast");
    res.set(field::transfer_encoding, "chunked");

    // No data yet, but we set more = true to indicate
    // that it might be coming later. Otherwise the
    // serializer::is_done would return true right after
    // sending the header.
    res.body().data = nullptr;
    res.body().more = true;

    // Create the serializer.
    response_serializer<buffer_body, fields> sr{res};

    // Send the header immediately.
    write_header(output, sr, ec);
    if(ec)
        return;

    // Alternate between reading from the child process
    // and sending all the process output until there
    // is no more output.
    do
    {
        // Read a buffer from the child process
        char buffer[2048];
        auto bytes_transferred = input.read_some(
            boost::asio::buffer(buffer, sizeof(buffer)), ec);
        if(ec == boost::asio::error::eof)
        {
            ec = {};

            // `nullptr` indicates there is no buffer
            res.body().data = nullptr;

            // `false` means no more data is coming
            res.body().more = false;
        }
        else
        {
            if(ec)
                return;

            // Point to our buffer with the bytes that
            // we received, and indicate that there may
            // be some more data coming
            res.body().data = buffer;
            res.body().size = bytes_transferred;
            res.body().more = true;
        }

        // Write everything in the body buffer
        write(output, sr, ec);

        // This error is returned by body_buffer during
        // serialization when it is done sending the data
        // provided and needs another buffer.
        if(ec == error::need_buffer)
        {
            ec = {};
            continue;
        }
        if(ec)
            return;
    }
    while(! sr.is_done());
}
```