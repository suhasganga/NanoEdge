###### [basic\_flat\_buffer::basic\_flat\_buffer (10 of 10 overloads)](overload10.html "basic_flat_buffer::basic_flat_buffer (10 of 10 overloads)")

Copy Constructor.

###### [Synopsis](overload10.html#beast.ref.boost__beast__basic_flat_buffer.basic_flat_buffer.overload10.synopsis)

```programlisting
template<
    class OtherAlloc>
basic_flat_buffer(
    basic_flat_buffer< OtherAlloc > const& other,
    Allocator const& alloc);
```

###### [Description](overload10.html#beast.ref.boost__beast__basic_flat_buffer.basic_flat_buffer.overload10.description)

This container is constructed with the contents of `other`
using copy semantics. The maximum size will be the same as the copied
object.

###### [Parameters](overload10.html#beast.ref.boost__beast__basic_flat_buffer.basic_flat_buffer.overload10.parameters)

| Name | Description |
| --- | --- |
| `other` | The object to copy from. |
| `alloc` | The allocator to use for the object. |

###### [Exceptions](overload10.html#beast.ref.boost__beast__basic_flat_buffer.basic_flat_buffer.overload10.exceptions)

| Type | Thrown On |
| --- | --- |
| `std::length_error` | if `other.size()` exceeds the maximum allocation size of `alloc`. |