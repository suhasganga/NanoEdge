###### [http::header::equal\_range (2 of 2 overloads)](overload2.html "http::header::equal_range (2 of 2 overloads)")

(Inherited from [`http::basic_fields`](../../boost__beast__http__basic_fields.html "http::basic_fields"))

Returns a range of iterators to the fields with the specified name.

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__header.equal_range.overload2.synopsis)

```programlisting
std::pair< const_iterator, const_iterator >
equal_range(
    string_view name) const;
```

###### [Description](overload2.html#beast.ref.boost__beast__http__header.equal_range.overload2.description)

This function returns the first and last iterators to the ordered fields
with the specified name.

###### [Remarks](overload2.html#beast.ref.boost__beast__http__header.equal_range.overload2.remarks)

The fields represented by the range are ordered. Its elements are guaranteed
to match the field ordering of the message. This means users do not need
to sort this range when comparing fields of the same name in different
messages.

###### [Parameters](overload2.html#beast.ref.boost__beast__http__header.equal_range.overload2.parameters)

| Name | Description |
| --- | --- |
| `name` | The field name. |

###### [Return Value](overload2.html#beast.ref.boost__beast__http__header.equal_range.overload2.return_value)

A range of iterators to fields with the same name, otherwise an empty
range.