###### [http::basic\_fields::erase (1 of 3 overloads)](overload1.html "http::basic_fields::erase (1 of 3 overloads)")

Remove a field.

###### [Synopsis](overload1.html#beast.ref.boost__beast__http__basic_fields.erase.overload1.synopsis)

```programlisting
const_iterator
erase(
    const_iterator pos);
```

###### [Description](overload1.html#beast.ref.boost__beast__http__basic_fields.erase.overload1.description)

References and iterators to the erased elements are invalidated. Other
references and iterators are not affected.

###### [Parameters](overload1.html#beast.ref.boost__beast__http__basic_fields.erase.overload1.parameters)

| Name | Description |
| --- | --- |
| `pos` | An iterator to the element to remove. |

###### [Return Value](overload1.html#beast.ref.boost__beast__http__basic_fields.erase.overload1.return_value)

An iterator following the last removed element. If the iterator refers
to the last element, the [`end()`](../end.html "http::basic_fields::end")
iterator is returned.