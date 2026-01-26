###### [http::message::message (14 of 14 overloads)](overload14.html "http::message::message (14 of 14 overloads)")

Construct a message.

###### [Synopsis](overload14.html#beast.ref.boost__beast__http__message.message.overload14.synopsis)

```programlisting
template<
    class... BodyArgs,
    class... FieldsArgs>
message(
    std::piecewise_construct_t,
    std::tuple< BodyArgs... > body_args,
    std::tuple< FieldsArgs... > fields_args);
```

###### [Parameters](overload14.html#beast.ref.boost__beast__http__message.message.overload14.parameters)

| Name | Description |
| --- | --- |
| `body_args` | A tuple forwarded as a parameter pack to the body constructor. |
| `fields_args` | A tuple forwarded as a parameter pack to the `Fields` constructor. |