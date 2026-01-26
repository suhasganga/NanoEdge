##### [zlib::z\_params::total\_in](total_in.html "zlib::z_params::total_in")

The total number of input bytes read so far.

###### [Synopsis](total_in.html#beast.ref.boost__beast__zlib__z_params.total_in.synopsis)

```programlisting
std::size_t total_in = 0;
```

###### [Description](total_in.html#beast.ref.boost__beast__zlib__z_params.total_in.description)

This field is set by the compression library and must not be updated by
the application.

This field can also be used for statistics or progress reports.

After compression, total\_in holds the total size of the uncompressed data
and may be saved for use by the decompressor (particularly if the decompressor
wants to decompress everything in a single step).