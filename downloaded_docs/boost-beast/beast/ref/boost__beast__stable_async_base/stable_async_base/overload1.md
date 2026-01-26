###### [stable\_async\_base::stable\_async\_base (1 of 2 overloads)](overload1.html "stable_async_base::stable_async_base (1 of 2 overloads)")

Constructor.

###### [Synopsis](overload1.html#beast.ref.boost__beast__stable_async_base.stable_async_base.overload1.synopsis)

```programlisting
template<
    class Handler>
stable_async_base(
    Handler&& handler,
    Executor1 const& ex1,
    Allocator const& alloc = Allocator());
```

###### [Parameters](overload1.html#beast.ref.boost__beast__stable_async_base.stable_async_base.overload1.parameters)

| Name | Description |
| --- | --- |
| `handler` | The final completion handler. The type of this object must meet the requirements of *CompletionHandler*. The implementation takes ownership of the handler by performing a decay-copy. |
| `ex1` | The executor associated with the implied I/O object target of the operation. The implementation shall maintain an executor work guard for the lifetime of the operation, or until the final completion handler is invoked, whichever is shorter. |
| `alloc` | The allocator to be associated with objects derived from this class. If `Allocator` is default-constructible, this parameter is optional and may be omitted. |