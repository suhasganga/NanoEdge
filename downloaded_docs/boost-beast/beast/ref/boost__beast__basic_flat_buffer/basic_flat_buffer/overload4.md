###### [basic\_flat\_buffer::basic\_flat\_buffer (4 of 10 overloads)](overload4.html "basic_flat_buffer::basic_flat_buffer (4 of 10 overloads)")

Constructor.

###### [Synopsis](overload4.html#beast.ref.boost__beast__basic_flat_buffer.basic_flat_buffer.overload4.synopsis)

```programlisting
basic_flat_buffer(
    std::size_t limit,
    Allocator const& alloc);
```

###### [Description](overload4.html#beast.ref.boost__beast__basic_flat_buffer.basic_flat_buffer.overload4.description)

After construction, [`capacity`](../capacity.html "basic_flat_buffer::capacity") will return zero, and
[`max_size`](../max_size.html "basic_flat_buffer::max_size") will return the specified
value of `limit`.

###### [Parameters](overload4.html#beast.ref.boost__beast__basic_flat_buffer.basic_flat_buffer.overload4.parameters)

| Name | Description |
| --- | --- |
| `limit` | The desired maximum size. |
| `alloc` | The allocator to use for the object. |

###### [Exception Safety](overload4.html#beast.ref.boost__beast__basic_flat_buffer.basic_flat_buffer.overload4.exception_safety)

No-throw guarantee.