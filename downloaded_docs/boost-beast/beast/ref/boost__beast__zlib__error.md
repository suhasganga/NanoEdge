#### [zlib::error](boost__beast__zlib__error.html "zlib::error")

Error codes returned by the deflate codecs.

##### [Synopsis](boost__beast__zlib__error.html#beast.ref.boost__beast__zlib__error.synopsis)

Defined in header `<boost/beast/zlib/error.hpp>`

```programlisting
enum error
```

##### [Values](boost__beast__zlib__error.html#beast.ref.boost__beast__zlib__error.values)

| Name | Description |
| --- | --- |
| `need_buffers` | Additional buffers are required.  This error indicates that one or both of the buffers provided buffers do not have sufficient available bytes to make forward progress.  This does not always indicate a failure condition.  Remarks  This is the same as `Z_BUF_ERROR` returned by ZLib. |
| `end_of_stream` | End of stream reached.  Remarks  This is the same as `Z_STREAM_END` returned by ZLib. |
| `need_dict` | Preset dictionary required.  This error indicates that a preset dictionary was not provided and is now needed at this point.  This does not always indicate a failure condition.  Remarks  This is the same as `Z_NEED_DICT` returned by ZLib. |
| `stream_error` | Invalid stream or parameters.  This error is returned when invalid parameters are passed, or the operation being performed is not consistent with the state of the stream. For example, attempting to write data when the end of stream is already reached.  Remarks  This is the same as `Z_STREAM_ERROR` returned by ZLib. |
| `invalid_block_type` | Invalid block type. |
| `invalid_stored_length` | Invalid stored block length. |
| `too_many_symbols` | Too many length or distance symbols. |
| `invalid_code_lengths` | Invalid code lengths. |
| `invalid_bit_length_repeat` | Invalid bit length repeat. |
| `missing_eob` | Missing end of block code. |
| `invalid_literal_length` | Invalid literal/length code. |
| `invalid_distance_code` | Invalid distance code. |
| `invalid_distance` | Invalid distance too far back. |
| `over_subscribed_length` | Over-subscribed length code. |
| `incomplete_length_set` | Incomplete length set. |
| `general` | general error |