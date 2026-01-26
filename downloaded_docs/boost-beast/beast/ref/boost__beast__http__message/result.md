##### [http::message::result](result.html "http::message::result")

(Inherited from [`http::header`](../boost__beast__http__header.html "http::header"))

The response status-code result.

###### [Synopsis](result.html#beast.ref.boost__beast__http__message.result.synopsis)

```programlisting
status
result() const;
```

###### [Description](result.html#beast.ref.boost__beast__http__message.result.description)

If the actual status code is not a known code, this function returns [`status::unknown`](../boost__beast__http__status.html "http::status").
Use [`result_int`](result_int.html "http::message::result_int") to return the raw status
code as a number.

###### [Remarks](result.html#beast.ref.boost__beast__http__message.result.remarks)

This member is only available when `isRequest
== false`.