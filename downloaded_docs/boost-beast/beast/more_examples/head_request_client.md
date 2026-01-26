### [HEAD request (Client) 💡](head_request_client.html "HEAD request (Client) 💡")

The [HEAD request](https://tools.ietf.org/html/rfc7231#section-4.3.2)
method indicates to the server that the client wishes to receive the entire
header that would be delivered if the method was GET, except that the body
is omitted. When a client wishes to receive the response to a HEAD request,
it is necessary to inform the parser not to expect a body. This is done by
calling [`basic_parser::skip`](../ref/boost__beast__http__basic_parser/skip.html "http::basic_parser::skip") with the value `true`, as shown in this example:

```programlisting
/** Send a HEAD request for a resource.

    This function submits a HEAD request for the specified resource
    and returns the response.

    @param res The response. This is an output parameter.

    @param stream The synchronous stream to use.

    @param buffer The buffer to use.

    @param target The request target.

    @param ec Set to the error, if any occurred.

    @throws std::invalid_argument if target is empty.
*/
template<
    class SyncStream,
    class DynamicBuffer
>
response<empty_body>
do_head_request(
    SyncStream& stream,
    DynamicBuffer& buffer,
    string_view target,
    error_code& ec)
{
    // Do some type checking to be a good citizen
    static_assert(is_sync_stream<SyncStream>::value,
        "SyncStream requirements not met");
    static_assert(
        boost::asio::is_dynamic_buffer<DynamicBuffer>::value,
        "DynamicBuffer requirements not met");

    // The interfaces we are using are low level and do not
    // perform any checking of arguments; so we do it here.
    if(target.empty())
        throw std::invalid_argument("target may not be empty");

    // Build the HEAD request for the target
    request<empty_body> req;
    req.version(11);
    req.method(verb::head);
    req.target(target);
    req.set(field::user_agent, "test");

    // A client MUST send a Host header field in all HTTP/1.1 request messages.
    // https://tools.ietf.org/html/rfc7230#section-5.4
    req.set(field::host, "localhost");

    // Now send it
    write(stream, req, ec);
    if(ec)
        return {};

    // Create a parser to read the response.
    // We use the `empty_body` type since
    // a response to a HEAD request MUST NOT
    // include a body.
    response_parser<empty_body> p;

    // Inform the parser that there will be no body.
    p.skip(true);

    // Read the message. Even though fields like
    // Content-Length or Transfer-Encoding may be
    // set, the message will not contain a body.
    read(stream, buffer, p, ec);
    if(ec)
        return {};

    // Transfer ownership of the response to the caller.
    return p.release();
}
```