###### [flat\_static\_buffer\_base::flat\_static\_buffer\_base (1 of 2 overloads)](overload1.html "flat_static_buffer_base::flat_static_buffer_base (1 of 2 overloads)")

Constructor.

###### [Synopsis](overload1.html#beast.ref.boost__beast__flat_static_buffer_base.flat_static_buffer_base.overload1.synopsis)

```programlisting
flat_static_buffer_base(
    void* p,
    std::size_t n);
```

###### [Description](overload1.html#beast.ref.boost__beast__flat_static_buffer_base.flat_static_buffer_base.overload1.description)

This creates a dynamic buffer using the provided storage area.

###### [Parameters](overload1.html#beast.ref.boost__beast__flat_static_buffer_base.flat_static_buffer_base.overload1.parameters)

| Name | Description |
| --- | --- |
| `p` | A pointer to valid storage of at least `n` bytes. |
| `n` | The number of valid bytes pointed to by `p`. |