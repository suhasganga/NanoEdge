###### [basic\_flat\_buffer::basic\_flat\_buffer (1 of 10 overloads)](overload1.html "basic_flat_buffer::basic_flat_buffer (1 of 10 overloads)")

Constructor.

###### [Synopsis](overload1.html#beast.ref.boost__beast__basic_flat_buffer.basic_flat_buffer.overload1.synopsis)

```programlisting
basic_flat_buffer();
```

###### [Description](overload1.html#beast.ref.boost__beast__basic_flat_buffer.basic_flat_buffer.overload1.description)

After construction, [`capacity`](../capacity.html "basic_flat_buffer::capacity") will return zero, and
[`max_size`](../max_size.html "basic_flat_buffer::max_size") will return the largest
value which may be passed to the allocator's `allocate`
function.