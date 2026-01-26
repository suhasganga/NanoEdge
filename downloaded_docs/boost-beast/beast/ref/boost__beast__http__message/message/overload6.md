###### [http::message::message (6 of 14 overloads)](overload6.html "http::message::message (6 of 14 overloads)")

Constructor.

###### [Synopsis](overload6.html#beast.ref.boost__beast__http__message.message.overload6.synopsis)

```programlisting
message(
    verb method,
    string_view target,
    unsigned version);
```

###### [Parameters](overload6.html#beast.ref.boost__beast__http__message.message.overload6.parameters)

| Name | Description |
| --- | --- |
| `method` | The request-method to use. |
| `target` | The request-target. |
| `version` | The HTTP-version. |

###### [Remarks](overload6.html#beast.ref.boost__beast__http__message.message.overload6.remarks)

This function is only available when `isRequest
== true`.