##### [http::serializer::writer\_impl](writer_impl.html "http::serializer::writer_impl")

Provides low-level access to the associated *BodyWriter*

###### [Synopsis](writer_impl.html#beast.ref.boost__beast__http__serializer.writer_impl.synopsis)

```programlisting
writer&
writer_impl();
```

###### [Description](writer_impl.html#beast.ref.boost__beast__http__serializer.writer_impl.description)

This function provides access to the instance of the writer associated
with the body and created by the serializer upon construction. The behavior
of accessing this object is defined by the specification of the particular
writer and its associated body.

###### [Return Value](writer_impl.html#beast.ref.boost__beast__http__serializer.writer_impl.return_value)

A reference to the writer.