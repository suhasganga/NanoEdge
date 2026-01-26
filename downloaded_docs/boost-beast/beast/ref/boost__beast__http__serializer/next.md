##### [http::serializer::next](next.html "http::serializer::next")

Returns the next set of buffers in the serialization.

###### [Synopsis](next.html#beast.ref.boost__beast__http__serializer.next.synopsis)

```programlisting
template<
    class Visit>
void
next(
    error_code& ec,
    Visit&& visit);
```

###### [Description](next.html#beast.ref.boost__beast__http__serializer.next.description)

This function will attempt to call the `visit`
function object with a *ConstBufferSequence* of unspecified
type representing the next set of buffers in the serialization of the message
represented by this object.

If there are no more buffers in the serialization, the visit function will
not be called. In this case, no error will be indicated, and the function
[`is_done`](is_done.html "http::serializer::is_done") will return `true`.

###### [Parameters](next.html#beast.ref.boost__beast__http__serializer.next.parameters)

| Name | Description |
| --- | --- |
| `ec` | Set to the error, if any occurred. |
| `visit` | The function to call. The equivalent function signature of this object must be:   ```table-programlisting template < class ConstBufferSequence> void visit(error_code&, ConstBufferSequence const &); ```   The function is not copied, if no error occurs it will be invoked before the call to [`next`](next.html "http::serializer::next") returns. |