##### [ref (3 of 4 overloads)](overload3.html "ref (3 of 4 overloads)")

Create a [`buffer_ref`](../boost__beast__buffer_ref.html "buffer_ref") for [`basic_multi_buffer`](../boost__beast__basic_multi_buffer.html "basic_multi_buffer").

###### [Synopsis](overload3.html#beast.ref.boost__beast__ref.overload3.synopsis)

Defined in header `<boost/beast/core/buffer_ref.hpp>`

```programlisting
template<
    class Allocator>
buffer_ref< basic_multi_buffer< Allocator > >
ref(
    basic_multi_buffer< Allocator >& buf);
```