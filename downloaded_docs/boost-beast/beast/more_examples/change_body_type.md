### [Change Body Type 💡](change_body_type.html "Change Body Type 💡")

Sophisticated servers may wish to defer the choice of the Body template type
until after the header is available. Then, a body type may be chosen depending
on the header contents. For example, depending on the verb, target path,
or target query parameters. To accomplish this, a parser is declared to read
in the header only, using a trivial body type such as [`empty_body`](../ref/boost__beast__http__empty_body.html "http::empty_body"). Then, a new parser is
constructed from this existing parser where the body type is conditionally
determined by information from the header or elsewhere.

This example illustrates how a server may make the commitment of a body type
depending on the method verb:

```programlisting
/** Handle a form POST request, choosing a body type depending on the Content-Type.

    This reads a request from the input stream. If the method is POST, and
    the Content-Type is "application/x-www-form-urlencoded  " or
    "multipart/form-data", a `string_body` is used to receive and store
    the message body. Otherwise, a `dynamic_body` is used to store the message
    body. After the request is received, the handler will be invoked with the
    request.

    @param stream The stream to read from.

    @param buffer The buffer to use for reading.

    @param handler The handler to invoke when the request is complete.
    The handler must be invokable with this signature:
    @code
    template<class Body>
    void handler(request<Body>&& req);
    @endcode

    @throws system_error Thrown on failure.
*/
template<
    class SyncReadStream,
    class DynamicBuffer,
    class Handler>
void
do_form_request(
    SyncReadStream& stream,
    DynamicBuffer& buffer,
    Handler&& handler)
{
    // Start with an empty_body parser
    request_parser<empty_body> req0;

    // Read just the header. Otherwise, the empty_body
    // would generate an error if body octets were received.
    read_header(stream, buffer, req0);

    // Choose a body depending on the method verb
    switch(req0.get().method())
    {
    case verb::post:
    {
        // If this is not a form upload then use a string_body
        if( req0.get()[field::content_type] != "application/x-www-form-urlencoded" &&
            req0.get()[field::content_type] != "multipart/form-data")
            goto do_dynamic_body;

        // Commit to string_body as the body type.
        // As long as there are no body octets in the parser
        // we are constructing from, no exception is thrown.
        request_parser<string_body> req{std::move(req0)};

        // Finish reading the message
        read(stream, buffer, req);

        // Call the handler. It can take ownership
        // if desired, since we are calling release()
        handler(req.release());
        break;
    }

    do_dynamic_body:
    default:
    {
        // Commit to dynamic_body as the body type.
        // As long as there are no body octets in the parser
        // we are constructing from, no exception is thrown.
        request_parser<dynamic_body> req{std::move(req0)};

        // Finish reading the message
        read(stream, buffer, req);

        // Call the handler. It can take ownership
        // if desired, since we are calling release()
        handler(req.release());
        break;
    }
    }
}
```