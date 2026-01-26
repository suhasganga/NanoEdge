##### [http::header::swap](swap.html "http::header::swap")

(Inherited from [`http::basic_fields`](../boost__beast__http__basic_fields.html "http::basic_fields"))

Return a buffer sequence representing the trailers.

###### [Synopsis](swap.html#beast.ref.boost__beast__http__header.swap.synopsis)

```programlisting
void
swap(
    basic_fields& other);
```

###### [Description](swap.html#beast.ref.boost__beast__http__header.swap.description)

This function returns a buffer sequence holding the serialized representation
of the trailer fields promised in the Accept field. Before calling this
function the Accept field must contain the exact trailer fields desired.
Each field must also exist. Swap this container with another