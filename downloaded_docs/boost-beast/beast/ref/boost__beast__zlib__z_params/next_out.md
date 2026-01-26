##### [zlib::z\_params::next\_out](next_out.html "zlib::z_params::next_out")

A pointer to the next output byte.

###### [Synopsis](next_out.html#beast.ref.boost__beast__zlib__z_params.next_out.synopsis)

```programlisting
void* next_out;
```

###### [Description](next_out.html#beast.ref.boost__beast__zlib__z_params.next_out.description)

The application must update `next_out`
and `avail_out` when avail\_out
has dropped to zero.