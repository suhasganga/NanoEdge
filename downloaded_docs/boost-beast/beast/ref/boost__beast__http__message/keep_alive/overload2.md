###### [http::message::keep\_alive (2 of 2 overloads)](overload2.html "http::message::keep_alive (2 of 2 overloads)")

Set the keep-alive message semantic option.

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__message.keep_alive.overload2.synopsis)

```programlisting
void
keep_alive(
    bool value);
```

###### [Description](overload2.html#beast.ref.boost__beast__http__message.keep_alive.overload2.description)

This function adjusts the Connection field to indicate whether or not
the connection should be kept open after the corresponding response.
The result depends on the version set on the message, which must be set
to the final value before making this call.

###### [Parameters](overload2.html#beast.ref.boost__beast__http__message.keep_alive.overload2.parameters)

| Name | Description |
| --- | --- |
| `value` | `true` if the connection should persist. |