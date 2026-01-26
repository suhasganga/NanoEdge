#### [buffers\_prefix\_view](boost__beast__buffers_prefix_view.html "buffers_prefix_view")

A buffer sequence adaptor that shortens the sequence size.

##### [Synopsis](boost__beast__buffers_prefix_view.html#beast.ref.boost__beast__buffers_prefix_view.synopsis)

Defined in header `<boost/beast/core/buffers_prefix.hpp>`

```programlisting
template<
    class BufferSequence>
class buffers_prefix_view
```

##### [Types](boost__beast__buffers_prefix_view.html#beast.ref.boost__beast__buffers_prefix_view.types)

| Name | Description |
| --- | --- |
| **[const\_iterator](boost__beast__buffers_prefix_view/const_iterator.html "buffers_prefix_view::const_iterator")** | A bidirectional iterator type that may be used to read elements. |
| **[value\_type](boost__beast__buffers_prefix_view/value_type.html "buffers_prefix_view::value_type")** | The type for each element in the list of buffers. |

##### [Member Functions](boost__beast__buffers_prefix_view.html#beast.ref.boost__beast__buffers_prefix_view.member_functions)

| Name | Description |
| --- | --- |
| **[begin](boost__beast__buffers_prefix_view/begin.html "buffers_prefix_view::begin")** | Returns an iterator to the first buffer in the sequence. |
| **[buffers\_prefix\_view](boost__beast__buffers_prefix_view/buffers_prefix_view.html "buffers_prefix_view::buffers_prefix_view") [constructor]** | Copy Constructor.  — Construct a buffer sequence prefix.  — Construct a buffer sequence prefix in-place. |
| **[end](boost__beast__buffers_prefix_view/end.html "buffers_prefix_view::end")** | Returns an iterator to one past the last buffer in the sequence. |
| **[operator=](boost__beast__buffers_prefix_view/operator_eq_.html "buffers_prefix_view::operator=")** | Copy Assignment. |

##### [Description](boost__beast__buffers_prefix_view.html#beast.ref.boost__beast__buffers_prefix_view.description)

The class adapts a buffer sequence to efficiently represent a shorter subset
of the original list of buffers starting with the first byte of the original
sequence.

##### [Template Parameters](boost__beast__buffers_prefix_view.html#beast.ref.boost__beast__buffers_prefix_view.template_parameters)

| Type | Description |
| --- | --- |
| `BufferSequence` | The buffer sequence to adapt. |