### [Expect 100-continue (Server) 💡](expect_100_continue_server.html "Expect 100-continue (Server) 💡")

The Expect field with the value "100-continue" in a request is
special. It indicates that the after sending the message header, a client
desires an immediate informational response before sending the message body,
which presumably may be expensive to compute or large. This behavior is described
in [rfc7231
section 5.1.1](https://tools.ietf.org/html/rfc7231#section-5.1.1). Handling the Expect field can be implemented easily
in a server by constructing a [`parser`](../ref/boost__beast__http__parser.html "http::parser") to read the header first,
then send an informational HTTP response, and finally read the body using
the same parser instance. A synchronous version of this server action looks
like this:

```programlisting
/** Receive a request, handling Expect: 100-continue if present.

    This function will read a request from the specified stream.
    If the request contains the Expect: 100-continue field, a
    status response will be delivered.

    @param stream The remote HTTP client stream.

    @param buffer The buffer used for reading.

    @param ec Set to the error, if any occurred.
*/
template<
    class SyncStream,
    class DynamicBuffer>
void
receive_expect_100_continue(
    SyncStream& stream,
    DynamicBuffer& buffer,
    error_code& ec)
{
    static_assert(is_sync_stream<SyncStream>::value,
        "SyncStream requirements not met");

    static_assert(
        boost::asio::is_dynamic_buffer<DynamicBuffer>::value,
        "DynamicBuffer requirements not met");

    // Declare a parser for a request with a string body
    request_parser<string_body> parser;

    // Read the header
    read_header(stream, buffer, parser, ec);
    if(ec)
        return;

    // Check for the Expect field value
    if(beast::iequals(parser.get()[field::expect], "100-continue"))
    {
        // send 100 response
        response<empty_body> res;
        res.version(11);
        res.result(status::continue_);
        res.set(field::server, "test");
        write(stream, res, ec);
        if(ec)
            return;
    }

    // Read the rest of the message.
    //
    read(stream, buffer, parser, ec);
}
```