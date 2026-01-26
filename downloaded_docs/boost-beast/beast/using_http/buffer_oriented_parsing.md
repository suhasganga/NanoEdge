### [Buffer-Oriented Parsing](buffer_oriented_parsing.html "Buffer-Oriented Parsing")

A subclass of [`basic_parser`](../ref/boost__beast__http__basic_parser.html "http::basic_parser") can be invoked directly,
without using the provided stream operations. This could be useful for implementing
algorithms on objects whose interface does not conform to [*Stream*](../concepts/streams.html "Streams").
For example, a [**ZeroMQ**
socket](http://zeromq.org/). The basic parser interface is interactive; the caller invokes
the function [`basic_parser::put`](../ref/boost__beast__http__basic_parser/put.html "http::basic_parser::put") repeatedly with buffers until
an error occurs or the parsing is done. The function [`basic_parser::put_eof`](../ref/boost__beast__http__basic_parser/put_eof.html "http::basic_parser::put_eof") Is used when the caller
knows that there will never be more data (for example, if the underlying
connection is closed),

##### [Parser Options](buffer_oriented_parsing.html#beast.using_http.buffer_oriented_parsing.parser_options)

The parser provides a few options which may be set before parsing begins:

**Table 1.25. Parser Options**

| Name | Default | Description |
| --- | --- | --- |
| [`eager`](../ref/boost__beast__http__basic_parser/eager/overload2.html "http::basic_parser::eager (2 of 2 overloads)") | `false` | Normally the parser returns after successfully parsing a structured element (header, chunk header, or chunk body) even if there are octets remaining in the input. This is necessary when attempting to parse the header first, or when the caller wants to inspect information which may be invalidated by subsequent parsing, such as a chunk extension. The `eager` option controls whether the parser keeps going after parsing structured element if there are octets remaining in the buffer and no error occurs. This option is automatically set or cleared during certain stream operations to improve performance with no change in functionality. |
| [`skip`](../ref/boost__beast__http__basic_parser/skip/overload2.html "http::basic_parser::skip (2 of 2 overloads)") | `false` | This option controls whether or not the parser expects to see an HTTP body, regardless of the presence or absence of certain fields such as Content-Length or a chunked Transfer-Encoding. Depending on the request, some responses do not carry a body. For example, a 200 response to a [CONNECT](https://tools.ietf.org/html/rfc7231#section-4.3.6) request from a tunneling proxy, or a response to a [HEAD](https://tools.ietf.org/html/rfc7231#section-4.3.2) request. In these cases, callers may use this function inform the parser that no body is expected. The parser will consider the message complete after the header has been received. |
| [`body_limit`](../ref/boost__beast__http__basic_parser/body_limit.html "http::basic_parser::body_limit") | 1MB/8MB | This function sets the maximum allowed size of the content body. When a body larger than the specified size is detected, an error is generated and parsing terminates. This setting helps protect servers from resource exhaustion attacks. The default limit when parsing requests is 1MB, and for parsing responses 8MB. |
| [`header_limit`](../ref/boost__beast__http__basic_parser/header_limit.html "http::basic_parser::header_limit") | 8KB | This function sets the maximum allowed size of the header including all field name, value, and delimiter characters and also including the CRLF sequences in the serialized input. |

  

#### [Read From std::istream 💡](buffer_oriented_parsing.html#beast.using_http.buffer_oriented_parsing.read_from_std_istream "Read From std::istream 💡")

The standard library provides the type `std::istream`
for performing high level read operations on character streams. The variable
`std::cin` is based on this input stream. This
example uses the buffer oriented interface of [`basic_parser`](../ref/boost__beast__http__basic_parser.html "http::basic_parser") to build a stream
operation which parses an HTTP message from a `std::istream`:

```programlisting
/** Read a message from a `std::istream`.

    This function attempts to parse a complete HTTP/1 message from the stream.

    @param is The `std::istream` to read from.

    @param buffer The buffer to use.

    @param msg The message to store the result.

    @param ec Set to the error, if any occurred.
*/
template<
    class Allocator,
    bool isRequest,
    class Body>
void
read_istream(
    std::istream& is,
    basic_flat_buffer<Allocator>& buffer,
    message<isRequest, Body, fields>& msg,
    error_code& ec)
{
    // Create the message parser
    //
    // Arguments passed to the parser's constructor are
    // forwarded to the message constructor. Here, we use
    // a move construction in case the caller has constructed
    // their message in a non-default way.
    //
    parser<isRequest, Body> p{std::move(msg)};

    do
    {
        // Extract whatever characters are presently available in the istream
        if(is.rdbuf()->in_avail() > 0)
        {
            // Get a mutable buffer sequence for writing
            auto const b = buffer.prepare(
                static_cast<std::size_t>(is.rdbuf()->in_avail()));

            // Now get everything we can from the istream
            buffer.commit(static_cast<std::size_t>(is.readsome(
                reinterpret_cast<char*>(b.data()), b.size())));
        }
        else if(buffer.size() == 0)
        {
            // Our buffer is empty and we need more characters, 
            // see if we've reached the end of file on the istream
            if(! is.eof())
            {
                // Get a mutable buffer sequence for writing
                auto const b = buffer.prepare(1024);

                // Try to get more from the istream. This might block.
                is.read(reinterpret_cast<char*>(b.data()), b.size());

                // If an error occurs on the istream then return it to the caller.
                if(is.fail() && ! is.eof())
                {
                    // We'll just re-use io_error since std::istream has no error_code interface.
                    ec = make_error_code(errc::io_error);
                    return;
                }

                // Commit the characters we got to the buffer.
                buffer.commit(static_cast<std::size_t>(is.gcount()));
            }
            else
            {
                // Inform the parser that we've reached the end of the istream.
                p.put_eof(ec);
                if(ec)
                    return;
                break;
            }
        }

        // Write the data to the parser
        auto const bytes_used = p.put(buffer.data(), ec);

        // This error means that the parser needs additional octets.
        if(ec == error::need_more)
            ec = {};
        if(ec)
            return;

        // Consume the buffer octets that were actually parsed.
        buffer.consume(bytes_used);
    }
    while(! p.is_done());

    // Transfer ownership of the message container in the parser to the caller.
    msg = p.release();
}
```

|  |  |
| --- | --- |
| [Tip] | Tip |
| Parsing from a `std::istream` could be implemented using an alternate strategy: adapt the `std::istream` interface to a [*SyncReadStream*](../../../../../../doc/html/boost_asio/reference/SyncReadStream.html), enabling use with the library's existing stream algorithms. This is left as an exercise for the reader. |