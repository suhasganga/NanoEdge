###### [basic\_stream::async\_connect (1 of 5 overloads)](overload1.html "basic_stream::async_connect (1 of 5 overloads)")

Connect the stream to the specified endpoint asynchronously.

###### [Synopsis](overload1.html#beast.ref.boost__beast__basic_stream.async_connect.overload1.synopsis)

```programlisting
template<
    class ConnectHandler = net::default_completion_token_t<executor_type>>
DEDUCED
async_connect(
    endpoint_type const& ep,
    ConnectHandler&& handler = net::default_completion_token_t< executor_type >{});
```

###### [Description](overload1.html#beast.ref.boost__beast__basic_stream.async_connect.overload1.description)

This function is used to asynchronously connect the underlying socket
to the specified remote endpoint. The function call always returns immediately.
The underlying socket is automatically opened if needed. An automatically
opened socket is not returned to the closed state upon failure.

If the timeout timer expires while the operation is outstanding, the
operation will be canceled and the completion handler will be invoked
with the error [`error::timeout`](../../boost__beast__error.html "error").

###### [Parameters](overload1.html#beast.ref.boost__beast__basic_stream.async_connect.overload1.parameters)

| Name | Description |
| --- | --- |
| `ep` | The remote endpoint to which the underlying socket will be connected. Copies will be made of the endpoint object as required. |
| `handler` | The completion handler to invoke when the operation completes. The implementation takes ownership of the handler by performing a decay-copy. The equivalent function signature of the handler must be:   ```table-programlisting void handler(     error_code ec         // Result of operation ); ```   If the handler has an associated immediate executor, an immediate completion will be dispatched to it. Otherwise, the handler will not be invoked from within this function. Invocation of the handler will be performed by dispatching to the immediate executor. If no immediate executor is specified, this is equivalent to using `net::post`. |

###### [Per-Operation Cancellation](overload1.html#beast.ref.boost__beast__basic_stream.async_connect.overload1.per_operation_cancellation)

This asynchronous operation supports cancellation for the following net::cancellation\_type
values:

* `net::cancellation_type::terminal`
* `net::cancellation_type::partial`
* `net::cancellation_type::total`

if they are also supported by the socket's `async_connect`
operation.

###### [See Also](overload1.html#beast.ref.boost__beast__basic_stream.async_connect.overload1.see_also)

[`async_connect`](../async_connect.html "basic_stream::async_connect")