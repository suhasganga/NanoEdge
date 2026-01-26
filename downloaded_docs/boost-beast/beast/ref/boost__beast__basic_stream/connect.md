##### [basic\_stream::connect](connect.html "basic_stream::connect")

Connect the stream to the specified endpoint.

```programlisting
void
connect(
    endpoint_type const& ep);
  » more...

void
connect(
    endpoint_type const& ep,
    error_code& ec);
  » more...
```

Establishes a connection by trying each endpoint in a sequence.

```programlisting
template<
    class EndpointSequence>
Protocol::endpoint
connect(
    EndpointSequence const& endpoints);
  » more...

template<
    class EndpointSequence>
Protocol::endpoint
connect(
    EndpointSequence const& endpoints,
    error_code& ec);
  » more...

template<
    class Iterator>
Iterator
connect(
    Iterator begin,
    Iterator end);
  » more...

template<
    class Iterator>
Iterator
connect(
    Iterator begin,
    Iterator end,
    error_code& ec);
  » more...

template<
    class EndpointSequence,
    class ConnectCondition>
Protocol::endpoint
connect(
    EndpointSequence const& endpoints,
    ConnectCondition connect_condition);
  » more...

template<
    class EndpointSequence,
    class ConnectCondition>
Protocol::endpoint
connect(
    EndpointSequence const& endpoints,
    ConnectCondition connect_condition,
    error_code& ec);
  » more...

template<
    class Iterator,
    class ConnectCondition>
Iterator
connect(
    Iterator begin,
    Iterator end,
    ConnectCondition connect_condition);
  » more...

template<
    class Iterator,
    class ConnectCondition>
Iterator
connect(
    Iterator begin,
    Iterator end,
    ConnectCondition connect_condition,
    error_code& ec);
  » more...
```