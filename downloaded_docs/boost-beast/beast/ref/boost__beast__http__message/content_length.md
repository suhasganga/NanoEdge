##### [http::message::content\_length](content_length.html "http::message::content_length")

Set or clear the Content-Length field.

###### [Synopsis](content_length.html#beast.ref.boost__beast__http__message.content_length.synopsis)

```programlisting
void
content_length(
    boost::optional< std::uint64_t > const& value);
```

###### [Description](content_length.html#beast.ref.boost__beast__http__message.content_length.description)

This function adjusts the Content-Length field as follows:

* If `value` specifies
  a value, the Content-Length field is set to the value. Otherwise
* The Content-Length field is erased.

If "chunked" token appears as the last item in the Transfer-Encoding
field it is unconditionally removed.

###### [Parameters](content_length.html#beast.ref.boost__beast__http__message.content_length.parameters)

| Name | Description |
| --- | --- |
| `value` | The value to set for Content-Length. |