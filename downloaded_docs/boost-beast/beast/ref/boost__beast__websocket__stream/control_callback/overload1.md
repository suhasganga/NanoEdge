###### [websocket::stream::control\_callback (1 of 2 overloads)](overload1.html "websocket::stream::control_callback (1 of 2 overloads)")

Set a callback to be invoked on each incoming control frame.

###### [Synopsis](overload1.html#beast.ref.boost__beast__websocket__stream.control_callback.overload1.synopsis)

```programlisting
void
control_callback(
    std::function< void(frame_type, string_view)> cb);
```

###### [Description](overload1.html#beast.ref.boost__beast__websocket__stream.control_callback.overload1.description)

Sets the callback to be invoked whenever a ping, pong, or close control
frame is received during a call to one of the following functions:

* [`beast::websocket::stream::read`](../read.html "websocket::stream::read")
* [`beast::websocket::stream::read_some`](../read_some.html "websocket::stream::read_some")
* [`beast::websocket::stream::async_read`](../async_read.html "websocket::stream::async_read")
* [`beast::websocket::stream::async_read_some`](../async_read_some.html "websocket::stream::async_read_some")

Unlike completion handlers, the callback will be invoked for each control
frame during a call to any synchronous or asynchronous read function.
The operation is passive, with no associated error code, and triggered
by reads.

For close frames, the close reason code may be obtained by calling the
function [`reason`](../reason.html "websocket::stream::reason").

###### [Parameters](overload1.html#beast.ref.boost__beast__websocket__stream.control_callback.overload1.parameters)

| Name | Description |
| --- | --- |
| `cb` | The function object to call, which must be invocable with this equivalent signature:   ```table-programlisting void callback(     frame_type kind,       // The type of frame     string_view payload    // The payload in the frame ); ```   The implementation type-erases the callback which may require a dynamic allocation. To prevent the possibility of a dynamic allocation, use `std::ref` to wrap the callback. If the read operation which receives the control frame is an asynchronous operation, the callback will be invoked using the same method as that used to invoke the final handler. |

###### [Remarks](overload1.html#beast.ref.boost__beast__websocket__stream.control_callback.overload1.remarks)

Incoming ping and close frames are automatically handled. Pings are responded
to with pongs, and a close frame is responded to with a close frame leading
to the closure of the stream. It is not necessary to manually send pings,
pongs, or close frames from inside the control callback. Attempting to
manually send a close frame from inside the control callback after receiving
a close frame will result in undefined behavior.