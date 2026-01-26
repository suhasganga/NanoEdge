###### [buffers\_adaptor::buffers\_adaptor (2 of 3 overloads)](overload2.html "buffers_adaptor::buffers_adaptor (2 of 3 overloads)")

Constructor.

###### [Synopsis](overload2.html#beast.ref.boost__beast__buffers_adaptor.buffers_adaptor.overload2.synopsis)

```programlisting
template<
    class... Args>
buffers_adaptor(
    boost::in_place_init_t,
    Args&&... args);
```

###### [Description](overload2.html#beast.ref.boost__beast__buffers_adaptor.buffers_adaptor.overload2.description)

This constructs the buffer adaptor in-place from a list of arguments.

###### [Parameters](overload2.html#beast.ref.boost__beast__buffers_adaptor.buffers_adaptor.overload2.parameters)

| Name | Description |
| --- | --- |
| `args` | Arguments forwarded to the buffers constructor. |