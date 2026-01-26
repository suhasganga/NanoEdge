### [HEAD response (Server) 💡](head_response_server.html "HEAD response (Server) 💡")

When a server receives a [HEAD
request](https://tools.ietf.org/html/rfc7231#section-4.3.2), the response should contain the entire header that would
be delivered if the method was GET, except that the body is omitted.

```programlisting
/** Handle a HEAD request for a resource.
*/
template<
    class SyncStream,
    class DynamicBuffer
>
void do_server_head(
    SyncStream& stream,
    DynamicBuffer& buffer,
    error_code& ec)
{
    static_assert(is_sync_stream<SyncStream>::value,
        "SyncStream requirements not met");
    static_assert(
        boost::asio::is_dynamic_buffer<DynamicBuffer>::value,
        "DynamicBuffer requirements not met");

    // We deliver this payload for all GET requests
    static std::string const payload = "Hello, world!";

    // Read the request
    request<string_body> req;
    read(stream, buffer, req, ec);
    if(ec)
        return;

    // Set up the response, starting with the common fields
    response<string_body> res;
    res.version(11);
    res.set(field::server, "test");

    // Now handle request-specific fields
    switch(req.method())
    {
    case verb::head:
    case verb::get:
    {
        // A HEAD request is handled by delivering the same
        // set of headers that would be sent for a GET request,
        // including the Content-Length, except for the body.
        res.result(status::ok);
        res.content_length(payload.size());

        // For GET requests, we include the body
        if(req.method() == verb::get)
        {
            // We deliver the same payload for GET requests
            // regardless of the target. A real server might
            // deliver a file based on the target.
            res.body() = payload;
        }
        break;
    }

    default:
    {
        // We return responses indicating an error if
        // we do not recognize the request method.
        res.result(status::bad_request);
        res.set(field::content_type, "text/plain");
        res.body() = "Invalid request-method '" + std::string(req.method_string()) + "'";
        res.prepare_payload();
        break;
    }
    }

    // Send the response
    write(stream, res, ec);
    if(ec)
        return;
}
```