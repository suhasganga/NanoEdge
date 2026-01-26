#### [buffers\_cat\_view](boost__beast__buffers_cat_view.html "buffers_cat_view")

A buffer sequence representing a concatenation of buffer sequences.

##### [Synopsis](boost__beast__buffers_cat_view.html#beast.ref.boost__beast__buffers_cat_view.synopsis)

Defined in header `<boost/beast/core/buffers_cat.hpp>`

```programlisting
template<
    class... Buffers>
class buffers_cat_view
```

##### [Types](boost__beast__buffers_cat_view.html#beast.ref.boost__beast__buffers_cat_view.types)

| Name | Description |
| --- | --- |
| **[value\_type](boost__beast__buffers_cat_view/value_type.html "buffers_cat_view::value_type")** | The type of buffer returned when dereferencing an iterator. |

##### [Member Functions](boost__beast__buffers_cat_view.html#beast.ref.boost__beast__buffers_cat_view.member_functions)

| Name | Description |
| --- | --- |
| **[begin](boost__beast__buffers_cat_view/begin.html "buffers_cat_view::begin")** | Returns an iterator to the first buffer in the sequence. |
| **[buffers\_cat\_view](boost__beast__buffers_cat_view/buffers_cat_view.html "buffers_cat_view::buffers_cat_view") [constructor]** | Copy Constructor.  — Constructor. |
| **[end](boost__beast__buffers_cat_view/end.html "buffers_cat_view::end")** | Returns an iterator to one past the last buffer in the sequence. |
| **[operator=](boost__beast__buffers_cat_view/operator_eq_.html "buffers_cat_view::operator=")** | Copy Assignment. |

##### [See Also](boost__beast__buffers_cat_view.html#beast.ref.boost__beast__buffers_cat_view.see_also)

[`buffers_cat`](boost__beast__buffers_cat.html "buffers_cat")