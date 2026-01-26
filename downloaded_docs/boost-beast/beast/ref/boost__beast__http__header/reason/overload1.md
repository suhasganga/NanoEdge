###### [http::header::reason (1 of 2 overloads)](overload1.html "http::header::reason (1 of 2 overloads)")

Return the response reason-phrase.

###### [Synopsis](overload1.html#beast.ref.boost__beast__http__header.reason.overload1.synopsis)

```programlisting
string_view
reason() const;
```

###### [Description](overload1.html#beast.ref.boost__beast__http__header.reason.overload1.description)

The reason-phrase is obsolete as of rfc7230.

###### [Remarks](overload1.html#beast.ref.boost__beast__http__header.reason.overload1.remarks)

This function is only available when `isRequest
== false`.