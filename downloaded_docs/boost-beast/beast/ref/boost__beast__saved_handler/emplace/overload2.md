###### [saved\_handler::emplace (2 of 2 overloads)](overload2.html "saved_handler::emplace (2 of 2 overloads)")

Store a completion handler in the container.

###### [Synopsis](overload2.html#beast.ref.boost__beast__saved_handler.emplace.overload2.synopsis)

```programlisting
template<
    class Handler>
void
emplace(
    Handler&& handler,
    net::cancellation_type cancel_type = net::cancellation_type::terminal);
```

###### [Description](overload2.html#beast.ref.boost__beast__saved_handler.emplace.overload2.description)

Requires this->[`has_value()`](../has_value.html "saved_handler::has_value")
== false . The implementation will use the handler's associated allocator
to obtian storage.

###### [Parameters](overload2.html#beast.ref.boost__beast__saved_handler.emplace.overload2.parameters)

| Name | Description |
| --- | --- |
| `handler` | The completion handler to store. The implementation takes ownership of the handler by performing a decay-copy. |
| `cancel_type` | The type of cancellation allowed to complete this op. |