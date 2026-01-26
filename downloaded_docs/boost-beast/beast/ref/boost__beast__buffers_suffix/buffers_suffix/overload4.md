###### [buffers\_suffix::buffers\_suffix (4 of 4 overloads)](overload4.html "buffers_suffix::buffers_suffix (4 of 4 overloads)")

Constructor.

###### [Synopsis](overload4.html#beast.ref.boost__beast__buffers_suffix.buffers_suffix.overload4.synopsis)

```programlisting
template<
    class... Args>
buffers_suffix(
    boost::in_place_init_t,
    Args&&... args);
```

###### [Description](overload4.html#beast.ref.boost__beast__buffers_suffix.buffers_suffix.overload4.description)

This constructs the buffer sequence in-place from a list of arguments.

###### [Parameters](overload4.html#beast.ref.boost__beast__buffers_suffix.buffers_suffix.overload4.parameters)

| Name | Description |
| --- | --- |
| `args` | Arguments forwarded to the buffers constructor. |