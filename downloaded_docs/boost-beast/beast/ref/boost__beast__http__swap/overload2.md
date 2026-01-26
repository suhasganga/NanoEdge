##### [http::swap (2 of 2 overloads)](overload2.html "http::swap (2 of 2 overloads)")

Swap two message objects.

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__swap.overload2.synopsis)

Defined in header `<boost/beast/http/message.hpp>`

```programlisting
template<
    bool isRequest,
    class Body,
    class Fields>
void
swap(
    message< isRequest, Body, Fields >& m1,
    message< isRequest, Body, Fields >& m2);
```

###### [Requirements:](overload2.html#beast.ref.boost__beast__http__swap.overload2.requirements)

`Body::value_type` and `Fields`
are **Swappable**.