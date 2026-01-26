###### [buffers\_cat\_view::buffers\_cat\_view (2 of 2 overloads)](overload2.html "buffers_cat_view::buffers_cat_view (2 of 2 overloads)")

Constructor.

###### [Synopsis](overload2.html#beast.ref.boost__beast__buffers_cat_view.buffers_cat_view.overload2.synopsis)

```programlisting
buffers_cat_view(
    Buffers const&... buffers);
```

###### [Parameters](overload2.html#beast.ref.boost__beast__buffers_cat_view.buffers_cat_view.overload2.parameters)

| Name | Description |
| --- | --- |
| `buffers` | The list of buffer sequences to concatenate. Copies of the arguments will be maintained for the lifetime of the concatenated sequence; however, the ownership of the memory buffers themselves is not transferred. |