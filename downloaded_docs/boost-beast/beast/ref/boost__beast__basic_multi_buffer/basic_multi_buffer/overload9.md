###### [basic\_multi\_buffer::basic\_multi\_buffer (9 of 10 overloads)](overload9.html "basic_multi_buffer::basic_multi_buffer (9 of 10 overloads)")

Copy Constructor.

###### [Synopsis](overload9.html#beast.ref.boost__beast__basic_multi_buffer.basic_multi_buffer.overload9.synopsis)

```programlisting
template<
    class OtherAlloc>
basic_multi_buffer(
    basic_multi_buffer< OtherAlloc > const& other);
```

###### [Description](overload9.html#beast.ref.boost__beast__basic_multi_buffer.basic_multi_buffer.overload9.description)

This container is constructed with the contents of `other`
using copy semantics. The maximum size will be the same as the copied
object.

###### [Parameters](overload9.html#beast.ref.boost__beast__basic_multi_buffer.basic_multi_buffer.overload9.parameters)

| Name | Description |
| --- | --- |
| `other` | The object to copy from. |

###### [Exceptions](overload9.html#beast.ref.boost__beast__basic_multi_buffer.basic_multi_buffer.overload9.exceptions)

| Type | Thrown On |
| --- | --- |
| `std::length_error` | if `other.size()` exceeds the maximum allocation size of the allocator. |