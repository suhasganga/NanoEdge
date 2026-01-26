##### [basic\_multi\_buffer::shrink\_to\_fit](shrink_to_fit.html "basic_multi_buffer::shrink_to_fit")

Reallocate the buffer to fit the readable bytes exactly.

###### [Synopsis](shrink_to_fit.html#beast.ref.boost__beast__basic_multi_buffer.shrink_to_fit.synopsis)

```programlisting
void
shrink_to_fit();
```

###### [Description](shrink_to_fit.html#beast.ref.boost__beast__basic_multi_buffer.shrink_to_fit.description)

Buffer sequences previously obtained using [`data`](data.html "basic_multi_buffer::data") or [`prepare`](prepare.html "basic_multi_buffer::prepare") become invalid.

###### [Exception Safety](shrink_to_fit.html#beast.ref.boost__beast__basic_multi_buffer.shrink_to_fit.exception_safety)

Strong guarantee.