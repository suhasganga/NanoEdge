###### [http::header::set (3 of 4 overloads)](overload3.html "http::header::set (3 of 4 overloads)")

(Inherited from [`http::basic_fields`](../../boost__beast__http__basic_fields.html "http::basic_fields"))

Set a field value, removing any other instances of that field.

###### [Synopsis](overload3.html#beast.ref.boost__beast__http__header.set.overload3.synopsis)

```programlisting
void
set(
    string_view name,
    string_view value);
```

###### [Description](overload3.html#beast.ref.boost__beast__http__header.set.overload3.description)

First removes any values with matching field names, then inserts the
new field value. The value can be an empty string.

###### [Parameters](overload3.html#beast.ref.boost__beast__http__header.set.overload3.parameters)

| Name | Description |
| --- | --- |
| `name` | The field name. It is interpreted as a case-insensitive string. |
| `value` | The field value. |

###### [Exceptions](overload3.html#beast.ref.boost__beast__http__header.set.overload3.exceptions)

| Type | Thrown On |
| --- | --- |
| `boost::system::system_error` | Thrown if an error occurs:  * If the size of `name`   exceeds [`max_name_size`](../max_name_size.html "http::header::max_name_size"),   the error code will be [`error::header_field_name_too_large`](../../boost__beast__http__error.html "http::error"). * If the size of `value`   exceeds [`max_value_size`](../max_value_size.html "http::header::max_value_size"),   the error code will be [`error::header_field_value_too_large`](../../boost__beast__http__error.html "http::error"). |