###### [test::basic\_stream::basic\_stream (5 of 7 overloads)](overload5.html "test::basic_stream::basic_stream (5 of 7 overloads)")

Construct a stream.

###### [Synopsis](overload5.html#beast.ref.boost__beast__test__basic_stream.basic_stream.overload5.synopsis)

```programlisting
basic_stream(
    net::io_context& ioc,
    fail_count& fc);
```

###### [Description](overload5.html#beast.ref.boost__beast__test__basic_stream.basic_stream.overload5.description)

The stream will be created in a disconnected state.

###### [Parameters](overload5.html#beast.ref.boost__beast__test__basic_stream.basic_stream.overload5.parameters)

| Name | Description |
| --- | --- |
| `ioc` | The `io_context` object that the stream will use to dispatch handlers for any asynchronous operations. |
| `fc` | The [`fail_count`](../../boost__beast__test__fail_count.html "test::fail_count") to associate with the stream. Each I/O operation performed on the stream will increment the fail count. When the fail count reaches its internal limit, a simulated failure error will be raised. |