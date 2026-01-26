##### [basic\_flat\_buffer::shrink\_to\_fit](shrink_to_fit.html "basic_flat_buffer::shrink_to_fit")

Request the removal of unused capacity.

###### [Synopsis](shrink_to_fit.html#beast.ref.boost__beast__basic_flat_buffer.shrink_to_fit.synopsis)

```programlisting
void
shrink_to_fit();
```

###### [Description](shrink_to_fit.html#beast.ref.boost__beast__basic_flat_buffer.shrink_to_fit.description)

This function attempts to reduce [`capacity()`](capacity.html "basic_flat_buffer::capacity")
to [`size()`](size.html "basic_flat_buffer::size"),
which may not succeed.

###### [Exception Safety](shrink_to_fit.html#beast.ref.boost__beast__basic_flat_buffer.shrink_to_fit.exception_safety)

No-throw guarantee.