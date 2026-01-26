###### [websocket::stream\_base::decorator::decorator (2 of 2 overloads)](overload2.html "websocket::stream_base::decorator::decorator (2 of 2 overloads)")

Construct a decorator option.

###### [Synopsis](overload2.html#beast.ref.boost__beast__websocket__stream_base__decorator.decorator.overload2.synopsis)

```programlisting
template<
    class Decorator>
decorator(
    Decorator&& f);
```

###### [Parameters](overload2.html#beast.ref.boost__beast__websocket__stream_base__decorator.decorator.overload2.parameters)

| Name | Description |
| --- | --- |
| `f` | An invocable function object. Ownership of the function object is transferred by decay-copy. |