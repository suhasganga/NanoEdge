###### [http::header::method\_string (1 of 2 overloads)](overload1.html "http::header::method_string (1 of 2 overloads)")

Return the request-method as a string.

###### [Synopsis](overload1.html#beast.ref.boost__beast__http__header.method_string.overload1.synopsis)

```programlisting
string_view
method_string() const;
```

###### [Remarks](overload1.html#beast.ref.boost__beast__http__header.method_string.overload1.remarks)

This function is only available when `isRequest
== true`.

###### [See Also](overload1.html#beast.ref.boost__beast__http__header.method_string.overload1.see_also)

[`method`](../method.html "http::header::method")