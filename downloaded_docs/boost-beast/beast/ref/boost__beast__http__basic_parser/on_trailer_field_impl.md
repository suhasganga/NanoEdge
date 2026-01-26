##### [http::basic\_parser::on\_trailer\_field\_impl](on_trailer_field_impl.html "http::basic_parser::on_trailer_field_impl")

Called once for each complete field in the HTTP trailer header.

###### [Synopsis](on_trailer_field_impl.html#beast.ref.boost__beast__http__basic_parser.on_trailer_field_impl.synopsis)

```programlisting
void
on_trailer_field_impl(
    field name,
    string_view name_string,
    string_view value,
    error_code& ec);
```

###### [Description](on_trailer_field_impl.html#beast.ref.boost__beast__http__basic_parser.on_trailer_field_impl.description)

This virtual function is invoked for each field that is received while
parsing the trailer part of a chunked HTTP message.

###### [Parameters](on_trailer_field_impl.html#beast.ref.boost__beast__http__basic_parser.on_trailer_field_impl.parameters)

| Name | Description |
| --- | --- |
| `name` | The known field enum value. If the name of the field is not recognized, this value will be [`field::unknown`](../boost__beast__http__field.html "http::field"). |
| `name_string` | The exact name of the field as received from the input, represented as a string. |
| `value` | A string holding the value of the field. |
| `ec` | An output parameter which the function may set to indicate an error. The error will be clear before this function is invoked. |