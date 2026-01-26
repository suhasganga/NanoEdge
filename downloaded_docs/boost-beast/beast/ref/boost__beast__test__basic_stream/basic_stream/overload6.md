###### [test::basic\_stream::basic\_stream (6 of 7 overloads)](overload6.html "test::basic_stream::basic_stream (6 of 7 overloads)")

Construct a stream.

###### [Synopsis](overload6.html#beast.ref.boost__beast__test__basic_stream.basic_stream.overload6.synopsis)

```programlisting
basic_stream(
    net::io_context& ioc,
    string_view s);
```

###### [Description](overload6.html#beast.ref.boost__beast__test__basic_stream.basic_stream.overload6.description)

The stream will be created in a disconnected state.

###### [Parameters](overload6.html#beast.ref.boost__beast__test__basic_stream.basic_stream.overload6.parameters)

| Name | Description |
| --- | --- |
| `ioc` | The `io_context` object that the stream will use to dispatch handlers for any asynchronous operations. |
| `s` | A string which will be appended to the input area, not including the null terminator. |