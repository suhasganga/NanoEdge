##### [basic\_stream::basic\_stream](basic_stream.html "basic_stream::basic_stream")

Constructor.

```programlisting
template<
    class... Args>
explicit
basic_stream(
    Args&&... args);
  » more...

template<
    class RatePolicy_,
    class... Args>
explicit
basic_stream(
    RatePolicy_&& policy,
    Args&&... args);
  » more...
```

Move constructor.

```programlisting
basic_stream(
    basic_stream&& other);
  » more...
```