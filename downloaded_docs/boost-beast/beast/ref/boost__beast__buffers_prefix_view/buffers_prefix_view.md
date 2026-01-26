##### [buffers\_prefix\_view::buffers\_prefix\_view](buffers_prefix_view.html "buffers_prefix_view::buffers_prefix_view")

Copy Constructor.

```programlisting
buffers_prefix_view(
    buffers_prefix_view const&);
  » more...
```

Construct a buffer sequence prefix.

```programlisting
buffers_prefix_view(
    std::size_t size,
    BufferSequence const& buffers);
  » more...
```

Construct a buffer sequence prefix in-place.

```programlisting
template<
    class... Args>
buffers_prefix_view(
    std::size_t size,
    boost::in_place_init_t,
    Args&&... args);
  » more...
```