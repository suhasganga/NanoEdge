###### [buffers\_prefix\_view::buffers\_prefix\_view (2 of 3 overloads)](overload2.html "buffers_prefix_view::buffers_prefix_view (2 of 3 overloads)")

Construct a buffer sequence prefix.

###### [Synopsis](overload2.html#beast.ref.boost__beast__buffers_prefix_view.buffers_prefix_view.overload2.synopsis)

```programlisting
buffers_prefix_view(
    std::size_t size,
    BufferSequence const& buffers);
```

###### [Parameters](overload2.html#beast.ref.boost__beast__buffers_prefix_view.buffers_prefix_view.overload2.parameters)

| Name | Description |
| --- | --- |
| `size` | The maximum number of bytes in the prefix. If this is larger than the size of passed buffers, the resulting sequence will represent the entire input sequence. |
| `buffers` | The buffer sequence to adapt. A copy of the sequence will be made, but ownership of the underlying memory is not transferred. The copy is maintained for the lifetime of the view. |