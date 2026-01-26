##### [websocket::stream\_base::timeout::suggested](suggested.html "websocket::stream_base::timeout::suggested")

Construct timeout settings with suggested values for a role.

###### [Synopsis](suggested.html#beast.ref.boost__beast__websocket__stream_base__timeout.suggested.synopsis)

```programlisting
static
timeout
suggested(
    role_type role);
```

###### [Description](suggested.html#beast.ref.boost__beast__websocket__stream_base__timeout.suggested.description)

This constructs the timeout settings with a predefined set of values which
varies depending on the desired role. The values are selected upon construction,
regardless of the current or actual role in use on the stream.

###### [Example](suggested.html#beast.ref.boost__beast__websocket__stream_base__timeout.suggested.example)

This statement sets the timeout settings of the stream to the suggested
values for the server role:

###### [Parameters](suggested.html#beast.ref.boost__beast__websocket__stream_base__timeout.suggested.parameters)

| Name | Description |
| --- | --- |
| `role` | The role of the websocket stream ([`role_type::client`](../boost__beast__role_type.html "role_type") or [`role_type::server`](../boost__beast__role_type.html "role_type")). |