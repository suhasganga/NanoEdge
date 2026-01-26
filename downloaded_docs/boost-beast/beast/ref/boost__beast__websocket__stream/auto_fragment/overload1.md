###### [websocket::stream::auto\_fragment (1 of 2 overloads)](overload1.html "websocket::stream::auto_fragment (1 of 2 overloads)")

Set the automatic fragmentation option.

###### [Synopsis](overload1.html#beast.ref.boost__beast__websocket__stream.auto_fragment.overload1.synopsis)

```programlisting
void
auto_fragment(
    bool value);
```

###### [Description](overload1.html#beast.ref.boost__beast__websocket__stream.auto_fragment.overload1.description)

Determines if outgoing message payloads are broken up into multiple pieces.

When the automatic fragmentation size is turned on, outgoing message
payloads are broken up into multiple frames no larger than the write
buffer size.

The default setting is to fragment messages.

###### [Parameters](overload1.html#beast.ref.boost__beast__websocket__stream.auto_fragment.overload1.parameters)

| Name | Description |
| --- | --- |
| `value` | A `bool` indicating if auto fragmentation should be on. |

###### [Example](overload1.html#beast.ref.boost__beast__websocket__stream.auto_fragment.overload1.example)

Setting the automatic fragmentation option:

```programlisting
ws.auto_fragment( true );
```