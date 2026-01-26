###### [http::serializer::serializer (1 of 3 overloads)](overload1.html "http::serializer::serializer (1 of 3 overloads)")

Move Constructor.

###### [Synopsis](overload1.html#beast.ref.boost__beast__http__serializer.serializer.overload1.synopsis)

```programlisting
serializer(
    serializer&&);
```

###### [Description](overload1.html#beast.ref.boost__beast__http__serializer.serializer.overload1.description)

###### [Remarks](overload1.html#beast.ref.boost__beast__http__serializer.serializer.overload1.remarks)

Moving or copying the serializer after the first call to [`serializer::next`](../next.html "http::serializer::next") results in undefined behavior.
Try to heap-allocate the serializer object if you need to move the serializer
between multiple async operations (for example, between a call to `async_write_header` and `async_write`).