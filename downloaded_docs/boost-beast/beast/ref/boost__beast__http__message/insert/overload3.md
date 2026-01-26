###### [http::message::insert (3 of 8 overloads)](overload3.html "http::message::insert (3 of 8 overloads)")

(Inherited from [`http::basic_fields`](../../boost__beast__http__basic_fields.html "http::basic_fields"))

Insert a field.

###### [Synopsis](overload3.html#beast.ref.boost__beast__http__message.insert.overload3.synopsis)

```programlisting
void
insert(
    string_view name,
    string_view value);
```

###### [Description](overload3.html#beast.ref.boost__beast__http__message.insert.overload3.description)

If one or more fields with the same name already exist, the new field
will be inserted after the last field with the matching name, in serialization
order. The value can be an empty string.

###### [Parameters](overload3.html#beast.ref.boost__beast__http__message.insert.overload3.parameters)

| Name | Description |
| --- | --- |
| `name` | The field name. It is interpreted as a case-insensitive string. |
| `value` | The field value. |

###### [Exceptions](overload3.html#beast.ref.boost__beast__http__message.insert.overload3.exceptions)

| Type | Thrown On |
| --- | --- |
| `boost::system::system_error` | Thrown if an error occurs:  * If the size of `name`   exceeds [`max_name_size`](../max_name_size.html "http::message::max_name_size"),   the error code will be [`error::header_field_name_too_large`](../../boost__beast__http__error.html "http::error"). * If the size of `value`   exceeds [`max_value_size`](../max_value_size.html "http::message::max_value_size"),   the error code will be [`error::header_field_value_too_large`](../../boost__beast__http__error.html "http::error"). |