##### [ref (4 of 4 overloads)](overload4.html "ref (4 of 4 overloads)")

Create a [`buffer_ref`](../boost__beast__buffer_ref.html "buffer_ref") for [`static_buffer`](../boost__beast__static_buffer.html "static_buffer").

###### [Synopsis](overload4.html#beast.ref.boost__beast__ref.overload4.synopsis)

Defined in header `<boost/beast/core/buffer_ref.hpp>`

```programlisting
template<
    std::size_t N>
buffer_ref< static_buffer< N > >
ref(
    static_buffer< N >& buf);
```