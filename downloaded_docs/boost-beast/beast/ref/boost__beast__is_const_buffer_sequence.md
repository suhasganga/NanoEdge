#### [is\_const\_buffer\_sequence](boost__beast__is_const_buffer_sequence.html "is_const_buffer_sequence")

Determine if a list of types satisfy the *ConstBufferSequence*
requirements.

##### [Synopsis](boost__beast__is_const_buffer_sequence.html#beast.ref.boost__beast__is_const_buffer_sequence.synopsis)

Defined in header `<boost/beast/core/buffer_traits.hpp>`

```programlisting
template<
    class... BufferSequence>
using is_const_buffer_sequence = see-below;
```

##### [Description](boost__beast__is_const_buffer_sequence.html#beast.ref.boost__beast__is_const_buffer_sequence.description)

This metafunction is used to determine if all of the specified types meet
the requirements for constant buffer sequences. This type alias will be
`std::true_type` if each specified type meets
the requirements, otherwise, this type alias will be `std::false_type`.

##### [Template Parameters](boost__beast__is_const_buffer_sequence.html#beast.ref.boost__beast__is_const_buffer_sequence.template_parameters)

| Type | Description |
| --- | --- |
| `BufferSequence` | A list of zero or more types to check. If this list is empty, the resulting type alias will be `std::true_type`. |