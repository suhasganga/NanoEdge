#### [http::obsolete\_reason](boost__beast__http__obsolete_reason.html "http::obsolete_reason")

Returns the obsolete reason-phrase text for a status code.

##### [Synopsis](boost__beast__http__obsolete_reason.html#beast.ref.boost__beast__http__obsolete_reason.synopsis)

Defined in header `<boost/beast/http/status.hpp>`

```programlisting
string_view
obsolete_reason(
    status v);
```

##### [Parameters](boost__beast__http__obsolete_reason.html#beast.ref.boost__beast__http__obsolete_reason.parameters)

| Name | Description |
| --- | --- |
| `v` | The status code to use. |