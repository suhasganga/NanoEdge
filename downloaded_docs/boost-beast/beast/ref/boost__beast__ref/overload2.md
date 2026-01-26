##### [ref (2 of 4 overloads)](overload2.html "ref (2 of 4 overloads)")

Create a [`buffer_ref`](../boost__beast__buffer_ref.html "buffer_ref") for [`flat_static_buffer`](../boost__beast__flat_static_buffer.html "flat_static_buffer").

###### [Synopsis](overload2.html#beast.ref.boost__beast__ref.overload2.synopsis)

Defined in header `<boost/beast/core/buffer_ref.hpp>`

```programlisting
template<
    std::size_t N>
buffer_ref< flat_static_buffer< N > >
ref(
    flat_static_buffer< N >& buf);
```