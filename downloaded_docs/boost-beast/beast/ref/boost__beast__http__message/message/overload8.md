###### [http::message::message (8 of 14 overloads)](overload8.html "http::message::message (8 of 14 overloads)")

Constructor.

###### [Synopsis](overload8.html#beast.ref.boost__beast__http__message.message.overload8.synopsis)

```programlisting
template<
    class BodyArg,
    class FieldsArg>
message(
    verb method,
    string_view target,
    unsigned version,
    BodyArg&& body_arg,
    FieldsArg&& fields_arg);
```

###### [Parameters](overload8.html#beast.ref.boost__beast__http__message.message.overload8.parameters)

| Name | Description |
| --- | --- |
| `method` | The request-method to use. |
| `target` | The request-target. |
| `version` | The HTTP-version. |
| `body_arg` | An argument forwarded to the `body` constructor. |
| `fields_arg` | An argument forwarded to the `Fields` constructor. |

###### [Remarks](overload8.html#beast.ref.boost__beast__http__message.message.overload8.remarks)

This function is only available when `isRequest
== true`.