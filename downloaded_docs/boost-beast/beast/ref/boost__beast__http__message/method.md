##### [http::message::method](method.html "http::message::method")

(Inherited from [`http::header`](../boost__beast__http__header.html "http::header"))

Return the request-method verb.

###### [Synopsis](method.html#beast.ref.boost__beast__http__message.method.synopsis)

```programlisting
verb
method() const;
```

###### [Description](method.html#beast.ref.boost__beast__http__message.method.description)

If the request-method is not one of the recognized verbs, [`verb::unknown`](../boost__beast__http__verb.html "http::verb") is returned. Callers may
use [`method_string`](method_string.html "http::message::method_string") to retrieve the
exact text.

###### [Remarks](method.html#beast.ref.boost__beast__http__message.method.remarks)

This function is only available when `isRequest
== true`.

###### [See Also](method.html#beast.ref.boost__beast__http__message.method.see_also)

[`method_string`](method_string.html "http::message::method_string")