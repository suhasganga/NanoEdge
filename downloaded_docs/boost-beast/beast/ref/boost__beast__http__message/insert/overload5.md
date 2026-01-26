###### [http::message::insert (5 of 8 overloads)](overload5.html "http::message::insert (5 of 8 overloads)")

(Inherited from [`http::basic_fields`](../../boost__beast__http__basic_fields.html "http::basic_fields"))

Insert a field.

###### [Synopsis](overload5.html#beast.ref.boost__beast__http__message.insert.overload5.synopsis)

```programlisting
void
insert(
    field name,
    string_view name_string,
    string_view value);
```

###### [Description](overload5.html#beast.ref.boost__beast__http__message.insert.overload5.description)

If one or more fields with the same name already exist, the new field
will be inserted after the last field with the matching name, in serialization
order. The value can be an empty string.

###### [Parameters](overload5.html#beast.ref.boost__beast__http__message.insert.overload5.parameters)

| Name | Description |
| --- | --- |
| `name` | The field name. |
| `name_string` | The literal text corresponding to the field name. If name != [`field::unknown`](../../boost__beast__http__field.html "http::field"), then this value must be equal to `to_string(name)` using a case-insensitive comparison, otherwise the behavior is undefined. |
| `value` | The field value. |

###### [Exceptions](overload5.html#beast.ref.boost__beast__http__message.insert.overload5.exceptions)

| Type | Thrown On |
| --- | --- |
| `boost::system::system_error` | Thrown if an error occurs:  * If the size of `name_string`   exceeds [`max_name_size`](../max_name_size.html "http::message::max_name_size"),   the error code will be [`error::header_field_name_too_large`](../../boost__beast__http__error.html "http::error"). * If the size of `value`   exceeds [`max_value_size`](../max_value_size.html "http::message::max_value_size"),   the error code will be [`error::header_field_value_too_large`](../../boost__beast__http__error.html "http::error"). |