###### [websocket::stream::stream (3 of 3 overloads)](overload3.html "websocket::stream::stream (3 of 3 overloads)")

Rebinding constructor.

###### [Synopsis](overload3.html#beast.ref.boost__beast__websocket__stream.stream.overload3.synopsis)

```programlisting
template<
    class Other>
stream(
    stream< Other >&& other);
```

###### [Description](overload3.html#beast.ref.boost__beast__websocket__stream.stream.overload3.description)

This constructor creates a the websocket stream from a websocket stream
with a different executor.

###### [Exceptions](overload3.html#beast.ref.boost__beast__websocket__stream.stream.overload3.exceptions)

| Type | Thrown On |
| --- | --- |
| `Any` | exception thrown by the NextLayer rebind constructor. |

###### [Parameters](overload3.html#beast.ref.boost__beast__websocket__stream.stream.overload3.parameters)

| Name | Description |
| --- | --- |
| `other` | The other websocket stream to construct from. |