##### [stable\_async\_base::complete\_now](complete_now.html "stable_async_base::complete_now")

(Inherited from [`async_base`](../boost__beast__async_base.html "async_base"))

Invoke the final completion handler.

###### [Synopsis](complete_now.html#beast.ref.boost__beast__stable_async_base.complete_now.synopsis)

```programlisting
template<
    class... Args>
void
complete_now(
    Args&&... args);
```

###### [Description](complete_now.html#beast.ref.boost__beast__stable_async_base.complete_now.description)

This invokes the final completion handler with the specified arguments
forwarded. It is undefined to call either of [`boost::beast::async_base::complete`](complete.html "stable_async_base::complete") or [`boost::beast::async_base::complete_now`](complete_now.html "stable_async_base::complete_now") more than once.

Any temporary objects allocated with [`boost::beast::allocate_stable`](../boost__beast__allocate_stable.html "allocate_stable") will be automatically
destroyed before the final completion handler is invoked.

###### [Parameters](complete_now.html#beast.ref.boost__beast__stable_async_base.complete_now.parameters)

| Name | Description |
| --- | --- |
| `args` | A list of optional parameters to invoke the handler with. The completion handler must be invocable with the parameter list, or else a compilation error will result. |