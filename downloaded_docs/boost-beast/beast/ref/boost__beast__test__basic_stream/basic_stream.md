##### [test::basic\_stream::basic\_stream](basic_stream.html "test::basic_stream::basic_stream")

Move Constructor.

```programlisting
basic_stream(
    basic_stream&& other);
  » more...

template<
    class Executor2>
basic_stream(
    basic_stream< Executor2 >&& other);
  » more...
```

Construct a stream.

```programlisting
template<
    class ExecutionContext,
    class = typename std::enable_if<            std::is_convertible<ExecutionContext&, net::execution_context&>::value>::type>
explicit
basic_stream(
    ExecutionContext& context);
  » more...

explicit
basic_stream(
    executor_type exec);
  » more...

basic_stream(
    net::io_context& ioc,
    fail_count& fc);
  » more...

basic_stream(
    net::io_context& ioc,
    string_view s);
  » more...

basic_stream(
    net::io_context& ioc,
    fail_count& fc,
    string_view s);
  » more...
```