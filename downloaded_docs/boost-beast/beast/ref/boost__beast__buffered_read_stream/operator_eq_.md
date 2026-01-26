##### [buffered\_read\_stream::operator=](operator_eq_.html "buffered_read_stream::operator=")

Move assignment.

###### [Synopsis](operator_eq_.html#beast.ref.boost__beast__buffered_read_stream.operator_eq_.synopsis)

```programlisting
buffered_read_stream&
operator=(
    buffered_read_stream&&);
```

###### [Remarks](operator_eq_.html#beast.ref.boost__beast__buffered_read_stream.operator_eq_.remarks)

The behavior of move assignment on or from streams with active or pending
operations is undefined.