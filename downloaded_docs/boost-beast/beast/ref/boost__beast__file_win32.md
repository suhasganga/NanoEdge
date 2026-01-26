#### [file\_win32](boost__beast__file_win32.html "file_win32")

An implementation of File for Win32.

##### [Synopsis](boost__beast__file_win32.html#beast.ref.boost__beast__file_win32.synopsis)

Defined in header `<boost/beast/core/file_win32.hpp>`

```programlisting
class file_win32
```

##### [Types](boost__beast__file_win32.html#beast.ref.boost__beast__file_win32.types)

| Name | Description |
| --- | --- |
| **[native\_handle\_type](boost__beast__file_win32/native_handle_type.html "file_win32::native_handle_type")** | The type of the underlying file handle. |

##### [Member Functions](boost__beast__file_win32.html#beast.ref.boost__beast__file_win32.member_functions)

| Name | Description |
| --- | --- |
| **[close](boost__beast__file_win32/close.html "file_win32::close")** | Close the file if open. |
| **[file\_win32](boost__beast__file_win32/file_win32.html "file_win32::file_win32") [constructor]** | Constructor. |
| **[is\_open](boost__beast__file_win32/is_open.html "file_win32::is_open")** | Returns `true` if the file is open. |
| **[native\_handle](boost__beast__file_win32/native_handle.html "file_win32::native_handle")** | Returns the native handle associated with the file.  — Set the native handle associated with the file. |
| **[open](boost__beast__file_win32/open.html "file_win32::open")** | Open a file at the given path with the specified mode. |
| **[operator=](boost__beast__file_win32/operator_eq_.html "file_win32::operator=")** | Assignment. |
| **[pos](boost__beast__file_win32/pos.html "file_win32::pos")** | Return the current position in the open file. |
| **[read](boost__beast__file_win32/read.html "file_win32::read")** | Read from the open file. |
| **[seek](boost__beast__file_win32/seek.html "file_win32::seek")** | Adjust the current position in the open file. |
| **[size](boost__beast__file_win32/size.html "file_win32::size")** | Return the size of the open file. |
| **[write](boost__beast__file_win32/write.html "file_win32::write")** | Write to the open file. |
| **[~file\_win32](boost__beast__file_win32/_dtor_file_win32.html "file_win32::~file_win32") [destructor]** | Destructor. |

##### [Description](boost__beast__file_win32.html#beast.ref.boost__beast__file_win32.description)

This class implements a *File* using Win32 native interfaces.