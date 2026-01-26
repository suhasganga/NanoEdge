##### [async\_base::async\_base](async_base.html "async_base::async_base")

Constructor.

```programlisting
template<
    class Handler>
async_base(
    Handler&& handler,
    Executor1 const& ex1,
    Allocator const& alloc = Allocator());
  » more...
```

Move Constructor.

```programlisting
async_base(
    async_base&& other);
  » more...
```

```programlisting
async_base(
    async_base const&) = delete;
  » more...
```