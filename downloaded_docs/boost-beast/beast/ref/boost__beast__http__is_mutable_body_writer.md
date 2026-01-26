#### [http::is\_mutable\_body\_writer](boost__beast__http__is_mutable_body_writer.html "http::is_mutable_body_writer")

Determine if a type has a nested *BodyWriter*.

##### [Synopsis](boost__beast__http__is_mutable_body_writer.html#beast.ref.boost__beast__http__is_mutable_body_writer.synopsis)

Defined in header `<boost/beast/http/type_traits.hpp>`

```programlisting
template<
    class T>
using is_mutable_body_writer = see-below;
```

##### [Description](boost__beast__http__is_mutable_body_writer.html#beast.ref.boost__beast__http__is_mutable_body_writer.description)

This alias template is `std::true_type`
when:

* `T` has a nested type named
  `writer`
* `writer` meets the requirements
  of *BodyWriter*.

##### [Template Parameters](boost__beast__http__is_mutable_body_writer.html#beast.ref.boost__beast__http__is_mutable_body_writer.template_parameters)

| Type | Description |
| --- | --- |
| `T` | The body type to test. |