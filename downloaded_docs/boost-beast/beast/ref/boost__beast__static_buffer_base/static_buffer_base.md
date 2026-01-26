##### [static\_buffer\_base::static\_buffer\_base](static_buffer_base.html "static_buffer_base::static_buffer_base")

Constructor.

###### [Synopsis](static_buffer_base.html#beast.ref.boost__beast__static_buffer_base.static_buffer_base.synopsis)

```programlisting
static_buffer_base(
    void* p,
    std::size_t size);
```

###### [Description](static_buffer_base.html#beast.ref.boost__beast__static_buffer_base.static_buffer_base.description)

This creates a dynamic buffer using the provided storage area.

###### [Parameters](static_buffer_base.html#beast.ref.boost__beast__static_buffer_base.static_buffer_base.parameters)

| Name | Description |
| --- | --- |
| `p` | A pointer to valid storage of at least `n` bytes. |
| `size` | The number of valid bytes pointed to by `p`. |