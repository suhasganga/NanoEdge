###### [http::header::at (1 of 2 overloads)](overload1.html "http::header::at (1 of 2 overloads)")

(Inherited from [`http::basic_fields`](../../boost__beast__http__basic_fields.html "http::basic_fields"))

Returns the value for a field, or throws an exception.

###### [Synopsis](overload1.html#beast.ref.boost__beast__http__header.at.overload1.synopsis)

```programlisting
string_view const
at(
    field name) const;
```

###### [Description](overload1.html#beast.ref.boost__beast__http__header.at.overload1.description)

If more than one field with the specified name exists, the first field
defined by insertion order is returned.

###### [Parameters](overload1.html#beast.ref.boost__beast__http__header.at.overload1.parameters)

| Name | Description |
| --- | --- |
| `name` | The name of the field. |

###### [Return Value](overload1.html#beast.ref.boost__beast__http__header.at.overload1.return_value)

The field value.

###### [Exceptions](overload1.html#beast.ref.boost__beast__http__header.at.overload1.exceptions)

| Type | Thrown On |
| --- | --- |
| `std::out_of_range` | if the field is not found. |