#### [Incremental Read 💡](incremental_read.html "Incremental Read 💡")

This function uses [`buffer_body`](../../ref/boost__beast__http__buffer_body.html "http::buffer_body") and parser stream
operations to read a message body progressively using a small, fixed-size
buffer:

```programlisting
/*  This function reads a message using a fixed size buffer to hold
    portions of the body, and prints the body contents to a `std::ostream`.
*/
template<
    bool isRequest,
    class SyncReadStream,
    class DynamicBuffer>
void
read_and_print_body(
    std::ostream& os,
    SyncReadStream& stream,
    DynamicBuffer& buffer,
    error_code& ec)
{
    parser<isRequest, buffer_body> p;
    read_header(stream, buffer, p, ec);
    if(ec)
        return;
    while(! p.is_done())
    {
        char buf[512];
        p.get().body().data = buf;
        p.get().body().size = sizeof(buf);
        read(stream, buffer, p, ec);
        if(ec == error::need_buffer)
            ec = {};
        if(ec)
            return;
        os.write(buf, sizeof(buf) - p.get().body().size);
    }
}
```