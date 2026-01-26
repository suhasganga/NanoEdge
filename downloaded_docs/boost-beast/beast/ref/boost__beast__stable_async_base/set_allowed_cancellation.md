##### [stable\_async\_base::set\_allowed\_cancellation](set_allowed_cancellation.html "stable_async_base::set_allowed_cancellation")

(Inherited from [`async_base`](../boost__beast__async_base.html "async_base"))

Set the allowed cancellation types, default is `terminal`.

###### [Synopsis](set_allowed_cancellation.html#beast.ref.boost__beast__stable_async_base.set_allowed_cancellation.synopsis)

```programlisting
void
set_allowed_cancellation(
    net::cancellation_type allowed_cancellation_types = net::cancellation_type::terminal);
```