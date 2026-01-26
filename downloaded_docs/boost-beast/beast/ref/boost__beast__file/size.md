##### [file::size](size.html "file::size")

(Inherited from [`file_stdio`](../boost__beast__file_stdio.html "file_stdio"))

Return the size of the open file.

###### [Synopsis](size.html#beast.ref.boost__beast__file.size.synopsis)

```programlisting
std::uint64_t
size(
    error_code& ec) const;
```

###### [Parameters](size.html#beast.ref.boost__beast__file.size.parameters)

| Name | Description |
| --- | --- |
| `ec` | Set to the error, if any occurred |

###### [Return Value](size.html#beast.ref.boost__beast__file.size.return_value)

The size in bytes