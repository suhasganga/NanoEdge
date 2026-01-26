###### [http::parser::parser (5 of 5 overloads)](overload5.html "http::parser::parser (5 of 5 overloads)")

Construct a parser from another parser, changing the Body type.

###### [Synopsis](overload5.html#beast.ref.boost__beast__http__parser.parser.overload5.synopsis)

```programlisting
template<
    class OtherBody,
    class... Args>
parser(
    parser< isRequest, OtherBody, Allocator >&& parser,
    Args&&... args);
```

###### [Description](overload5.html#beast.ref.boost__beast__http__parser.parser.overload5.description)

This constructs a new parser by move constructing the header from another
parser with a different body type. The constructed-from parser must not
have any parsed body octets or initialized *BodyReader*,
otherwise an exception is generated.

###### [Example](overload5.html#beast.ref.boost__beast__http__parser.parser.overload5.example)

```programlisting
// Deferred body type commitment
request_parser<empty_body> req0;
...
request_parser<string_body> req{std::move(req0)};
```

If an exception is thrown, the state of the constructed-from parser is
undefined.

###### [Parameters](overload5.html#beast.ref.boost__beast__http__parser.parser.overload5.parameters)

| Name | Description |
| --- | --- |
| `parser` | The other parser to construct from. After this call returns, the constructed-from parser may only be destroyed. |
| `args` | Optional arguments forwarded to the message constructor. |

###### [Exceptions](overload5.html#beast.ref.boost__beast__http__parser.parser.overload5.exceptions)

| Type | Thrown On |
| --- | --- |
| `std::invalid_argument` | Thrown when the constructed-from parser has already initialized a body reader. |

###### [Remarks](overload5.html#beast.ref.boost__beast__http__parser.parser.overload5.remarks)

This function participates in overload resolution only if the other parser
uses a different body type.