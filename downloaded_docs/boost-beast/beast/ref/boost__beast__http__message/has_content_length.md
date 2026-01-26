##### [http::message::has\_content\_length](has_content_length.html "http::message::has_content_length")

Returns `true` if the Content-Length
field is present.

###### [Synopsis](has_content_length.html#beast.ref.boost__beast__http__message.has_content_length.synopsis)

```programlisting
bool
has_content_length() const;
```

###### [Description](has_content_length.html#beast.ref.boost__beast__http__message.has_content_length.description)

This function inspects the fields and returns `true`
if the Content-Length field is present. The properties of the body are
not checked, this only looks for the field.