#### [allocate\_stable](boost__beast__allocate_stable.html "allocate_stable")

Allocate a temporary object to hold stable asynchronous operation state.

##### [Synopsis](boost__beast__allocate_stable.html#beast.ref.boost__beast__allocate_stable.synopsis)

Defined in header `<boost/beast/core/async_base.hpp>`

```programlisting
template<
    class State,
    class Handler,
    class Executor1,
    class Allocator,
    class... Args>
State&
allocate_stable(
    stable_async_base< Handler, Executor1, Allocator >& base,
    Args&&... args);
```

##### [Description](boost__beast__allocate_stable.html#beast.ref.boost__beast__allocate_stable.description)

The object will be destroyed just before the completion handler is invoked,
or when the base is destroyed.

##### [Template Parameters](boost__beast__allocate_stable.html#beast.ref.boost__beast__allocate_stable.template_parameters)

| Type | Description |
| --- | --- |
| `State` | The type of object to allocate. |

##### [Parameters](boost__beast__allocate_stable.html#beast.ref.boost__beast__allocate_stable.parameters)

| Name | Description |
| --- | --- |
| `base` | The helper to allocate from. |
| `args` | An optional list of parameters to forward to the constructor of the object being allocated. |

##### [See Also](boost__beast__allocate_stable.html#beast.ref.boost__beast__allocate_stable.see_also)

[`stable_async_base`](boost__beast__stable_async_base.html "stable_async_base")