##### [basic\_multi\_buffer::operator=](operator_eq_.html "basic_multi_buffer::operator=")

Move Assignment.

```programlisting
basic_multi_buffer&
operator=(
    basic_multi_buffer&& other);
  » more...
```

Copy Assignment.

```programlisting
basic_multi_buffer&
operator=(
    basic_multi_buffer const& other);
  » more...

template<
    class OtherAlloc>
basic_multi_buffer&
operator=(
    basic_multi_buffer< OtherAlloc > const& other);
  » more...
```