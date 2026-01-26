##### [http::swap (1 of 2 overloads)](overload1.html "http::swap (1 of 2 overloads)")

Swap two header objects.

###### [Synopsis](overload1.html#beast.ref.boost__beast__http__swap.overload1.synopsis)

Defined in header `<boost/beast/http/message.hpp>`

```programlisting
template<
    bool isRequest,
    class Fields>
void
swap(
    header< isRequest, Fields >& m1,
    header< isRequest, Fields >& m2);
```

###### [Requirements](overload1.html#beast.ref.boost__beast__http__swap.overload1.requirements)

`Fields` is **Swappable**.