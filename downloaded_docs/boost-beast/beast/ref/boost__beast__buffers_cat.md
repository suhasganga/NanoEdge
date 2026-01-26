#### [buffers\_cat](boost__beast__buffers_cat.html "buffers_cat")

Concatenate 1 or more buffer sequences.

##### [Synopsis](boost__beast__buffers_cat.html#beast.ref.boost__beast__buffers_cat.synopsis)

Defined in header `<boost/beast/core/buffers_cat.hpp>`

```programlisting
template<
    class... BufferSequence>
buffers_cat_view< BufferSequence... >
buffers_cat(
    BufferSequence const&... buffers);
```

##### [Description](boost__beast__buffers_cat.html#beast.ref.boost__beast__buffers_cat.description)

This function returns a constant or mutable buffer sequence which, when iterated,
efficiently concatenates the input buffer sequences. Copies of the arguments
passed will be made; however, the returned object does not take ownership
of the underlying memory. The application is still responsible for managing
the lifetime of the referenced memory.

##### [Parameters](boost__beast__buffers_cat.html#beast.ref.boost__beast__buffers_cat.parameters)

| Name | Description |
| --- | --- |
| `buffers` | The list of buffer sequences to concatenate. |

##### [Return Value](boost__beast__buffers_cat.html#beast.ref.boost__beast__buffers_cat.return_value)

A new buffer sequence that represents the concatenation of the input buffer
sequences. This buffer sequence will be a *MutableBufferSequence*
if each of the passed buffer sequences is also a *MutableBufferSequence*;
otherwise the returned buffer sequence will be a *ConstBufferSequence*.

##### [See Also](boost__beast__buffers_cat.html#beast.ref.boost__beast__buffers_cat.see_also)

[`buffers_cat_view`](boost__beast__buffers_cat_view.html "buffers_cat_view")