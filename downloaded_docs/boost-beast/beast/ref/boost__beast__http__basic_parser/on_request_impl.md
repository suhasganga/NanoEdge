##### [http::basic\_parser::on\_request\_impl](on_request_impl.html "http::basic_parser::on_request_impl")

Called after receiving the request-line.

###### [Synopsis](on_request_impl.html#beast.ref.boost__beast__http__basic_parser.on_request_impl.synopsis)

```programlisting
void
on_request_impl(
    verb method,
    string_view method_str,
    string_view target,
    int version,
    error_code& ec);
```

###### [Description](on_request_impl.html#beast.ref.boost__beast__http__basic_parser.on_request_impl.description)

This virtual function is invoked after receiving a request-line when parsing
HTTP requests. It can only be called when `isRequest
== true`.

###### [Parameters](on_request_impl.html#beast.ref.boost__beast__http__basic_parser.on_request_impl.parameters)

| Name | Description |
| --- | --- |
| `method` | The verb enumeration. If the method string is not one of the predefined strings, this value will be [`verb::unknown`](../boost__beast__http__verb.html "http::verb"). |
| `method_str` | The unmodified string representing the verb. |
| `target` | The request-target. |
| `version` | The HTTP-version. This will be 10 for HTTP/1.0, and 11 for HTTP/1.1. |
| `ec` | An output parameter which the function may set to indicate an error. The error will be clear before this function is invoked. |