##### [file\_win32::write](write.html "file_win32::write")

Write to the open file.

###### [Synopsis](write.html#beast.ref.boost__beast__file_win32.write.synopsis)

```programlisting
std::size_t
write(
    void const* buffer,
    std::size_t n,
    error_code& ec);
```

###### [Parameters](write.html#beast.ref.boost__beast__file_win32.write.parameters)

| Name | Description |
| --- | --- |
| `buffer` | The buffer holding the data to write |
| `n` | The number of bytes to write |
| `ec` | Set to the error, if any occurred |