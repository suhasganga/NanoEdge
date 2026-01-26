### [Timeouts](timeouts.html "Timeouts")

While [`basic_stream`](../ref/boost__beast__basic_stream.html "basic_stream") and [`tcp_stream`](../ref/boost__beast__basic_stream.html "basic_stream") support timeouts on general
logical operations, the websocket stream has a more sophisticated timeout
mechanism built-in which may be enabled and configured. The timeout features
of the TCP or basic stream should not be used when working with a websocket
stream. The interface to these timeout features is shown in this table.

**Table 1.36. WebSocket Timeout Interface**

| Name | Description |
| --- | --- |
| [`stream_base::timeout`](../ref/boost__beast__websocket__stream_base__timeout.html "websocket::stream_base::timeout") | This represents configured timeout settings for a websocket stream. |
| [`stream_base::timeout::suggested`](../ref/boost__beast__websocket__stream_base__timeout/suggested.html "websocket::stream_base::timeout::suggested") | This function returns the suggested timeout settings for a given role (client or server). |
| [`stream::set_option`](../ref/boost__beast__websocket__stream/set_option.html "websocket::stream::set_option") | This function sets timeout and other options on the stream. |

  

There are three timeout settings which may be set independently on the stream:

**Table 1.37. WebSocket Timeout Interface (2)**

| Name | Type | Description |
| --- | --- | --- |
| [`timeout::handshake_timeout`](../ref/boost__beast__websocket__stream_base__timeout/handshake_timeout.html "websocket::stream_base::timeout::handshake_timeout") | `duration` | This is the amount of time after which a handshake will time out. The handshake timeout applies to client handshakes, server handshakes, as well as the websocket closing handshake performed when either end of the connection wish to shut down. The value returned by [`stream_base::none()`](../ref/boost__beast__websocket__stream_base/none.html "websocket::stream_base::none") may be assigned to disable this timeout. |
| [`timeout::idle_timeout`](../ref/boost__beast__websocket__stream_base__timeout/idle_timeout.html "websocket::stream_base::timeout::idle_timeout") | `duration` | If no data or control frames are received from the peer for a time equal to the idle timeout, then the connection will time out. The value returned by [`stream_base::none()`](../ref/boost__beast__websocket__stream_base/none.html "websocket::stream_base::none") may be assigned to disable this timeout. |
| [`timeout::keep_alive_pings`](../ref/boost__beast__websocket__stream_base__timeout/keep_alive_pings.html "websocket::stream_base::timeout::keep_alive_pings") | `bool` | If the idle timeout is enabled, then the value of this setting controls whether or not a ping frame will be sent to the peer if no data is received for half of the idle timeout interval. |

  

By default, timeouts on websocket streams are disabled. The easiest way to
turn them on is to set the suggested timeout settings on the stream.

```programlisting
// Apply suggested timeout options for the server role to the stream
ws.set_option(stream_base::timeout::suggested(role_type::server));
```

For manual control over the settings, a timeout options object may be constructed.
Here we enable only the handshake timeout.

```programlisting
stream_base::timeout opt{
    std::chrono::seconds(30),   // handshake timeout
    stream_base::none(),        // idle timeout
    false
};

// Set the timeout options on the stream.
ws.set_option(opt);
```

Timeout notifications are delivered to the caller by invoking the completion
handler for an outstanding asynchronous read operation with the error code
[`error::timeout`](../ref/boost__beast__error.html "error").
The implementation will close the socket or stream before delivering this
error. It is not necessary to manually shut down the connection, as it will
already be shut down. A read operation must be outstanding for the error
to be delivered.

```programlisting
ws.async_read(b,
    [](error_code ec, std::size_t)
    {
        if(ec == beast::error::timeout)
            std::cerr << "timeout, connection closed!";
    });
```

|  |  |
| --- | --- |
| [Note] | Note |
| Websocket timeout features are available only when using asynchronous I/O. |

The timeouts on the websocket stream are incompatible with the timeouts used
in the `tcp_stream`. When constructing
a websocket stream from a tcp stream that has timeouts enabled, the timeout
should be disabled first before constructing the websocket stream, as shown.

```programlisting
// Disable any timeouts on the tcp_stream
sock.expires_never();

// Construct the websocket stream, taking ownership of the existing tcp_stream
stream<tcp_stream> ws(std::move(sock));
```