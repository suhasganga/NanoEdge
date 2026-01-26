###### [basic\_stream::async\_connect (5 of 5 overloads)](overload5.html "basic_stream::async_connect (5 of 5 overloads)")

Establishes a connection by trying each endpoint in a sequence asynchronously.

###### [Synopsis](overload5.html#beast.ref.boost__beast__basic_stream.async_connect.overload5.synopsis)

```programlisting
template<
    class Iterator,
    class ConnectCondition,
    class IteratorConnectHandler = net::default_completion_token_t<executor_type>>
DEDUCED
async_connect(
    Iterator begin,
    Iterator end,
    ConnectCondition connect_condition,
    IteratorConnectHandler&& handler = net::default_completion_token_t< executor_type >{});
```

###### [Description](overload5.html#beast.ref.boost__beast__basic_stream.async_connect.overload5.description)

This function attempts to connect the stream to one of a sequence of
endpoints by trying each endpoint until a connection is successfully
established. The algorithm, known as a *composed asynchronous
operation*, is implemented in terms of calls to the underlying
socket's `async_connect`
function.

If the timeout timer expires while the operation is outstanding, the
current connection attempt will be canceled and the completion handler
will be invoked with the error [`error::timeout`](../../boost__beast__error.html "error").

###### [Parameters](overload5.html#beast.ref.boost__beast__basic_stream.async_connect.overload5.parameters)

| Name | Description |
| --- | --- |
| `begin` | An iterator pointing to the start of a sequence of endpoints. |
| `end` | An iterator pointing to the end of a sequence of endpoints. |
| `connect_condition` | A function object that is called prior to each connection attempt. The signature of the function object must be:   ```table-programlisting bool connect_condition(     error_code const & ec,     typename Protocol::endpoint const & next); ``` |
| `handler` | The completion handler to invoke when the operation completes. The implementation takes ownership of the handler by performing a decay-copy. The equivalent function signature of the handler must be:   ```table-programlisting void handler(     // Result of operation. if the sequence is empty, set to     // net::error::not_found. Otherwise, contains the     // error from the last connection attempt.     error_code const & error,      // On success, an iterator denoting the successfully     // connected endpoint. Otherwise, the end iterator.     Iterator iterator ); ```   If the handler has an associated immediate executor, an immediate completion will be dispatched to it. Otherwise, the handler will not be invoked from within this function. Invocation of the handler will be performed by dispatching to the immediate executor. If no immediate executor is specified, this is equivalent to using `net::post`. |

###### [Per-Operation Cancellation](overload5.html#beast.ref.boost__beast__basic_stream.async_connect.overload5.per_operation_cancellation)

This asynchronous operation supports cancellation for the following net::cancellation\_type
values:

* `net::cancellation_type::terminal`
* `net::cancellation_type::partial`
* `net::cancellation_type::total`

if they are also supported by the socket's `async_connect`
operation.