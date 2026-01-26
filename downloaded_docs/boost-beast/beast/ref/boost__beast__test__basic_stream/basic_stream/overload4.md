###### [test::basic\_stream::basic\_stream (4 of 7 overloads)](overload4.html "test::basic_stream::basic_stream (4 of 7 overloads)")

Construct a stream.

###### [Synopsis](overload4.html#beast.ref.boost__beast__test__basic_stream.basic_stream.overload4.synopsis)

```programlisting
basic_stream(
    executor_type exec);
```

###### [Description](overload4.html#beast.ref.boost__beast__test__basic_stream.basic_stream.overload4.description)

The stream will be created in a disconnected state.

###### [Parameters](overload4.html#beast.ref.boost__beast__test__basic_stream.basic_stream.overload4.parameters)

| Name | Description |
| --- | --- |
| `exec` | The `executor` object that the stream will use to dispatch handlers for any asynchronous operations. |