#### [websocket::close\_reason](boost__beast__websocket__close_reason.html "websocket::close_reason")

Description of the close reason.

##### [Synopsis](boost__beast__websocket__close_reason.html#beast.ref.boost__beast__websocket__close_reason.synopsis)

Defined in header `<boost/beast/websocket/rfc6455.hpp>`

```programlisting
struct close_reason
```

##### [Member Functions](boost__beast__websocket__close_reason.html#beast.ref.boost__beast__websocket__close_reason.member_functions)

| Name | Description |
| --- | --- |
| **[close\_reason](boost__beast__websocket__close_reason/close_reason.html "websocket::close_reason::close_reason") [constructor]** | Default constructor.  — Construct from a code.  — Construct from a reason string. code is [`close_code::normal`](boost__beast__websocket__close_code.html "websocket::close_code").  — Construct from a reason string literal. code is [`close_code::normal`](boost__beast__websocket__close_code.html "websocket::close_code").  — Construct from a close code and reason string. |
| **[operator bool](boost__beast__websocket__close_reason/operator_bool.html "websocket::close_reason::operator bool")** | Returns `true` if a code was specified. |

##### [Data Members](boost__beast__websocket__close_reason.html#beast.ref.boost__beast__websocket__close_reason.data_members)

| Name | Description |
| --- | --- |
| **[code](boost__beast__websocket__close_reason/code.html "websocket::close_reason::code")** | The close code. |
| **[reason](boost__beast__websocket__close_reason/reason.html "websocket::close_reason::reason")** | The optional utf8-encoded reason string. |

##### [Description](boost__beast__websocket__close_reason.html#beast.ref.boost__beast__websocket__close_reason.description)

This object stores the close code (if any) and the optional utf-8 encoded
implementation defined reason string.