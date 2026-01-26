###### [http::header::erase (1 of 3 overloads)](overload1.html "http::header::erase (1 of 3 overloads)")

(Inherited from [`http::basic_fields`](../../boost__beast__http__basic_fields.html "http::basic_fields"))

Remove a field.

###### [Synopsis](overload1.html#beast.ref.boost__beast__http__header.erase.overload1.synopsis)

```programlisting
const_iterator
erase(
    const_iterator pos);
```

###### [Description](overload1.html#beast.ref.boost__beast__http__header.erase.overload1.description)

References and iterators to the erased elements are invalidated. Other
references and iterators are not affected.

###### [Parameters](overload1.html#beast.ref.boost__beast__http__header.erase.overload1.parameters)

| Name | Description |
| --- | --- |
| `pos` | An iterator to the element to remove. |

###### [Return Value](overload1.html#beast.ref.boost__beast__http__header.erase.overload1.return_value)

An iterator following the last removed element. If the iterator refers
to the last element, the [`end()`](../end.html "http::header::end")
iterator is returned.