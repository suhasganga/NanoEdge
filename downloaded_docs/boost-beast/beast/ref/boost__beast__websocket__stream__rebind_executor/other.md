##### [websocket::stream::rebind\_executor::other](other.html "websocket::stream::rebind_executor::other")

The stream type when rebound to the specified executor.

###### [Synopsis](other.html#beast.ref.boost__beast__websocket__stream__rebind_executor.other.synopsis)

```programlisting
using other = stream< typename next_layer_type::template rebind_executor< Executor1 >::other, deflateSupported >;
```

###### [Types](other.html#beast.ref.boost__beast__websocket__stream__rebind_executor.other.types)

| Name | Description |
| --- | --- |
| **[executor\_type](../boost__beast__websocket__stream/executor_type.html "websocket::stream::executor_type")** | The type of the executor associated with the object. |
| **[is\_deflate\_supported](../boost__beast__websocket__stream/is_deflate_supported.html "websocket::stream::is_deflate_supported")** | Indicates if the permessage-deflate extension is supported. |
| **[next\_layer\_type](../boost__beast__websocket__stream/next_layer_type.html "websocket::stream::next_layer_type")** | The type of the next layer. |
| **[rebind\_executor](../boost__beast__websocket__stream__rebind_executor.html "websocket::stream::rebind_executor") [constructor]** | Rebinds the stream type to another executor. |

###### [Member Functions](other.html#beast.ref.boost__beast__websocket__stream__rebind_executor.other.member_functions)

| Name | Description |
| --- | --- |
| **[accept](../boost__beast__websocket__stream/accept.html "websocket::stream::accept")** | Perform the WebSocket handshake in the server role.  — Read and respond to a WebSocket HTTP Upgrade request.  — Respond to a WebSocket HTTP Upgrade request. |
| **[async\_accept](../boost__beast__websocket__stream/async_accept.html "websocket::stream::async_accept")** | Perform the WebSocket handshake asynchronously in the server role. |
| **[async\_close](../boost__beast__websocket__stream/async_close.html "websocket::stream::async_close")** | Perform the WebSocket closing handshake asynchronously and close the underlying stream. |
| **[async\_handshake](../boost__beast__websocket__stream/async_handshake.html "websocket::stream::async_handshake")** | Perform the WebSocket handshake asynchronously in the client role. |
| **[async\_ping](../boost__beast__websocket__stream/async_ping.html "websocket::stream::async_ping")** | Send a websocket ping control frame asynchronously. |
| **[async\_pong](../boost__beast__websocket__stream/async_pong.html "websocket::stream::async_pong")** | Send a websocket pong control frame asynchronously. |
| **[async\_read](../boost__beast__websocket__stream/async_read.html "websocket::stream::async_read")** | Read a complete message asynchronously. |
| **[async\_read\_some](../boost__beast__websocket__stream/async_read_some.html "websocket::stream::async_read_some")** | Read some message data asynchronously. |
| **[async\_write](../boost__beast__websocket__stream/async_write.html "websocket::stream::async_write")** | Write a complete message asynchronously. |
| **[async\_write\_some](../boost__beast__websocket__stream/async_write_some.html "websocket::stream::async_write_some")** | Write some message data asynchronously. |
| **[auto\_fragment](../boost__beast__websocket__stream/auto_fragment.html "websocket::stream::auto_fragment")** | Set the automatic fragmentation option.  — Returns `true` if the automatic fragmentation option is set. |
| **[binary](../boost__beast__websocket__stream/binary.html "websocket::stream::binary")** | Set the binary message write option.  — Returns `true` if the binary message write option is set. |
| **[close](../boost__beast__websocket__stream/close.html "websocket::stream::close")** | Perform the WebSocket closing handshake and close the underlying stream. |
| **[compress](../boost__beast__websocket__stream/compress.html "websocket::stream::compress")** | Set the compress message write option.  — Returns `true` if the compress message write option is set. |
| **[control\_callback](../boost__beast__websocket__stream/control_callback.html "websocket::stream::control_callback")** | Set a callback to be invoked on each incoming control frame.  — Reset the control frame callback. |
| **[get\_executor](../boost__beast__websocket__stream/get_executor.html "websocket::stream::get_executor")** | Get the executor associated with the object. |
| **[get\_option](../boost__beast__websocket__stream/get_option.html "websocket::stream::get_option")** | Get the option value.  — Get the timeout option.  — Get the permessage-deflate extension options. |
| **[get\_status](../boost__beast__websocket__stream/get_status.html "websocket::stream::get_status")** | Get the status of the permessage-deflate extension. |
| **[got\_binary](../boost__beast__websocket__stream/got_binary.html "websocket::stream::got_binary")** | Returns `true` if the latest message data indicates binary. |
| **[got\_text](../boost__beast__websocket__stream/got_text.html "websocket::stream::got_text")** | Returns `true` if the latest message data indicates text. |
| **[handshake](../boost__beast__websocket__stream/handshake.html "websocket::stream::handshake")** | Perform the WebSocket handshake in the client role. |
| **[is\_message\_done](../boost__beast__websocket__stream/is_message_done.html "websocket::stream::is_message_done")** | Returns `true` if the last completed read finished the current message. |
| **[is\_open](../boost__beast__websocket__stream/is_open.html "websocket::stream::is_open")** | Returns `true` if the stream is open. |
| **[next\_layer](../boost__beast__websocket__stream/next_layer.html "websocket::stream::next_layer")** | Get a reference to the next layer. |
| **[operator=](../boost__beast__websocket__stream/operator_eq_.html "websocket::stream::operator=")** | Move assignment (deleted) |
| **[ping](../boost__beast__websocket__stream/ping.html "websocket::stream::ping")** | Send a websocket ping control frame. |
| **[pong](../boost__beast__websocket__stream/pong.html "websocket::stream::pong")** | Send a websocket pong control frame. |
| **[read](../boost__beast__websocket__stream/read.html "websocket::stream::read")** | Read a complete message. |
| **[read\_message\_max](../boost__beast__websocket__stream/read_message_max.html "websocket::stream::read_message_max")** | Set the maximum incoming message size option.  — Returns the maximum incoming message size setting. |
| **[read\_size\_hint](../boost__beast__websocket__stream/read_size_hint.html "websocket::stream::read_size_hint")** | Returns a suggested maximum buffer size for the next call to read. |
| **[read\_some](../boost__beast__websocket__stream/read_some.html "websocket::stream::read_some")** | Read some message data. |
| **[reason](../boost__beast__websocket__stream/reason.html "websocket::stream::reason")** | Returns the close reason received from the remote peer. |
| **[secure\_prng](../boost__beast__websocket__stream/secure_prng.html "websocket::stream::secure_prng")** | Set whether the PRNG is cryptographically secure. |
| **[set\_option](../boost__beast__websocket__stream/set_option.html "websocket::stream::set_option")** | Set the option value.  — Set the timeout option.  — Set the permessage-deflate extension options. |
| **[stream](../boost__beast__websocket__stream/stream.html "websocket::stream::stream")** | Constructor.  — Rebinding constructor. |
| **[text](../boost__beast__websocket__stream/text.html "websocket::stream::text")** | Set the text message write option.  — Returns `true` if the text message write option is set. |
| **[write](../boost__beast__websocket__stream/write.html "websocket::stream::write")** | Write a complete message. |
| **[write\_buffer\_bytes](../boost__beast__websocket__stream/write_buffer_bytes.html "websocket::stream::write_buffer_bytes")** | Set the write buffer size option.  — Returns the size of the write buffer. |
| **[write\_some](../boost__beast__websocket__stream/write_some.html "websocket::stream::write_some")** | Write some message data. |
| **[~stream](../boost__beast__websocket__stream/_dtor_stream.html "websocket::stream::~stream") [destructor]** | Destructor. |

