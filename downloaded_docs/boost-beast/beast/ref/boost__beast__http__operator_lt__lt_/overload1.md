##### [http::operator<< (1 of 5 overloads)](overload1.html "http::operator<< (1 of 5 overloads)")

Serialize an HTTP/1 header to a `std::ostream`.

###### [Synopsis](overload1.html#beast.ref.boost__beast__http__operator_lt__lt_.overload1.synopsis)

Defined in header `<boost/beast/http/write.hpp>`

```programlisting
template<
    bool isRequest,
    class Fields>
std::ostream&
operator<<(
    std::ostream& os,
    header< isRequest, Fields > const& msg);
```

###### [Description](overload1.html#beast.ref.boost__beast__http__operator_lt__lt_.overload1.description)

The function converts the header to its HTTP/1 serialized representation
and stores the result in the output stream.

###### [Parameters](overload1.html#beast.ref.boost__beast__http__operator_lt__lt_.overload1.parameters)

| Name | Description |
| --- | --- |
| `os` | The output stream to write to. |
| `msg` | The message fields to write. |