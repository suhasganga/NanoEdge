#### [Reading large response body 💡](read_large_response_body.html "Reading large response body 💡")

This example presents how to increase the default limit of the response
body size, thus the content larger than the default 8MB can be read.

```programlisting
/*  This function uses custom size limit of the resposne body.
    The key method is 'body_limit' of the parser.
    body_limit is expressed in bytes.
*/
template<
    class SyncReadStream,
    class DynamicBuffer,
    bool isRequest, class Body, class Allocator>
std::size_t
read_large_response_body(
    SyncReadStream& stream,
    DynamicBuffer& buffer,
    message<isRequest, Body, basic_fields<Allocator>>& msg,
    std::size_t body_limit,
    error_code& ec)
{
    parser<isRequest, Body, Allocator> p(std::move(msg));
    p.eager(true);
    p.body_limit(body_limit);
    auto const bytes_transferred =
        http::read(stream, buffer, p, ec);
    if(ec)
        return bytes_transferred;
    msg = p.release();
    return bytes_transferred;
}
```