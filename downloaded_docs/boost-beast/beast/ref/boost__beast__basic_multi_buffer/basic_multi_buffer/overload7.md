###### [basic\_multi\_buffer::basic\_multi\_buffer (7 of 10 overloads)](overload7.html "basic_multi_buffer::basic_multi_buffer (7 of 10 overloads)")

Copy Constructor.

###### [Synopsis](overload7.html#beast.ref.boost__beast__basic_multi_buffer.basic_multi_buffer.overload7.synopsis)

```programlisting
basic_multi_buffer(
    basic_multi_buffer const& other);
```

###### [Description](overload7.html#beast.ref.boost__beast__basic_multi_buffer.basic_multi_buffer.overload7.description)

This container is constructed with the contents of `other`
using copy semantics. The maximum size will be the same as the copied
object.

###### [Parameters](overload7.html#beast.ref.boost__beast__basic_multi_buffer.basic_multi_buffer.overload7.parameters)

| Name | Description |
| --- | --- |
| `other` | The object to copy from. |

###### [Exceptions](overload7.html#beast.ref.boost__beast__basic_multi_buffer.basic_multi_buffer.overload7.exceptions)

| Type | Thrown On |
| --- | --- |
| `std::length_error` | if `other.size()` exceeds the maximum allocation size of the allocator. |