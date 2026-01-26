###### [http::parser::parser (4 of 5 overloads)](overload4.html "http::parser::parser (4 of 5 overloads)")

Constructor.

###### [Synopsis](overload4.html#beast.ref.boost__beast__http__parser.parser.overload4.synopsis)

```programlisting
template<
    class... Args>
parser(
    Args&&... args);
```

###### [Parameters](overload4.html#beast.ref.boost__beast__http__parser.parser.overload4.parameters)

| Name | Description |
| --- | --- |
| `args` | Optional arguments forwarded to the [`http::message`](../../boost__beast__http__message.html "http::message")  constructor. |

###### [Remarks](overload4.html#beast.ref.boost__beast__http__parser.parser.overload4.remarks)

This function participates in overload resolution only if the first argument
is not a [`parser`](../../boost__beast__http__parser.html "http::parser").