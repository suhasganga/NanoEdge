###### [websocket::stream::set\_option (2 of 3 overloads)](overload2.html "websocket::stream::set_option (2 of 3 overloads)")

Set the timeout option.

###### [Synopsis](overload2.html#beast.ref.boost__beast__websocket__stream.set_option.overload2.synopsis)

```programlisting
void
set_option(
    timeout const& opt);
```

###### [Exceptions](overload2.html#beast.ref.boost__beast__websocket__stream.set_option.overload2.exceptions)

| Type | Thrown On |
| --- | --- |
| `[link beast.ref.boost__beast__system_error system_error]` | on failure to reset the timer. |