###### [http::header::method (1 of 2 overloads)](overload1.html "http::header::method (1 of 2 overloads)")

Return the request-method verb.

###### [Synopsis](overload1.html#beast.ref.boost__beast__http__header.method.overload1.synopsis)

```programlisting
verb
method() const;
```

###### [Description](overload1.html#beast.ref.boost__beast__http__header.method.overload1.description)

If the request-method is not one of the recognized verbs, [`verb::unknown`](../../boost__beast__http__verb.html "http::verb") is returned. Callers
may use [`method_string`](../method_string.html "http::header::method_string") to retrieve the
exact text.

###### [Remarks](overload1.html#beast.ref.boost__beast__http__header.method.overload1.remarks)

This function is only available when `isRequest
== true`.

###### [See Also](overload1.html#beast.ref.boost__beast__http__header.method.overload1.see_also)

[`method_string`](../method_string.html "http::header::method_string")