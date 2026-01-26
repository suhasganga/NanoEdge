#### [lowest\_layer\_type](boost__beast__lowest_layer_type.html "lowest_layer_type")

A trait to determine the lowest layer type of a stack of stream layers.

##### [Synopsis](boost__beast__lowest_layer_type.html#beast.ref.boost__beast__lowest_layer_type.synopsis)

Defined in header `<boost/beast/core/stream_traits.hpp>`

```programlisting
template<
    class T>
using lowest_layer_type = see-below;
```

##### [Description](boost__beast__lowest_layer_type.html#beast.ref.boost__beast__lowest_layer_type.description)

If `t.next_layer()`
is well-defined for an object `t`
of type `T`, then [`lowest_layer_type`](boost__beast__lowest_layer_type.html "lowest_layer_type")<T> will
be an alias for [`lowest_layer_type`](boost__beast__lowest_layer_type.html "lowest_layer_type")<decltype(t.next\_layer())>
, otherwise it will be the type `std::remove_reference<T>`.

##### [Parameters](boost__beast__lowest_layer_type.html#beast.ref.boost__beast__lowest_layer_type.parameters)

| Name | Description |
| --- | --- |
| `T` | The type to determine the lowest layer type of. |

##### [Return Value](boost__beast__lowest_layer_type.html#beast.ref.boost__beast__lowest_layer_type.return_value)

The type of the lowest layer.