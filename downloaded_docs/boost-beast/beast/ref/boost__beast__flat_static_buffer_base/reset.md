##### [flat\_static\_buffer\_base::reset](reset.html "flat_static_buffer_base::reset")

Reset the pointed-to buffer.

###### [Synopsis](reset.html#beast.ref.boost__beast__flat_static_buffer_base.reset.synopsis)

```programlisting
void
reset(
    void* p,
    std::size_t n);
```

###### [Description](reset.html#beast.ref.boost__beast__flat_static_buffer_base.reset.description)

This function resets the internal state to the buffer provided. All input
and output sequences are invalidated. This function allows the derived
class to construct its members before initializing the static buffer.

###### [Parameters](reset.html#beast.ref.boost__beast__flat_static_buffer_base.reset.parameters)

| Name | Description |
| --- | --- |
| `p` | A pointer to valid storage of at least `n` bytes. |
| `n` | The number of valid bytes pointed to by `p`. |

###### [Exception Safety](reset.html#beast.ref.boost__beast__flat_static_buffer_base.reset.exception_safety)

No-throw guarantee.