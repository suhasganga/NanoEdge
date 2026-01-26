##### [http::message::target](target.html "http::message::target")

(Inherited from [`http::header`](../boost__beast__http__header.html "http::header"))

Returns the request-target string.

###### [Synopsis](target.html#beast.ref.boost__beast__http__message.target.synopsis)

```programlisting
string_view
target() const;
```

###### [Description](target.html#beast.ref.boost__beast__http__message.target.description)

The request target string returned is the same string which was received
from the network or stored. In particular, it will contain url-encoded
characters and should follow the syntax rules for URIs used with HTTP.

###### [Remarks](target.html#beast.ref.boost__beast__http__message.target.remarks)

This function is only available when `isRequest
== true`.