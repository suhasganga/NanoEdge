##### [http::message::method\_string](method_string.html "http::message::method_string")

(Inherited from [`http::header`](../boost__beast__http__header.html "http::header"))

Return the request-method as a string.

###### [Synopsis](method_string.html#beast.ref.boost__beast__http__message.method_string.synopsis)

```programlisting
string_view
method_string() const;
```

###### [Remarks](method_string.html#beast.ref.boost__beast__http__message.method_string.remarks)

This function is only available when `isRequest
== true`.

###### [See Also](method_string.html#beast.ref.boost__beast__http__message.method_string.see_also)

[`method`](method.html "http::message::method")