###### [http::message::erase (2 of 3 overloads)](overload2.html "http::message::erase (2 of 3 overloads)")

(Inherited from [`http::basic_fields`](../../boost__beast__http__basic_fields.html "http::basic_fields"))

Remove all fields with the specified name.

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__message.erase.overload2.synopsis)

```programlisting
std::size_t
erase(
    field name);
```

###### [Description](overload2.html#beast.ref.boost__beast__http__message.erase.overload2.description)

All fields with the same field name are erased from the container. References
and iterators to the erased elements are invalidated. Other references
and iterators are not affected.

###### [Parameters](overload2.html#beast.ref.boost__beast__http__message.erase.overload2.parameters)

| Name | Description |
| --- | --- |
| `name` | The field name. |

###### [Return Value](overload2.html#beast.ref.boost__beast__http__message.erase.overload2.return_value)

The number of fields removed.