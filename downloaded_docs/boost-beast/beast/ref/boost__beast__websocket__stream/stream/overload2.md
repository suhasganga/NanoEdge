###### [websocket::stream::stream (2 of 3 overloads)](overload2.html "websocket::stream::stream (2 of 3 overloads)")

Constructor.

###### [Synopsis](overload2.html#beast.ref.boost__beast__websocket__stream.stream.overload2.synopsis)

```programlisting
template<
    class... Args>
stream(
    Args&&... args);
```

###### [Description](overload2.html#beast.ref.boost__beast__websocket__stream.stream.overload2.description)

This constructor creates a websocket stream and initializes the next
layer object.

###### [Exceptions](overload2.html#beast.ref.boost__beast__websocket__stream.stream.overload2.exceptions)

| Type | Thrown On |
| --- | --- |
| `Any` | exceptions thrown by the NextLayer constructor. |

###### [Parameters](overload2.html#beast.ref.boost__beast__websocket__stream.stream.overload2.parameters)

| Name | Description |
| --- | --- |
| `args` | The arguments to be passed to initialize the next layer object. The arguments are forwarded to the next layer's constructor. |