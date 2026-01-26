###### [basic\_stream::basic\_stream (1 of 3 overloads)](overload1.html "basic_stream::basic_stream (1 of 3 overloads)")

Constructor.

###### [Synopsis](overload1.html#beast.ref.boost__beast__basic_stream.basic_stream.overload1.synopsis)

```programlisting
template<
    class... Args>
basic_stream(
    Args&&... args);
```

###### [Description](overload1.html#beast.ref.boost__beast__basic_stream.basic_stream.overload1.description)

This constructor creates the stream by forwarding all arguments to the
underlying socket. The socket then needs to be open and connected or
accepted before data can be sent or received on it.

###### [Parameters](overload1.html#beast.ref.boost__beast__basic_stream.basic_stream.overload1.parameters)

| Name | Description |
| --- | --- |
| `args` | A list of parameters forwarded to the constructor of the underlying socket. |