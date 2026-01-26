###### [http::header::set (1 of 4 overloads)](overload1.html "http::header::set (1 of 4 overloads)")

(Inherited from [`http::basic_fields`](../../boost__beast__http__basic_fields.html "http::basic_fields"))

Set a field value, removing any other instances of that field.

###### [Synopsis](overload1.html#beast.ref.boost__beast__http__header.set.overload1.synopsis)

```programlisting
void
set(
    field name,
    string_view value);
```

###### [Description](overload1.html#beast.ref.boost__beast__http__header.set.overload1.description)

First removes any values with matching field names, then inserts the
new field value. The value may be an empty string.

###### [Parameters](overload1.html#beast.ref.boost__beast__http__header.set.overload1.parameters)

| Name | Description |
| --- | --- |
| `name` | The field name. |
| `value` | The field value. |

###### [Exceptions](overload1.html#beast.ref.boost__beast__http__header.set.overload1.exceptions)

| Type | Thrown On |
| --- | --- |
| `boost::system::system_error` | Thrown if an error occurs:  * If the size of `value`   exceeds [`max_value_size`](../max_value_size.html "http::header::max_value_size"),   the error code will be [`error::header_field_value_too_large`](../../boost__beast__http__error.html "http::error"). |