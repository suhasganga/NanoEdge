###### [http::header::target (2 of 2 overloads)](overload2.html "http::header::target (2 of 2 overloads)")

Set the request-target string.

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__header.target.overload2.synopsis)

```programlisting
void
target(
    string_view s);
```

###### [Description](overload2.html#beast.ref.boost__beast__http__header.target.overload2.description)

It is the caller's responsibility to ensure that the request target string
follows the syntax rules for URIs used with HTTP. In particular, reserved
or special characters must be url-encoded. The implementation does not
perform syntax checking on the passed string.

###### [Parameters](overload2.html#beast.ref.boost__beast__http__header.target.overload2.parameters)

| Name | Description |
| --- | --- |
| `s` | A string representing the request-target. |

###### [Remarks](overload2.html#beast.ref.boost__beast__http__header.target.overload2.remarks)

This function is only available when `isRequest
== true`.