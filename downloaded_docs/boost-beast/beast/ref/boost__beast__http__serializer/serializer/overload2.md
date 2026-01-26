###### [http::serializer::serializer (2 of 3 overloads)](overload2.html "http::serializer::serializer (2 of 3 overloads)")

Copy Constructor.

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__serializer.serializer.overload2.synopsis)

```programlisting
serializer(
    serializer const&);
```

###### [Description](overload2.html#beast.ref.boost__beast__http__serializer.serializer.overload2.description)

###### [Remarks](overload2.html#beast.ref.boost__beast__http__serializer.serializer.overload2.remarks)

Moving or copying the serializer after the first call to [`serializer::next`](../next.html "http::serializer::next") results in undefined behavior.
Try to heap-allocate the serializer object if you need to move the serializer
between multiple async operations (for example, between a call to `async_write_header` and `async_write`).