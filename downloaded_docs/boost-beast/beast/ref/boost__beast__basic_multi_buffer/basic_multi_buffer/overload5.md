###### [basic\_multi\_buffer::basic\_multi\_buffer (5 of 10 overloads)](overload5.html "basic_multi_buffer::basic_multi_buffer (5 of 10 overloads)")

Move Constructor.

###### [Synopsis](overload5.html#beast.ref.boost__beast__basic_multi_buffer.basic_multi_buffer.overload5.synopsis)

```programlisting
basic_multi_buffer(
    basic_multi_buffer&& other);
```

###### [Description](overload5.html#beast.ref.boost__beast__basic_multi_buffer.basic_multi_buffer.overload5.description)

The container is constructed with the contents of `other`
using move semantics. The maximum size will be the same as the moved-from
object.

Buffer sequences previously obtained from `other`
using [`data`](../data.html "basic_multi_buffer::data") or [`prepare`](../prepare.html "basic_multi_buffer::prepare") remain valid after the
move.

###### [Parameters](overload5.html#beast.ref.boost__beast__basic_multi_buffer.basic_multi_buffer.overload5.parameters)

| Name | Description |
| --- | --- |
| `other` | The object to move from. After the move, the moved-from object will have zero capacity, zero readable bytes, and zero writable bytes. |

###### [Exception Safety](overload5.html#beast.ref.boost__beast__basic_multi_buffer.basic_multi_buffer.overload5.exception_safety)

No-throw guarantee.