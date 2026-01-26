##### [http::parser::is\_done](is_done.html "http::parser::is_done")

(Inherited from [`http::basic_parser`](../boost__beast__http__basic_parser.html "http::basic_parser"))

Returns `true` if the message
is complete.

###### [Synopsis](is_done.html#beast.ref.boost__beast__http__parser.is_done.synopsis)

```programlisting
bool
is_done() const;
```

###### [Description](is_done.html#beast.ref.boost__beast__http__parser.is_done.description)

The message is complete after the full header is prduced and one of the
following is true:

* The skip body option was set.
* The semantics of the message indicate there is no body.
* The semantics of the message indicate a body is expected, and the entire
  body was parsed.