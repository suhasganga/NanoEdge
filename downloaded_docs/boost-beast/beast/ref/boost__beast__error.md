#### [error](boost__beast__error.html "error")

Error codes returned from library operations.

##### [Synopsis](boost__beast__error.html#beast.ref.boost__beast__error.synopsis)

Defined in header `<boost/beast/core/error.hpp>`

```programlisting
enum error
```

##### [Values](boost__beast__error.html#beast.ref.boost__beast__error.values)

| Name | Description |
| --- | --- |
| `timeout` | The socket was closed due to a timeout.  This error indicates that a socket was closed due to a a timeout detected during an operation.  Error codes with this value will compare equal to [`condition::timeout`](boost__beast__condition.html "condition"). |