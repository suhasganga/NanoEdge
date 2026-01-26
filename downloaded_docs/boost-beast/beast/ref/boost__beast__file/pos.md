##### [file::pos](pos.html "file::pos")

(Inherited from [`file_stdio`](../boost__beast__file_stdio.html "file_stdio"))

Return the current position in the open file.

###### [Synopsis](pos.html#beast.ref.boost__beast__file.pos.synopsis)

```programlisting
std::uint64_t
pos(
    error_code& ec) const;
```

###### [Parameters](pos.html#beast.ref.boost__beast__file.pos.parameters)

| Name | Description |
| --- | --- |
| `ec` | Set to the error, if any occurred |

###### [Return Value](pos.html#beast.ref.boost__beast__file.pos.return_value)

The offset in bytes from the beginning of the file