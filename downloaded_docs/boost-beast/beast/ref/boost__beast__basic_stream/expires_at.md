##### [basic\_stream::expires\_at](expires_at.html "basic_stream::expires_at")

Set the timeout for subsequent logical operations.

###### [Synopsis](expires_at.html#beast.ref.boost__beast__basic_stream.expires_at.synopsis)

```programlisting
void
expires_at(
    net::steady_timer::time_point expiry_time);
```

###### [Description](expires_at.html#beast.ref.boost__beast__basic_stream.expires_at.description)

This sets either the read timer, the write timer, or both timers to expire
at the specified time point. If a timer expires when the corresponding
asynchronous operation is outstanding, the stream will be closed and any
outstanding operations will complete with the error [`beast::error::timeout`](../boost__beast__error.html "error"). Otherwise, if the timer
expires while no operations are outstanding, and the expiraton is not set
again, the next operation will time out immediately.

The timer applies collectively to any asynchronous reads or writes initiated
after the expiration is set, until the expiration is set again. A call
to [`async_connect`](async_connect.html "basic_stream::async_connect") counts as both a
read and a write.

###### [Parameters](expires_at.html#beast.ref.boost__beast__basic_stream.expires_at.parameters)

| Name | Description |
| --- | --- |
| `expiry_time` | The time point after which a logical operation should be considered timed out. |