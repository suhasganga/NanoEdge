##### [http::message::version](version.html "http::message::version")

(Inherited from [`http::header`](../boost__beast__http__header.html "http::header"))

Return the HTTP-version.

###### [Synopsis](version.html#beast.ref.boost__beast__http__message.version.synopsis)

```programlisting
unsigned
version() const;
```

###### [Description](version.html#beast.ref.boost__beast__http__message.version.description)

This holds both the major and minor version numbers, using these formulas:

```programlisting
unsigned major = version / 10;
unsigned minor = version % 10;
```

Newly constructed headers will use HTTP/1.1 by default.