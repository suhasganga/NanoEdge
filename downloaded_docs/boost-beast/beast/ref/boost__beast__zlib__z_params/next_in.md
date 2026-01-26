##### [zlib::z\_params::next\_in](next_in.html "zlib::z_params::next_in")

A pointer to the next input byte.

###### [Synopsis](next_in.html#beast.ref.boost__beast__zlib__z_params.next_in.synopsis)

```programlisting
void const* next_in;
```

###### [Description](next_in.html#beast.ref.boost__beast__zlib__z_params.next_in.description)

If there is no more input, this may be set to `nullptr`.

The application must update `next_in`
and `avail_in` when `avail_in` has dropped to zero.