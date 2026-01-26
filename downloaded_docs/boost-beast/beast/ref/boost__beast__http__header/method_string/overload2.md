###### [http::header::method\_string (2 of 2 overloads)](overload2.html "http::header::method_string (2 of 2 overloads)")

Set the request-method.

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__header.method_string.overload2.synopsis)

```programlisting
void
method_string(
    string_view s);
```

###### [Description](overload2.html#beast.ref.boost__beast__http__header.method_string.overload2.description)

This function will set the request-method a known verb if the string
matches, otherwise it will store a copy of the passed string.

###### [Parameters](overload2.html#beast.ref.boost__beast__http__header.method_string.overload2.parameters)

| Name | Description |
| --- | --- |
| `s` | A string representing the request-method. |

###### [Remarks](overload2.html#beast.ref.boost__beast__http__header.method_string.overload2.remarks)

This function is only available when `isRequest
== true`.