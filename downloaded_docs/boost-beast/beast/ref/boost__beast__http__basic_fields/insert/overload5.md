###### [http::basic\_fields::insert (5 of 8 overloads)](overload5.html "http::basic_fields::insert (5 of 8 overloads)")

Insert a field.

###### [Synopsis](overload5.html#beast.ref.boost__beast__http__basic_fields.insert.overload5.synopsis)

```programlisting
void
insert(
    field name,
    string_view name_string,
    string_view value);
```

###### [Description](overload5.html#beast.ref.boost__beast__http__basic_fields.insert.overload5.description)

If one or more fields with the same name already exist, the new field
will be inserted after the last field with the matching name, in serialization
order. The value can be an empty string.

###### [Parameters](overload5.html#beast.ref.boost__beast__http__basic_fields.insert.overload5.parameters)

| Name | Description |
| --- | --- |
| `name` | The field name. |
| `name_string` | The literal text corresponding to the field name. If name != [`field::unknown`](../../boost__beast__http__field.html "http::field"), then this value must be equal to `to_string(name)` using a case-insensitive comparison, otherwise the behavior is undefined. |
| `value` | The field value. |

###### [Exceptions](overload5.html#beast.ref.boost__beast__http__basic_fields.insert.overload5.exceptions)

| Type | Thrown On |
| --- | --- |
| `boost::system::system_error` | Thrown if an error occurs:  * If the size of `name_string`   exceeds [`max_name_size`](../max_name_size.html "http::basic_fields::max_name_size"),   the error code will be [`error::header_field_name_too_large`](../../boost__beast__http__error.html "http::error"). * If the size of `value`   exceeds [`max_value_size`](../max_value_size.html "http::basic_fields::max_value_size"),   the error code will be [`error::header_field_value_too_large`](../../boost__beast__http__error.html "http::error"). |