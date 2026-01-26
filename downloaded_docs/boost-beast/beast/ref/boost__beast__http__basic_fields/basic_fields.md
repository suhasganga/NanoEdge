##### [http::basic\_fields::basic\_fields](basic_fields.html "http::basic_fields::basic_fields")

Constructor.

```programlisting
basic_fields();
  » more...

explicit
basic_fields(
    Allocator const& alloc);
  » more...
```

Move constructor.

```programlisting
basic_fields(
    basic_fields&&);
  » more...

basic_fields(
    basic_fields&&,
    Allocator const& alloc);
  » more...
```

Copy constructor.

```programlisting
basic_fields(
    basic_fields const&);
  » more...

basic_fields(
    basic_fields const&,
    Allocator const& alloc);
  » more...

template<
    class OtherAlloc>
basic_fields(
    basic_fields< OtherAlloc > const&);
  » more...

template<
    class OtherAlloc>
basic_fields(
    basic_fields< OtherAlloc > const&,
    Allocator const& alloc);
  » more...
```