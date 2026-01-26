##### [test::basic\_stream::operator=](operator_eq_.html "test::basic_stream::operator=")

Move Assignment.

###### [Synopsis](operator_eq_.html#beast.ref.boost__beast__test__basic_stream.operator_eq_.synopsis)

```programlisting
basic_stream&
operator=(
    basic_stream&& other);
```

###### [Description](operator_eq_.html#beast.ref.boost__beast__test__basic_stream.operator_eq_.description)

Moving the stream while asynchronous operations are pending results in
undefined behavior.