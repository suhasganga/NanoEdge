### [File](File.html "File")

The **File** concept abstracts access to files
in the underlying file system. To support other platform interfaces, users
may author their own **File** types which meet
these requirements.

##### [Associated Types](File.html#beast.concepts.File.associated_types)

* [`file_mode`](../ref/boost__beast__file_mode.html "file_mode")
* [`is_file`](../ref/boost__beast__is_file.html "is_file")

##### [Requirements](File.html#beast.concepts.File.requirements)

In this table:

* `F` is a **File**
  type
* `f` is an instance of
  `F`
* `p` is a value of type
  `char const*` which points to a null terminated utf-8
  encoded string.
* `m` is an instance of
  [`file_mode`](../ref/boost__beast__file_mode.html "file_mode")
* `n` is a number of bytes,
  convertible to `std::size_t`
* `o` is a byte offset in
  the file, convertible to `std::uint64_t`
* `b` is any non-const pointer
  to memory
* `c` is any possibly-const
  pointer to memory
* `ec` is a reference of
  type [`error_code`](../ref/boost__beast__error_code.html "error_code")

**Table 1.45. Valid expressions**

| Expression | Type | Semantics, Pre/Post-conditions |
| --- | --- | --- |
| Operation | Return Type | Semantics, Pre/Post-conditions |
| `F()` |  | Default constructable |
| `f.~F()` |  | Destructible. If `f` refers to an open file, it is first closed as if by a call to `close` with the error ignored. |
| `f.is_open()` | `bool` | Returns `true` if `f` refers to an open file, `false` otherwise. |
| `f.close(ec)` |  | If `f` refers to an open file, this function attempts to close the file. Regardless of whether an error occurs or not, a subsequent call to `f.is_open()` will return `false`. The function will ensure that `!ec` is `true` if there was no error or set to the appropriate error code if an error occurred. |
| `f.open(p,m,ec)` |  | Attempts to open the file at the path specified by `p` with the mode specified by `m`. Upon success, a subsequent call to `f.is_open()` will return `true`. If `f` refers to an open file, it is first closed as if by a call to `close` with the error ignored. The function will ensure that `!ec` is `true` if there was no error or set to the appropriate error code if an error occurred. |
| `f.size(ec)` | `std::uint64_t` | If `f` refers to an open file, this function attempts to determine the file size and return its value. If `f` does not refer to an open file, the function will set `ec` to `errc::invalid_argument` and return 0. The function will ensure that `!ec` is `true` if there was no error or set to the appropriate error code if an error occurred. |
| `f.pos(ec)` | `std::uint64_t` | If `f` refers to an open file, this function attempts to determine the current file offset and return it. If `f` does not refer to an open file, the function will set `ec` to `errc::invalid_argument` and return 0. The function will ensure that `!ec` is `true` if there was no error or set to the appropriate error code if an error occurred. |
| `f.seek(o,ec)` |  | Attempts to reposition the current file offset to the value `o`, which represents a byte offset relative to the beginning of the file. If `f` does not refer to an open file, the function will set `ec` to `errc::invalid_argument` and return immediately. The function will ensure that `!ec` is `true` if there was no error or set to the appropriate error code if an error occurred. |
| `f.read(b,n,ec)` | `std::size_t` | Attempts to read `n` bytes starting at the current file offset from the open file referred to by `f`. Bytes read are stored in the memory buffer at address `b` which must be at least `n` bytes in size. The function advances the file offset by the amount read, and returns the number of bytes actually read, which may be less than `n`. If `f` does not refer to an open file, the function will set `ec` to `errc::invalid_argument` and return immediately. The function will ensure that `!ec` is `true` if there was no error or set to the appropriate error code if an error occurred. If an end-of-file condition is detected prior to reading any bytes, the function will ensure that `!ec` is `true` and the return value shall be 0. |
| `f.write(c,n,ec)` | `std::size_t` | Attempts to write `n` bytes from the buffer pointed to by `c` to the current file offset of the open file referred to by `f`. The memory buffer at `c` must point to storage of at least `n` bytes meant to be copied to the file. The function advances the file offset by the amount written, and returns the number of bytes actually written, which may be less than `n`. If `f` does not refer to an open file, the function will set `ec` to `errc::invalid_argument` and return immediately. The function will ensure that `!ec` is `true` if there was no error or set to the appropriate error code if an error occurred. |

  

##### [Exemplar](File.html#beast.concepts.File.exemplar)

```programlisting
struct File
{
    /** Default constructor

        There is no open file initially.
    */
    File();

    /** Destructor

        If the file is open it is first closed.
    */
    ~File();

    /// Returns `true` if the file is open
    bool
    is_open() const;

    /// Close the file if open
    void
    close(error_code& ec);

    /// Open a file at the given path with the specified mode
    void
    open(char const* path, file_mode mode, error_code& ec);

    /// Return the size of the open file
    std::uint64_t
    size(error_code& ec) const;

    /// Return the current position in the open file
    std::uint64_t
    pos(error_code& ec) const;

    /// Adjust the current position in the open file
    void
    seek(std::uint64_t offset, error_code& ec);

    /// Read from the open file
    std::size_t
    read(void* buffer, std::size_t n, error_code& ec) const;

    /// Write to the open file
    std::size_t
    write(void const* buffer, std::size_t n, error_code& ec);
};
```

##### [Models](File.html#beast.concepts.File.models)

* [`file_posix`](../ref/boost__beast__file_posix.html "file_posix")
* [`file_stdio`](../ref/boost__beast__file_stdio.html "file_stdio")
* [`file_win32`](../ref/boost__beast__file_win32.html "file_win32")