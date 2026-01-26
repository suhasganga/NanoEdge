###### [http::header::method (2 of 2 overloads)](overload2.html "http::header::method (2 of 2 overloads)")

Set the request-method.

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__header.method.overload2.synopsis)

```programlisting
void
method(
    verb v);
```

###### [Description](overload2.html#beast.ref.boost__beast__http__header.method.overload2.description)

This function will set the method for requests to a known verb.

###### [Parameters](overload2.html#beast.ref.boost__beast__http__header.method.overload2.parameters)

| Name | Description |
| --- | --- |
| `v` | The request method verb to set. This may not be [`verb::unknown`](../../boost__beast__http__verb.html "http::verb"). |

###### [Exceptions](overload2.html#beast.ref.boost__beast__http__header.method.overload2.exceptions)

| Type | Thrown On |
| --- | --- |
| `std::invalid_argument` | when v == [`verb::unknown`](../../boost__beast__http__verb.html "http::verb"). |

###### [Remarks](overload2.html#beast.ref.boost__beast__http__header.method.overload2.remarks)

This function is only available when `isRequest
== true`.