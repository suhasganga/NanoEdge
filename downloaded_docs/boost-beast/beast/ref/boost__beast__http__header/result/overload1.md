###### [http::header::result (1 of 3 overloads)](overload1.html "http::header::result (1 of 3 overloads)")

The response status-code result.

###### [Synopsis](overload1.html#beast.ref.boost__beast__http__header.result.overload1.synopsis)

```programlisting
status
result() const;
```

###### [Description](overload1.html#beast.ref.boost__beast__http__header.result.overload1.description)

If the actual status code is not a known code, this function returns
[`status::unknown`](../../boost__beast__http__status.html "http::status").
Use [`result_int`](../result_int.html "http::header::result_int") to return the raw
status code as a number.

###### [Remarks](overload1.html#beast.ref.boost__beast__http__header.result.overload1.remarks)

This member is only available when `isRequest
== false`.