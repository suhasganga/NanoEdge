##### [static\_buffer::clear](clear.html "static_buffer::clear")

Clear the readable and writable bytes to zero.

###### [Synopsis](clear.html#beast.ref.boost__beast__static_buffer.clear.synopsis)

```programlisting
void
clear();
```

###### [Description](clear.html#beast.ref.boost__beast__static_buffer.clear.description)

This function causes the readable and writable bytes to become empty. The
capacity is not changed.

Buffer sequences previously obtained using [`data`](data.html "static_buffer::data") or [`prepare`](prepare.html "static_buffer::prepare") become invalid.

###### [Exception Safety](clear.html#beast.ref.boost__beast__static_buffer.clear.exception_safety)

No-throw guarantee.