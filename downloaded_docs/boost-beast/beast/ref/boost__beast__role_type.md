#### [role\_type](boost__beast__role_type.html "role_type")

The role of local or remote peer.

##### [Synopsis](boost__beast__role_type.html#beast.ref.boost__beast__role_type.synopsis)

Defined in header `<boost/beast/core/role.hpp>`

```programlisting
enum role_type
```

##### [Values](boost__beast__role_type.html#beast.ref.boost__beast__role_type.values)

| Name | Description |
| --- | --- |
| `client` | The stream is operating as a client. |
| `server` | The stream is operating as a server. |

##### [Description](boost__beast__role_type.html#beast.ref.boost__beast__role_type.description)

Whether the endpoint is a client or server affects the behavior of teardown.
The teardown behavior also depends on the type of the stream being torn down.

The default implementation of teardown for regular TCP/IP sockets is as follows:

* In the client role, a TCP/IP shutdown is sent after reading all remaining
  data on the connection.
* In the server role, a TCP/IP shutdown is sent before reading all remaining
  data on the connection.

When the next layer type is a `net::ssl::stream`, the connection is closed by performing
the SSL closing handshake corresponding to the role type, client or server.