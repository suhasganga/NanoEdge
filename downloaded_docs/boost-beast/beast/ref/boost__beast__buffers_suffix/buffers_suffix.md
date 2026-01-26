##### [buffers\_suffix::buffers\_suffix](buffers_suffix.html "buffers_suffix::buffers_suffix")

Constructor.

```programlisting
buffers_suffix();
  » more...

explicit
buffers_suffix(
    BufferSequence const& buffers);
  » more...

template<
    class... Args>
explicit
buffers_suffix(
    boost::in_place_init_t,
    Args&&... args);
  » more...
```

Copy Constructor.

```programlisting
buffers_suffix(
    buffers_suffix const&);
  » more...
```