#### [zlib::z\_params](boost__beast__zlib__z_params.html "zlib::z_params")

Deflate codec parameters.

##### [Synopsis](boost__beast__zlib__z_params.html#beast.ref.boost__beast__zlib__z_params.synopsis)

Defined in header `<boost/beast/zlib/zlib.hpp>`

```programlisting
struct z_params
```

##### [Data Members](boost__beast__zlib__z_params.html#beast.ref.boost__beast__zlib__z_params.data_members)

| Name | Description |
| --- | --- |
| **[avail\_in](boost__beast__zlib__z_params/avail_in.html "zlib::z_params::avail_in")** | The number of bytes of input available at `next_in`. |
| **[avail\_out](boost__beast__zlib__z_params/avail_out.html "zlib::z_params::avail_out")** | The remaining bytes of space at `next_out`. |
| **[data\_type](boost__beast__zlib__z_params/data_type.html "zlib::z_params::data_type")** | Best guess about the data type: binary or text. |
| **[next\_in](boost__beast__zlib__z_params/next_in.html "zlib::z_params::next_in")** | A pointer to the next input byte. |
| **[next\_out](boost__beast__zlib__z_params/next_out.html "zlib::z_params::next_out")** | A pointer to the next output byte. |
| **[total\_in](boost__beast__zlib__z_params/total_in.html "zlib::z_params::total_in")** | The total number of input bytes read so far. |
| **[total\_out](boost__beast__zlib__z_params/total_out.html "zlib::z_params::total_out")** | The total number of bytes output so far. |

##### [Description](boost__beast__zlib__z_params.html#beast.ref.boost__beast__zlib__z_params.description)

Objects of this type are filled in by callers and provided to the deflate
codec to define the input and output areas for the next compress or decompress
operation.

The application must update next\_in and avail\_in when avail\_in has dropped
to zero. It must update next\_out and avail\_out when avail\_out has dropped
to zero. The application must initialize zalloc, zfree and opaque before
calling the init function. All other fields are set by the compression library
and must not be updated by the application.

The fields total\_in and total\_out can be used for statistics or progress
reports. After compression, total\_in holds the total size of the uncompressed
data and may be saved for use in the decompressor (particularly if the decompressor
wants to decompress everything in a single step).