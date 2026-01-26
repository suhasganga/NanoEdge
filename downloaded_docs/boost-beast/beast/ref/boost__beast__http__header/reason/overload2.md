###### [http::header::reason (2 of 2 overloads)](overload2.html "http::header::reason (2 of 2 overloads)")

Set the response reason-phrase (deprecated)

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__header.reason.overload2.synopsis)

```programlisting
void
reason(
    string_view s);
```

###### [Description](overload2.html#beast.ref.boost__beast__http__header.reason.overload2.description)

This function sets a custom reason-phrase to a copy of the string passed
in. Normally it is not necessary to set the reason phrase on an outgoing
response object; the implementation will automatically use the standard
reason text for the corresponding status code.

To clear a previously set custom phrase, pass an empty string. This will
restore the default standard reason text based on the status code used
when serializing.

The reason-phrase is obsolete as of rfc7230.

###### [Parameters](overload2.html#beast.ref.boost__beast__http__header.reason.overload2.parameters)

| Name | Description |
| --- | --- |
| `s` | The string to use for the reason-phrase. |

###### [Remarks](overload2.html#beast.ref.boost__beast__http__header.reason.overload2.remarks)

This function is only available when `isRequest
== false`.