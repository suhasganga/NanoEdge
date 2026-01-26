###### [basic\_multi\_buffer::basic\_multi\_buffer (8 of 10 overloads)](overload8.html "basic_multi_buffer::basic_multi_buffer (8 of 10 overloads)")

Copy Constructor.

###### [Synopsis](overload8.html#beast.ref.boost__beast__basic_multi_buffer.basic_multi_buffer.overload8.synopsis)

```programlisting
basic_multi_buffer(
    basic_multi_buffer const& other,
    Allocator const& alloc);
```

###### [Description](overload8.html#beast.ref.boost__beast__basic_multi_buffer.basic_multi_buffer.overload8.description)

This container is constructed with the contents of `other`
using copy semantics and the specified allocator. The maximum size will
be the same as the copied object.

###### [Parameters](overload8.html#beast.ref.boost__beast__basic_multi_buffer.basic_multi_buffer.overload8.parameters)

| Name | Description |
| --- | --- |
| `other` | The object to copy from. |
| `alloc` | The allocator to use for the object. |

###### [Exceptions](overload8.html#beast.ref.boost__beast__basic_multi_buffer.basic_multi_buffer.overload8.exceptions)

| Type | Thrown On |
| --- | --- |
| `std::length_error` | if `other.size()` exceeds the maximum allocation size of `alloc`. |