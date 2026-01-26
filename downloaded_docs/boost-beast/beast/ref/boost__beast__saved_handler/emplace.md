##### [saved\_handler::emplace](emplace.html "saved_handler::emplace")

Store a completion handler in the container.

```programlisting
template<
    class Handler,
    class Allocator>
void
emplace(
    Handler&& handler,
    Allocator const& alloc,
    net::cancellation_type cancel_type = net::cancellation_type::terminal);
  » more...

template<
    class Handler>
void
emplace(
    Handler&& handler,
    net::cancellation_type cancel_type = net::cancellation_type::terminal);
  » more...
```