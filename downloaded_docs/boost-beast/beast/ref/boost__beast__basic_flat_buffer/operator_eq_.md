##### [basic\_flat\_buffer::operator=](operator_eq_.html "basic_flat_buffer::operator=")

Move Assignment.

```programlisting
basic_flat_buffer&
operator=(
    basic_flat_buffer&& other);
  » more...
```

Copy Assignment.

```programlisting
basic_flat_buffer&
operator=(
    basic_flat_buffer const& other);
  » more...
```

Copy assignment.

```programlisting
template<
    class OtherAlloc>
basic_flat_buffer&
operator=(
    basic_flat_buffer< OtherAlloc > const& other);
  » more...
```