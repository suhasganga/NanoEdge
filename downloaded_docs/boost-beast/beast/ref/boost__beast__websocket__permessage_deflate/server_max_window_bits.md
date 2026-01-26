##### [websocket::permessage\_deflate::server\_max\_window\_bits](server_max_window_bits.html "websocket::permessage_deflate::server_max_window_bits")

Maximum server window bits to offer.

###### [Synopsis](server_max_window_bits.html#beast.ref.boost__beast__websocket__permessage_deflate.server_max_window_bits.synopsis)

```programlisting
int server_max_window_bits = 15;
```

###### [Remarks](server_max_window_bits.html#beast.ref.boost__beast__websocket__permessage_deflate.server_max_window_bits.remarks)

Due to a bug in ZLib, this value must be greater than 8.