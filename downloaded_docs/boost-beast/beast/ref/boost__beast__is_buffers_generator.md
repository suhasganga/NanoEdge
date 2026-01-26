#### [is\_buffers\_generator](boost__beast__is_buffers_generator.html "is_buffers_generator")

Determine if type satisfies the *BuffersGenerator* requirements.

##### [Synopsis](boost__beast__is_buffers_generator.html#beast.ref.boost__beast__is_buffers_generator.synopsis)

Defined in header `<boost/beast/core/buffers_generator.hpp>`

```programlisting
template<
    class T>
struct is_buffers_generator :
    public integral_constant< bool, automatically_determined >
```

##### [Description](boost__beast__is_buffers_generator.html#beast.ref.boost__beast__is_buffers_generator.description)

This metafunction is used to determine if the specified type meets the requirements
for a buffers generator.

The static member `value` will
evaluate to `true` if so, `false` otherwise.

##### [Template Parameters](boost__beast__is_buffers_generator.html#beast.ref.boost__beast__is_buffers_generator.template_parameters)

| Type | Description |
| --- | --- |
| `T` | a type to check |