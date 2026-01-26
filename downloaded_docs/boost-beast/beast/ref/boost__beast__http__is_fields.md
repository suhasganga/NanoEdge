#### [http::is\_fields](boost__beast__http__is_fields.html "http::is_fields")

Determine if a type meets the *Fields* named requirements.

##### [Synopsis](boost__beast__http__is_fields.html#beast.ref.boost__beast__http__is_fields.synopsis)

Defined in header `<boost/beast/http/type_traits.hpp>`

```programlisting
template<
    class T>
using is_fields = see-below;
```

##### [Description](boost__beast__http__is_fields.html#beast.ref.boost__beast__http__is_fields.description)

This alias template is `std::true_type`
if `T` meets the requirements,
otherwise it is `std::false_type`.

##### [Template Parameters](boost__beast__http__is_fields.html#beast.ref.boost__beast__http__is_fields.template_parameters)

| Type | Description |
| --- | --- |
| `T` | The type to test. |

##### [Example](boost__beast__http__is_fields.html#beast.ref.boost__beast__http__is_fields.example)

Use with `static_assert`:

```programlisting
template < bool isRequest, class Body, class Fields>
void f(message<isRequest, Body, Fields> const &)
{
    static_assert (is_fields<Fields>::value,
        "Fields type requirements not met" );
...
```

Use with `std::enable_if` (SFINAE):

```programlisting
template < bool isRequest, class Body, class Fields>
typename std::enable_if<is_fields<Fields>::value>::type
f(message<isRequest, Body, Fields> const &);
```