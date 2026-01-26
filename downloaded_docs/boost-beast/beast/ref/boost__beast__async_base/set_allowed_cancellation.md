##### [async\_base::set\_allowed\_cancellation](set_allowed_cancellation.html "async_base::set_allowed_cancellation")

Set the allowed cancellation types, default is `terminal`.

###### [Synopsis](set_allowed_cancellation.html#beast.ref.boost__beast__async_base.set_allowed_cancellation.synopsis)

```programlisting
void
set_allowed_cancellation(
    net::cancellation_type allowed_cancellation_types = net::cancellation_type::terminal);
```