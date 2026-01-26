###### [basic\_multi\_buffer::basic\_multi\_buffer (6 of 10 overloads)](overload6.html "basic_multi_buffer::basic_multi_buffer (6 of 10 overloads)")

Move Constructor.

###### [Synopsis](overload6.html#beast.ref.boost__beast__basic_multi_buffer.basic_multi_buffer.overload6.synopsis)

```programlisting
basic_multi_buffer(
    basic_multi_buffer&& other,
    Allocator const& alloc);
```

###### [Description](overload6.html#beast.ref.boost__beast__basic_multi_buffer.basic_multi_buffer.overload6.description)

Using `alloc` as the allocator
for the new container, the contents of `other`
are moved. If `alloc != other.get_allocator()`, this results in a copy. The maximum
size will be the same as the moved-from object.

Buffer sequences previously obtained from `other`
using [`data`](../data.html "basic_multi_buffer::data") or [`prepare`](../prepare.html "basic_multi_buffer::prepare") become invalid after
the move.

###### [Parameters](overload6.html#beast.ref.boost__beast__basic_multi_buffer.basic_multi_buffer.overload6.parameters)

| Name | Description |
| --- | --- |
| `other` | The object to move from. After the move, the moved-from object will have zero capacity, zero readable bytes, and zero writable bytes. |
| `alloc` | The allocator to use for the object. |

###### [Exceptions](overload6.html#beast.ref.boost__beast__basic_multi_buffer.basic_multi_buffer.overload6.exceptions)

| Type | Thrown On |
| --- | --- |
| `std::length_error` | if `other.size()` exceeds the maximum allocation size of `alloc`. |