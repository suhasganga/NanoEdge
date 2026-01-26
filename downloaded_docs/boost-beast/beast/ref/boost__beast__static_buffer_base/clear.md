##### [static\_buffer\_base::clear](clear.html "static_buffer_base::clear")

Clear the readable and writable bytes to zero.

###### [Synopsis](clear.html#beast.ref.boost__beast__static_buffer_base.clear.synopsis)

```programlisting
void
clear();
```

###### [Description](clear.html#beast.ref.boost__beast__static_buffer_base.clear.description)

This function causes the readable and writable bytes to become empty. The
capacity is not changed.

Buffer sequences previously obtained using [`data`](data.html "static_buffer_base::data") or [`prepare`](prepare.html "static_buffer_base::prepare") become invalid.

###### [Exception Safety](clear.html#beast.ref.boost__beast__static_buffer_base.clear.exception_safety)

No-throw guarantee.