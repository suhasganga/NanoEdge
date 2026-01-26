###### [basic\_stream::async\_connect (3 of 5 overloads)](overload3.html "basic_stream::async_connect (3 of 5 overloads)")

Establishes a connection by trying each endpoint in a sequence asynchronously.

###### [Synopsis](overload3.html#beast.ref.boost__beast__basic_stream.async_connect.overload3.synopsis)

```programlisting
template<
    class EndpointSequence,
    class ConnectCondition,
    class RangeConnectHandler = net::default_completion_token_t<executor_type>>
DEDUCED
async_connect(
    EndpointSequence const& endpoints,
    ConnectCondition connect_condition,
    RangeConnectHandler&& handler = net::default_completion_token_t< executor_type >{});
```

###### [Description](overload3.html#beast.ref.boost__beast__basic_stream.async_connect.overload3.description)

This function attempts to connect the stream to one of a sequence of
endpoints by trying each endpoint until a connection is successfully
established. The underlying socket is automatically opened if needed.
An automatically opened socket is not returned to the closed state upon
failure.

The algorithm, known as a *composed asynchronous operation*,
is implemented in terms of calls to the underlying socket's `async_connect` function.

If the timeout timer expires while the operation is outstanding, the
current connection attempt will be canceled and the completion handler
will be invoked with the error [`error::timeout`](../../boost__beast__error.html "error").

###### [Parameters](overload3.html#beast.ref.boost__beast__basic_stream.async_connect.overload3.parameters)

| Name | Description |
| --- | --- |
| `endpoints` | A sequence of endpoints. This this object must meet the requirements of *EndpointSequence*. |
| `connect_condition` | A function object that is called prior to each connection attempt. The signature of the function object must be:   ```table-programlisting bool connect_condition(     error_code const & ec,     typename Protocol::endpoint const & next); ```   The `ec` parameter contains the result from the most recent connect operation. Before the first connection attempt, `ec` is always set to indicate success. The `next` parameter is the next endpoint to be tried. The function object should return true if the next endpoint should be tried, and false if it should be skipped. |
| `handler` | The completion handler to invoke when the operation completes. The implementation takes ownership of the handler by performing a decay-copy. The equivalent function signature of the handler must be:   ```table-programlisting void handler(     // Result of operation. if the sequence is empty, set to     // net::error::not_found. Otherwise, contains the     // error from the last connection attempt.     error_code const & error,      // On success, the successfully connected endpoint.     // Otherwise, a default-constructed endpoint.     typename Protocol::endpoint const & endpoint ); ```   If the handler has an associated immediate executor, an immediate completion will be dispatched to it. Otherwise, the handler will not be invoked from within this function. Invocation of the handler will be performed by dispatching to the immediate executor. If no immediate executor is specified, this is equivalent to using `net::post`. |

###### [Example](overload3.html#beast.ref.boost__beast__basic_stream.async_connect.overload3.example)

The following connect condition function object can be used to output
information about the individual connection attempts:

```programlisting
struct my_connect_condition
{
    bool operator()(
        error_code const & ec,
        net::ip::tcp::endpoint const & next)
    {
        if (ec)
            std::cout << "Error: " << ec.message() << std::endl;
        std::cout << "Trying: " << next << std::endl;
        return true ;
    }
};
```

###### [Per-Operation Cancellation](overload3.html#beast.ref.boost__beast__basic_stream.async_connect.overload3.per_operation_cancellation)

This asynchronous operation supports cancellation for the following net::cancellation\_type
values:

* `net::cancellation_type::terminal`
* `net::cancellation_type::partial`
* `net::cancellation_type::total`

if they are also supported by the socket's `async_connect`
operation.