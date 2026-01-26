#### [http::file\_body](boost__beast__http__file_body.html "http::file_body")

A message body represented by a file on the filesystem.

##### [Synopsis](boost__beast__http__file_body.html#beast.ref.boost__beast__http__file_body.synopsis)

Defined in header `<boost/beast/http/file_body.hpp>`

```programlisting
using file_body = basic_file_body< file >;
```

##### [Types](boost__beast__http__file_body.html#beast.ref.boost__beast__http__file_body.types)

| Name | Description |
| --- | --- |
| **[file\_type](boost__beast__http__basic_file_body/file_type.html "http::basic_file_body::file_type")** | The type of File this body uses. |
| **[reader](boost__beast__http__basic_file_body__reader.html "http::basic_file_body::reader")** | Algorithm for storing buffers when parsing. |
| **[value\_type](boost__beast__http__basic_file_body__value_type.html "http::basic_file_body::value_type")** | The type of the [`message::body`](boost__beast__http__message/body.html "http::message::body") member. |
| **[writer](boost__beast__http__basic_file_body__writer.html "http::basic_file_body::writer")** | Algorithm for retrieving buffers when serializing. |

##### [Static Member Functions](boost__beast__http__file_body.html#beast.ref.boost__beast__http__file_body.static_member_functions)

| Name | Description |
| --- | --- |
| **[size](boost__beast__http__basic_file_body/size.html "http::basic_file_body::size")** | Returns the size of the body. |

Messages with this type have bodies represented by a file on the file system.
When parsing a message using this body type, the data is stored in the file
pointed to by the path, which must be writable. When serializing, the implementation
will read the file and present those octets as the body content. This may
be used to serve content from a directory as part of a web service.

##### [Template Parameters](boost__beast__http__file_body.html#beast.ref.boost__beast__http__file_body.template_parameters)

| Type | Description |
| --- | --- |
| `File` | The implementation to use for accessing files. This type must meet the requirements of *File*. |

##### [Types](boost__beast__http__file_body.html#beast.ref.boost__beast__http__file_body.types0)

| Name | Description |
| --- | --- |
| **[native\_handle\_type](boost__beast__file/native_handle_type.html "file::native_handle_type")** | The type of the underlying file handle. |

##### [Member Functions](boost__beast__http__file_body.html#beast.ref.boost__beast__http__file_body.member_functions)

| Name | Description |
| --- | --- |
| **[close](boost__beast__file/close.html "file::close")** | Close the file if open. |
| **[is\_open](boost__beast__file/is_open.html "file::is_open")** | Returns `true` if the file is open. |
| **[native\_handle](boost__beast__file/native_handle.html "file::native_handle")** | Returns the native handle associated with the file.  — Set the native handle associated with the file. |
| **[open](boost__beast__file/open.html "file::open")** | Open a file at the given path with the specified mode. |
| **[pos](boost__beast__file/pos.html "file::pos")** | Return the current position in the open file. |
| **[read](boost__beast__file/read.html "file::read")** | Read from the open file. |
| **[seek](boost__beast__file/seek.html "file::seek")** | Adjust the current position in the open file. |
| **[size](boost__beast__file/size.html "file::size")** | Return the size of the open file. |
| **[write](boost__beast__file/write.html "file::write")** | Write to the open file. |

This alias is set to the best available implementation of *File*
given the platform and build settings.