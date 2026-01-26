##### [websocket::stream::secure\_prng](secure_prng.html "websocket::stream::secure_prng")

Set whether the PRNG is cryptographically secure.

###### [Synopsis](secure_prng.html#beast.ref.boost__beast__websocket__stream.secure_prng.synopsis)

```programlisting
void
secure_prng(
    bool value);
```

###### [Description](secure_prng.html#beast.ref.boost__beast__websocket__stream.secure_prng.description)

This controls whether or not the source of pseudo-random numbers used to
produce the masks required by the WebSocket protocol are of cryptographic
quality. When the setting is `true`,
a strong algorithm is used which cannot be guessed by observing outputs.
When the setting is `false`,
a much faster algorithm is used. Masking is only performed by streams operating
in the client mode. For streams operating in the server mode, this setting
has no effect. By default, newly constructed streams use a secure PRNG.

If the WebSocket stream is used with an encrypted SSL or TLS next layer,
if it is known to the application that intermediate proxies are not vulnerable
to cache poisoning, or if the application is designed such that an attacker
cannot send arbitrary inputs to the stream interface, then the faster algorithm
may be used.

For more information please consult the WebSocket protocol RFC.

###### [Parameters](secure_prng.html#beast.ref.boost__beast__websocket__stream.secure_prng.parameters)

| Name | Description |
| --- | --- |
| `value` | `true` if the PRNG algorithm should be cryptographically secure. |