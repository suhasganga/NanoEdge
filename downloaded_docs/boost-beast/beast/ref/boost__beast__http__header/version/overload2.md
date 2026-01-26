###### [http::header::version (2 of 2 overloads)](overload2.html "http::header::version (2 of 2 overloads)")

Set the HTTP-version.

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__header.version.overload2.synopsis)

```programlisting
void
version(
    unsigned value);
```

###### [Description](overload2.html#beast.ref.boost__beast__http__header.version.overload2.description)

This holds both the major and minor version numbers, using these formulas:

```programlisting
unsigned major = version / 10;
unsigned minor = version % 10;
```

Newly constructed headers will use HTTP/1.1 by default.

###### [Parameters](overload2.html#beast.ref.boost__beast__http__header.version.overload2.parameters)

| Name | Description |
| --- | --- |
| `value` | The version number to use |