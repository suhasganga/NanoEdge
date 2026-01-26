###### [http::header::at (2 of 2 overloads)](overload2.html "http::header::at (2 of 2 overloads)")

(Inherited from [`http::basic_fields`](../../boost__beast__http__basic_fields.html "http::basic_fields"))

Returns the value for a field, or throws an exception.

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__header.at.overload2.synopsis)

```programlisting
string_view const
at(
    string_view name) const;
```

###### [Description](overload2.html#beast.ref.boost__beast__http__header.at.overload2.description)

If more than one field with the specified name exists, the first field
defined by insertion order is returned.

###### [Parameters](overload2.html#beast.ref.boost__beast__http__header.at.overload2.parameters)

| Name | Description |
| --- | --- |
| `name` | The name of the field. It is interpreted as a case-insensitive string. |

###### [Return Value](overload2.html#beast.ref.boost__beast__http__header.at.overload2.return_value)

The field value.

###### [Exceptions](overload2.html#beast.ref.boost__beast__http__header.at.overload2.exceptions)

| Type | Thrown On |
| --- | --- |
| `std::out_of_range` | if the field is not found. |