##### [http::header::result\_int](result_int.html "http::header::result_int")

The response status-code expressed as an integer.

###### [Synopsis](result_int.html#beast.ref.boost__beast__http__header.result_int.synopsis)

```programlisting
unsigned
result_int() const;
```

###### [Description](result_int.html#beast.ref.boost__beast__http__header.result_int.description)

This returns the raw status code as an integer, even when that code is
not in the list of known status codes.

###### [Remarks](result_int.html#beast.ref.boost__beast__http__header.result_int.remarks)

This member is only available when `isRequest
== false`.