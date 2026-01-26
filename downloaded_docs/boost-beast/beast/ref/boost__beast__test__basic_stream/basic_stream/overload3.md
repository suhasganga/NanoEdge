###### [test::basic\_stream::basic\_stream (3 of 7 overloads)](overload3.html "test::basic_stream::basic_stream (3 of 7 overloads)")

Construct a stream.

###### [Synopsis](overload3.html#beast.ref.boost__beast__test__basic_stream.basic_stream.overload3.synopsis)

```programlisting
template<
    class ExecutionContext,
    class = typename std::enable_if<            std::is_convertible<ExecutionContext&, net::execution_context&>::value>::type>
basic_stream(
    ExecutionContext& context);
```

###### [Description](overload3.html#beast.ref.boost__beast__test__basic_stream.basic_stream.overload3.description)

The stream will be created in a disconnected state.

###### [Parameters](overload3.html#beast.ref.boost__beast__test__basic_stream.basic_stream.overload3.parameters)

| Name | Description |
| --- | --- |
| `context` | The `io_context` object that the stream will use to dispatch handlers for any asynchronous operations. |