###### [basic\_flat\_buffer::max\_size (1 of 2 overloads)](overload1.html "basic_flat_buffer::max_size (1 of 2 overloads)")

Set the maximum allowed capacity.

###### [Synopsis](overload1.html#beast.ref.boost__beast__basic_flat_buffer.max_size.overload1.synopsis)

```programlisting
void
max_size(
    std::size_t n);
```

###### [Description](overload1.html#beast.ref.boost__beast__basic_flat_buffer.max_size.overload1.description)

This function changes the currently configured upper limit on capacity
to the specified value.

###### [Parameters](overload1.html#beast.ref.boost__beast__basic_flat_buffer.max_size.overload1.parameters)

| Name | Description |
| --- | --- |
| `n` | The maximum number of bytes ever allowed for capacity. |

###### [Exception Safety](overload1.html#beast.ref.boost__beast__basic_flat_buffer.max_size.overload1.exception_safety)

No-throw guarantee.