###### [http::header::equal\_range (1 of 2 overloads)](overload1.html "http::header::equal_range (1 of 2 overloads)")

(Inherited from [`http::basic_fields`](../../boost__beast__http__basic_fields.html "http::basic_fields"))

Returns a range of iterators to the fields with the specified name.

###### [Synopsis](overload1.html#beast.ref.boost__beast__http__header.equal_range.overload1.synopsis)

```programlisting
std::pair< const_iterator, const_iterator >
equal_range(
    field name) const;
```

###### [Description](overload1.html#beast.ref.boost__beast__http__header.equal_range.overload1.description)

This function returns the first and last iterators to the ordered fields
with the specified name.

###### [Remarks](overload1.html#beast.ref.boost__beast__http__header.equal_range.overload1.remarks)

The fields represented by the range are ordered. Its elements are guaranteed
to match the field ordering of the message. This means users do not need
to sort this range when comparing fields of the same name in different
messages.

###### [Parameters](overload1.html#beast.ref.boost__beast__http__header.equal_range.overload1.parameters)

| Name | Description |
| --- | --- |
| `name` | The field name. |

###### [Return Value](overload1.html#beast.ref.boost__beast__http__header.equal_range.overload1.return_value)

A range of iterators to fields with the same name, otherwise an empty
range.