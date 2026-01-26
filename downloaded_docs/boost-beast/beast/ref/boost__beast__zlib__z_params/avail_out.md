##### [zlib::z\_params::avail\_out](avail_out.html "zlib::z_params::avail_out")

The remaining bytes of space at `next_out`.

###### [Synopsis](avail_out.html#beast.ref.boost__beast__zlib__z_params.avail_out.synopsis)

```programlisting
std::size_t avail_out;
```

###### [Description](avail_out.html#beast.ref.boost__beast__zlib__z_params.avail_out.description)

The application must update `next_out`
and `avail_out` when avail\_out
has dropped to zero.