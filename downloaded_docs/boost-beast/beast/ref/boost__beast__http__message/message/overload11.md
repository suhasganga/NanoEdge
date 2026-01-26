###### [http::message::message (11 of 14 overloads)](overload11.html "http::message::message (11 of 14 overloads)")

Constructor.

###### [Synopsis](overload11.html#beast.ref.boost__beast__http__message.message.overload11.synopsis)

```programlisting
template<
    class BodyArg,
    class FieldsArg>
message(
    status result,
    unsigned version,
    BodyArg&& body_arg,
    FieldsArg&& fields_arg);
```

###### [Parameters](overload11.html#beast.ref.boost__beast__http__message.message.overload11.parameters)

| Name | Description |
| --- | --- |
| `result` | The status-code for the response. |
| `version` | The HTTP-version. |
| `body_arg` | An argument forwarded to the `body` constructor. |
| `fields_arg` | An argument forwarded to the `Fields` base class constructor. |

###### [Remarks](overload11.html#beast.ref.boost__beast__http__message.message.overload11.remarks)

This member is only available when `isRequest
== false`.