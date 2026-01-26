### [Buffer-Oriented Serializing](buffer_oriented_serializing.html "Buffer-Oriented Serializing")

An instance of [`serializer`](../ref/boost__beast__http__serializer.html "http::serializer") can be invoked directly,
without using the provided stream operations. This could be useful for implementing
algorithms on objects whose interface does not conform to [*Stream*](../concepts/streams.html "Streams").
For example, a [**libuv**
socket](https://github.com/libuv/libuv). The serializer interface is interactive; the caller invokes
it repeatedly to produce buffers until all of the serialized octets have
been generated. Then the serializer is destroyed.

To obtain the serialized next buffer sequence, call [`serializer::next`](../ref/boost__beast__http__serializer/next.html "http::serializer::next"). Then, call [`serializer::consume`](../ref/boost__beast__http__serializer/consume.html "http::serializer::consume") to indicate the number of
bytes consumed. This updates the next set of buffers to be returned, if any.
`serializer::next` takes an error code parameter and
invokes a visitor argument with the error code and buffer of unspecified
type. In C++14 this is easily expressed with a generic lambda. The function
[`serializer::is_done`](../ref/boost__beast__http__serializer/is_done.html "http::serializer::is_done") will return `true` when all the buffers have been produced.
This C++14 example prints the buffers to standard output:

```programlisting
template<bool isRequest, class Body, class Fields>
void
print_cxx14(message<isRequest, Body, Fields> const& m)
{
    error_code ec;
    serializer<isRequest, Body, Fields> sr{m};
    do
    {
        sr.next(ec,
            [&sr](error_code& ec, auto const& buffer)
            {
                ec = {};
                std::cout << make_printable(buffer);
                sr.consume(buffer_bytes(buffer));
            });
    }
    while(! ec && ! sr.is_done());
    if(! ec)
        std::cout << std::endl;
    else
        std::cerr << ec.message() << std::endl;
}
```

Generic lambda expressions are only available in C++14 or later. A functor
with a templated function call operator is necessary to use C++11 as shown:

```programlisting
template<class Serializer>
struct lambda
{
    Serializer& sr;

    lambda(Serializer& sr_) : sr(sr_) {}

    template<class ConstBufferSequence>
    void operator()(error_code& ec, ConstBufferSequence const& buffer) const
    {
        ec = {};
        std::cout << make_printable(buffer);
        sr.consume(buffer_bytes(buffer));
    }
};

template<bool isRequest, class Body, class Fields>
void
print(message<isRequest, Body, Fields> const& m)
{
    error_code ec;
    serializer<isRequest, Body, Fields> sr{m};
    do
    {
        sr.next(ec, lambda<decltype(sr)>{sr});
    }
    while(! ec && ! sr.is_done());
    if(! ec)
        std::cout << std::endl;
    else
        std::cerr << ec.message() << std::endl;
}
```

##### [Split Serialization](buffer_oriented_serializing.html#beast.using_http.buffer_oriented_serializing.split_serialization)

In some cases, such as the handling of the [Expect:
100-continue](https://tools.ietf.org/html/rfc7231#section-5.1.1) field, it may be desired to first serialize the header,
perform some other action, and then continue with serialization of the body.
This is accomplished by calling [`serializer::split`](../ref/boost__beast__http__serializer/split.html "http::serializer::split") with a boolean indicating
that when buffers are produced, the last buffer containing serialized header
octets will not contain any octets corresponding to the body. The function
[`serializer::is_header_done`](../ref/boost__beast__http__serializer/is_header_done.html "http::serializer::is_header_done") informs the caller
whether the header been serialized fully. In this C++14 example we print
the header first, followed by the body:

```programlisting
template<bool isRequest, class Body, class Fields>
void
split_print_cxx14(message<isRequest, Body, Fields> const& m)
{
    error_code ec;
    serializer<isRequest, Body, Fields> sr{m};
    sr.split(true);
    std::cout << "Header:" << std::endl;
    do
    {
        sr.next(ec,
            [&sr](error_code& ec, auto const& buffer)
            {
                ec = {};
                std::cout << make_printable(buffer);
                sr.consume(buffer_bytes(buffer));
            });
    }
    while(! sr.is_header_done());
    if(! ec && ! sr.is_done())
    {
        std::cout << "Body:" << std::endl;
        do
        {
            sr.next(ec,
                [&sr](error_code& ec, auto const& buffer)
                {
                    ec = {};
                    std::cout << make_printable(buffer);
                    sr.consume(buffer_bytes(buffer));
                });
        }
        while(! ec && ! sr.is_done());
    }
    if(ec)
        std::cerr << ec.message() << std::endl;
}
```

#### [Write To std::ostream 💡](buffer_oriented_serializing.html#beast.using_http.buffer_oriented_serializing.write_to_std_ostream "Write To std::ostream 💡")

The standard library provides the type `std::ostream`
for performing high level write operations on character streams. The variable
`std::cout` is based on this output stream.
This example uses the buffer oriented interface of [`serializer`](../ref/boost__beast__http__serializer.html "http::serializer") to write an HTTP message
to a `std::ostream`:

```programlisting
// The detail namespace means "not public"
namespace detail {

// This helper is needed for C++11.
// When invoked with a buffer sequence, writes the buffers `to the std::ostream`.
template<class Serializer>
class write_ostream_helper
{
    Serializer& sr_;
    std::ostream& os_;

public:
    write_ostream_helper(Serializer& sr, std::ostream& os)
        : sr_(sr)
        , os_(os)
    {
    }

    // This function is called by the serializer
    template<class ConstBufferSequence>
    void
    operator()(error_code& ec, ConstBufferSequence const& buffers) const
    {
        // Error codes must be cleared on success
        ec = {};

        // Keep a running total of how much we wrote
        std::size_t bytes_transferred = 0;

        // Loop over the buffer sequence
        for(auto it = boost::asio::buffer_sequence_begin(buffers);
            it != boost::asio::buffer_sequence_end(buffers); ++it)
        {
            // This is the next buffer in the sequence
            boost::asio::const_buffer const buffer = *it;

            // Write it to the std::ostream
            os_.write(
                reinterpret_cast<char const*>(buffer.data()),
                buffer.size());

            // If the std::ostream fails, convert it to an error code
            if(os_.fail())
            {
                ec = make_error_code(errc::io_error);
                return;
            }

            // Adjust our running total
            bytes_transferred += buffer_size(buffer);
        }

        // Inform the serializer of the amount we consumed
        sr_.consume(bytes_transferred);
    }
};

} // detail

/** Write a message to a `std::ostream`.

    This function writes the serialized representation of the
    HTTP/1 message to the sream.

    @param os The `std::ostream` to write to.

    @param msg The message to serialize.

    @param ec Set to the error, if any occurred.
*/
template<
    bool isRequest,
    class Body,
    class Fields>
void
write_ostream(
    std::ostream& os,
    message<isRequest, Body, Fields>& msg,
    error_code& ec)
{
    // Create the serializer instance
    serializer<isRequest, Body, Fields> sr{msg};

    // This lambda is used as the "visit" function
    detail::write_ostream_helper<decltype(sr)> lambda{sr, os};
    do
    {
        // In C++14 we could use a generic lambda but since we want
        // to require only C++11, the lambda is written out by hand.
        // This function call retrieves the next serialized buffers.
        sr.next(ec, lambda);
        if(ec)
            return;
    }
    while(! sr.is_done());
}
```

|  |  |
| --- | --- |
| [Tip] | Tip |
| Serializing to a `std::ostream` could be implemented using an alternate strategy: adapt the `std::ostream` interface to a [*SyncWriteStream*](../../../../../../doc/html/boost_asio/reference/SyncWriteStream.html), enabling use with the library's existing stream algorithms. This is left as an exercise for the reader. |