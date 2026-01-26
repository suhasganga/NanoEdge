###### [saved\_handler::emplace (1 of 2 overloads)](overload1.html "saved_handler::emplace (1 of 2 overloads)")

Store a completion handler in the container.

###### [Synopsis](overload1.html#beast.ref.boost__beast__saved_handler.emplace.overload1.synopsis)

```programlisting
template<
    class Handler,
    class Allocator>
void
emplace(
    Handler&& handler,
    Allocator const& alloc,
    net::cancellation_type cancel_type = net::cancellation_type::terminal);
```

###### [Description](overload1.html#beast.ref.boost__beast__saved_handler.emplace.overload1.description)

Requires this->[`has_value()`](../has_value.html "saved_handler::has_value")
== false .

###### [Parameters](overload1.html#beast.ref.boost__beast__saved_handler.emplace.overload1.parameters)

| Name | Description |
| --- | --- |
| `handler` | The completion handler to store. The implementation takes ownership of the handler by performing a decay-copy. |
| `alloc` | The allocator to use. |
| `cancel_type` | The type of cancellation allowed to complete this op. |