##### [buffers\_adaptor::buffers\_adaptor](buffers_adaptor.html "buffers_adaptor::buffers_adaptor")

Construct a buffers adaptor.

```programlisting
explicit
buffers_adaptor(
    MutableBufferSequence const& buffers);
  » more...
```

Constructor.

```programlisting
template<
    class... Args>
explicit
buffers_adaptor(
    boost::in_place_init_t,
    Args&&... args);
  » more...
```

Copy Constructor.

```programlisting
buffers_adaptor(
    buffers_adaptor const& other);
  » more...
```