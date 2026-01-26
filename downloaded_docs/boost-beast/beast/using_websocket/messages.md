### [Messages](messages.html "Messages")

Once a websocket session is established, messages can be sent unsolicited
by either peer at any time. A message is made up of one or more *messages
frames*. Each frame is prefixed with the size of the payload in
bytes, followed by the data. A frame also contains a flag (called 'fin')
indicating whether or not it is the last frame of the message. When a message
is made up from only one frame, it is possible to know immediately what the
size of the message will be. Otherwise, the total size of the message can
only be determined once the last frame is received.

The boundaries between frames of a multi-frame message are not not considered
part of the message. Intermediaries such as proxies which forward the websocket
traffic are free to "reframe" (split frames and combine them) the
message in arbitrary ways. These intermediaries include Beast, which can
reframe messages automatically in some cases depending on the options set
on the stream.

|  |  |
| --- | --- |
| [Caution] | Caution |
| An algorithm should never depend on the way that incoming or outgoing messages are split up into frames. |

Messages can be either text or binary. A message sent as text must contain
consist of valid utf8, while a message sent as binary may contain arbitrary
data. In addition to message frames, websocket provides *control
frames* in the form of ping, pong, and close messages which have
a small upper limit on their payload size. Depending on how a message is
framed, control frames may have more opportunities to be sent in-between.

##### [Sending](messages.html#beast.using_websocket.messages.sending)

These stream members are used to write websocket messages:

**Table 1.34. WebSocket Stream Write Operations**

| Function | Description |
| --- | --- |
| [`write`](../ref/boost__beast__websocket__stream/write/overload2.html "websocket::stream::write (2 of 2 overloads)"), [`async_write`](../ref/boost__beast__websocket__stream/async_write.html "websocket::stream::async_write") | Send a buffer sequence as a complete message. |
| [`write_some`](../ref/boost__beast__websocket__stream/write_some/overload2.html "websocket::stream::write_some (2 of 2 overloads)"), [`async_write_some`](../ref/boost__beast__websocket__stream/async_write_some.html "websocket::stream::async_write_some") | Send a buffer sequence as part of a message. |

  

This example shows how to send a buffer sequence as a complete message.

```programlisting
net::const_buffer b("Hello, world!", 13);

// This sets all outgoing messages to be sent as text.
// Text messages must contain valid utf8, this is checked
// when reading but not when writing.

ws.text(true);

// Write the buffer as text
ws.write(b);
```

The same message could be sent in two or more frames thusly.

##### [Receiving](messages.html#beast.using_websocket.messages.receiving)

**Table 1.35. WebSocket Stream Read Operations**

| Function | Description |
| --- | --- |
| [`read`](../ref/boost__beast__websocket__stream/read/overload2.html "websocket::stream::read (2 of 2 overloads)"), [`async_read`](../ref/boost__beast__websocket__stream/async_read.html "websocket::stream::async_read") | Read a complete message into a [*DynamicBuffer*](../concepts/DynamicBuffer.html "DynamicBuffer"). |
| [`read_some`](../ref/boost__beast__websocket__stream/read_some/overload2.html "websocket::stream::read_some (2 of 4 overloads)"), [`async_read_some`](../ref/boost__beast__websocket__stream/async_read_some/overload1.html "websocket::stream::async_read_some (1 of 2 overloads)") | Read part of a message into a [*DynamicBuffer*](../concepts/DynamicBuffer.html "DynamicBuffer"). |
| [`read_some`](../ref/boost__beast__websocket__stream/read_some/overload4.html "websocket::stream::read_some (4 of 4 overloads)"), [`async_read_some`](../ref/boost__beast__websocket__stream/async_read_some/overload2.html "websocket::stream::async_read_some (2 of 2 overloads)") | Read part of a message into a [*MutableBufferSequence*](../../../../../../doc/html/boost_asio/reference/MutableBufferSequence.html). |

  

After the WebSocket handshake is accomplished, callers may send and receive
messages using the message oriented interface. This interface requires that
all of the buffers representing the message are known ahead of time:

```programlisting
// This DynamicBuffer will hold the received message
flat_buffer buffer;

// Read a complete message into the buffer's input area
ws.read(buffer);

// Set text mode if the received message was also text,
// otherwise binary mode will be set.
ws.text(ws.got_text());

// Echo the received message back to the peer. If the received
// message was in text mode, the echoed message will also be
// in text mode, otherwise it will be in binary mode.
ws.write(buffer.data());

// Discard all of the bytes stored in the dynamic buffer,
// otherwise the next call to read will append to the existing
// data instead of building a fresh message.
buffer.consume(buffer.size());
```

|  |  |
| --- | --- |
| [Important] | Important |
| [`websocket::stream`](../ref/boost__beast__websocket__stream.html "websocket::stream") is not thread-safe. Calls to stream member functions must all be made from the same implicit or explicit strand. |

##### [Frames](messages.html#beast.using_websocket.messages.frames)

Some use-cases make it impractical or impossible to buffer the entire message
ahead of time:

* Streaming multimedia to an endpoint.
* Sending a message that does not fit in memory at once.
* Providing incremental results as they become available.

For these cases, the partial data oriented interface may be used. This example
reads and echoes a complete message using this interface:

```programlisting
// This DynamicBuffer will hold the received message
multi_buffer buffer;

// Read the next message in pieces
do
{
    // Append up to 512 bytes of the message into the buffer
    ws.read_some(buffer, 512);
}
while(! ws.is_message_done());

// At this point we have a complete message in the buffer, now echo it

// The echoed message will be sent in binary mode if the received
// message was in binary mode, otherwise we will send in text mode.
ws.binary(ws.got_binary());

// This buffer adaptor allows us to iterate through buffer in pieces
buffers_suffix<multi_buffer::const_buffers_type> cb{buffer.data()};

// Echo the received message in pieces.
// This will cause the message to be broken up into multiple frames.
for(;;)
{
    if(buffer_bytes(cb) > 512)
    {
        // There are more than 512 bytes left to send, just
        // send the next 512 bytes. The value `false` informs
        // the stream that the message is not complete.
        ws.write_some(false, buffers_prefix(512, cb));

        // This efficiently discards data from the adaptor by
        // simply ignoring it, but does not actually affect the
        // underlying dynamic buffer.
        cb.consume(512);
    }
    else
    {
        // Only 512 bytes or less remain, so write the whole
        // thing and inform the stream that this piece represents
        // the end of the message by passing `true`.
        ws.write_some(true, cb);
        break;
    }
}

// Discard all of the bytes stored in the dynamic buffer,
// otherwise the next call to read will append to the existing
// data instead of building a fresh message.
buffer.consume(buffer.size());
```