### [Files](files.html "Files")

Often when implementing network algorithms such as servers, it is necessary
to interact with files on the system. Beast defines the [*File*](../concepts/File.html "File")
concept and several models to facilitate cross-platform interaction with
the underlying filesystem:

**Table 1.12. File Types**

| Name | Description |
| --- | --- |
| [`file`](../ref/boost__beast__file.html "file") | `file` is a type alias to one of the following implementations, depending on what is available on the target platform. |
| [`file_stdio`](../ref/boost__beast__file_stdio.html "file_stdio") | This implementation of [*File*](../concepts/File.html "File") uses the C++ standard library facilities obtained by including `<cstdio>`. |
| [`file_win32`](../ref/boost__beast__file_win32.html "file_win32") | This implements a [*File*](../concepts/File.html "File") for the Win32 API. It provides low level access to the native file handle when necessary. |
| [`file_posix`](../ref/boost__beast__file_posix.html "file_posix") | For POSIX systems, this class provides a suitable implementation of [*File*](../concepts/File.html "File") which wraps the native file descriptor and provides it if necessary. |