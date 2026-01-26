###### [basic\_multi\_buffer::basic\_multi\_buffer (1 of 10 overloads)](overload1.html "basic_multi_buffer::basic_multi_buffer (1 of 10 overloads)")

Constructor.

###### [Synopsis](overload1.html#beast.ref.boost__beast__basic_multi_buffer.basic_multi_buffer.overload1.synopsis)

```programlisting
basic_multi_buffer();
```

###### [Description](overload1.html#beast.ref.boost__beast__basic_multi_buffer.basic_multi_buffer.overload1.description)

After construction, [`capacity`](../capacity.html "basic_multi_buffer::capacity") will return zero, and
[`max_size`](../max_size.html "basic_multi_buffer::max_size") will return the largest
value which may be passed to the allocator's `allocate`
function.