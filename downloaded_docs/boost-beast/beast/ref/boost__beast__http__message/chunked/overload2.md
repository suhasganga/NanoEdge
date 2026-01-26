###### [http::message::chunked (2 of 2 overloads)](overload2.html "http::message::chunked (2 of 2 overloads)")

Set or clear the chunked Transfer-Encoding.

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__message.chunked.overload2.synopsis)

```programlisting
void
chunked(
    bool value);
```

###### [Description](overload2.html#beast.ref.boost__beast__http__message.chunked.overload2.description)

This function will set or remove the "chunked" transfer encoding
as the last item in the list of encodings in the field.

If the result of removing the chunked token results in an empty string,
the field is erased.

The Content-Length field is erased unconditionally.