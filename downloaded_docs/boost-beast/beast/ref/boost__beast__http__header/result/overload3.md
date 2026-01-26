###### [http::header::result (3 of 3 overloads)](overload3.html "http::header::result (3 of 3 overloads)")

Set the response status-code as an integer.

###### [Synopsis](overload3.html#beast.ref.boost__beast__http__header.result.overload3.synopsis)

```programlisting
void
result(
    unsigned v);
```

###### [Description](overload3.html#beast.ref.boost__beast__http__header.result.overload3.description)

This sets the status code to the exact number passed in. If the number
does not correspond to one of the known status codes, the function [`result`](../result.html "http::header::result")
will return [`status::unknown`](../../boost__beast__http__status.html "http::status"). Use [`result_int`](../result_int.html "http::header::result_int") to obtain the original
raw status-code.

###### [Parameters](overload3.html#beast.ref.boost__beast__http__header.result.overload3.parameters)

| Name | Description |
| --- | --- |
| `v` | The status-code integer to set. |

###### [Exceptions](overload3.html#beast.ref.boost__beast__http__header.result.overload3.exceptions)

| Type | Thrown On |
| --- | --- |
| `std::invalid_argument` | if `v > 999`. |