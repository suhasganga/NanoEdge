##### [http::message::reason](reason.html "http::message::reason")

(Inherited from [`http::header`](../boost__beast__http__header.html "http::header"))

Return the response reason-phrase.

###### [Synopsis](reason.html#beast.ref.boost__beast__http__message.reason.synopsis)

```programlisting
string_view
reason() const;
```

###### [Description](reason.html#beast.ref.boost__beast__http__message.reason.description)

The reason-phrase is obsolete as of rfc7230.

###### [Remarks](reason.html#beast.ref.boost__beast__http__message.reason.remarks)

This function is only available when `isRequest
== false`.