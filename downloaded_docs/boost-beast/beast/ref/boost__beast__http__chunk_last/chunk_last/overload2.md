###### [http::chunk\_last::chunk\_last (2 of 4 overloads)](overload2.html "http::chunk_last::chunk_last (2 of 4 overloads)")

Constructor.

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__chunk_last.chunk_last.overload2.synopsis)

```programlisting
chunk_last(
    Trailer const& trailer);
```

###### [Parameters](overload2.html#beast.ref.boost__beast__http__chunk_last.chunk_last.overload2.parameters)

| Name | Description |
| --- | --- |
| `trailer` | The trailer to use. This may be a type meeting the requirements of either Fields or ConstBufferSequence. If it is a ConstBufferSequence, the trailer must be formatted correctly as per rfc7230 including a CRLF on its own line to denote the end of the trailer. |