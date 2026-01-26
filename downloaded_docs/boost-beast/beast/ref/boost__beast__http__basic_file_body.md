#### [http::basic\_file\_body](boost__beast__http__basic_file_body.html "http::basic_file_body")

A message body represented by a file on the filesystem.

##### [Synopsis](boost__beast__http__basic_file_body.html#beast.ref.boost__beast__http__basic_file_body.synopsis)

Defined in header `<boost/beast/http/basic_file_body.hpp>`

```programlisting
template<
    class File>
struct basic_file_body
```

##### [Types](boost__beast__http__basic_file_body.html#beast.ref.boost__beast__http__basic_file_body.types)

| Name | Description |
| --- | --- |
| **[file\_type](boost__beast__http__basic_file_body/file_type.html "http::basic_file_body::file_type")** | The type of File this body uses. |
| **[reader](boost__beast__http__basic_file_body__reader.html "http::basic_file_body::reader")** | Algorithm for storing buffers when parsing. |
| **[value\_type](boost__beast__http__basic_file_body__value_type.html "http::basic_file_body::value_type")** | The type of the [`message::body`](boost__beast__http__message/body.html "http::message::body") member. |
| **[writer](boost__beast__http__basic_file_body__writer.html "http::basic_file_body::writer")** | Algorithm for retrieving buffers when serializing. |

##### [Static Member Functions](boost__beast__http__basic_file_body.html#beast.ref.boost__beast__http__basic_file_body.static_member_functions)

| Name | Description |
| --- | --- |
| **[size](boost__beast__http__basic_file_body/size.html "http::basic_file_body::size")** | Returns the size of the body. |

##### [Description](boost__beast__http__basic_file_body.html#beast.ref.boost__beast__http__basic_file_body.description)

Messages with this type have bodies represented by a file on the file system.
When parsing a message using this body type, the data is stored in the file
pointed to by the path, which must be writable. When serializing, the implementation
will read the file and present those octets as the body content. This may
be used to serve content from a directory as part of a web service.

##### [Template Parameters](boost__beast__http__basic_file_body.html#beast.ref.boost__beast__http__basic_file_body.template_parameters)

| Type | Description |
| --- | --- |
| `File` | The implementation to use for accessing files. This type must meet the requirements of *File*. |