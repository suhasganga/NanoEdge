#### [file](boost__beast__file.html "file")

An implementation of File.

##### [Synopsis](boost__beast__file.html#beast.ref.boost__beast__file.synopsis)

Defined in header `<boost/beast/core/file.hpp>`

```programlisting
struct file :
    public file_stdio
```

##### [Types](boost__beast__file.html#beast.ref.boost__beast__file.types)

| Name | Description |
| --- | --- |
| **[native\_handle\_type](boost__beast__file/native_handle_type.html "file::native_handle_type")** | The type of the underlying file handle. |

##### [Member Functions](boost__beast__file.html#beast.ref.boost__beast__file.member_functions)

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

##### [Description](boost__beast__file.html#beast.ref.boost__beast__file.description)

This alias is set to the best available implementation of *File*
given the platform and build settings.