###### [http::header::result (2 of 3 overloads)](overload2.html "http::header::result (2 of 3 overloads)")

Set the response status-code.

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__header.result.overload2.synopsis)

```programlisting
void
result(
    status v);
```

###### [Parameters](overload2.html#beast.ref.boost__beast__http__header.result.overload2.parameters)

| Name | Description |
| --- | --- |
| `v` | The code to set. |

###### [Remarks](overload2.html#beast.ref.boost__beast__http__header.result.overload2.remarks)

This member is only available when `isRequest
== false`.