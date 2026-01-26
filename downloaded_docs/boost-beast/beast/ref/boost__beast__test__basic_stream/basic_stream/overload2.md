###### [test::basic\_stream::basic\_stream (2 of 7 overloads)](overload2.html "test::basic_stream::basic_stream (2 of 7 overloads)")

Move Constructor.

###### [Synopsis](overload2.html#beast.ref.boost__beast__test__basic_stream.basic_stream.overload2.synopsis)

```programlisting
template<
    class Executor2>
basic_stream(
    basic_stream< Executor2 >&& other);
```

###### [Description](overload2.html#beast.ref.boost__beast__test__basic_stream.basic_stream.overload2.description)

Moving the stream while asynchronous operations are pending results in
undefined behavior.