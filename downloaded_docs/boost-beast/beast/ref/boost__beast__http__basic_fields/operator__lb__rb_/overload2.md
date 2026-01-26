###### [http::basic\_fields::operator[] (2 of 2 overloads)](overload2.html "http::basic_fields::operator[] (2 of 2 overloads)")

Returns the value for a case-insensitive matching header, or `""` if it does not exist.

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__basic_fields.operator__lb__rb_.overload2.synopsis)

```programlisting
string_view const
operator[](
    string_view name) const;
```

###### [Description](overload2.html#beast.ref.boost__beast__http__basic_fields.operator__lb__rb_.overload2.description)

If more than one field with the specified name exists, the first field
defined by insertion order is returned.

###### [Parameters](overload2.html#beast.ref.boost__beast__http__basic_fields.operator__lb__rb_.overload2.parameters)

| Name | Description |
| --- | --- |
| `name` | The name of the field. It is interpreted as a case-insensitive string. |