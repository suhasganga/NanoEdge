#### [file\_posix](boost__beast__file_posix.html "file_posix")

An implementation of File for POSIX systems.

##### [Synopsis](boost__beast__file_posix.html#beast.ref.boost__beast__file_posix.synopsis)

Defined in header `<boost/beast/core/file_posix.hpp>`

```programlisting
class file_posix
```

##### [Types](boost__beast__file_posix.html#beast.ref.boost__beast__file_posix.types)

| Name | Description |
| --- | --- |
| **[native\_handle\_type](boost__beast__file_posix/native_handle_type.html "file_posix::native_handle_type")** | The type of the underlying file handle. |

##### [Member Functions](boost__beast__file_posix.html#beast.ref.boost__beast__file_posix.member_functions)

| Name | Description |
| --- | --- |
| **[close](boost__beast__file_posix/close.html "file_posix::close")** | Close the file if open. |
| **[file\_posix](boost__beast__file_posix/file_posix.html "file_posix::file_posix") [constructor]** | Constructor. |
| **[is\_open](boost__beast__file_posix/is_open.html "file_posix::is_open")** | Returns `true` if the file is open. |
| **[native\_handle](boost__beast__file_posix/native_handle.html "file_posix::native_handle")** | Returns the native handle associated with the file.  — Set the native handle associated with the file. |
| **[open](boost__beast__file_posix/open.html "file_posix::open")** | Open a file at the given path with the specified mode. |
| **[operator=](boost__beast__file_posix/operator_eq_.html "file_posix::operator=")** | Assignment. |
| **[pos](boost__beast__file_posix/pos.html "file_posix::pos")** | Return the current position in the open file. |
| **[read](boost__beast__file_posix/read.html "file_posix::read")** | Read from the open file. |
| **[seek](boost__beast__file_posix/seek.html "file_posix::seek")** | Adjust the current position in the open file. |
| **[size](boost__beast__file_posix/size.html "file_posix::size")** | Return the size of the open file. |
| **[write](boost__beast__file_posix/write.html "file_posix::write")** | Write to the open file. |
| **[~file\_posix](boost__beast__file_posix/_dtor_file_posix.html "file_posix::~file_posix") [destructor]** | Destructor. |

##### [Description](boost__beast__file_posix.html#beast.ref.boost__beast__file_posix.description)

This class implements a *File* using POSIX interfaces.