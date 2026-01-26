#### [ref](boost__beast__ref.html "ref")

Create a [`buffer_ref`](boost__beast__buffer_ref.html "buffer_ref") for [`basic_flat_buffer`](boost__beast__basic_flat_buffer.html "basic_flat_buffer").

```programlisting
template<
    class Allocator>
buffer_ref< basic_flat_buffer< Allocator > >
ref(
    basic_flat_buffer< Allocator >& buf);
  » more...
```

Create a [`buffer_ref`](boost__beast__buffer_ref.html "buffer_ref") for [`flat_static_buffer`](boost__beast__flat_static_buffer.html "flat_static_buffer").

```programlisting
template<
    std::size_t N>
buffer_ref< flat_static_buffer< N > >
ref(
    flat_static_buffer< N >& buf);
  » more...
```

Create a [`buffer_ref`](boost__beast__buffer_ref.html "buffer_ref") for [`basic_multi_buffer`](boost__beast__basic_multi_buffer.html "basic_multi_buffer").

```programlisting
template<
    class Allocator>
buffer_ref< basic_multi_buffer< Allocator > >
ref(
    basic_multi_buffer< Allocator >& buf);
  » more...
```

Create a [`buffer_ref`](boost__beast__buffer_ref.html "buffer_ref") for [`static_buffer`](boost__beast__static_buffer.html "static_buffer").

```programlisting
template<
    std::size_t N>
buffer_ref< static_buffer< N > >
ref(
    static_buffer< N >& buf);
  » more...
```