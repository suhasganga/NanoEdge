##### [stable\_async\_base::stable\_async\_base](stable_async_base.html "stable_async_base::stable_async_base")

Constructor.

```programlisting
template<
    class Handler>
stable_async_base(
    Handler&& handler,
    Executor1 const& ex1,
    Allocator const& alloc = Allocator());
  » more...
```

Move Constructor.

```programlisting
stable_async_base(
    stable_async_base&& other);
  » more...
```