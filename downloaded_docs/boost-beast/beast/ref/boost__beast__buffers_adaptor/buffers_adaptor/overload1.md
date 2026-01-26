###### [buffers\_adaptor::buffers\_adaptor (1 of 3 overloads)](overload1.html "buffers_adaptor::buffers_adaptor (1 of 3 overloads)")

Construct a buffers adaptor.

###### [Synopsis](overload1.html#beast.ref.boost__beast__buffers_adaptor.buffers_adaptor.overload1.synopsis)

```programlisting
buffers_adaptor(
    MutableBufferSequence const& buffers);
```

###### [Parameters](overload1.html#beast.ref.boost__beast__buffers_adaptor.buffers_adaptor.overload1.parameters)

| Name | Description |
| --- | --- |
| `buffers` | The mutable buffer sequence to wrap. A copy of the object will be made, but ownership of the memory is not transferred. |