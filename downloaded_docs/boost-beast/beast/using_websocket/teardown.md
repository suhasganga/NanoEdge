### [Teardown](teardown.html "Teardown")

The WebSocket protocol requirements described in rfc6455 section 7.1.1 outline
an operation described as [*Close
the WebSocket Connection*](https://tools.ietf.org/html/rfc6455#section-7.1.1). This operation cleanly discards
bytes remaining at receiving endpoints and also closes the underlying TCP/IP
connection. Orderly shutdowns are always preferred; for TLS or SSL streams,
a protocol-level shutdown is desired. This presents a small issue for the
[`stream`](../ref/boost__beast__websocket__stream.html "websocket::stream")
implementation: the stream's `NextLayer`
template type requires only [*SyncStream*](../concepts/streams.html#beast.concepts.streams.SyncStream)
or [*AsyncStream*](../concepts/streams.html#beast.concepts.streams.AsyncStream),
but those concepts do not support the operations to shut down the connection.

To enable the implementation to perform the shutdown components of the close
operation, the library exposes two customization points expressed as free
functions associated with the next layer type:

* [`teardown`](../ref/boost__beast__websocket__teardown.html "websocket::teardown"): Overloads of this
  function drain and shut down a stream synchronously.
* [`async_teardown`](../ref/boost__beast__websocket__async_teardown.html "websocket::async_teardown"): Overloads of
  this function drain and shut down a stream asynchronously.

The implementation provides suitable overloads of the teardown customization
points when websocket streams are instantiated using the Asio types [`tcp::socket`](../../../../../../doc/html/boost_asio/reference/ip__tcp/socket.html)
or [`net::ssl::stream`](../../../../../../doc/html/boost_asio/reference/ssl__stream.html)
for the next layer. In this case no user action is required. However, when
the websocket stream is instantiated for a user-defined type, compile errors
will result if the customization points are not provided for the user defined
type. Furthermore, user-defined types that wrap one of the Asio objects mentioned
earlier may wish to invoke a teardown customization point for the wrapped
object. This is how those tasks are accomplished.

##### [User-defined Teardown](teardown.html#beast.using_websocket.teardown.user_defined_teardown)

To provide overloads of teardown for a user-defined type, simply declare
the two free functions with the correct signature, accepting a reference
to the user-defined type as the stream parameter:

```programlisting
struct custom_stream;

void
teardown(
    role_type role,
    custom_stream& stream,
    error_code& ec);

template<class TeardownHandler>
void
async_teardown(
    role_type role,
    custom_stream& stream,
    TeardownHandler&& handler);
```

When the implementation invokes the asynchronous teardown function, it always
uses an invokable completion handler. It is not necessary to specify the
return type customization when creating user-defined overloads of `async_teardown`.

##### [Invoking Teardown](teardown.html#beast.using_websocket.teardown.invoking_teardown)

To invoke the customization point, first bring the default implementation
into scope with a `using` statement.
Then call the customization point without namespace qualification, allowing
argument-dependent lookup to take effect:

```programlisting
template <class NextLayer>
struct custom_wrapper
{
    NextLayer next_layer;

    template<class... Args>
    explicit
    custom_wrapper(Args&&... args)
        : next_layer(std::forward<Args>(args)...)
    {
    }

    friend
    void
    teardown(
        role_type role,
        custom_wrapper& stream,
        error_code& ec)
    {
        using boost::beast::websocket::teardown;
        teardown(role, stream.next_layer, ec);
    }

    template<class TeardownHandler>
    friend
    void
    async_teardown(
        role_type role,
        custom_wrapper& stream,
        TeardownHandler&& handler)
    {
        using boost::beast::websocket::async_teardown;
        async_teardown(role, stream.next_layer, std::forward<TeardownHandler>(handler));
    }
};
```