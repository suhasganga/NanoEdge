##### [ref (1 of 4 overloads)](overload1.html "ref (1 of 4 overloads)")

Create a [`buffer_ref`](../boost__beast__buffer_ref.html "buffer_ref") for [`basic_flat_buffer`](../boost__beast__basic_flat_buffer.html "basic_flat_buffer").

###### [Synopsis](overload1.html#beast.ref.boost__beast__ref.overload1.synopsis)

Defined in header `<boost/beast/core/buffer_ref.hpp>`

```programlisting
template<
    class Allocator>
buffer_ref< basic_flat_buffer< Allocator > >
ref(
    basic_flat_buffer< Allocator >& buf);
```