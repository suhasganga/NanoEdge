###### [http::serializer::serializer (3 of 3 overloads)](overload3.html "http::serializer::serializer (3 of 3 overloads)")

Constructor.

###### [Synopsis](overload3.html#beast.ref.boost__beast__http__serializer.serializer.overload3.synopsis)

```programlisting
serializer(
    value_type& msg);
```

###### [Description](overload3.html#beast.ref.boost__beast__http__serializer.serializer.overload3.description)

The implementation guarantees that the message passed on construction
will not be accessed until the first call to [`next`](../next.html "http::serializer::next"). This allows the message
to be lazily created. For example, if the header is filled in before
serialization.

###### [Parameters](overload3.html#beast.ref.boost__beast__http__serializer.serializer.overload3.parameters)

| Name | Description |
| --- | --- |
| `msg` | A reference to the message to serialize, which must remain valid for the lifetime of the serializer. Depending on the type of Body used, this may or may not be a `const` reference. |

###### [Remarks](overload3.html#beast.ref.boost__beast__http__serializer.serializer.overload3.remarks)

This function participates in overload resolution only if Body::writer
is constructible from a `const`
message reference.