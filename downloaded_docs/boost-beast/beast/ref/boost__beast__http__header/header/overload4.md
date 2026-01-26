###### [http::header::header (4 of 4 overloads)](overload4.html "http::header::header (4 of 4 overloads)")

Constructor.

###### [Synopsis](overload4.html#beast.ref.boost__beast__http__header.header.overload4.synopsis)

```programlisting
template<
    class... Args>
header(
    Args&&... args);
```

###### [Parameters](overload4.html#beast.ref.boost__beast__http__header.header.overload4.parameters)

| Name | Description |
| --- | --- |
| `args` | Arguments forwarded to the `Fields` base class constructor. |

###### [Remarks](overload4.html#beast.ref.boost__beast__http__header.header.overload4.remarks)

This constructor participates in overload resolution if and only if the
first parameter is not convertible to [`header`](../../boost__beast__http__header.html "http::header"), [`verb`](../../boost__beast__http__verb.html "http::verb"), or [`status`](../../boost__beast__http__status.html "http::status").