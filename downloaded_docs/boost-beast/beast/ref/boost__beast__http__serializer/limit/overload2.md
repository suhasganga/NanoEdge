###### [http::serializer::limit (2 of 2 overloads)](overload2.html "http::serializer::limit (2 of 2 overloads)")

Set the serialized buffer size limit.

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__serializer.limit.overload2.synopsis)

```programlisting
void
limit(
    std::size_t limit);
```

###### [Description](overload2.html#beast.ref.boost__beast__http__serializer.limit.overload2.description)

This function adjusts the limit on the maximum size of the buffers passed
to the visitor. The new size limit takes effect in the following call
to [`next`](../next.html "http::serializer::next").

The default is no buffer size limit.

###### [Parameters](overload2.html#beast.ref.boost__beast__http__serializer.limit.overload2.parameters)

| Name | Description |
| --- | --- |
| `limit` | The new buffer size limit. If this number is zero, the size limit is removed. |