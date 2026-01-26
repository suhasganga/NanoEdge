##### [http::basic\_chunk\_extensions::value\_type](value_type.html "http::basic_chunk_extensions::value_type")

The type of value when iterating.

###### [Synopsis](value_type.html#beast.ref.boost__beast__http__basic_chunk_extensions.value_type.synopsis)

```programlisting
using value_type = std::pair< string_view, string_view >;
```

###### [Description](value_type.html#beast.ref.boost__beast__http__basic_chunk_extensions.value_type.description)

The first element of the pair is the name, and the second element is the
value which may be empty. The value is stored in its raw representation,
without quotes or escapes.