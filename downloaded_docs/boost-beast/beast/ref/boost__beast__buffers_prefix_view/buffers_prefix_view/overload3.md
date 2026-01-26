###### [buffers\_prefix\_view::buffers\_prefix\_view (3 of 3 overloads)](overload3.html "buffers_prefix_view::buffers_prefix_view (3 of 3 overloads)")

Construct a buffer sequence prefix in-place.

###### [Synopsis](overload3.html#beast.ref.boost__beast__buffers_prefix_view.buffers_prefix_view.overload3.synopsis)

```programlisting
template<
    class... Args>
buffers_prefix_view(
    std::size_t size,
    boost::in_place_init_t,
    Args&&... args);
```

###### [Parameters](overload3.html#beast.ref.boost__beast__buffers_prefix_view.buffers_prefix_view.overload3.parameters)

| Name | Description |
| --- | --- |
| `size` | The maximum number of bytes in the prefix. If this is larger than the size of passed buffers, the resulting sequence will represent the entire input sequence. |
| `args` | Arguments forwarded to the contained buffer's constructor. |