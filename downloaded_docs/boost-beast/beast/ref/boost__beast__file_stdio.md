#### [file\_stdio](boost__beast__file_stdio.html "file_stdio")

An implementation of File which uses cstdio.

##### [Synopsis](boost__beast__file_stdio.html#beast.ref.boost__beast__file_stdio.synopsis)

Defined in header `<boost/beast/core/file_stdio.hpp>`

```programlisting
class file_stdio
```

##### [Types](boost__beast__file_stdio.html#beast.ref.boost__beast__file_stdio.types)

| Name | Description |
| --- | --- |
| **[native\_handle\_type](boost__beast__file_stdio/native_handle_type.html "file_stdio::native_handle_type")** | The type of the underlying file handle. |

##### [Member Functions](boost__beast__file_stdio.html#beast.ref.boost__beast__file_stdio.member_functions)

| Name | Description |
| --- | --- |
| **[close](boost__beast__file_stdio/close.html "file_stdio::close")** | Close the file if open. |
| **[file\_stdio](boost__beast__file_stdio/file_stdio.html "file_stdio::file_stdio") [constructor]** | Constructor. |
| **[is\_open](boost__beast__file_stdio/is_open.html "file_stdio::is_open")** | Returns `true` if the file is open. |
| **[native\_handle](boost__beast__file_stdio/native_handle.html "file_stdio::native_handle")** | Returns the native handle associated with the file.  — Set the native handle associated with the file. |
| **[open](boost__beast__file_stdio/open.html "file_stdio::open")** | Open a file at the given path with the specified mode. |
| **[operator=](boost__beast__file_stdio/operator_eq_.html "file_stdio::operator=")** | Assignment. |
| **[pos](boost__beast__file_stdio/pos.html "file_stdio::pos")** | Return the current position in the open file. |
| **[read](boost__beast__file_stdio/read.html "file_stdio::read")** | Read from the open file. |
| **[seek](boost__beast__file_stdio/seek.html "file_stdio::seek")** | Adjust the current position in the open file. |
| **[size](boost__beast__file_stdio/size.html "file_stdio::size")** | Return the size of the open file. |
| **[write](boost__beast__file_stdio/write.html "file_stdio::write")** | Write to the open file. |
| **[~file\_stdio](boost__beast__file_stdio/_dtor_file_stdio.html "file_stdio::~file_stdio") [destructor]** | Destructor. |

##### [Description](boost__beast__file_stdio.html#beast.ref.boost__beast__file_stdio.description)

This class implements a file using the interfaces present in the C++ Standard
Library, in `<stdio>`.