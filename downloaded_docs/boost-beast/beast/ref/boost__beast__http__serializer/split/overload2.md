###### [http::serializer::split (2 of 2 overloads)](overload2.html "http::serializer::split (2 of 2 overloads)")

Set whether the header and body are written separately.

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__serializer.split.overload2.synopsis)

```programlisting
void
split(
    bool v);
```

###### [Description](overload2.html#beast.ref.boost__beast__http__serializer.split.overload2.description)

When the split feature is enabled, the implementation will write only
the octets corresponding to the serialized header first. If the header
has already been written, this function will have no effect on output.