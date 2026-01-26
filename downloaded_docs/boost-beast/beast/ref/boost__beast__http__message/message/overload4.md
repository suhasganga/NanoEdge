###### [http::message::message (4 of 14 overloads)](overload4.html "http::message::message (4 of 14 overloads)")

Constructor.

###### [Synopsis](overload4.html#beast.ref.boost__beast__http__message.message.overload4.synopsis)

```programlisting
template<
    class... BodyArgs>
message(
    header_type&& h,
    BodyArgs&&... body_args);
```

###### [Parameters](overload4.html#beast.ref.boost__beast__http__message.message.overload4.parameters)

| Name | Description |
| --- | --- |
| `h` | The header to move construct from. |
| `body_args` | Optional arguments forwarded to the `body` constructor. |