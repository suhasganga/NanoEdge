###### [http::basic\_fields::operator[] (1 of 2 overloads)](overload1.html "http::basic_fields::operator[] (1 of 2 overloads)")

Returns the value for a field, or `""`
if it does not exist.

###### [Synopsis](overload1.html#beast.ref.boost__beast__http__basic_fields.operator__lb__rb_.overload1.synopsis)

```programlisting
string_view const
operator[](
    field name) const;
```

###### [Description](overload1.html#beast.ref.boost__beast__http__basic_fields.operator__lb__rb_.overload1.description)

If more than one field with the specified name exists, the first field
defined by insertion order is returned.

###### [Parameters](overload1.html#beast.ref.boost__beast__http__basic_fields.operator__lb__rb_.overload1.parameters)

| Name | Description |
| --- | --- |
| `name` | The name of the field. |