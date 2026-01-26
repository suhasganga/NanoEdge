#### [file\_mode](boost__beast__file_mode.html "file_mode")

File open modes.

##### [Synopsis](boost__beast__file_mode.html#beast.ref.boost__beast__file_mode.synopsis)

Defined in header `<boost/beast/core/file_base.hpp>`

```programlisting
enum file_mode
```

##### [Values](boost__beast__file_mode.html#beast.ref.boost__beast__file_mode.values)

| Name | Description |
| --- | --- |
| `read` | Random read-only access to an existing file. |
| `scan` | Sequential read-only access to an existing file. |
| `write` | Random reading and writing to a new or truncated file.  This mode permits random-access reading and writing for the specified file. If the file does not exist prior to the function call, it is created with an initial size of zero bytes. Otherwise if the file already exists, the size is truncated to zero bytes. |
| `write_new` | Random reading and writing to a new file only.  This mode permits random-access reading and writing for the specified file. The file will be created with an initial size of zero bytes. If the file already exists prior to the function call, an error is returned and no file is opened. |
| `write_existing` | Random write-only access to existing file.  If the file does not exist, an error is generated. |
| `append` | Appending to a new or existing file.  The current file position shall be set to the end of the file prior to each write.  * If the file does not exist, it is created.  * If the file exists, the new data gets appended. |
| `append_existing` | Appending to an existing file.  The current file position shall be set to the end of the file prior to each write.  If the file does not exist, an error is generated. |

##### [Description](boost__beast__file_mode.html#beast.ref.boost__beast__file_mode.description)

These modes are used when opening files using instances of the *File*
concept.

##### [See Also](boost__beast__file_mode.html#beast.ref.boost__beast__file_mode.see_also)

[`file_stdio`](boost__beast__file_stdio.html "file_stdio")