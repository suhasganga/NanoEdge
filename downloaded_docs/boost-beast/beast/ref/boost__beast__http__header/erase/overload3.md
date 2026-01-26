###### [http::header::erase (3 of 3 overloads)](overload3.html "http::header::erase (3 of 3 overloads)")

(Inherited from [`http::basic_fields`](../../boost__beast__http__basic_fields.html "http::basic_fields"))

Remove all fields with the specified name.

###### [Synopsis](overload3.html#beast.ref.boost__beast__http__header.erase.overload3.synopsis)

```programlisting
std::size_t
erase(
    string_view name);
```

###### [Description](overload3.html#beast.ref.boost__beast__http__header.erase.overload3.description)

All fields with the same field name are erased from the container. References
and iterators to the erased elements are invalidated. Other references
and iterators are not affected.

###### [Parameters](overload3.html#beast.ref.boost__beast__http__header.erase.overload3.parameters)

| Name | Description |
| --- | --- |
| `name` | The field name. It is interpreted as a case-insensitive string. |

###### [Return Value](overload3.html#beast.ref.boost__beast__http__header.erase.overload3.return_value)

The number of fields removed.