###### [http::basic\_fields::swap (2 of 2 overloads)](overload2.html "http::basic_fields::swap (2 of 2 overloads)")

Return a buffer sequence representing the trailers.

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__basic_fields.swap.overload2.synopsis)

```programlisting
void
swap(
    basic_fields& other);
```

###### [Description](overload2.html#beast.ref.boost__beast__http__basic_fields.swap.overload2.description)

This function returns a buffer sequence holding the serialized representation
of the trailer fields promised in the Accept field. Before calling this
function the Accept field must contain the exact trailer fields desired.
Each field must also exist. Swap this container with another