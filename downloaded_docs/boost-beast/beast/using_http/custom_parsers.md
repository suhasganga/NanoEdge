### [Custom Parsers](custom_parsers.html "Custom Parsers")

While the parsers included in the library will handle a broad number of use-cases,
the [`basic_parser`](../ref/boost__beast__http__basic_parser.html "http::basic_parser") interface can be subclassed
to implement custom strategies for storing parsed results: the basic parser
processes input buffers into elements according to the HTTP/1 protocol specification,
while the derived class decides what to do with those elements. Custom parsers
will work with all of the HTTP stream read algorithms, as those algorithms
use only the basic parser interface. Some use cases for implementing custom
parsers are:

* Inspect incoming header fields and keep or discard them.
* Use a container provided by an external interface.

The basic parser uses virtual functions. To declare your user-defined parser,
derive from [`basic_parser`](../ref/boost__beast__http__basic_parser.html "http::basic_parser") and implement all the
required virtual functions. A declaration for the derived class may look
like this:

```programlisting
template<bool isRequest>
class custom_parser : public basic_parser<isRequest>
{
private:
    /** Called after receiving the request-line.

        This virtual function is invoked after receiving a request-line
        when parsing HTTP requests.
        It can only be called when `isRequest == true`.

        @param method The verb enumeration. If the method string is not
        one of the predefined strings, this value will be @ref verb::unknown.

        @param method_str The unmodified string representing the verb.

        @param target The request-target.

        @param version The HTTP-version. This will be 10 for HTTP/1.0,
        and 11 for HTTP/1.1.

        @param ec An output parameter which the function may set to indicate
        an error. The error will be clear before this function is invoked.
    */
    void
    on_request_impl(
        verb method,                // The method verb, verb::unknown if no match
        string_view method_str,     // The method as a string
        string_view target,         // The request-target
        int version,                // The HTTP-version
        error_code& ec) override;   // The error returned to the caller, if any

    /** Called after receiving the status-line.

        This virtual function is invoked after receiving a status-line
        when parsing HTTP responses.
        It can only be called when `isRequest == false`.

        @param code The numeric status code.

        @param reason The reason-phrase. Note that this value is
        now obsolete, and only provided for historical or diagnostic
        purposes.

        @param version The HTTP-version. This will be 10 for HTTP/1.0,
        and 11 for HTTP/1.1.

        @param ec An output parameter which the function may set to indicate
        an error. The error will be clear before this function is invoked.
    */
    void
    on_response_impl(
        int code,                   // The status-code
        string_view reason,         // The obsolete reason-phrase
        int version,                // The HTTP-version
        error_code& ec) override;   // The error returned to the caller, if any

    /** Called once for each complete field in the HTTP header.

        This virtual function is invoked for each field that is received
        while parsing an HTTP message.

        @param name The known field enum value. If the name of the field
        is not recognized, this value will be @ref field::unknown.

        @param name_string The exact name of the field as received from
        the input, represented as a string.

        @param value A string holding the value of the field.

        @param ec An output parameter which the function may set to indicate
        an error. The error will be clear before this function is invoked.
    */
    void
    on_field_impl(
        field f,                    // The known-field enumeration constant
        string_view name,           // The field name string.
        string_view value,          // The field value
        error_code& ec) override;   // The error returned to the caller, if any

    /** Called once after the complete HTTP header is received.

        This virtual function is invoked once, after the complete HTTP
        header is received while parsing a message.

        @param ec An output parameter which the function may set to indicate
        an error. The error will be clear before this function is invoked.
    */
    void
    on_header_impl(
        error_code& ec) override;   // The error returned to the caller, if any

    /** Called once before the body is processed.

        This virtual function is invoked once, before the content body is
        processed (but after the complete header is received).

        @param content_length A value representing the content length in
        bytes if the length is known (this can include a zero length).
        Otherwise, the value will be `boost::none`.

        @param ec An output parameter which the function may set to indicate
        an error. The error will be clear before this function is invoked.
    */
    void
    on_body_init_impl(
        boost::optional<
            std::uint64_t> const&
                content_length,     // Content length if known, else `boost::none`
        error_code& ec) override;   // The error returned to the caller, if any

    /** Called each time additional data is received representing the content body.

        This virtual function is invoked for each piece of the body which is
        received while parsing of a message. This function is only used when
        no chunked transfer encoding is present.

        @param body A string holding the additional body contents. This may
        contain nulls or unprintable characters.

        @param ec An output parameter which the function may set to indicate
        an error. The error will be clear before this function is invoked.

        @see on_chunk_body_impl
    */
    std::size_t
    on_body_impl(
        string_view s,              // A portion of the body
        error_code& ec) override;   // The error returned to the caller, if any

    /** Called each time a new chunk header of a chunk encoded body is received.

        This function is invoked each time a new chunk header is received.
        The function is only used when the chunked transfer encoding is present.

        @param size The size of this chunk, in bytes.

        @param extensions A string containing the entire chunk extensions.
        This may be empty, indicating no extensions are present.

        @param ec An output parameter which the function may set to indicate
        an error. The error will be clear before this function is invoked.
    */
    void
    on_chunk_header_impl(
        std::uint64_t size,         // The size of the upcoming chunk,
                                    // or zero for the last chunk
        string_view extension,      // The chunk extensions (may be empty)
        error_code& ec) override;   // The error returned to the caller, if any

    /** Called each time additional data is received representing part of a body chunk.

        This virtual function is invoked for each piece of the body which is
        received while parsing of a message. This function is only used when
        no chunked transfer encoding is present.

        @param remain The number of bytes remaining in this chunk. This includes
        the contents of passed `body`. If this value is zero, then this represents
        the final chunk.

        @param body A string holding the additional body contents. This may
        contain nulls or unprintable characters.

        @param ec An output parameter which the function may set to indicate
        an error. The error will be clear before this function is invoked.

        @return This function should return the number of bytes actually consumed
        from the `body` value. Any bytes that are not consumed on this call
        will be presented in a subsequent call.

        @see on_body_impl
    */
    std::size_t
    on_chunk_body_impl(
        std::uint64_t remain,       // The number of bytes remaining in the chunk,
                                    // including what is being passed here.
                                    // or zero for the last chunk
        string_view body,           // The next piece of the chunk body
        error_code& ec) override;   // The error returned to the caller, if any

    /** Called once when the complete message is received.

        This virtual function is invoked once, after successfully parsing
        a complete HTTP message.

        @param ec An output parameter which the function may set to indicate
        an error. The error will be clear before this function is invoked.
    */
    void
    on_finish_impl(
        error_code& ec) override;   // The error returned to the caller, if any

public:
    custom_parser() = default;
};
```