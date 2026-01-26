###### [http::message::message (10 of 14 overloads)](overload10.html "http::message::message (10 of 14 overloads)")

Constructor.

###### [Synopsis](overload10.html#beast.ref.boost__beast__http__message.message.overload10.synopsis)

```programlisting
template<
    class BodyArg>
message(
    status result,
    unsigned version,
    BodyArg&& body_arg);
```

###### [Parameters](overload10.html#beast.ref.boost__beast__http__message.message.overload10.parameters)

| Name | Description |
| --- | --- |
| `result` | The status-code for the response. |
| `version` | The HTTP-version. |
| `body_arg` | An argument forwarded to the `body` constructor. |

###### [Remarks](overload10.html#beast.ref.boost__beast__http__message.message.overload10.remarks)

This member is only available when `isRequest
== false`.