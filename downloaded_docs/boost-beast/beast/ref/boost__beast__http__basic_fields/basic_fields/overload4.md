###### [http::basic\_fields::basic\_fields (4 of 8 overloads)](overload4.html "http::basic_fields::basic_fields (4 of 8 overloads)")

Move constructor.

###### [Synopsis](overload4.html#beast.ref.boost__beast__http__basic_fields.basic_fields.overload4.synopsis)

```programlisting
basic_fields(
    basic_fields&&,
    Allocator const& alloc);
```

###### [Description](overload4.html#beast.ref.boost__beast__http__basic_fields.basic_fields.overload4.description)

The state of the moved-from object is as if constructed using the same
allocator.

###### [Parameters](overload4.html#beast.ref.boost__beast__http__basic_fields.basic_fields.overload4.parameters)

| Name | Description |
| --- | --- |
| `alloc` | The allocator to use. |