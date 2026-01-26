##### [stable\_async\_base::allocate\_stable](allocate_stable.html "stable_async_base::allocate_stable")

Allocate a temporary object to hold operation state.

###### [Synopsis](allocate_stable.html#beast.ref.boost__beast__stable_async_base.allocate_stable.synopsis)

Defined in header `<boost/beast/core/async_base.hpp>`

```programlisting
template<
    class State,
    class Handler,
    class Executor1_,
    class Allocator_,
    class... Args>
State&
allocate_stable(
    stable_async_base< Handler_, Executor1_, Allocator_ >& base,
    Args&&... args);
```

###### [Description](allocate_stable.html#beast.ref.boost__beast__stable_async_base.allocate_stable.description)

The object will be destroyed just before the completion handler is invoked,
or when the operation base is destroyed.