##### [http::message::need\_eof](need_eof.html "http::message::need_eof")

Returns `true` if the message
semantics require an end of file.

###### [Synopsis](need_eof.html#beast.ref.boost__beast__http__message.need_eof.synopsis)

```programlisting
bool
need_eof() const;
```

###### [Description](need_eof.html#beast.ref.boost__beast__http__message.need_eof.description)

For HTTP requests, this function returns the logical NOT of a call to
[`keep_alive`](keep_alive.html "http::message::keep_alive").

For HTTP responses, this function returns the logical NOT of a call to
[`keep_alive`](keep_alive.html "http::message::keep_alive") if any of the following
are true:

* [`has_content_length`](has_content_length.html "http::message::has_content_length") would return
  `true`
* [`chunked`](chunked.html "http::message::chunked") would return `true`
* [`result`](result.html "http::message::result") returns [`status::no_content`](../boost__beast__http__status.html "http::status")
* [`result`](result.html "http::message::result") returns [`status::not_modified`](../boost__beast__http__status.html "http::status")
* [`result`](result.html "http::message::result") returns any informational
  status class (100 to 199)

Otherwise, the function returns `true`.

###### [See Also](need_eof.html#beast.ref.boost__beast__http__message.need_eof.see_also)

<https://tools.ietf.org/html/rfc7230#section-3.3>