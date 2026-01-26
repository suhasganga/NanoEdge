##### [websocket::stream\_base::timeout::handshake\_timeout](handshake_timeout.html "websocket::stream_base::timeout::handshake_timeout")

Time limit on handshake, accept, and close operations:

###### [Synopsis](handshake_timeout.html#beast.ref.boost__beast__websocket__stream_base__timeout.handshake_timeout.synopsis)

```programlisting
duration handshake_timeout;
```

###### [Description](handshake_timeout.html#beast.ref.boost__beast__websocket__stream_base__timeout.handshake_timeout.description)

This value whether or not there is a time limit, and the duration of that
time limit, for asynchronous handshake, accept, and close operations. If
this is equal to the value [`none`](../boost__beast__websocket__stream_base/none.html "websocket::stream_base::none") then there will be no time
limit. Otherwise, if any of the applicable operations takes longer than
this amount of time, the operation will be canceled and a timeout error
delivered to the completion handler.