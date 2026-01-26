##### [zlib::z\_params::avail\_in](avail_in.html "zlib::z_params::avail_in")

The number of bytes of input available at `next_in`.

###### [Synopsis](avail_in.html#beast.ref.boost__beast__zlib__z_params.avail_in.synopsis)

```programlisting
std::size_t avail_in;
```

###### [Description](avail_in.html#beast.ref.boost__beast__zlib__z_params.avail_in.description)

If there is no more input, this should be set to zero.

The application must update `next_in`
and `avail_in` when `avail_in` has dropped to zero.