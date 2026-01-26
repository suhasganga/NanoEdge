##### [async\_base::complete](complete.html "async_base::complete")

Invoke the final completion handler, maybe using post.

###### [Synopsis](complete.html#beast.ref.boost__beast__async_base.complete.synopsis)

```programlisting
template<
    class... Args>
void
complete(
    bool is_continuation,
    Args&&... args);
```

###### [Description](complete.html#beast.ref.boost__beast__async_base.complete.description)

This invokes the final completion handler with the specified arguments
forwarded. It is undefined to call either of [`boost::beast::async_base::complete`](complete.html "async_base::complete") or [`boost::beast::async_base::complete_now`](complete_now.html "async_base::complete_now") more than once.

Any temporary objects allocated with [`boost::beast::allocate_stable`](../boost__beast__allocate_stable.html "allocate_stable") will be automatically
destroyed before the final completion handler is invoked.

###### [Parameters](complete.html#beast.ref.boost__beast__async_base.complete.parameters)

| Name | Description |
| --- | --- |
| `is_continuation` | If this value is `false`, then the handler will be submitted to the to the immediate executor using `net::dispatch`. If the handler has no immediate executor, this will submit to the executor via `net::post`. Otherwise the handler will be invoked as if by calling [`boost::beast::async_base::complete_now`](complete_now.html "async_base::complete_now"). |
| `args` | A list of optional parameters to invoke the handler with. The completion handler must be invocable with the parameter list, or else a compilation error will result. |