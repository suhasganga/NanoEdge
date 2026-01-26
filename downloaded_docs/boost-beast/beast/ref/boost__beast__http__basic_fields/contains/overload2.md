###### [http::basic\_fields::contains (2 of 2 overloads)](overload2.html "http::basic_fields::contains (2 of 2 overloads)")

Returns `true` if there is
a field with the specified name.

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__basic_fields.contains.overload2.synopsis)

```programlisting
bool
contains(
    string_view name) const;
```

###### [Parameters](overload2.html#beast.ref.boost__beast__http__basic_fields.contains.overload2.parameters)

| Name | Description |
| --- | --- |
| `name` | The field name. It is interpreted as a case-insensitive string. |