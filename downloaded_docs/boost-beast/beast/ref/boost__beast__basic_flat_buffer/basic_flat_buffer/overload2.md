###### [basic\_flat\_buffer::basic\_flat\_buffer (2 of 10 overloads)](overload2.html "basic_flat_buffer::basic_flat_buffer (2 of 10 overloads)")

Constructor.

###### [Synopsis](overload2.html#beast.ref.boost__beast__basic_flat_buffer.basic_flat_buffer.overload2.synopsis)

```programlisting
basic_flat_buffer(
    std::size_t limit);
```

###### [Description](overload2.html#beast.ref.boost__beast__basic_flat_buffer.basic_flat_buffer.overload2.description)

After construction, [`capacity`](../capacity.html "basic_flat_buffer::capacity") will return zero, and
[`max_size`](../max_size.html "basic_flat_buffer::max_size") will return the specified
value of `limit`.

###### [Parameters](overload2.html#beast.ref.boost__beast__basic_flat_buffer.basic_flat_buffer.overload2.parameters)

| Name | Description |
| --- | --- |
| `limit` | The desired maximum size. |