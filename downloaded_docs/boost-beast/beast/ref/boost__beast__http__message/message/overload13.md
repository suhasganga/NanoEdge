###### [http::message::message (13 of 14 overloads)](overload13.html "http::message::message (13 of 14 overloads)")

Construct a message.

###### [Synopsis](overload13.html#beast.ref.boost__beast__http__message.message.overload13.synopsis)

```programlisting
template<
    class... BodyArgs>
message(
    std::piecewise_construct_t,
    std::tuple< BodyArgs... > body_args);
```

###### [Parameters](overload13.html#beast.ref.boost__beast__http__message.message.overload13.parameters)

| Name | Description |
| --- | --- |
| `body_args` | A tuple forwarded as a parameter pack to the body constructor. |