#### [http::status\_class](boost__beast__http__status_class.html "http::status_class")

Represents the class of a status-code.

##### [Synopsis](boost__beast__http__status_class.html#beast.ref.boost__beast__http__status_class.synopsis)

Defined in header `<boost/beast/http/status.hpp>`

```programlisting
enum status_class
```

##### [Values](boost__beast__http__status_class.html#beast.ref.boost__beast__http__status_class.values)

| Name | Description |
| --- | --- |
| `unknown` | Unknown status-class. |
| `informational` | The request was received, continuing processing. |
| `successful` | The request was successfully received, understood, and accepted. |
| `redirection` | Further action needs to be taken in order to complete the request. |
| `client_error` | The request contains bad syntax or cannot be fulfilled. |
| `server_error` | The server failed to fulfill an apparently valid request. |