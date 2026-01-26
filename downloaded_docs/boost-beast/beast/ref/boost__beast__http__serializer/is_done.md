##### [http::serializer::is\_done](is_done.html "http::serializer::is_done")

Return `true` if serialization
is complete.

###### [Synopsis](is_done.html#beast.ref.boost__beast__http__serializer.is_done.synopsis)

```programlisting
bool
is_done() const;
```

###### [Description](is_done.html#beast.ref.boost__beast__http__serializer.is_done.description)

The operation is complete when all octets corresponding to the serialized
representation of the message have been successfully retrieved.