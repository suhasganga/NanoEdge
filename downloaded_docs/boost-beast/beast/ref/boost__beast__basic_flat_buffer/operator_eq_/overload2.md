###### [basic\_flat\_buffer::operator= (2 of 3 overloads)](overload2.html "basic_flat_buffer::operator= (2 of 3 overloads)")

Copy Assignment.

###### [Synopsis](overload2.html#beast.ref.boost__beast__basic_flat_buffer.operator_eq_.overload2.synopsis)

```programlisting
basic_flat_buffer&
operator=(
    basic_flat_buffer const& other);
```

###### [Description](overload2.html#beast.ref.boost__beast__basic_flat_buffer.operator_eq_.overload2.description)

The container is assigned with the contents of `other`
using copy semantics. The maximum size will be the same as the copied
object.

After the copy, `this` will
have zero writable bytes.

###### [Parameters](overload2.html#beast.ref.boost__beast__basic_flat_buffer.operator_eq_.overload2.parameters)

| Name | Description |
| --- | --- |
| `other` | The object to copy from. |

###### [Exceptions](overload2.html#beast.ref.boost__beast__basic_flat_buffer.operator_eq_.overload2.exceptions)

| Type | Thrown On |
| --- | --- |
| `std::length_error` | if `other.size()` exceeds the maximum allocation size of the allocator. |