#### [http::is\_body](boost__beast__http__is_body.html "http::is_body")

Determine if a type meets the *Body* named requirements.

##### [Synopsis](boost__beast__http__is_body.html#beast.ref.boost__beast__http__is_body.synopsis)

Defined in header `<boost/beast/http/type_traits.hpp>`

```programlisting
template<
    class T>
using is_body = see-below;
```

##### [Description](boost__beast__http__is_body.html#beast.ref.boost__beast__http__is_body.description)

This alias template is `std::true_type`
if `T` meets the requirements,
otherwise it is `std::false_type`.

##### [Template Parameters](boost__beast__http__is_body.html#beast.ref.boost__beast__http__is_body.template_parameters)

| Type | Description |
| --- | --- |
| `T` | The type to test. |

##### [Example](boost__beast__http__is_body.html#beast.ref.boost__beast__http__is_body.example)

```programlisting
template < bool isRequest, class Body, class Fields>
void check_body(message<isRequest, Body, Fields> const &)
{
    static_assert (is_body<Body>::value,
        "Body type requirements not met" );
}
```