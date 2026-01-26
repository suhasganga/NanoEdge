###### [http::basic\_fields::insert (1 of 8 overloads)](overload1.html "http::basic_fields::insert (1 of 8 overloads)")

Insert a field.

###### [Synopsis](overload1.html#beast.ref.boost__beast__http__basic_fields.insert.overload1.synopsis)

```programlisting
void
insert(
    field name,
    string_view value);
```

###### [Description](overload1.html#beast.ref.boost__beast__http__basic_fields.insert.overload1.description)

If one or more fields with the same name already exist, the new field
will be inserted after the last field with the matching name, in serialization
order. The value can be an empty string.

###### [Parameters](overload1.html#beast.ref.boost__beast__http__basic_fields.insert.overload1.parameters)

| Name | Description |
| --- | --- |
| `name` | The field name. |
| `value` | The field value. |

###### [Exceptions](overload1.html#beast.ref.boost__beast__http__basic_fields.insert.overload1.exceptions)

| Type | Thrown On |
| --- | --- |
| `boost::system::system_error` | Thrown if an error occurs:  * If the size of `value`   exceeds [`max_value_size`](../max_value_size.html "http::basic_fields::max_value_size"),   the error code will be [`error::header_field_value_too_large`](../../boost__beast__http__error.html "http::error"). |