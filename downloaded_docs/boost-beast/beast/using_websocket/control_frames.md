### [Control Frames](control_frames.html "Control Frames")

Control frames are small (less than 128 bytes) messages entirely contained
in an individual WebSocket frame. They may be sent at any time by either
peer on an established connection, and can appear in between continuation
frames for a message. There are three types of control frames: ping, pong,
and close.

A sent ping indicates a request that the sender wants to receive a pong.
A pong is a response to a ping. Pongs may be sent unsolicited, at any time.
One use for an unsolicited pong is to inform the remote peer that the session
is still active after a long period of inactivity. A close frame indicates
that the remote peer wishes to close the WebSocket connection. The connection
is considered gracefully closed when each side has sent and received a close
frame.

During read operations, Beast automatically reads and processes control frames.
If a control callback is registered, the callback is notified of the incoming
control frame. The implementation will respond to pings automatically. The
receipt of a close frame initiates the WebSocket close procedure, eventually
resulting in the error code [`error::closed`](../ref/boost__beast__websocket__error.html "websocket::error") being delivered to the caller
in a subsequent read operation, assuming no other error takes place.

A consequence of this automatic behavior is that caller-initiated read operations
can cause socket writes. However, these writes will not compete with caller-initiated
write operations. For the purposes of correctness with respect to the stream
invariants, caller-initiated read operations still only count as a read.
This means that callers can have a simultaneously active read, write, and
ping/pong operation in progress, while the implementation also automatically
handles control frames.

##### [Control Callback](control_frames.html#beast.using_websocket.control_frames.control_callback)

Ping, pong, and close messages are control frames which may be sent at any
time by either peer on an established WebSocket connection. They are sent
using the functions [`ping`](../ref/boost__beast__websocket__stream/ping.html "websocket::stream::ping"), [`pong`](../ref/boost__beast__websocket__stream/pong.html "websocket::stream::pong"). and [`close`](../ref/boost__beast__websocket__stream/close.html "websocket::stream::close"). To be notified of control
frames, callers may register a *control callback* using
[`control_callback`](../ref/boost__beast__websocket__stream/control_callback.html "websocket::stream::control_callback"). The object provided
with this option should be callable with the following signature:

```programlisting
ws.control_callback(
    [](frame_type kind, string_view payload)
    {
        // Do something with the payload
        boost::ignore_unused(kind, payload);
    });
```

When a control callback is registered, it will be invoked for all pings,
pongs, and close frames received through either synchronous read functions
or asynchronous read functions. The type of frame and payload text are passed
as parameters to the control callback. If the frame is a close frame, the
close reason may be obtained by calling [`reason`](../ref/boost__beast__websocket__stream/reason.html "websocket::stream::reason").

Unlike regular completion handlers used in calls to asynchronous initiation
functions, the control callback only needs to be set once. The callback is
not reset after being called. The same callback is used for both synchronous
and asynchronous reads. The callback is passive; in order to be called, a
stream read operation must be active.

|  |  |
| --- | --- |
| [Note] | Note |
| When an asynchronous read function receives a control frame, the control callback is invoked in the same manner as that used to invoke the final completion handler of the corresponding read function. |

##### [Close Frames](control_frames.html#beast.using_websocket.control_frames.close_frames)

The WebSocket protocol defines a procedure and control message for initiating
a close of the session. In this procedure, a host requests the close by sending
a [*close
frame*](https://tools.ietf.org/html/rfc6455#section-5.5.1). To request a close use a close function such as
[`close`](../ref/boost__beast__websocket__stream/close/overload2.html "websocket::stream::close (2 of 2 overloads)") or [`async_close`](../ref/boost__beast__websocket__stream/async_close.html "websocket::stream::async_close"):

```programlisting
ws.close(close_code::normal);
```

The close function will send a close frame, read and discard incoming message
data until receiving a close frame, and then shut down the underlying connection
before returning.

When a close frame is received by during a read operation, the implementation
will automatically respond with a close frame and then shut down the underlying
connection before returning. In this case, the read operation will complete
with the code [`error::closed`](../ref/boost__beast__websocket__error.html "websocket::error"). This indicates to the caller
that the connection has been closed cleanly.

|  |  |
| --- | --- |
| [Important] | Important |
| To receive the [`error::closed`](../ref/boost__beast__websocket__error.html "websocket::error") error, a read operation is required. |

##### [Auto-fragment](control_frames.html#beast.using_websocket.control_frames.auto_fragment)

To ensure timely delivery of control frames, large outgoing messages can
be broken up into smaller sized frames. The automatic fragment option turns
on this feature, and the write buffer size option determines the maximum
size of the fragments:

```programlisting
ws.auto_fragment(true);
ws.write_buffer_bytes(16384);
```