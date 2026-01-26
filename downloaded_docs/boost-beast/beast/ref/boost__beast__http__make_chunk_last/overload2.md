##### [http::make\_chunk\_last (2 of 2 overloads)](overload2.html "http::make_chunk_last (2 of 2 overloads)")

Returns a [`chunk_last`](../boost__beast__http__chunk_last.html "http::chunk_last").

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__make_chunk_last.overload2.synopsis)

Defined in header `<boost/beast/http/chunk_encode.hpp>`

```programlisting
template<
    class Trailer,
    class... Args>
chunk_last< Trailer >
make_chunk_last(
    Trailer const& trailer,
    Args&&... args);
```

###### [Description](overload2.html#beast.ref.boost__beast__http__make_chunk_last.overload2.description)

This function construct and returns a complete [`chunk_last`](../boost__beast__http__chunk_last.html "http::chunk_last") for a last chunk containing
the specified trailers.

###### [Parameters](overload2.html#beast.ref.boost__beast__http__make_chunk_last.overload2.parameters)

| Name | Description |
| --- | --- |
| `trailer` | A ConstBufferSequence or |

###### [Remarks](overload2.html#beast.ref.boost__beast__http__make_chunk_last.overload2.remarks)

This function is provided as a notational convenience to omit specification
of the class template arguments.

###### [Parameters](overload2.html#beast.ref.boost__beast__http__make_chunk_last.overload2.parameters0)

| Name | Description |
| --- | --- |
| `args` | Optional arguments passed to the [`chunk_last`](../boost__beast__http__chunk_last.html "http::chunk_last") constructor. |