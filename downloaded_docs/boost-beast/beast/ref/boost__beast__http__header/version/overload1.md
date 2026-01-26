###### [http::header::version (1 of 2 overloads)](overload1.html "http::header::version (1 of 2 overloads)")

Return the HTTP-version.

###### [Synopsis](overload1.html#beast.ref.boost__beast__http__header.version.overload1.synopsis)

```programlisting
unsigned
version() const;
```

###### [Description](overload1.html#beast.ref.boost__beast__http__header.version.overload1.description)

This holds both the major and minor version numbers, using these formulas:

```programlisting
unsigned major = version / 10;
unsigned minor = version % 10;
```

Newly constructed headers will use HTTP/1.1 by default.