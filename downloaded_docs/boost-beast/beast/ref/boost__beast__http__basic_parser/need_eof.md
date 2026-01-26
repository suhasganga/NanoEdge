##### [http::basic\_parser::need\_eof](need_eof.html "http::basic_parser::need_eof")

Returns `true` if the message
semantics require an end of file.

###### [Synopsis](need_eof.html#beast.ref.boost__beast__http__basic_parser.need_eof.synopsis)

```programlisting
bool
need_eof() const;
```

###### [Description](need_eof.html#beast.ref.boost__beast__http__basic_parser.need_eof.description)

Depending on the contents of the header, the parser may require and end
of file notification to know where the end of the body lies. If this function
returns `true` it will be necessary
to call [`put_eof`](put_eof.html "http::basic_parser::put_eof") when there will never
be additional data from the input.