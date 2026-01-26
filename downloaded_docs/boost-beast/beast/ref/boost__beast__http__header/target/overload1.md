###### [http::header::target (1 of 2 overloads)](overload1.html "http::header::target (1 of 2 overloads)")

Returns the request-target string.

###### [Synopsis](overload1.html#beast.ref.boost__beast__http__header.target.overload1.synopsis)

```programlisting
string_view
target() const;
```

###### [Description](overload1.html#beast.ref.boost__beast__http__header.target.overload1.description)

The request target string returned is the same string which was received
from the network or stored. In particular, it will contain url-encoded
characters and should follow the syntax rules for URIs used with HTTP.

###### [Remarks](overload1.html#beast.ref.boost__beast__http__header.target.overload1.remarks)

This function is only available when `isRequest
== true`.