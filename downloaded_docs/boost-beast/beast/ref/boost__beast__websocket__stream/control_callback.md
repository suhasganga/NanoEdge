##### [websocket::stream::control\_callback](control_callback.html "websocket::stream::control_callback")

Set a callback to be invoked on each incoming control frame.

```programlisting
void
control_callback(
    std::function< void(frame_type, string_view)> cb);
  » more...
```

Reset the control frame callback.

```programlisting
void
control_callback();
  » more...
```