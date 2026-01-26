#### [executor\_type](boost__beast__executor_type.html "executor_type")

A trait to determine the return type of get\_executor.

##### [Synopsis](boost__beast__executor_type.html#beast.ref.boost__beast__executor_type.synopsis)

Defined in header `<boost/beast/core/stream_traits.hpp>`

```programlisting
template<
    class T>
using executor_type = see-below;
```

##### [Description](boost__beast__executor_type.html#beast.ref.boost__beast__executor_type.description)

This type alias will be the type of values returned by by calling member
`get_exector` on an object
of type `T&`.

##### [Parameters](boost__beast__executor_type.html#beast.ref.boost__beast__executor_type.parameters)

| Name | Description |
| --- | --- |
| `T` | The type to query |

##### [Return Value](boost__beast__executor_type.html#beast.ref.boost__beast__executor_type.return_value)

The type of values returned from `get_executor`.