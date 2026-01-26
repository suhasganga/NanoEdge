##### [websocket::permessage\_deflate::client\_max\_window\_bits](client_max_window_bits.html "websocket::permessage_deflate::client_max_window_bits")

Maximum client window bits to offer.

###### [Synopsis](client_max_window_bits.html#beast.ref.boost__beast__websocket__permessage_deflate.client_max_window_bits.synopsis)

```programlisting
int client_max_window_bits = 15;
```

###### [Remarks](client_max_window_bits.html#beast.ref.boost__beast__websocket__permessage_deflate.client_max_window_bits.remarks)

Due to a bug in ZLib, this value must be greater than 8.