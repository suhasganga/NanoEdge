##### [http::buffer\_body::value\_type::more](more.html "http::buffer_body::value_type::more")

`true` if this is not the last
buffer.

###### [Synopsis](more.html#beast.ref.boost__beast__http__buffer_body__value_type.more.synopsis)

```programlisting
bool more = true;
```

###### [Description](more.html#beast.ref.boost__beast__http__buffer_body__value_type.more.description)

###### [When Serializing](more.html#beast.ref.boost__beast__http__buffer_body__value_type.more.when_serializing)

If this is `true` and `data` is `nullptr`,
the error [`error::need_buffer`](../boost__beast__http__error.html "http::error") will be returned from
[`serializer::get`](../boost__beast__http__serializer/get.html "http::serializer::get")

###### [When Parsing](more.html#beast.ref.boost__beast__http__buffer_body__value_type.more.when_parsing)

This field is not used during parsing.