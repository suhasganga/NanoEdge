##### [http::parser::release](release.html "http::parser::release")

Returns ownership of the parsed message.

###### [Synopsis](release.html#beast.ref.boost__beast__http__parser.release.synopsis)

```programlisting
value_type
release();
```

###### [Description](release.html#beast.ref.boost__beast__http__parser.release.description)

Ownership is transferred to the caller. Depending on the parser's progress,
parts of this object may be incomplete.

###### [Requires](release.html#beast.ref.boost__beast__http__parser.release.requires)

[`value_type`](value_type.html "http::parser::value_type")is **MoveConstructible**