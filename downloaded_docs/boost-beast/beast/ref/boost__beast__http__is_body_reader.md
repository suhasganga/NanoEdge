#### [http::is\_body\_reader](boost__beast__http__is_body_reader.html "http::is_body_reader")

Determine if a type has a nested *BodyReader*.

##### [Synopsis](boost__beast__http__is_body_reader.html#beast.ref.boost__beast__http__is_body_reader.synopsis)

Defined in header `<boost/beast/http/type_traits.hpp>`

```programlisting
template<
    class T>
using is_body_reader = see-below;
```

##### [Description](boost__beast__http__is_body_reader.html#beast.ref.boost__beast__http__is_body_reader.description)

This alias template is `std::true_type`
when:

* `T` has a nested type named
  `reader`
* `reader` meets the requirements
  of *BodyReader*.

##### [Template Parameters](boost__beast__http__is_body_reader.html#beast.ref.boost__beast__http__is_body_reader.template_parameters)

| Type | Description |
| --- | --- |
| `T` | The body type to test. |

##### [Example](boost__beast__http__is_body_reader.html#beast.ref.boost__beast__http__is_body_reader.example)

```programlisting
template < bool isRequest, class Body, class Fields>
void check_can_parse(message<isRequest, Body, Fields>&)
{
    static_assert (is_body_reader<Body>::value,
        "Cannot parse Body, no reader" );
}
```