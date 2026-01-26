###### [test::basic\_stream::basic\_stream (1 of 7 overloads)](overload1.html "test::basic_stream::basic_stream (1 of 7 overloads)")

Move Constructor.

###### [Synopsis](overload1.html#beast.ref.boost__beast__test__basic_stream.basic_stream.overload1.synopsis)

```programlisting
basic_stream(
    basic_stream&& other);
```

###### [Description](overload1.html#beast.ref.boost__beast__test__basic_stream.basic_stream.overload1.description)

Moving the stream while asynchronous operations are pending results in
undefined behavior.