###### [basic\_flat\_buffer::operator= (3 of 3 overloads)](overload3.html "basic_flat_buffer::operator= (3 of 3 overloads)")

Copy assignment.

###### [Synopsis](overload3.html#beast.ref.boost__beast__basic_flat_buffer.operator_eq_.overload3.synopsis)

```programlisting
template<
    class OtherAlloc>
basic_flat_buffer&
operator=(
    basic_flat_buffer< OtherAlloc > const& other);
```

###### [Description](overload3.html#beast.ref.boost__beast__basic_flat_buffer.operator_eq_.overload3.description)

The container is assigned with the contents of `other`
using copy semantics. The maximum size will be the same as the copied
object.

After the copy, `this` will
have zero writable bytes.

###### [Parameters](overload3.html#beast.ref.boost__beast__basic_flat_buffer.operator_eq_.overload3.parameters)

| Name | Description |
| --- | --- |
| `other` | The object to copy from. |

###### [Exceptions](overload3.html#beast.ref.boost__beast__basic_flat_buffer.operator_eq_.overload3.exceptions)

| Type | Thrown On |
| --- | --- |
| `std::length_error` | if `other.size()` exceeds the maximum allocation size of the allocator. |