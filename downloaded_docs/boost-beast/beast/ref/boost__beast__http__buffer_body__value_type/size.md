##### [http::buffer\_body::value\_type::size](size.html "http::buffer_body::value_type::size")

The number of octets in the buffer pointed to by [`data`](data.html "http::buffer_body::value_type::data").

###### [Synopsis](size.html#beast.ref.boost__beast__http__buffer_body__value_type.size.synopsis)

```programlisting
std::size_t size = 0;
```

###### [Description](size.html#beast.ref.boost__beast__http__buffer_body__value_type.size.description)

###### [When Serializing](size.html#beast.ref.boost__beast__http__buffer_body__value_type.size.when_serializing)

If `data` is `nullptr` during serialization, this value
is ignored. Otherwise, it represents the number of valid body octets pointed
to by `data`.

###### [When Parsing](size.html#beast.ref.boost__beast__http__buffer_body__value_type.size.when_parsing)

The value of this field will be decremented during parsing to indicate
the number of remaining free octets in the buffer pointed to by `data`. When it reaches zero, the parser
will return [`error::need_buffer`](../boost__beast__http__error.html "http::error"), indicating to the
caller that the values of `data`
and `size` should be updated
to point to a new memory buffer.