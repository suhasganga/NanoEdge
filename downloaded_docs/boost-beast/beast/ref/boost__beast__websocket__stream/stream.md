##### [websocket::stream::stream](stream.html "websocket::stream::stream")

Constructor.

```programlisting
stream(
    stream&&);
  » more...

template<
    class... Args>
explicit
stream(
    Args&&... args);
  » more...
```

Rebinding constructor.

```programlisting
template<
    class Other>
explicit
stream(
    stream< Other >&& other);
  » more...
```