The [`stream`](../boost__beast__websocket__stream.html "websocket::stream") class template provides
asynchronous and blocking message-oriented functionality necessary for
clients and servers to utilize the WebSocket protocol.

For asynchronous operations, the application must ensure that they are
are all performed within the same implicit or explicit strand.

###### [Thread Safety](other.html#beast.ref.boost__beast__websocket__stream__rebind_executor.other.thread_safety)

*Distinct**objects:*Safe.

*Shared**objects:*Unsafe. The application
must also ensure that all asynchronous operations are performed within
the same implicit or explicit strand.

###### [Example](other.html#beast.ref.boost__beast__websocket__stream__rebind_executor.other.example)

To declare the [`stream`](../boost__beast__websocket__stream.html "websocket::stream") object with a [`tcp_stream`](../boost__beast__tcp_stream.html "tcp_stream") in a multi-threaded
asynchronous program using a strand, you may write:

```programlisting
websocket::stream<tcp_stream> ws{net::make_strand(ioc)};
```

Alternatively, for a single-threaded or synchronous application you may
write:

```programlisting
websocket::stream<tcp_stream> ws(ioc);
```

###### [Template Parameters](other.html#beast.ref.boost__beast__websocket__stream__rebind_executor.other.template_parameters)

| Type | Description |
| --- | --- |
| `NextLayer` | The type representing the next layer, to which data will be read and written during operations. For synchronous operations, the type must support the *SyncStream* concept. For asynchronous operations, the type must support the *AsyncStream* concept. |
| `deflateSupported` | A `bool` indicating whether or not the stream will be capable of negotiating the permessage-deflate websocket extension. Note that even if this is set to `true`, the permessage deflate options (set by the caller at runtime) must still have the feature enabled for a successful negotiation to occur. |

###### [Remarks](other.html#beast.ref.boost__beast__websocket__stream__rebind_executor.other.remarks)

A stream object must not be moved or destroyed while there are pending
asynchronous operations associated with it.

###### [See Also](other.html#beast.ref.boost__beast__websocket__stream__rebind_executor.other.see_also)

* [Websocket
  Opening Handshake Client Requirements (RFC6455)](https://tools.ietf.org/html/rfc6455#section-4.1)
* [Websocket
  Opening Handshake Server Requirements (RFC6455)](https://tools.ietf.org/html/rfc6455#section-4.2)
* [Websocket
  Closing Handshake (RFC6455)](https://tools.ietf.org/html/rfc6455#section-7.1.2)
* [Websocket
  Close (RFC6455)](https://tools.ietf.org/html/rfc6455#section-5.5.1)
* [WebSocket
  Ping (RFC6455)](https://tools.ietf.org/html/rfc6455#section-5.5.2)
* [WebSocket
  Pong (RFC6455)](https://tools.ietf.org/html/rfc6455#section-5.5.3)
* [Host field
  (RFC7230)](https://tools.ietf.org/html/rfc7230#section-5.4)
* [request-target
  (RFC7230)](https://tools.ietf.org/html/rfc7230#section-3.1.1)
* [origin-form
  (RFC7230)](https://tools.ietf.org/html/rfc7230#section-5.3.1)

###### [Types](other.html#beast.ref.boost__beast__websocket__stream__rebind_executor.other.types0)

| Name | Description |
| --- | --- |
| **[other](other.html "websocket::stream::rebind_executor::other")** | The stream type when rebound to the specified executor. |