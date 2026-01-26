#### [http::operator<<](boost__beast__http__operator_lt__lt_.html "http::operator<<")

Serialize an HTTP/1 header to a `std::ostream`.

```programlisting
template<
    bool isRequest,
    class Fields>
std::ostream&
operator<<(
    std::ostream& os,
    header< isRequest, Fields > const& msg);
  » more...
```

Serialize an HTTP/1 message to a `std::ostream`.

```programlisting
template<
    bool isRequest,
    class Body,
    class Fields>
std::ostream&
operator<<(
    std::ostream& os,
    message< isRequest, Body, Fields > const& msg);
  » more...
```

Write the text for a request method verb to an output stream.

```programlisting
std::ostream&
operator<<(
    std::ostream& os,
    verb v);
  » more...
```

Outputs the standard reason phrase of a status code to a stream.

```programlisting
std::ostream&
operator<<(
    std::ostream&,
    status);
  » more...
```

Write the text for a field name to an output stream.

```programlisting
std::ostream&
operator<<(
    std::ostream& os,
    field f);
  » more...
```