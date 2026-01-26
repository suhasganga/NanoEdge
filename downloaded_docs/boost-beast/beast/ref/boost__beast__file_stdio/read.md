##### [file\_stdio::read](read.html "file_stdio::read")

Read from the open file.

###### [Synopsis](read.html#beast.ref.boost__beast__file_stdio.read.synopsis)

```programlisting
std::size_t
read(
    void* buffer,
    std::size_t n,
    error_code& ec) const;
```

###### [Parameters](read.html#beast.ref.boost__beast__file_stdio.read.parameters)

| Name | Description |
| --- | --- |
| `buffer` | The buffer for storing the result of the read |
| `n` | The number of bytes to read |
| `ec` | Set to the error, if any occurred |