###### [websocket::stream::read\_message\_max (1 of 2 overloads)](overload1.html "websocket::stream::read_message_max (1 of 2 overloads)")

Set the maximum incoming message size option.

###### [Synopsis](overload1.html#beast.ref.boost__beast__websocket__stream.read_message_max.overload1.synopsis)

```programlisting
void
read_message_max(
    std::size_t amount);
```

###### [Description](overload1.html#beast.ref.boost__beast__websocket__stream.read_message_max.overload1.description)

Sets the largest permissible incoming message size. Message frame fields
indicating a size that would bring the total message size over this limit
will cause a protocol failure.

The default setting is 16 megabytes. A value of zero indicates a limit
of the maximum value of a `std::uint64_t`.

###### [Example](overload1.html#beast.ref.boost__beast__websocket__stream.read_message_max.overload1.example)

Setting the maximum read message size.

```programlisting
ws.read_message_max(65536);
```

###### [Parameters](overload1.html#beast.ref.boost__beast__websocket__stream.read_message_max.overload1.parameters)

| Name | Description |
| --- | --- |
| `amount` | The limit on the size of incoming messages. |