##### [basic\_stream::async\_connect](async_connect.html "basic_stream::async_connect")

Connect the stream to the specified endpoint asynchronously.

```programlisting
template<
    class ConnectHandler = net::default_completion_token_t<executor_type>>
DEDUCED
async_connect(
    endpoint_type const& ep,
    ConnectHandler&& handler = net::default_completion_token_t< executor_type >{});
  » more...
```

Establishes a connection by trying each endpoint in a sequence asynchronously.

```programlisting
template<
    class EndpointSequence,
    class RangeConnectHandler = net::default_completion_token_t<executor_type>>
DEDUCED
async_connect(
    EndpointSequence const& endpoints,
    RangeConnectHandler&& handler = net::default_completion_token_t< executor_type >{});
  » more...

template<
    class EndpointSequence,
    class ConnectCondition,
    class RangeConnectHandler = net::default_completion_token_t<executor_type>>
DEDUCED
async_connect(
    EndpointSequence const& endpoints,
    ConnectCondition connect_condition,
    RangeConnectHandler&& handler = net::default_completion_token_t< executor_type >{});
  » more...

template<
    class Iterator,
    class IteratorConnectHandler = net::default_completion_token_t<executor_type>>
DEDUCED
async_connect(
    Iterator begin,
    Iterator end,
    IteratorConnectHandler&& handler = net::default_completion_token_t< executor_type >{});
  » more...

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
  » more...
```