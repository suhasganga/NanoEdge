###### [http::message::message (9 of 14 overloads)](overload9.html "http::message::message (9 of 14 overloads)")

Constructor.

###### [Synopsis](overload9.html#beast.ref.boost__beast__http__message.message.overload9.synopsis)

```programlisting
message(
    status result,
    unsigned version);
```

###### [Parameters](overload9.html#beast.ref.boost__beast__http__message.message.overload9.parameters)

| Name | Description |
| --- | --- |
| `result` | The status-code for the response. |
| `version` | The HTTP-version. |

###### [Remarks](overload9.html#beast.ref.boost__beast__http__message.message.overload9.remarks)

This member is only available when `isRequest
== false`.