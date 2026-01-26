##### [http::basic\_file\_body::value\_type::reset](reset.html "http::basic_file_body::value_type::reset")

Set the open file.

###### [Synopsis](reset.html#beast.ref.boost__beast__http__basic_file_body__value_type.reset.synopsis)

```programlisting
void
reset(
    File&& file,
    error_code& ec);
```

###### [Description](reset.html#beast.ref.boost__beast__http__basic_file_body__value_type.reset.description)

This function is used to set the open file. Any previously set file will
be closed.

###### [Parameters](reset.html#beast.ref.boost__beast__http__basic_file_body__value_type.reset.parameters)

| Name | Description |
| --- | --- |
| `file` | The file to set. The file must be open or else an error occurs |
| `ec` | Set to the error, if any occurred |