##### [http::parser::body\_limit](body_limit.html "http::parser::body_limit")

(Inherited from [`http::basic_parser`](../boost__beast__http__basic_parser.html "http::basic_parser"))

Set the limit on the payload body.

###### [Synopsis](body_limit.html#beast.ref.boost__beast__http__parser.body_limit.synopsis)

```programlisting
void
body_limit(
    boost::optional< std::uint64_t > v);
```

###### [Description](body_limit.html#beast.ref.boost__beast__http__parser.body_limit.description)

This function sets the maximum allowed size of the payload body, before
any encodings except chunked have been removed. Depending on the message
semantics, one of these cases will apply:

* The Content-Length is specified and exceeds the limit. In this case
  the result [`error::body_limit`](../boost__beast__http__error.html "http::error") is returned immediately
  after the header is parsed.
* The Content-Length is unspecified and the chunked encoding is not specified
  as the last encoding. In this case the end of message is determined
  by the end of file indicator on the associated stream or input source.
  If a sufficient number of body payload octets are presented to the
  parser to exceed the configured limit, the parse fails with the result
  [`error::body_limit`](../boost__beast__http__error.html "http::error")
* The Transfer-Encoding specifies the chunked encoding as the last encoding.
  In this case, when the number of payload body octets produced by removing
  the chunked encoding exceeds the configured limit, the parse fails
  with the result [`error::body_limit`](../boost__beast__http__error.html "http::error").

Setting the limit after any body octets have been parsed results in undefined
behavior.

The default limit is 1MB for requests and 8MB for responses.

###### [Parameters](body_limit.html#beast.ref.boost__beast__http__parser.body_limit.parameters)

| Name | Description |
| --- | --- |
| `v` | An optional integral value representing the body limit. If this is equal to `boost::none`, then the body limit is disabled. |