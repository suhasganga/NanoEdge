###### [basic\_stream::connect (2 of 10 overloads)](overload2.html "basic_stream::connect (2 of 10 overloads)")

Connect the stream to the specified endpoint.

###### [Synopsis](overload2.html#beast.ref.boost__beast__basic_stream.connect.overload2.synopsis)

```programlisting
void
connect(
    endpoint_type const& ep,
    error_code& ec);
```

###### [Description](overload2.html#beast.ref.boost__beast__basic_stream.connect.overload2.description)

This function is used to connect the underlying socket to the specified
remote endpoint. The function call will block until the connection is
successfully made or an error occurs. The underlying socket is automatically
opened if needed. An automatically opened socket is not returned to the
closed state upon failure.

###### [Parameters](overload2.html#beast.ref.boost__beast__basic_stream.connect.overload2.parameters)

| Name | Description |
| --- | --- |
| `ep` | The remote endpoint to connect to. |
| `ec` | Set to indicate what error occurred, if any. |

###### [See Also](overload2.html#beast.ref.boost__beast__basic_stream.connect.overload2.see_also)

[`connect`](../connect.html "basic_stream::connect")