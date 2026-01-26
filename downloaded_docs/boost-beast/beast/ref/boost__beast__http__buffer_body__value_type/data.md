##### [http::buffer\_body::value\_type::data](data.html "http::buffer_body::value_type::data")

A pointer to a contiguous area of memory of [`size`](size.html "http::buffer_body::value_type::size") octets, else `nullptr`.

###### [Synopsis](data.html#beast.ref.boost__beast__http__buffer_body__value_type.data.synopsis)

```programlisting
void* data = nullptr;
```

###### [Description](data.html#beast.ref.boost__beast__http__buffer_body__value_type.data.description)

###### [When Serializing](data.html#beast.ref.boost__beast__http__buffer_body__value_type.data.when_serializing)

If this is `nullptr` and `more` is `true`,
the error [`error::need_buffer`](../boost__beast__http__error.html "http::error") will be returned from
[`serializer::get`](../boost__beast__http__serializer/get.html "http::serializer::get") Otherwise, the serializer
will use the memory pointed to by `data`
having `size` octets of valid
storage as the next buffer representing the body.

###### [When Parsing](data.html#beast.ref.boost__beast__http__buffer_body__value_type.data.when_parsing)

If this is `nullptr`, the error
[`error::need_buffer`](../boost__beast__http__error.html "http::error")
will be returned from [`parser::put`](../boost__beast__http__parser/put.html "http::parser::put"). Otherwise, the parser will
store body octets into the memory pointed to by `data`
having `size` octets of valid
storage. After octets are stored, the `data`
and `size` members are adjusted:
`data` is incremented to
point to the next octet after the data written, while `size`
is decremented to reflect the remaining space at the memory location pointed
to by `data`.