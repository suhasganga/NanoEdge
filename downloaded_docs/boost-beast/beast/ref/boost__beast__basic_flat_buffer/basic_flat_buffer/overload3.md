###### [basic\_flat\_buffer::basic\_flat\_buffer (3 of 10 overloads)](overload3.html "basic_flat_buffer::basic_flat_buffer (3 of 10 overloads)")

Constructor.

###### [Synopsis](overload3.html#beast.ref.boost__beast__basic_flat_buffer.basic_flat_buffer.overload3.synopsis)

```programlisting
basic_flat_buffer(
    Allocator const& alloc);
```

###### [Description](overload3.html#beast.ref.boost__beast__basic_flat_buffer.basic_flat_buffer.overload3.description)

After construction, [`capacity`](../capacity.html "basic_flat_buffer::capacity") will return zero, and
[`max_size`](../max_size.html "basic_flat_buffer::max_size") will return the largest
value which may be passed to the allocator's `allocate`
function.

###### [Parameters](overload3.html#beast.ref.boost__beast__basic_flat_buffer.basic_flat_buffer.overload3.parameters)

| Name | Description |
| --- | --- |
| `alloc` | The allocator to use for the object. |

###### [Exception Safety](overload3.html#beast.ref.boost__beast__basic_flat_buffer.basic_flat_buffer.overload3.exception_safety)

No-throw guarantee.