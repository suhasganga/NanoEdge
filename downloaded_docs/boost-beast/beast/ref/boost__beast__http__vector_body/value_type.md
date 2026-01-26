##### [http::vector\_body::value\_type](value_type.html "http::vector_body::value_type")

The type of container used for the body.

###### [Synopsis](value_type.html#beast.ref.boost__beast__http__vector_body.value_type.synopsis)

```programlisting
using value_type = std::vector< T, Allocator >;
```

###### [Description](value_type.html#beast.ref.boost__beast__http__vector_body.value_type.description)

This determines the type of [`message::body`](../boost__beast__http__message/body.html "http::message::body") when this body type is used
with a message container.