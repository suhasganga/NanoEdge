###### [websocket::stream::write\_buffer\_bytes (1 of 2 overloads)](overload1.html "websocket::stream::write_buffer_bytes (1 of 2 overloads)")

Set the write buffer size option.

###### [Synopsis](overload1.html#beast.ref.boost__beast__websocket__stream.write_buffer_bytes.overload1.synopsis)

```programlisting
void
write_buffer_bytes(
    std::size_t amount);
```

###### [Description](overload1.html#beast.ref.boost__beast__websocket__stream.write_buffer_bytes.overload1.description)

Sets the size of the write buffer used by the implementation to send
frames. The write buffer is needed when masking payload data in the client
role, compressing frames, or auto-fragmenting message data.

Lowering the size of the buffer can decrease the memory requirements
for each connection, while increasing the size of the buffer can reduce
the number of calls made to the next layer to write data.

The default setting is 4096. The minimum value is 8.

The write buffer size can only be changed when the stream is not open.
Undefined behavior results if the option is modified after a successful
WebSocket handshake.

###### [Example](overload1.html#beast.ref.boost__beast__websocket__stream.write_buffer_bytes.overload1.example)

Setting the write buffer size.

```programlisting
ws.write_buffer_bytes(8192);
```

###### [Parameters](overload1.html#beast.ref.boost__beast__websocket__stream.write_buffer_bytes.overload1.parameters)

| Name | Description |
| --- | --- |
| `amount` | The size of the write buffer in bytes. |