##### [file\_win32::seek](seek.html "file_win32::seek")

Adjust the current position in the open file.

###### [Synopsis](seek.html#beast.ref.boost__beast__file_win32.seek.synopsis)

```programlisting
void
seek(
    std::uint64_t offset,
    error_code& ec);
```

###### [Parameters](seek.html#beast.ref.boost__beast__file_win32.seek.parameters)

| Name | Description |
| --- | --- |
| `offset` | The offset in bytes from the beginning of the file |
| `ec` | Set to the error, if any occurred |