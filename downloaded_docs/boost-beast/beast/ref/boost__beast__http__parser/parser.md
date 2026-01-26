##### [http::parser::parser](parser.html "http::parser::parser")

Constructor (disallowed)

```programlisting
parser(
    parser const&) = delete;
  » more...

parser(
    parser&& other) = delete;
  » more...
```

Constructor.

```programlisting
parser();
  » more...

template<
    class... Args>
explicit
parser(
    Args&&... args);
  » more...
```

Construct a parser from another parser, changing the Body type.

```programlisting
template<
    class OtherBody,
    class... Args>
explicit
parser(
    parser< isRequest, OtherBody, Allocator >&& parser,
    Args&&... args);
  » more...
```