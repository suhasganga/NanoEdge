##### [http::basic\_file\_body::value\_type::seek](seek.html "http::basic_file_body::value_type::seek")

Set the cursor position of the file.

###### [Synopsis](seek.html#beast.ref.boost__beast__http__basic_file_body__value_type.seek.synopsis)

```programlisting
void
seek(
    std::uint64_t offset,
    error_code& ec);
```

###### [Description](seek.html#beast.ref.boost__beast__http__basic_file_body__value_type.seek.description)

This function can be used to move the cursor of the file ahead so that
only a part gets read. This file will also adjust the [`value_type`](../boost__beast__http__basic_file_body__value_type.html "http::basic_file_body::value_type"), in case the file is
already part of a body.

###### [Parameters](seek.html#beast.ref.boost__beast__http__basic_file_body__value_type.seek.parameters)

| Name | Description |
| --- | --- |
| `offset` | The offset in bytes from the beginning of the file |
| `ec` | Set to the error, if any occurred |