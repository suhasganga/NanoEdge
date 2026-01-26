###### [http::message::operator[] (2 of 2 overloads)](overload2.html "http::message::operator[] (2 of 2 overloads)")

(Inherited from [`http::basic_fields`](../../boost__beast__http__basic_fields.html "http::basic_fields"))

Returns the value for a case-insensitive matching header, or `""` if it does not exist.

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__message.operator__lb__rb_.overload2.synopsis)

```programlisting
string_view const
operator[](
    string_view name) const;
```

###### [Description](overload2.html#beast.ref.boost__beast__http__message.operator__lb__rb_.overload2.description)

If more than one field with the specified name exists, the first field
defined by insertion order is returned.

###### [Parameters](overload2.html#beast.ref.boost__beast__http__message.operator__lb__rb_.overload2.parameters)

| Name | Description |
| --- | --- |
| `name` | The name of the field. It is interpreted as a case-insensitive string. |