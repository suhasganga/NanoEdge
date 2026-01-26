###### [http::parser::eager (2 of 2 overloads)](overload2.html "http::parser::eager (2 of 2 overloads)")

(Inherited from [`http::basic_parser`](../../boost__beast__http__basic_parser.html "http::basic_parser"))

Set the eager parse option.

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__parser.eager.overload2.synopsis)

```programlisting
void
eager(
    bool v);
```

###### [Description](overload2.html#beast.ref.boost__beast__http__parser.eager.overload2.description)

Normally the parser returns after successfully parsing a structured element
(header, chunk header, or chunk body) even if there are octets remaining
in the input. This is necessary when attempting to parse the header first,
or when the caller wants to inspect information which may be invalidated
by subsequent parsing, such as a chunk extension. The `eager`
option controls whether the parser keeps going after parsing structured
element if there are octets remaining in the buffer and no error occurs.
This option is automatically set or cleared during certain stream operations
to improve performance with no change in functionality.

The default setting is `false`.

###### [Parameters](overload2.html#beast.ref.boost__beast__http__parser.eager.overload2.parameters)

| Name | Description |
| --- | --- |
| `v` | `true` to set the eager parse option or `false` to disable it. |