###### [http::basic\_fields::count (2 of 2 overloads)](overload2.html "http::basic_fields::count (2 of 2 overloads)")

Return the number of fields with the specified name.

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__basic_fields.count.overload2.synopsis)

```programlisting
std::size_t
count(
    string_view name) const;
```

###### [Parameters](overload2.html#beast.ref.boost__beast__http__basic_fields.count.overload2.parameters)

| Name | Description |
| --- | --- |
| `name` | The field name. It is interpreted as a case-insensitive string. |