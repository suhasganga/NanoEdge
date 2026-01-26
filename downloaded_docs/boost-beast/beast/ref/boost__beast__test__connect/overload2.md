##### [test::connect (2 of 2 overloads)](overload2.html "test::connect (2 of 2 overloads)")

Return a new stream connected to the given stream.

###### [Synopsis](overload2.html#beast.ref.boost__beast__test__connect.overload2.synopsis)

Defined in header `<boost/beast/_experimental/test/stream.hpp>`

```programlisting
template<
    class... Args>
basic_stream
connect(
    basic_stream& to,
    Args&&... args);
```

###### [Parameters](overload2.html#beast.ref.boost__beast__test__connect.overload2.parameters)

| Name | Description |
| --- | --- |
| `to` | The stream to connect to. |
| `args` | Optional arguments forwarded to the new stream's constructor. |

###### [Return Value](overload2.html#beast.ref.boost__beast__test__connect.overload2.return_value)

The new, connected stream.