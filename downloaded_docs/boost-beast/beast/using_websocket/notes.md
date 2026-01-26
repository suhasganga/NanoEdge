### [Notes](notes.html "Notes")

Because calls to read data may return a variable amount of bytes, the interface
to calls that read data require an object that meets the requirements of
[*DynamicBuffer*](../concepts/DynamicBuffer.html "DynamicBuffer").
This concept is modeled on [`net::streambuf`](../../../../../../doc/html/boost_asio/reference/streambuf.html).

The implementation does not perform queueing or buffering of messages. If
desired, these features should be provided by callers. The impact of this
design is that library users are in full control of the allocation strategy
used to store data and the back-pressure applied on the read and write side
of the underlying TCP/IP connection.

##### [Asynchronous Operations](notes.html#beast.using_websocket.notes.asynchronous_operations)

Asynchronous versions are available for all functions:

```programlisting
flat_buffer buffer;

ws.async_read(buffer,
    [](error_code, std::size_t)
    {
        // Do something with the buffer
    });
```

Calls to asynchronous initiation functions support the extensible asynchronous
model developed by the Boost.Asio author, allowing for traditional completion
handlers, stackful or stackless coroutines, and even futures:

```programlisting
void echo(stream<tcp_stream>& ws,
    multi_buffer& buffer, net::yield_context yield)
{
    ws.async_read(buffer, yield);
    std::future<std::size_t> fut =
        ws.async_write(buffer.data(), net::use_future);
}
```

The example programs that come with the library demonstrate the usage of
websocket stream operations with all asynchronous varieties.

##### [The io\_context](notes.html#beast.using_websocket.notes.the_io_context)

The creation and operation of the [`net::io_context`](../../../../../../doc/html/boost_asio/reference/io_context.html)
associated with the underlying stream is left to the callers, permitting
any implementation strategy including one that does not require threads for
environments where threads are unavailable. Beast WebSocket itself does not
use or require threads.

##### [Thread Safety](notes.html#beast.using_websocket.notes.thread_safety)

Like a regular [Boost.Asio](../../../../../../libs/asio/index.html)
socket, a [`stream`](../ref/boost__beast__websocket__stream.html "websocket::stream") is not thread safe. Callers
are responsible for synchronizing operations on the socket using an implicit
or explicit strand, as per the Asio documentation. The websocket stream asynchronous
interface supports one of each of the following operations to be active at
the same time:

* [`async_read`](../ref/boost__beast__websocket__stream/async_read.html "websocket::stream::async_read") or [`async_read_some`](../ref/boost__beast__websocket__stream/async_read_some.html "websocket::stream::async_read_some")
* [`async_write`](../ref/boost__beast__websocket__stream/async_write.html "websocket::stream::async_write") or [`async_write_some`](../ref/boost__beast__websocket__stream/async_write_some.html "websocket::stream::async_write_some")
* [`async_ping`](../ref/boost__beast__websocket__stream/async_ping.html "websocket::stream::async_ping") or [`async_pong`](../ref/boost__beast__websocket__stream/async_pong.html "websocket::stream::async_pong")
* [`async_close`](../ref/boost__beast__websocket__stream/async_close.html "websocket::stream::async_close")

For example, the following code is produces undefined behavior, because the
program is attempting to perform two simultaneous reads:

```programlisting
ws.async_read(b, [](error_code, std::size_t){});
ws.async_read(b, [](error_code, std::size_t){});
```

However, this code is correct:

```programlisting
ws.async_read(b, [](error_code, std::size_t){});
ws.async_write(b.data(), [](error_code, std::size_t){});
ws.async_ping({}, [](error_code){});
ws.async_close({}, [](error_code){});
```

The implementation uses composed asynchronous operations; although some individual
operations can perform both reads and writes, this behavior is coordinated
internally to make sure the underlying stream is operated in a safe fashion.
This allows an asynchronous read operation to respond to a received ping
frame even while a user-initiated call to asynchronous write is active.