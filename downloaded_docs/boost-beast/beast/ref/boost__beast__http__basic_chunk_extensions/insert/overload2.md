###### [http::basic\_chunk\_extensions::insert (2 of 2 overloads)](overload2.html "http::basic_chunk_extensions::insert (2 of 2 overloads)")

Insert an extension value.

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__basic_chunk_extensions.insert.overload2.synopsis)

```programlisting
void
insert(
    string_view name,
    string_view value);
```

###### [Parameters](overload2.html#beast.ref.boost__beast__http__basic_chunk_extensions.insert.overload2.parameters)

| Name | Description |
| --- | --- |
| `name` | The name of the extension |
| `value` | The value to insert. Depending on the contents, the serialized extension may use a quoted string. |