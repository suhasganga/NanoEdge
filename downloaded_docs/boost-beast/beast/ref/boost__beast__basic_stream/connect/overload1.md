###### [basic\_stream::connect (1 of 10 overloads)](overload1.html "basic_stream::connect (1 of 10 overloads)")

Connect the stream to the specified endpoint.

###### [Synopsis](overload1.html#beast.ref.boost__beast__basic_stream.connect.overload1.synopsis)

```programlisting
void
connect(
    endpoint_type const& ep);
```

###### [Description](overload1.html#beast.ref.boost__beast__basic_stream.connect.overload1.description)

This function is used to connect the underlying socket to the specified
remote endpoint. The function call will block until the connection is
successfully made or an error occurs. The underlying socket is automatically
opened if needed. An automatically opened socket is not returned to the
closed state upon failure.

###### [Parameters](overload1.html#beast.ref.boost__beast__basic_stream.connect.overload1.parameters)

| Name | Description |
| --- | --- |
| `ep` | The remote endpoint to connect to. |

###### [Exceptions](overload1.html#beast.ref.boost__beast__basic_stream.connect.overload1.exceptions)

| Type | Thrown On |
| --- | --- |
| `[link beast.ref.boost__beast__system_error system_error]` | Thrown on failure. |

###### [See Also](overload1.html#beast.ref.boost__beast__basic_stream.connect.overload1.see_also)

[`connect`](../connect.html "basic_stream::connect")