#### [http::buffer\_body::value\_type](boost__beast__http__buffer_body__value_type.html "http::buffer_body::value_type")

The type of the body member when used in a message.

##### [Synopsis](boost__beast__http__buffer_body__value_type.html#beast.ref.boost__beast__http__buffer_body__value_type.synopsis)

Defined in header `<boost/beast/http/buffer_body.hpp>`

```programlisting
struct value_type
```

##### [Data Members](boost__beast__http__buffer_body__value_type.html#beast.ref.boost__beast__http__buffer_body__value_type.data_members)

| Name | Description |
| --- | --- |
| **[data](boost__beast__http__buffer_body__value_type/data.html "http::buffer_body::value_type::data")** | A pointer to a contiguous area of memory of [`size`](boost__beast__http__buffer_body__value_type/size.html "http::buffer_body::value_type::size") octets, else `nullptr`. |
| **[more](boost__beast__http__buffer_body__value_type/more.html "http::buffer_body::value_type::more")** | `true` if this is not the last buffer. |
| **[size](boost__beast__http__buffer_body__value_type/size.html "http::buffer_body::value_type::size")** | The number of octets in the buffer pointed to by [`data`](boost__beast__http__buffer_body__value_type/data.html "http::buffer_body::value_type::data"). |