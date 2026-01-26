### [Chunked Encoding](chunked_encoding.html "Chunked Encoding")

For message payloads whose size is not known ahead of time, HTTP version
1.1 defines the [*chunked*](https://tools.ietf.org/html/rfc7230#section-4.1)
transfer coding. This coding consists of zero or more [*chunked
bodies*](https://tools.ietf.org/html/rfc7230#section-4.1), followed by a [*last
chunk*](https://tools.ietf.org/html/rfc7230#section-4.1). Each chunked body may contain optional application-defined,
connection-specific [*chunk-extensions*](https://tools.ietf.org/html/rfc7230#section-4.1.1).
The last chunk may contain additional HTTP field values in a section of the
last chunk called a [*chunk-trailer*](https://tools.ietf.org/html/rfc7230#section-4.1.2).
The field values are "promised" in the header as a comma delimited
list of field names in the [**Trailer**](https://tools.ietf.org/html/rfc7230#section-4.4) field value. Clients indicate their
willingness to accept trailers by including the "trailers" token
in the [**TE**](https://tools.ietf.org/html/rfc7230#section-4.3) field value.

##### [Serializing Chunks](chunked_encoding.html#beast.using_http.chunked_encoding.serializing_chunks)

The [`serializer`](../ref/boost__beast__http__serializer.html "http::serializer") automatically applies
the chunked transfer encoding when a message returns `true`
from [`message::chunked`](../ref/boost__beast__http__message/chunked/overload1.html "http::message::chunked (1 of 2 overloads)"). The boundaries between
chunks emitted by the serializer are implementation defined. Chunk extensions
and trailers are omitted. Applications which need precise control over the
chunk boundaries, extensions, and trailers may use a set of helper classes
which enable manual emission of message payloads using chunk encoding.

To use these helper classes, first serialize the header portion of the message
using the standard interface. Then prepare the buffers, chunk extensions,
and desired trailers, and use them with these helpers:

**Table 1.26. Chunking Helpers**

| Name | Description |
| --- | --- |
| [`chunk_body`](../ref/boost__beast__http__chunk_body.html "http::chunk_body") | A buffer sequence representing a complete chunk body. |
| [`chunk_crlf`](../ref/boost__beast__http__chunk_crlf.html "http::chunk_crlf") | A buffer sequence representing the CRLF (`"\r\n"`) delimiter. This class is used when the caller desires to emit the chunk body in two or more individual stream operations. |
| [`chunk_extensions`](../ref/boost__beast__http__chunk_extensions.html "http::chunk_extensions")  [`basic_chunk_extensions`](../ref/boost__beast__http__basic_chunk_extensions.html "http::basic_chunk_extensions") | This is a simple, allocating container which lets callers easily build up a set of chunk extensions. |
| [`chunk_header`](../ref/boost__beast__http__chunk_header.html "http::chunk_header") | A buffer sequence representing a hex-encoded chunk size, followed by an optional set of chunk extensions, including the terminating CRLF (`"\r\n"`) delimiter which precedes the chunk body. This class is used when the caller desires to emit the chunk body in two or more individual stream operations. |
| [`chunk_last`](../ref/boost__beast__http__chunk_last.html "http::chunk_last") | A buffer sequence representing a last chunk. The last chunk indicates the end of the chunked message payload, and may contain optional trailer fields. |
| [`make_chunk`](../ref/boost__beast__http__make_chunk.html "http::make_chunk")  [`make_chunk_last`](../ref/boost__beast__http__make_chunk_last.html "http::make_chunk_last") | These helper functions are used to construct a chunk or last chunk directly at call sites. |

  

We demonstrate the use of these objects first by declaring a function which
returns the next buffer sequence to use as a chunk body:

```programlisting
// This function returns the buffer containing the next chunk body
net::const_buffer get_next_chunk_body();
```

This example demonstrates sending a complete chunked message payload manually.
No chunk extensions or trailers are emitted:

```programlisting
// Prepare an HTTP/1.1 response with a chunked body
response<empty_body> res{status::ok, 11};
res.set(field::server, "Beast");

// Set Transfer-Encoding to "chunked".
// If a Content-Length was present, it is removed.
res.chunked(true);

// Set up the serializer
response_serializer<empty_body> sr{res};

// Write the header first
write_header(sock, sr);

// Now manually emit three chunks:
net::write(sock, make_chunk(get_next_chunk_body()));
net::write(sock, make_chunk(get_next_chunk_body()));
net::write(sock, make_chunk(get_next_chunk_body()));

// We are responsible for sending the last chunk:
net::write(sock, make_chunk_last());
```

The following code sends additional chunks, and sets chunk extensions using
the helper container. The container automatically quotes values in the serialized
output when necessary:

```programlisting
// Prepare a set of chunk extension to emit with the body
chunk_extensions ext;
ext.insert("mp3");
ext.insert("title", "Beale Street Blues");
ext.insert("artist", "W.C. Handy");

// Write the next chunk with the chunk extensions
// The implementation will make a copy of the extensions object,
// so the caller does not need to manage lifetime issues.
net::write(sock, make_chunk(get_next_chunk_body(), ext));

// Write the next chunk with the chunk extensions
// The implementation will make a copy of the extensions object, storing the copy
// using the custom allocator, so the caller does not need to manage lifetime issues.
net::write(sock, make_chunk(get_next_chunk_body(), ext, std::allocator<char>{}));

// Write the next chunk with the chunk extensions
// The implementation allocates memory using the default allocator and takes ownership
// of the extensions object, so the caller does not need to manage lifetime issues.
// Note: ext is moved
net::write(sock, make_chunk(get_next_chunk_body(), std::move(ext)));
```

Callers can take over the generation and management of the extensions buffer
by passing a non-owning string. Note that this requires the string contents
to adhere to the correct syntax for chunk extensions, including the needed
double quotes for values which contain spaces:

```programlisting
// Manually specify the chunk extensions.
// Some of the strings contain spaces and a period and must be quoted
net::write(sock, make_chunk(get_next_chunk_body(),
    ";mp3"
    ";title=\"Danny Boy\""
    ";artist=\"Fred E. Weatherly\""
    ));
```

The next code sample emits a chunked response which promises two trailer
fields and delivers them in the last chunk. The implementation allocates
memory using the default or a passed-in allocator to hold the state information
required to serialize the trailer:

```programlisting
// Prepare a chunked HTTP/1.1 response with some trailer fields
response<empty_body> res{status::ok, 11};
res.set(field::server, "Beast");

// Inform the client of the trailer fields we will send
res.set(field::trailer, "Content-Digest");

res.chunked(true);

// Serialize the header and two chunks
response_serializer<empty_body> sr{res};
write_header(sock, sr);
net::write(sock, make_chunk(get_next_chunk_body()));
net::write(sock, make_chunk(get_next_chunk_body()));

// Prepare the trailer
fields trailer;
trailer.set(field::content_digest, "f4a5c16584f03d90");

// Emit the trailer in the last chunk.
// The implementation will use the default allocator to create the storage for holding
// the serialized fields.
net::write(sock, make_chunk_last(trailer));
```

Using a custom allocator to serialize the last chunk:

```programlisting
// Use a custom allocator for serializing the last chunk
fields trailer;
trailer.set(field::server_timing, "custom-metric;dur=123.4");
net::write(sock, make_chunk_last(trailer, std::allocator<char>{}));
```

Alternatively, callers can take over the generation and lifetime management
of the serialized trailer fields by passing in a non-owning string:

```programlisting
// Manually emit a trailer.
// We are responsible for ensuring that the trailer format adheres to the specification.
string_view ext =
    "Content-Digest: f4a5c16584f03d90\r\n"
    "\r\n";
net::write(sock, make_chunk_last(net::const_buffer{ext.data(), ext.size()}));
```

For the ultimate level of control, a caller can manually compose the chunk
itself by first emitting a header with the correct chunk body size, and then
by emitting the chunk body in multiple calls to the stream write function.
In this case the caller is responsible for also emitting the terminating
CRLF (`"\r\n"`):

```programlisting
// Prepare a chunked HTTP/1.1 response and send the header
response<empty_body> res{status::ok, 11};
res.set(field::server, "Beast");
res.chunked(true);
response_serializer<empty_body> sr{res};
write_header(sock, sr);

// Obtain three body buffers up front
auto const cb1 = get_next_chunk_body();
auto const cb2 = get_next_chunk_body();
auto const cb3 = get_next_chunk_body();

// Manually emit a chunk by first writing the chunk-size header with the correct size
net::write(sock, chunk_header{
    buffer_bytes(cb1) +
    buffer_bytes(cb2) +
    buffer_bytes(cb3)});

// And then output the chunk body in three pieces ("chunk the chunk")
net::write(sock, cb1);
net::write(sock, cb2);
net::write(sock, cb3);

// When we go this deep, we are also responsible for the terminating CRLF
net::write(sock, chunk_crlf{});
```

##### [Parsing Chunks](chunked_encoding.html#beast.using_http.chunked_encoding.parsing_chunks)

The [`parser`](../ref/boost__beast__http__parser.html "http::parser")
automatically removes the chunked transfer coding when it is the last encoding
in the list. However, it also discards the chunk extensions and does not
provide a way to determine the boundaries between chunks. Advanced applications
which need to access the chunk extensions or read complete individual chunks
may use a callback interface provided by [`parser`](../ref/boost__beast__http__parser.html "http::parser"):

**Table 1.27. Chunking Parse Callbacks**

| Name | Description |
| --- | --- |
| [`on_chunk_header`](../ref/boost__beast__http__parser/on_chunk_header.html "http::parser::on_chunk_header") | Set a callback to be invoked on each chunk header.  The callback will be invoked once for every chunk in the message payload, as well as once for the last chunk. The invocation happens after the chunk header is available but before any body octets have been parsed.  The extensions are provided in raw, validated form, use [`chunk_extensions::parse`](../ref/boost__beast__http__basic_chunk_extensions/parse.html "http::basic_chunk_extensions::parse") to parse the extensions into a structured container for easier access. The implementation type-erases the callback without requiring a dynamic allocation. For this reason, the callback object is passed by a non-constant reference.  The function object will be called with this equivalent signature:   ```programlisting void callback(     std::uint64_t size,         // Size of the chunk, zero for the last chunk     string_view extensions,     // The chunk-extensions in raw form     error_code& ec);            // May be set by the callback to indicate an error ``` |
| [`on_chunk_body`](../ref/boost__beast__http__parser/on_chunk_body.html "http::parser::on_chunk_body") | Set a callback to be invoked on chunk body data.  The callback will be invoked one or more times to provide buffers corresponding to the chunk body for the current chunk. The callback receives the number of octets remaining in this chunk body including the octets in the buffer provided.  The callback must return the number of octets actually consumed. Any octets not consumed will be presented again in a subsequent invocation of the callback. The implementation type-erases the callback without requiring a dynamic allocation. For this reason, the callback object is passed by a non-constant reference.  The function object will be called with this equivalent signature:   ```programlisting std::size_t callback(     std::uint64_t remain,       // Octets remaining in this chunk, includes `body`     string_view body,           // A buffer holding some or all of the remainder of the chunk body     error_code& ec);            // May be set by the callback to indicate an error ``` |

  

This example will read a message header from the stream, and then manually
read each chunk. It recognizes the chunk boundaries and outputs the contents
of each chunk as it comes in. Any chunk extensions are printed, each extension
on its own line. Finally, any trailers promised in the header are printed.

```programlisting
/** Read a message with a chunked body and print the chunks and extensions
*/
template<
    bool isRequest,
    class SyncReadStream,
    class DynamicBuffer>
void
print_chunked_body(
    std::ostream& os,
    SyncReadStream& stream,
    DynamicBuffer& buffer,
    error_code& ec)
{
    // Declare the parser with an empty body since
    // we plan on capturing the chunks ourselves.
    parser<isRequest, empty_body> p;

    // First read the complete header
    read_header(stream, buffer, p, ec);
    if(ec)
        return;

    // This container will hold the extensions for each chunk
    chunk_extensions ce;

    // This string will hold the body of each chunk
    std::string chunk;

    // Declare our chunk header callback  This is invoked
    // after each chunk header and also after the last chunk.
    auto header_cb =
    [&](std::uint64_t size,         // Size of the chunk, or zero for the last chunk
        string_view extensions,     // The raw chunk-extensions string. Already validated.
        error_code& ev)             // We can set this to indicate an error
    {
        // Parse the chunk extensions so we can access them easily
        ce.parse(extensions, ev);
        if(ev)
            return;

        // See if the chunk is too big
        if(size > (std::numeric_limits<std::size_t>::max)())
        {
            ev = error::body_limit;
            return;
        }

        // Make sure we have enough storage, and
        // reset the container for the upcoming chunk
        chunk.reserve(static_cast<std::size_t>(size));
        chunk.clear();
    };

    // Set the callback. The function requires a non-const reference so we
    // use a local variable, since temporaries can only bind to const refs.
    p.on_chunk_header(header_cb);

    // Declare the chunk body callback. This is called one or
    // more times for each piece of a chunk body.
    auto body_cb =
    [&](std::uint64_t remain,   // The number of bytes left in this chunk
        string_view body,       // A buffer holding chunk body data
        error_code& ec)         // We can set this to indicate an error
    {
        // If this is the last piece of the chunk body,
        // set the error so that the call to `read` returns
        // and we can process the chunk.
        if(remain == body.size())
            ec = error::end_of_chunk;

        // Append this piece to our container
        chunk.append(body.data(), body.size());

        // The return value informs the parser of how much of the body we
        // consumed. We will indicate that we consumed everything passed in.
        return body.size();
    };
    p.on_chunk_body(body_cb);

    while(! p.is_done())
    {
        // Read as much as we can. When we reach the end of the chunk, the chunk
        // body callback will make the read return with the end_of_chunk error.
        read(stream, buffer, p, ec);
        if(! ec)
            continue;
        else if(ec != error::end_of_chunk)
            return;
        else
            ec = {};

        // We got a whole chunk, print the extensions:
        for(auto const& extension : ce)
        {
            os << "Extension: " << extension.first;
            if(! extension.second.empty())
                os << " = " << extension.second << std::endl;
            else
                os << std::endl;
        }

        // Now print the chunk body
        os << "Chunk Body: " << chunk << std::endl;
    }

    // Get a reference to the parsed message, this is for convenience
    auto const& msg = p.get();

    // Check each field promised in the "Trailer" header and output it
    for(auto const& name : token_list{msg[field::trailer]})
    {
        // Find the trailer field
        auto it = msg.find(name);
        if(it == msg.end())
        {
            // Oops! They promised the field but failed to deliver it
            os << "Missing Trailer: " << name << std::endl;
            continue;
        }
        os << it->name() << ": " << it->value() << std::endl;
    }
}
```

Given the HTTP response as input on the left, the output of the function
shown above is shown on the right:

**Table 1.28. Chunk Parsing Example Output**

| Input | Output |
| --- | --- |
| ```programlisting HTTP/1.1 200 OK\r\n Server: test\r\n Trailer: Expires, Content-MD5\r\n Transfer-Encoding: chunked\r\n \r\n 5\r\n First\r\n d;quality=1.0\r\n Hello, world!\r\n e;file=abc.txt;quality=0.7\r\n The Next Chunk\r\n 8;last\r\n Last one\r\n 0\r\n Expires: never\r\n Content-MD5: f4a5c16584f03d90\r\n \r\n ``` | ```programlisting Chunk Body: First Extension: quality = 1.0 Chunk Body: Hello, world! Extension: file = abc.txt Extension: quality = 0.7 Chunk Body: The Next Chunk Extension: last Chunk Body: Last one Expires: never Content-MD5: f4a5c16584f03d90 ``` |