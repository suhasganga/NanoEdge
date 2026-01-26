##### [basic\_flat\_buffer::clear](clear.html "basic_flat_buffer::clear")

Set the size of the readable and writable bytes to zero.

###### [Synopsis](clear.html#beast.ref.boost__beast__basic_flat_buffer.clear.synopsis)

```programlisting
void
clear();
```

###### [Description](clear.html#beast.ref.boost__beast__basic_flat_buffer.clear.description)

This clears the buffer without changing capacity. Buffer sequences previously
obtained using [`data`](data.html "basic_flat_buffer::data") or [`prepare`](prepare.html "basic_flat_buffer::prepare") become invalid.

###### [Exception Safety](clear.html#beast.ref.boost__beast__basic_flat_buffer.clear.exception_safety)

No-throw guarantee.