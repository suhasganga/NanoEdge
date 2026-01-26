###### [http::basic\_fields::find (1 of 2 overloads)](overload1.html "http::basic_fields::find (1 of 2 overloads)")

Returns an iterator to the case-insensitive matching field.

###### [Synopsis](overload1.html#beast.ref.boost__beast__http__basic_fields.find.overload1.synopsis)

```programlisting
const_iterator
find(
    field name) const;
```

###### [Description](overload1.html#beast.ref.boost__beast__http__basic_fields.find.overload1.description)

If more than one field with the specified name exists, the first field
defined by insertion order is returned.

###### [Parameters](overload1.html#beast.ref.boost__beast__http__basic_fields.find.overload1.parameters)

| Name | Description |
| --- | --- |
| `name` | The field name. |

###### [Return Value](overload1.html#beast.ref.boost__beast__http__basic_fields.find.overload1.return_value)

An iterator to the matching field, or [`end()`](../end.html "http::basic_fields::end")
if no match was found.