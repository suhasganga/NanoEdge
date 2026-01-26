###### [http::header::find (2 of 2 overloads)](overload2.html "http::header::find (2 of 2 overloads)")

(Inherited from [`http::basic_fields`](../../boost__beast__http__basic_fields.html "http::basic_fields"))

Returns an iterator to the case-insensitive matching field name.

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__header.find.overload2.synopsis)

```programlisting
const_iterator
find(
    string_view name) const;
```

###### [Description](overload2.html#beast.ref.boost__beast__http__header.find.overload2.description)

If more than one field with the specified name exists, the first field
defined by insertion order is returned.

###### [Parameters](overload2.html#beast.ref.boost__beast__http__header.find.overload2.parameters)

| Name | Description |
| --- | --- |
| `name` | The field name. It is interpreted as a case-insensitive string. |

###### [Return Value](overload2.html#beast.ref.boost__beast__http__header.find.overload2.return_value)

An iterator to the matching field, or [`end()`](../end.html "http::header::end")
if no match was found.