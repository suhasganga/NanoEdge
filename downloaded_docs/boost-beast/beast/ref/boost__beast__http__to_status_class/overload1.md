##### [http::to\_status\_class (1 of 2 overloads)](overload1.html "http::to_status_class (1 of 2 overloads)")

Convert an integer to a [`status_class`](../boost__beast__http__status_class.html "http::status_class").

###### [Synopsis](overload1.html#beast.ref.boost__beast__http__to_status_class.overload1.synopsis)

Defined in header `<boost/beast/http/status.hpp>`

```programlisting
status_class
to_status_class(
    unsigned v);
```

###### [Parameters](overload1.html#beast.ref.boost__beast__http__to_status_class.overload1.parameters)

| Name | Description |
| --- | --- |
| `v` | The integer representing a status code. |

###### [Return Value](overload1.html#beast.ref.boost__beast__http__to_status_class.overload1.return_value)

The status class. If the integer does not match a known status class,
[`status_class::unknown`](../boost__beast__http__status_class.html "http::status_class") is returned.