###### [http::message::message (7 of 14 overloads)](overload7.html "http::message::message (7 of 14 overloads)")

Constructor.

###### [Synopsis](overload7.html#beast.ref.boost__beast__http__message.message.overload7.synopsis)

```programlisting
template<
    class BodyArg>
message(
    verb method,
    string_view target,
    unsigned version,
    BodyArg&& body_arg);
```

###### [Parameters](overload7.html#beast.ref.boost__beast__http__message.message.overload7.parameters)

| Name | Description |
| --- | --- |
| `method` | The request-method to use. |
| `target` | The request-target. |
| `version` | The HTTP-version. |
| `body_arg` | An argument forwarded to the `body` constructor. |

###### [Remarks](overload7.html#beast.ref.boost__beast__http__message.message.overload7.remarks)

This function is only available when `isRequest
== true`.