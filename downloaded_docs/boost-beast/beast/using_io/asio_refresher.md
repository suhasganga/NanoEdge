### [Refresher](asio_refresher.html "Refresher")

To use Beast effectively, a prior understanding of Networking is required.
This section reviews these concepts as a reminder and guide for further learning.

A [*network*](https://en.wikipedia.org/wiki/Computer_network)
allows programs located anywhere to exchange information after opting-in
to communications by establishing a [*connection*](https://en.wikipedia.org/wiki/Data_link).
Data may be reliably transferred across a connection in both directions ([*full-duplex*](https://en.wikipedia.org/wiki/Duplex_(telecommunications)))
with bytes arriving in the same order they were sent. These connections,
along with the objects and types used to represent them, are collectively
termed [*streams*](../concepts/streams.html "Streams").
The computer or device attached to the network is called a [*host*](https://en.wikipedia.org/wiki/Host_(network)),
and the program on the other end of an established connection is called a
[*peer*](https://en.wikipedia.org/wiki/Peer-to-peer).

The [*internet*](https://en.wikipedia.org/wiki/Internet)
is a global network of interconnected computers that use a variety of standardized
communication protocols to exchange information. The most popular protocol
is [*TCP/IP*](https://en.wikipedia.org/wiki/Transmission_Control_Protocol),
which this library relies on exclusively. The protocol takes care of the
low level details so that applications see a *stream*,
which is the reliable, full-duplex connection carrying the ordered set of
bytes described above. A [*server*](https://en.wikipedia.org/wiki/Server_(computing))
is a powerful, always-on host at a well-known network name or network address
which provides data services. A [*client*](https://en.wikipedia.org/wiki/Client_(computing))
is a transient peer which connects to a server to exchange data, and goes
offline.

A vendor supplies a program called a [*device
driver*](https://en.wikipedia.org/wiki/Device_driver), enabling networking hardware such as an [*ethernet
adaptor*](https://en.wikipedia.org/wiki/Network_interface_controller) to talk to the operating system. This in turn
permits running programs to interact with networking using various flavors
of interfaces such as [*Berkeley
sockets*](https://en.wikipedia.org/wiki/Berkeley_sockets) or [*Windows
Sockets 2*](https://en.wikipedia.org/wiki/Winsock) ("Winsock").

Networking in C++, represented by [Boost.Asio](../../../../../../libs/asio/index.html),
[Asio](https://think-async.com/Asio/), and [Networking
TS](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2018/n4771.pdf), provides a layer of abstraction to interact portably with the
operating system facilities for not just networking but general [*input/output*](https://en.wikipedia.org/wiki/Input/output)
("I/O").

##### [Buffers](asio_refresher.html#beast.using_io.asio_refresher.buffers)

A [*buffer*](https://en.wikipedia.org/wiki/Data_buffer)
holds a contiguous sequence of bytes used when performing I/O. The types
[`net::const_buffer`](../../../../../../doc/html/boost_asio/reference/const_buffer.html)
and [`net::mutable_buffer`](../../../../../../doc/html/boost_asio/reference/mutable_buffer.html)
represent these memory regions as type-safe pointer/size pairs:

```programlisting
net::const_buffer cb("Hello, world!", 13);
assert(string_view(reinterpret_cast<char const*>(
    cb.data()), cb.size()) == "Hello, world!");

char storage[13];
net::mutable_buffer mb(storage, sizeof(storage));
std::memcpy(mb.data(), cb.data(), mb.size());
assert(string_view(reinterpret_cast<char const*>(
    mb.data()), mb.size()) == "Hello, world!");
```

|  |  |
| --- | --- |
| [Tip] | Tip |
| `const_buffer` and `mutable_buffer` are preferred over `std::span<byte>` and `span<byte const>` because [`std::span`](https://en.cppreference.com/w/cpp/container/span) does too much. It not only type-erases the original pointer but also recasts it to a pointer-to-byte. The operating system doesn't care about this, but if a user wants to send and receive an array of some other type, presenting it as an array of bytes which supports bitwise operations is unnecessary. Custom buffer types also enable implementations to provide targeted features such as [*buffer debugging*](../../../../../../doc/html/boost_asio/overview/core/buffers.html#boost_asio.overview.core.buffers.buffer_debugging) without changing the more general vocabulary types. |

The concepts [*ConstBufferSequence*](../../../../../../doc/html/boost_asio/reference/ConstBufferSequence.html)
and [*MutableBufferSequence*](../../../../../../doc/html/boost_asio/reference/MutableBufferSequence.html)
describe bidirectional ranges whose value type is convertible to `const_buffer` and `mutable_buffer`
respectively. These sequences allow transacting with multiple buffers in
a single function call, a technique called [*scatter/gather
I/O*](https://en.wikipedia.org/wiki/Vectored_I/O). Buffers and buffer sequences are non-owning; copies
produce shallow references and not duplicates of the underlying memory. Each
of these statements declares a buffer sequence:

```programlisting
net::const_buffer b1;                   // a ConstBufferSequence by definition
net::mutable_buffer b2;                 // a MutableBufferSequence by definition
std::array<net::const_buffer, 3> b3;    // A ConstBufferSequence by named requirements
```

The functions [`net::buffer_size`](../../../../../../doc/html/boost_asio/reference/buffer_size.html)
and [`net::buffer_copy`](../../../../../../doc/html/boost_asio/reference/buffer_copy.html)
determine the total number of bytes in a buffer sequence, and transfer some
or all of bytes from one buffer sequence to another respectively. The function
`buffer_size` is a customization
point: user defined overloads in foreign namespaces are possible, and callers
should invoke `buffer_size`
without namespace qualification. The functions [`net::buffer_sequence_begin`](../../../../../../doc/html/boost_asio/reference/buffer_sequence_begin.html)
and [`net::buffer_sequence_end`](../../../../../../doc/html/boost_asio/reference/buffer_sequence_end.html)
are used to obtain a pair of iterators for traversing the sequence. Beast
provides a set of buffer sequence types and algorithms such as [`buffers_cat`](../ref/boost__beast__buffers_cat.html "buffers_cat"), [`buffers_front`](../ref/boost__beast__buffers_front.html "buffers_front"), [`buffers_prefix`](../ref/boost__beast__buffers_prefix.html "buffers_prefix"), [`buffers_range`](../ref/boost__beast__buffers_range.html "buffers_range"), and [`buffers_suffix`](../ref/boost__beast__buffers_suffix.html "buffers_suffix"). This example returns
the bytes in a buffer sequence as a string:

```programlisting
template <class ConstBufferSequence>
std::string string_from_buffers (ConstBufferSequence const& buffers)
{
    // check that the type meets the requirements using the provided type traits
    static_assert(
        net::is_const_buffer_sequence<ConstBufferSequence>::value,
        "ConstBufferSequence type requirements not met");

    // optimization: reserve all the space for the string first
    std::string result;
    result.reserve(beast::buffer_bytes(buffers));        // beast version of net::buffer_size

    // iterate over each buffer in the sequence and append it to the string
    for(auto it = net::buffer_sequence_begin(buffers);  // returns an iterator to beginning of the sequence
        it != net::buffer_sequence_end(buffers);)       // returns a past-the-end iterator to the sequence
    {
        // A buffer sequence iterator's value_type is always convertible to net::const_buffer
        net::const_buffer buffer = *it++;

        // A cast is always required to out-out of type-safety
        result.append(static_cast<char const*>(buffer.data()), buffer.size());
    }
    return result;
}
```

The [*DynamicBuffer*](../concepts/DynamicBuffer.html "DynamicBuffer")
concept defines a resizable buffer sequence interface. Algorithms may be
expressed in terms of dynamic buffers when the memory requirements are not
known ahead of time, for example when reading an HTTP message from a stream.
Beast provides a well-rounded collection of dynamic buffer types such as
[`buffers_adaptor`](../ref/boost__beast__buffers_adaptor.html "buffers_adaptor"),
[`flat_buffer`](../ref/boost__beast__flat_buffer.html "flat_buffer"),
[`multi_buffer`](../ref/boost__beast__multi_buffer.html "multi_buffer"),
and [`static_buffer`](../ref/boost__beast__static_buffer.html "static_buffer").
The following function reads data from a [`tcp_stream`](../ref/boost__beast__tcp_stream.html "tcp_stream") into a dynamic buffer
until it encountering a newline character, using [`net::buffers_iterator`](../../../../../../doc/html/boost_asio/reference/buffers_iterator.html)
to treat the contents of the buffer as a range of characters:

```programlisting
// Read a line ending in '\n' from a socket, returning
// the number of characters up to but not including the newline
template <class DynamicBuffer>
std::size_t read_line(net::ip::tcp::socket& sock, DynamicBuffer& buffer)
{
    // this alias keeps things readable
    using range = net::buffers_iterator<
        typename DynamicBuffer::const_buffers_type>;

    for(;;)
    {
        // get iterators representing the range of characters in the buffer
        auto begin = range::begin(buffer.data());
        auto end = range::end(buffer.data());

        // search for "\n" and return if found
        auto pos = std::find(begin, end, '\n');
        if(pos != range::end(buffer.data()))
            return std::distance(begin, end);

        // Determine the number of bytes to read,
        // using available capacity in the buffer first.
        std::size_t bytes_to_read = std::min<std::size_t>(
              std::max<std::size_t>(512,                // under 512 is too little,
                  buffer.capacity() - buffer.size()),
              std::min<std::size_t>(65536,              // and over 65536 is too much.
                  buffer.max_size() - buffer.size()));

        // Read up to bytes_to_read bytes into the dynamic buffer
        buffer.commit(sock.read_some(buffer.prepare(bytes_to_read)));
    }
}
```

##### [Synchronous I/O](asio_refresher.html#beast.using_io.asio_refresher.synchronous_i_o)

Synchronous input and output is accomplished through blocking function calls
that return with the result of the operation. Such operations typically cannot
be canceled and do not have a method for setting a timeout. The [*SyncReadStream*](../../../../../../doc/html/boost_asio/reference/SyncReadStream.html)
and [*SyncWriteStream*](../../../../../../doc/html/boost_asio/reference/SyncWriteStream.html)
concepts define requirements for *synchronous streams*:
a portable I/O abstraction that transfers data using buffer sequences to
represent bytes and either `error_code`
or an exception to report any failures. [*net::basic\_stream\_socket*](../../../../../../doc/html/boost_asio/reference/basic_stream_socket.html)
is a synchronous stream commonly used to form TCP/IP connections. User-defined
types which meet the requirements are possible:

```programlisting
// Meets the requirements of SyncReadStream
struct sync_read_stream
{
    // Returns the number of bytes read upon success, otherwise throws an exception
    template <class MutableBufferSequence>
    std::size_t read_some(MutableBufferSequence const& buffers);

    // Returns the number of bytes read successfully, sets the error code if a failure occurs
    template <class MutableBufferSequence>
    std::size_t read_some(MutableBufferSequence const& buffers, error_code& ec);
};

// Meets the requirements of SyncWriteStream
struct sync_write_stream
{
    // Returns the number of bytes written upon success, otherwise throws an exception
    template <class ConstBufferSequence>
    std::size_t write_some(ConstBufferSequence const& buffers);

    // Returns the number of bytes written successfully, sets the error code if a failure occurs
    template <class ConstBufferSequence>
    std::size_t write_some(ConstBufferSequence const& buffers, error_code& ec);
};
```

A *synchronous stream algorithm* is written as a function
template accepting a stream object meeting the named requirements for synchronous
reading, writing, or both. This example shows an algorithm which writes text
and uses exceptions to indicate errors:

```programlisting
template <class SyncWriteStream>
void hello (SyncWriteStream& stream)
{
    net::const_buffer cb("Hello, world!", 13);
    do
    {
        auto bytes_transferred = stream.write_some(cb); // may throw
        cb += bytes_transferred; // adjust the pointer and size
    }
    while (cb.size() > 0);
}
```

The same algorithm may be expressed using error codes instead of exceptions:

```programlisting
template <class SyncWriteStream>
void hello (SyncWriteStream& stream, error_code& ec)
{
    net::const_buffer cb("Hello, world!", 13);
    do
    {
        auto bytes_transferred = stream.write_some(cb, ec);
        cb += bytes_transferred; // adjust the pointer and size
    }
    while (cb.size() > 0 && ! ec);
}
```

##### [Asynchronous I/O](asio_refresher.html#beast.using_io.asio_refresher.asynchronous_i_o)

An asynchronous operation begins with a call to an [*initiating
function*](../../../../../../doc/html/boost_asio/reference/asynchronous_operations.html), which starts the operation and returns to the
caller immediately. This *outstanding* asynchronous operation
proceeds concurrently without blocking the caller. When the externally observable
side effects are fully established, a movable function object known as a
[*completion
handler*](../../../../../../doc/html/boost_asio/reference/CompletionHandler.html) provided in the initiating function call is queued
for execution with the results, which may include the error code and other
specific information. An asynchronous operation is said to be *completed*
after the completion handler is queued. The code that follows shows how some
text may be written to a socket asynchronously, invoking a lambda when the
operation is complete:

```programlisting
// initiate an asynchronous write operation
net::async_write(sock, net::const_buffer("Hello, world!", 13),
    [](error_code ec, std::size_t bytes_transferred)
    {
        // this lambda is invoked when the write operation completes
        if(! ec)
            assert(bytes_transferred == 13);
        else
            std::cerr << "Error: " << ec.message() << "\n";

        (void)bytes_transferred;
    });
// meanwhile, the operation is outstanding and execution continues from here
```

Every completion handler (also referred to as a [*continuation*](https://en.wikipedia.org/wiki/Continuation))
has both an [*associated
allocator*](../../../../../../doc/html/boost_asio/overview/core/allocation.html) returned by [`net::get_associated_allocator`](../../../../../../doc/html/boost_asio/reference/get_associated_allocator.html),
, an [*associated
cancellation slot*](../../../../../../doc/html/boost_asio/reference/associated_cancellation_slot.html) returned by [`net::get_associated_cancellation_slot`](../../../../../../doc/html/boost_asio/reference/associated_cancellation_slot.html).
and an [*associated
executor*](../../../../../../doc/html/boost_asio/reference/associated_executor.html) returned by [`net::get_associated_executor`](../../../../../../doc/html/boost_asio/reference/get_associated_executor.html).
These associations may be specified intrusively:

```programlisting
// The following is a completion handler expressed
// as a function object, with a nested associated
// allocator and a nested associated executor.
struct handler
{
    using allocator_type = std::allocator<char>;
    allocator_type get_allocator() const noexcept;

    using executor_type = boost::asio::io_context::executor_type;
    executor_type get_executor() const noexcept;

    using cancellation_slot_type =  boost::asio::cancellation_slot;
    cancellation_slot_type get_cancellation_slot() const noexcept;

    void operator()(boost::beast::error_code, std::size_t);
};
```

Or these associations may be specified non-intrusively, by specializing the
class templates [`net::associated_allocator`](../../../../../../doc/html/boost_asio/reference/associated_allocator.html)
, [`net::associated_cancellation_slot`](../../../../../../doc/html/boost_asio/reference/associated_cancellation_slot.html)
and [`net::associated_executor`](../../../../../../doc/html/boost_asio/reference/associated_executor.html):

```programlisting
namespace boost {
namespace asio {

template<class Allocator>
struct associated_allocator<handler, Allocator>
{
    using type = std::allocator<void>;

    static
    type
    get(handler const& h,
        Allocator const& alloc = Allocator{}) noexcept;
};

template<class Executor>
struct associated_executor<handler, Executor>
{
    using type = any_io_executor;

    static
    type
    get(handler const& h,
        Executor const& ex = Executor{}) noexcept;
};

template<class CancellationSlot>
struct associated_cancellation_slot<handler, CancellationSlot>
{
    using type = cancellation_slot;

    static
    type
    get(handler const& h,
        CancellationSlot const& cs = CancellationSlot{}) noexcept;
};

} // boost
} // asio
```

The function [`net::bind_executor`](../../../../../../doc/html/boost_asio/reference/bind_executor.html)
may be used when the caller wants to change the executor of a completion
handler.

The allocator is used by the implementation to obtain any temporary storage
necessary to perform the operation. Temporary allocations are always freed
before the completion handler is invoked. The executor is a cheaply copyable
object providing the algorithm used to invoke the completion handler. Unless
customized by the caller, a completion handler defaults to using `std::allocator<void>`
and the executor of the corresponding I/O object.

The function [`net::bind_allocator`](../../../../../../doc/html/boost_asio/reference/bind_allocator.html)
can be used when the caller wants to assign a custom allocator to the operation.

A completion token's associated cancellation\_slot can be used to cancel single
operations. This is often passed through by the completion token such as
[`net::use_awaitable`](../../../../../../doc/html/boost_asio/reference/use_awaitable.html)
or [`net::yield_context`](../../../../../../doc/html/boost_asio/reference/yield_context.html)
.

The available [cancellation
types](../../../../../../doc/html/boost_asio/reference/cancellation_type.html) are listed below.

1. `terminal` Requests cancellation
   where, following a successful cancellation, the only safe operations
   on the I/O object are closure or destruction.
2. `partial` Requests cancellation
   where a successful cancellation may result in partial side effects or
   no side effects. Following cancellation, the I/O object is in a well-known
   state, and may be used for further operations.
3. `total` Requests cancellation
   where a successful cancellation results in no apparent side effects.
   Following cancellation, the I/O object is in the same observable state
   as it was prior to the operation.

Networking prescribes facilities to determine the context in which handlers
run. Every I/O object refers to an [*ExecutionContext*](../../../../../../doc/html/boost_asio/reference/ExecutionContext.html)
for obtaining the [*Executor*](../../../../../../doc/html/boost_asio/reference/Executor1.html)
instance used to invoke completion handlers. An executor determines where
and how completion handlers are invoked. Executors obtained from an instance
of [`net::io_context`](../../../../../../doc/html/boost_asio/reference/io_context.html)
offer a basic guarantee: handlers will only be invoked from threads which
are currently calling [`net::io_context::run`](../../../../../../doc/html/boost_asio/reference/io_context/run/overload1.html).

The [*AsyncReadStream*](../../../../../../doc/html/boost_asio/reference/AsyncReadStream.html)
and [*AsyncWriteStream*](../../../../../../doc/html/boost_asio/reference/AsyncWriteStream.html)
concepts define requirements for *asynchronous streams*:
a portable I/O abstraction that exchanges data asynchronously using buffer
sequences to represent bytes and `error_code`
to report any failures. An *asynchronous stream algorithm*
is written as a templated initiating function template accepting a stream
object meeting the named requirements for asynchronous reading, writing,
or both. This example shows an algorithm which writes some text to an asynchronous
stream:

```programlisting
template <class AsyncWriteStream, class WriteHandler>
void async_hello (AsyncWriteStream& stream, WriteHandler&& handler)
{
    net::async_write (stream,
        net::buffer("Hello, world!", 13),
        std::forward<WriteHandler>(handler));
}
```

##### [Concurrency](asio_refresher.html#beast.using_io.asio_refresher.concurrency)

I/O objects such as sockets and streams **are not thread-safe**.
Although it is possible to have more than one operation outstanding (for
example, a simultaneous asynchronous read and asynchronous write) the stream
object itself may only be accessed from one thread at a time. This means
that member functions such as move constructors, destructors, or initiating
functions must not be called concurrently. Usually this is accomplished with
synchronization primitives such as a [`mutex`](https://en.cppreference.com/w/cpp/thread/mutex), but concurrent network programs
need a better way to access shared resources, since acquiring ownership of
a mutex could block threads from performing uncontended work. For efficiency,
networking adopts a model of using threads without explicit locking by requiring
all access to I/O objects to be performed within a [*strand*](../../../../../../doc/html/boost_asio/overview/core/strands.html).

##### [Universal Model](asio_refresher.html#beast.using_io.asio_refresher.universal_model)

Because completion handlers cause an inversion of the flow of control, sometimes
other methods of attaching a continuation are desired. Networking provides
the [*Universal
Model for Asynchronous Operations*](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2013/n3747.pdf), providing a customizable
means for transforming the signature of the initiating function to use other
types of objects and methods in place of a completion handler callback. For
example to call to write a string to a socket asynchronously, using a `std::future`
to receive the number of bytes transferred thus looks like this:

```programlisting
std::future<std::size_t> f = net::async_write(sock,
    net::const_buffer("Hello, world!", 13), net::use_future);
```

This functionality is enabled by passing the variable [`net::use_future`](../../../../../../doc/html/boost_asio/reference/use_future.html)
(of type [`net::use_future_t<>`](../../../../../../doc/html/boost_asio/reference/use_future_t.html)) in place of the completion
handler. The same `async_write`
function overload can work with a [*fiber*](https://en.wikipedia.org/wiki/Fiber_(computer_science))
launched with [`asio::spawn`](../../../../../../doc/html/boost_asio/reference/spawn/overload1.html):

```programlisting
asio::spawn(
    sock.get_executor(),
    [&sock](net::yield_context yield)
    {
        std::size_t bytes_transferred = net::async_write(sock,
            net::const_buffer("Hello, world!", 13), yield);
        (void)bytes_transferred;
    },
    asio::detached);
```

In both of these cases, an object with a specific type is used in place of
the completion handler, and the return value of the initiating function is
transformed from `void` to `std::future<std::size_t>` or `std::size_t`.
The handler is sometimes called a [*CompletionToken*](../../../../../../doc/html/boost_asio/reference/asynchronous_operations.html#boost_asio.reference.asynchronous_operations.completion_tokens_and_handlers)
when used in this context. The return type transformation is supported by
customization points in the initiating function signature. Here is the signature
for [`net::async_write`](../../../../../../doc/html/boost_asio/reference/async_write/overload1.html):

Note that a `spawn` function
itself has a completion signature, but we're ignoring it's result in the
example by using `asio::detached`.

```programlisting
template<
    class AsyncWriteStream,
    class ConstBufferSequence,
    class CompletionToken>
auto
async_write(
    AsyncWriteStream* stream,                       // references are passed as pointers
    ConstBufferSequence const& buffers,
    CompletionToken&& token)                        // a handler, or a special object.
    ->
    typename net::async_result<                     // return-type customization point.
        typename std::decay<CompletionToken>::type, // type used to specialize async_result.
        void(error_code, std::size_t)               // underlying completion handler signature.
            >::return_type;
```

The type of the function's return value is determined by the [`net::async_result`](../../../../../../doc/html/boost_asio/reference/async_result.html)
customization point, which comes with specializations for common library
types such as `std::future` and may also be specialized for
user-defined types. The body of the initiating function calls the [`net::async_initiate`](../../../../../../doc/html/boost_asio/reference/async_initiate.html)
helper to capture the arguments and forward them to the specialization of
`async_result`. An additional
"initiation function" object is provided which `async_result`
may use to immediately launch the operation, or defer the launch of the operation
until some point in the future (this is called "lazy execution").
The initiation function object receives the internal completion handler which
matches the signature expected by the initiating function:

```programlisting
return net::async_initiate<
    CompletionToken,
    void(error_code, std::size_t)>(
        run_async_write{},              // The "initiation" object.
        token,                          // Token must come before other arguments.
        &stream,                        // Additional captured arguments are
        buffers);                       //   forwarded to the initiation object.
```

This transformed, internal handler is responsible for the finalizing step
that delivers the result of the operation to the caller. For example, when
using `net::use_future` the internal handler will deliver
the result by calling [`std::promise::set_value`](https://en.cppreference.com/w/cpp/thread/promise/set_value)
on the promise object returned by the initiating function.

##### [Using Networking](asio_refresher.html#beast.using_io.asio_refresher.using_networking)

Most library stream algorithms require a [`tcp::socket`](../../../../../../doc/html/boost_asio/reference/ip__tcp/socket.html),
[`net::ssl::stream`](../../../../../../doc/html/boost_asio/reference/ssl__stream.html),
or other [*Stream*](../concepts/streams.html "Streams")
object that has already established communication with a remote peer. This
example is provided as a reminder of how to work with sockets:

```programlisting
// The resolver is used to look up IP addresses and port numbers from a domain and service name pair
tcp::resolver r{ioc};

// A socket represents the local end of a connection between two peers
tcp::socket stream{ioc};

// Establish a connection before sending and receiving data
net::connect(stream, r.resolve("www.example.com", "http"));

// At this point `stream` is a connected to a remote
// host and may be used to perform stream operations.
```

Throughout this documentation identifiers with the following names have special
meaning:

**Table 1.3. Global Variables**

| Name | Description |
| --- | --- |
| [**`ioc`**](../../../../../../doc/html/boost_asio/reference/io_context.html) | A variable of type [`net::io_context`](../../../../../../doc/html/boost_asio/reference/io_context.html) which is running on one separate thread, and upon which an [`net::executor_work_guard`](../../../../../../doc/html/boost_asio/reference/executor_work_guard.html) object has been constructed. |
| [**`sock`**](../../../../../../doc/html/boost_asio/reference/ip__tcp/socket.html) | A variable of type [`tcp::socket`](../../../../../../doc/html/boost_asio/reference/ip__tcp/socket.html) which has already been connected to a remote host. |
| [**`ssl_sock`**](../../../../../../doc/html/boost_asio/reference/ssl__stream.html) | A variable of type [`net::ssl::stream<tcp::socket>`](../../../../../../doc/html/boost_asio/reference/ssl__stream.html) which is already connected and has handshaked with a remote host. |
| [**`ws`**](../ref/boost__beast__websocket__stream.html "websocket::stream") | A variable of type [`websocket::stream<tcp::socket>`](../ref/boost__beast__websocket__stream.html "websocket::stream") which is already connected with a remote host. |