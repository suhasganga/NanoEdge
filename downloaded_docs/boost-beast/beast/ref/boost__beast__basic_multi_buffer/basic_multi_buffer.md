##### [basic\_multi\_buffer::basic\_multi\_buffer](basic_multi_buffer.html "basic_multi_buffer::basic_multi_buffer")

Constructor.

```programlisting
basic_multi_buffer();
  » more...

explicit
basic_multi_buffer(
    std::size_t limit);
  » more...

explicit
basic_multi_buffer(
    Allocator const& alloc);
  » more...

basic_multi_buffer(
    std::size_t limit,
    Allocator const& alloc);
  » more...
```

Move Constructor.

```programlisting
basic_multi_buffer(
    basic_multi_buffer&& other);
  » more...

basic_multi_buffer(
    basic_multi_buffer&& other,
    Allocator const& alloc);
  » more...
```

Copy Constructor.

```programlisting
basic_multi_buffer(
    basic_multi_buffer const& other);
  » more...

basic_multi_buffer(
    basic_multi_buffer const& other,
    Allocator const& alloc);
  » more...

template<
    class OtherAlloc>
basic_multi_buffer(
    basic_multi_buffer< OtherAlloc > const& other);
  » more...

template<
    class OtherAlloc>
basic_multi_buffer(
    basic_multi_buffer< OtherAlloc > const& other,
    allocator_type const& alloc);
  » more...
```