##### [stable\_async\_base::~stable\_async\_base](_dtor_stable_async_base.html "stable_async_base::~stable_async_base")

Destructor.

###### [Synopsis](_dtor_stable_async_base.html#beast.ref.boost__beast__stable_async_base._dtor_stable_async_base.synopsis)

```programlisting
~stable_async_base();
```

###### [Description](_dtor_stable_async_base.html#beast.ref.boost__beast__stable_async_base._dtor_stable_async_base.description)

If the completion handler was not invoked, then any state objects allocated
with [`allocate_stable`](allocate_stable.html "stable_async_base::allocate_stable") will be destroyed
here.