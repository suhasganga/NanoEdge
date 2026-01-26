###### [http::parser::merge\_all\_trailers (2 of 2 overloads)](overload2.html "http::parser::merge_all_trailers (2 of 2 overloads)")

Set whether the parser is allowed to merge all trailer fields.

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__parser.merge_all_trailers.overload2.synopsis)

```programlisting
void
merge_all_trailers(
    bool v);
```

###### [Description](overload2.html#beast.ref.boost__beast__http__parser.merge_all_trailers.overload2.description)

By default, the parser merges only a set of well-known trailer fields.
When this option is enabled, the parser merges all trailer fields listed
in the `Trailer` header
field in the header section of the message.

###### [Remarks](overload2.html#beast.ref.boost__beast__http__parser.merge_all_trailers.overload2.remarks)

Enabling this option can introduce security risks if untrusted input
is processed and the `Trailer`
header field in the header section of the message is not properly validated.

The default value is `false`,
which merges only the following well-known trailer fields:

* `Digest`
* `Content-Digest`
* `Repr-Digest`
* `Signature`
* `Signature-Input`
* `Server-Timing`
* `ETag`
* `Link`
* `Alt-Svc`

###### [Parameters](overload2.html#beast.ref.boost__beast__http__parser.merge_all_trailers.overload2.parameters)

| Name | Description |
| --- | --- |
| `v` | `true` to merge all trailer fields, or `false` to merge only the well-known ones. |