###### [http::message::operator[] (1 of 2 overloads)](overload1.html "http::message::operator[] (1 of 2 overloads)")

(Inherited from [`http::basic_fields`](../../boost__beast__http__basic_fields.html "http::basic_fields"))

Returns the value for a field, or `""`
if it does not exist.

###### [Synopsis](overload1.html#beast.ref.boost__beast__http__message.operator__lb__rb_.overload1.synopsis)

```programlisting
string_view const
operator[](
    field name) const;
```

###### [Description](overload1.html#beast.ref.boost__beast__http__message.operator__lb__rb_.overload1.description)

If more than one field with the specified name exists, the first field
defined by insertion order is returned.

###### [Parameters](overload1.html#beast.ref.boost__beast__http__message.operator__lb__rb_.overload1.parameters)

| Name | Description |
| --- | --- |
| `name` | The name of the field. |