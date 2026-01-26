##### [file\_stdio::open](open.html "file_stdio::open")

Open a file at the given path with the specified mode.

###### [Synopsis](open.html#beast.ref.boost__beast__file_stdio.open.synopsis)

```programlisting
void
open(
    char const* path,
    file_mode mode,
    error_code& ec);
```

###### [Parameters](open.html#beast.ref.boost__beast__file_stdio.open.parameters)

| Name | Description |
| --- | --- |
| `path` | The utf-8 encoded path to the file |
| `mode` | The file mode to use |
| `ec` | Set to the error, if any occurred |