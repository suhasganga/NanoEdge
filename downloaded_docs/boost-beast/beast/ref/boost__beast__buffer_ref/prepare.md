##### [buffer\_ref::prepare](prepare.html "buffer_ref::prepare")

Get a list of buffers that represents the output sequence, with the given
size.

###### [Synopsis](prepare.html#beast.ref.boost__beast__buffer_ref.prepare.synopsis)

```programlisting
mutable_buffers_type
prepare(
    std::size_t n);
```

###### [Description](prepare.html#beast.ref.boost__beast__buffer_ref.prepare.description)

Ensures that the output sequence can accommodate `n`
bytes, resizing the vector object as necessary.

###### [Return Value](prepare.html#beast.ref.boost__beast__buffer_ref.prepare.return_value)

An object of type [`mutable_buffers_type`](mutable_buffers_type.html "buffer_ref::mutable_buffers_type") that satisfies
MutableBufferSequence requirements, representing vector memory at the start
of the output sequence of size `n`.

###### [Exceptions](prepare.html#beast.ref.boost__beast__buffer_ref.prepare.exceptions)

| Type | Thrown On |
| --- | --- |
| `std::length_error` | If [`size()`](size.html "buffer_ref::size") + n > [`max_size()`](max_size.html "buffer_ref::max_size"). |

###### [Remarks](prepare.html#beast.ref.boost__beast__buffer_ref.prepare.remarks)

The returned object is invalidated by any `dynamic_vector_buffer`
or `vector` member function
that modifies the input sequence or output sequence.