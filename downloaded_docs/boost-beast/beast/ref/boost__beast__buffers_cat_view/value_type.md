##### [buffers\_cat\_view::value\_type](value_type.html "buffers_cat_view::value_type")

The type of buffer returned when dereferencing an iterator.

###### [Synopsis](value_type.html#beast.ref.boost__beast__buffers_cat_view.value_type.synopsis)

```programlisting
using value_type = see-below;
```

###### [Description](value_type.html#beast.ref.boost__beast__buffers_cat_view.value_type.description)

If every buffer sequence in the view is a *MutableBufferSequence*,
then [`value_type`](value_type.html "buffers_cat_view::value_type") will be `net::mutable_buffer`. Otherwise, [`value_type`](value_type.html "buffers_cat_view::value_type") will be `net::const_buffer`.