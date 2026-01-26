#### [websocket::seed\_prng](boost__beast__websocket__seed_prng.html "websocket::seed_prng")

Manually provide a one-time seed to initialize the PRNG.

##### [Synopsis](boost__beast__websocket__seed_prng.html#beast.ref.boost__beast__websocket__seed_prng.synopsis)

Defined in header `<boost/beast/websocket/stream.hpp>`

```programlisting
void
seed_prng(
    std::seed_seq& ss);
```

##### [Description](boost__beast__websocket__seed_prng.html#beast.ref.boost__beast__websocket__seed_prng.description)

This function invokes the specified seed sequence to produce a seed suitable
for use with the pseudo-random number generator used to create masks and
perform WebSocket protocol handshakes.

If a seed is not manually provided, the implementation will perform a one-time
seed generation using `std::random_device`.
This function may be used when the application runs in an environment where
the random device is unreliable or does not provide sufficient entropy.

##### [Preconditions](boost__beast__websocket__seed_prng.html#beast.ref.boost__beast__websocket__seed_prng.preconditions)

This function may not be called after any websocket [`stream`](boost__beast__websocket__stream.html "websocket::stream") objects have been constructed.

##### [Parameters](boost__beast__websocket__seed_prng.html#beast.ref.boost__beast__websocket__seed_prng.parameters)

| Name | Description |
| --- | --- |
| `ss` | A reference to a `std::seed_seq` which will be used to seed the pseudo-random number generator. The seed sequence should have at least 256 bits of entropy. |

##### [See Also](boost__beast__websocket__seed_prng.html#beast.ref.boost__beast__websocket__seed_prng.see_also)

[`stream::secure_prng`](boost__beast__websocket__stream/secure_prng.html "websocket::stream::secure_prng")