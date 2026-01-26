###### [http::header::count (2 of 2 overloads)](overload2.html "http::header::count (2 of 2 overloads)")

(Inherited from [`http::basic_fields`](../../boost__beast__http__basic_fields.html "http::basic_fields"))

Return the number of fields with the specified name.

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__header.count.overload2.synopsis)

```programlisting
std::size_t
count(
    string_view name) const;
```

###### [Parameters](overload2.html#beast.ref.boost__beast__http__header.count.overload2.parameters)

| Name | Description |
| --- | --- |
| `name` | The field name. It is interpreted as a case-insensitive string. |