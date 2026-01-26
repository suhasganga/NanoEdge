###### [http::chunk\_last::chunk\_last (3 of 4 overloads)](overload3.html "http::chunk_last::chunk_last (3 of 4 overloads)")

Constructor.

###### [Synopsis](overload3.html#beast.ref.boost__beast__http__chunk_last.chunk_last.overload3.synopsis)

```programlisting
template<
    class Allocator>
chunk_last(
    Trailer const& trailer,
    Allocator const& allocator);
```

###### [Parameters](overload3.html#beast.ref.boost__beast__http__chunk_last.chunk_last.overload3.parameters)

| Name | Description |
| --- | --- |
| `trailer` | The trailer to use. This type must meet the requirements of Fields. |
| `allocator` | The allocator to use for storing temporary data associated with the serialized trailer buffers. |