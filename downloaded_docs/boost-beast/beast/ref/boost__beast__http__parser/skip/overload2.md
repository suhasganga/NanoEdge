###### [http::parser::skip (2 of 2 overloads)](overload2.html "http::parser::skip (2 of 2 overloads)")

(Inherited from [`http::basic_parser`](../../boost__beast__http__basic_parser.html "http::basic_parser"))

Set the skip parse option.

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__parser.skip.overload2.synopsis)

```programlisting
void
skip(
    bool v);
```

###### [Description](overload2.html#beast.ref.boost__beast__http__parser.skip.overload2.description)

This option controls whether or not the parser expects to see an HTTP
body, regardless of the presence or absence of certain fields such as
Content-Length or a chunked Transfer-Encoding. Depending on the request,
some responses do not carry a body. For example, a 200 response to a
CONNECT request from a tunneling proxy, or a response to a HEAD request.
In these cases, callers may use this function inform the parser that
no body is expected. The parser will consider the message complete after
the header has been received.

###### [Parameters](overload2.html#beast.ref.boost__beast__http__parser.skip.overload2.parameters)

| Name | Description |
| --- | --- |
| `v` | `true` to set the skip body option or `false` to disable it. |

###### [Remarks](overload2.html#beast.ref.boost__beast__http__parser.skip.overload2.remarks)

This function must called before any bytes are processed.