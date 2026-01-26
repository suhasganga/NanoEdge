##### [websocket::close\_reason::close\_reason](close_reason.html "websocket::close_reason::close_reason")

Default constructor.

```programlisting
close_reason();
  » more...
```

Construct from a code.

```programlisting
close_reason(
    std::uint16_t code_);
  » more...
```

Construct from a reason string. code is [`close_code::normal`](../boost__beast__websocket__close_code.html "websocket::close_code").

```programlisting
close_reason(
    string_view s);
  » more...
```

Construct from a reason string literal. code is [`close_code::normal`](../boost__beast__websocket__close_code.html "websocket::close_code").

```programlisting
close_reason(
    char const* s);
  » more...
```

Construct from a close code and reason string.

```programlisting
close_reason(
    close_code code_,
    string_view s);
  » more...
```