### [Expect 100-continue (Client) 💡](expect_100_continue_client.html "Expect 100-continue (Client) 💡")

The Expect field with the value "100-continue" in a request is
special. It indicates that the after sending the message header, a client
desires an immediate informational response before sending the message body,
which presumably may be expensive to compute or large. This behavior is described
in [rfc7231
section 5.1.1](https://tools.ietf.org/html/rfc7231#section-5.1.1). Invoking the 100-continue behavior is implemented
easily in a client by constructing a [`serializer`](../ref/boost__beast__http__serializer.html "http::serializer") to send the header first,
then receiving the server response, and finally conditionally send the body
using the same serializer instance. A synchronous, simplified version (no
timeout) of this client action looks like this:

```programlisting
/** Send a request with Expect: 100-continue

    This function will send a request with the Expect: 100-continue
    field by first sending the header, then waiting for a successful
    response from the server before continuing to send the body. If
    a non-successful server response is received, the function
    returns immediately.

    @param stream The remote HTTP server stream.

    @param buffer The buffer used for reading.

    @param req The request to send. This function modifies the object:
    the Expect header field is inserted into the message if it does
    not already exist, and set to "100-continue".

    @param ec Set to the error, if any occurred.
*/
template<
    class SyncStream,
    class DynamicBuffer,
    class Body, class Allocator>
void
send_expect_100_continue(
    SyncStream& stream,
    DynamicBuffer& buffer,
    request<Body, basic_fields<Allocator>>& req,
    error_code& ec)
{
    static_assert(is_sync_stream<SyncStream>::value,
        "SyncStream requirements not met");

    static_assert(
        boost::asio::is_dynamic_buffer<DynamicBuffer>::value,
        "DynamicBuffer requirements not met");

    // Insert or replace the Expect field
    req.set(field::expect, "100-continue");

    // Create the serializer
    request_serializer<Body, basic_fields<Allocator>> sr{req};

    // Send just the header
    write_header(stream, sr, ec);
    if(ec)
        return;

    // Read the response from the server.
    // A robust client could set a timeout here.
    {
        response<string_body> res;
        read(stream, buffer, res, ec);
        if(ec)
            return;
        if(res.result() != status::continue_)
        {
            // The server indicated that it will not
            // accept the request, so skip sending the body.
            return;
        }
    }

    // Server is OK with the request, send the body
    write(stream, sr, ec);
}
```