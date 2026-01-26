##### [http::operator<< (2 of 5 overloads)](overload2.html "http::operator<< (2 of 5 overloads)")

Serialize an HTTP/1 message to a `std::ostream`.

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__operator_lt__lt_.overload2.synopsis)

Defined in header `<boost/beast/http/write.hpp>`

```programlisting
template<
    bool isRequest,
    class Body,
    class Fields>
std::ostream&
operator<<(
    std::ostream& os,
    message< isRequest, Body, Fields > const& msg);
```

###### [Description](overload2.html#beast.ref.boost__beast__http__operator_lt__lt_.overload2.description)

The function converts the message to its HTTP/1 serialized representation
and stores the result in the output stream.

The implementation will automatically perform chunk encoding if the contents
of the message indicate that chunk encoding is required.

###### [Parameters](overload2.html#beast.ref.boost__beast__http__operator_lt__lt_.overload2.parameters)

| Name | Description |
| --- | --- |
| `os` | The output stream to write to. |
| `msg` | The message to write. |