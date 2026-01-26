###### [basic\_flat\_buffer::basic\_flat\_buffer (5 of 10 overloads)](overload5.html "basic_flat_buffer::basic_flat_buffer (5 of 10 overloads)")

Move Constructor.

###### [Synopsis](overload5.html#beast.ref.boost__beast__basic_flat_buffer.basic_flat_buffer.overload5.synopsis)

```programlisting
basic_flat_buffer(
    basic_flat_buffer&& other);
```

###### [Description](overload5.html#beast.ref.boost__beast__basic_flat_buffer.basic_flat_buffer.overload5.description)

The container is constructed with the contents of `other`
using move semantics. The maximum size will be the same as the moved-from
object.

Buffer sequences previously obtained from `other`
using [`data`](../data.html "basic_flat_buffer::data") or [`prepare`](../prepare.html "basic_flat_buffer::prepare") remain valid after the
move.

###### [Parameters](overload5.html#beast.ref.boost__beast__basic_flat_buffer.basic_flat_buffer.overload5.parameters)

| Name | Description |
| --- | --- |
| `other` | The object to move from. After the move, the moved-from object will have zero capacity, zero readable bytes, and zero writable bytes. |

###### [Exception Safety](overload5.html#beast.ref.boost__beast__basic_flat_buffer.basic_flat_buffer.overload5.exception_safety)

No-throw guarantee.