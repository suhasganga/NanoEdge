##### [basic\_stream::expires\_after](expires_after.html "basic_stream::expires_after")

Set the timeout for subsequent logical operations.

###### [Synopsis](expires_after.html#beast.ref.boost__beast__basic_stream.expires_after.synopsis)

```programlisting
void
expires_after(
    net::steady_timer::duration expiry_time);
```

###### [Description](expires_after.html#beast.ref.boost__beast__basic_stream.expires_after.description)

This sets either the read timer, the write timer, or both timers to expire
after the specified amount of time has elapsed. If a timer expires when
the corresponding asynchronous operation is outstanding, the stream will
be closed and any outstanding operations will complete with the error
[`beast::error::timeout`](../boost__beast__error.html "error").
Otherwise, if the timer expires while no operations are outstanding, and
the expiraton is not set again, the next operation will time out immediately.

The timer applies collectively to any asynchronous reads or writes initiated
after the expiration is set, until the expiration is set again. A call
to [`async_connect`](async_connect.html "basic_stream::async_connect") counts as both a
read and a write.

###### [Parameters](expires_after.html#beast.ref.boost__beast__basic_stream.expires_after.parameters)

| Name | Description |
| --- | --- |
| `expiry_time` | The amount of time after which a logical operation should be considered timed out. |