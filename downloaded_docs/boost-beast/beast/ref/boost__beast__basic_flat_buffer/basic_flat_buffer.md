##### [basic\_flat\_buffer::basic\_flat\_buffer](basic_flat_buffer.html "basic_flat_buffer::basic_flat_buffer")

Constructor.

```programlisting
basic_flat_buffer();
  » more...

explicit
basic_flat_buffer(
    std::size_t limit);
  » more...

explicit
basic_flat_buffer(
    Allocator const& alloc);
  » more...

basic_flat_buffer(
    std::size_t limit,
    Allocator const& alloc);
  » more...
```

Move Constructor.

```programlisting
basic_flat_buffer(
    basic_flat_buffer&& other);
  » more...

basic_flat_buffer(
    basic_flat_buffer&& other,
    Allocator const& alloc);
  » more...
```

Copy Constructor.

```programlisting
basic_flat_buffer(
    basic_flat_buffer const& other);
  » more...

basic_flat_buffer(
    basic_flat_buffer const& other,
    Allocator const& alloc);
  » more...

template<
    class OtherAlloc>
basic_flat_buffer(
    basic_flat_buffer< OtherAlloc > const& other);
  » more...

template<
    class OtherAlloc>
basic_flat_buffer(
    basic_flat_buffer< OtherAlloc > const& other,
    Allocator const& alloc);
  » more...
```