##### [file\_posix::pos](pos.html "file_posix::pos")

Return the current position in the open file.

###### [Synopsis](pos.html#beast.ref.boost__beast__file_posix.pos.synopsis)

```programlisting
std::uint64_t
pos(
    error_code& ec) const;
```

###### [Parameters](pos.html#beast.ref.boost__beast__file_posix.pos.parameters)

| Name | Description |
| --- | --- |
| `ec` | Set to the error, if any occurred |

###### [Return Value](pos.html#beast.ref.boost__beast__file_posix.pos.return_value)

The offset in bytes from the beginning of the file