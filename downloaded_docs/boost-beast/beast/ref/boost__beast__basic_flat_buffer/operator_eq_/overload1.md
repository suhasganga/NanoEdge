###### [basic\_flat\_buffer::operator= (1 of 3 overloads)](overload1.html "basic_flat_buffer::operator= (1 of 3 overloads)")

Move Assignment.

###### [Synopsis](overload1.html#beast.ref.boost__beast__basic_flat_buffer.operator_eq_.overload1.synopsis)

```programlisting
basic_flat_buffer&
operator=(
    basic_flat_buffer&& other);
```

###### [Description](overload1.html#beast.ref.boost__beast__basic_flat_buffer.operator_eq_.overload1.description)

The container is assigned with the contents of `other`
using move semantics. The maximum size will be the same as the moved-from
object.

Buffer sequences previously obtained from `other`
using [`data`](../data.html "basic_flat_buffer::data") or [`prepare`](../prepare.html "basic_flat_buffer::prepare") remain valid after the
move.

###### [Parameters](overload1.html#beast.ref.boost__beast__basic_flat_buffer.operator_eq_.overload1.parameters)

| Name | Description |
| --- | --- |
| `other` | The object to move from. After the move, the moved-from object will have zero capacity, zero readable bytes, and zero writable bytes. |

###### [Exception Safety](overload1.html#beast.ref.boost__beast__basic_flat_buffer.operator_eq_.overload1.exception_safety)

No-throw guarantee.