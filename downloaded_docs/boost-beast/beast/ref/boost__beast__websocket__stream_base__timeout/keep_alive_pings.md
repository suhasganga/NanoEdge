##### [websocket::stream\_base::timeout::keep\_alive\_pings](keep_alive_pings.html "websocket::stream_base::timeout::keep_alive_pings")

Automatic ping setting.

###### [Synopsis](keep_alive_pings.html#beast.ref.boost__beast__websocket__stream_base__timeout.keep_alive_pings.synopsis)

```programlisting
bool keep_alive_pings;
```

###### [Description](keep_alive_pings.html#beast.ref.boost__beast__websocket__stream_base__timeout.keep_alive_pings.description)

If the idle interval is set, this setting affects the behavior of the stream
when no data is received for the timeout interval as follows:

* When `keep_alive_pings`
  is `true`, an idle ping
  will be sent automatically. If another timeout interval elapses with
  no received data then the connection will be closed. An outstanding
  read operation must be pending, which will complete immediately the
  error [`beast::error::timeout`](../boost__beast__error.html "error").
* When `keep_alive_pings`
  is `false`, the connection
  will be closed if there has been no activity. Both websocket message
  frames and control frames count as activity. An outstanding read operation
  must be pending, which will complete immediately the error [`beast::error::timeout`](../boost__beast__error.html "error").