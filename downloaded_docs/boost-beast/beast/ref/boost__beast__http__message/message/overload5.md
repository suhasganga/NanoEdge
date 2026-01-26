###### [http::message::message (5 of 14 overloads)](overload5.html "http::message::message (5 of 14 overloads)")

Constructor.

###### [Synopsis](overload5.html#beast.ref.boost__beast__http__message.message.overload5.synopsis)

```programlisting
template<
    class... BodyArgs>
message(
    header_type const& h,
    BodyArgs&&... body_args);
```

###### [Parameters](overload5.html#beast.ref.boost__beast__http__message.message.overload5.parameters)

| Name | Description |
| --- | --- |
| `h` | The header to copy construct from. |
| `body_args` | Optional arguments forwarded to the `body` constructor. |