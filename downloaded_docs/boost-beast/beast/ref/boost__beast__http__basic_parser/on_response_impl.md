##### [http::basic\_parser::on\_response\_impl](on_response_impl.html "http::basic_parser::on_response_impl")

Called after receiving the status-line.

###### [Synopsis](on_response_impl.html#beast.ref.boost__beast__http__basic_parser.on_response_impl.synopsis)

```programlisting
void
on_response_impl(
    int code,
    string_view reason,
    int version,
    error_code& ec);
```

###### [Description](on_response_impl.html#beast.ref.boost__beast__http__basic_parser.on_response_impl.description)

This virtual function is invoked after receiving a status-line when parsing
HTTP responses. It can only be called when `isRequest
== false`.

###### [Parameters](on_response_impl.html#beast.ref.boost__beast__http__basic_parser.on_response_impl.parameters)

| Name | Description |
| --- | --- |
| `code` | The numeric status code. |
| `reason` | The reason-phrase. Note that this value is now obsolete, and only provided for historical or diagnostic purposes. |
| `version` | The HTTP-version. This will be 10 for HTTP/1.0, and 11 for HTTP/1.1. |
| `ec` | An output parameter which the function may set to indicate an error. The error will be clear before this function is invoked. |