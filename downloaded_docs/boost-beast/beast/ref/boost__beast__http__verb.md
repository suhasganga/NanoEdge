#### [http::verb](boost__beast__http__verb.html "http::verb")

HTTP request method verbs.

##### [Synopsis](boost__beast__http__verb.html#beast.ref.boost__beast__http__verb.synopsis)

Defined in header `<boost/beast/http/verb.hpp>`

```programlisting
enum verb
```

##### [Values](boost__beast__http__verb.html#beast.ref.boost__beast__http__verb.values)

| Name | Description |
| --- | --- |
| `unknown` | An unknown method.  This value indicates that the request method string is not one of the recognized verbs. Callers interested in the method should use an interface which returns the original string. |
| `delete_` | The DELETE method deletes the specified resource. |
| `get` | The GET method requests a representation of the specified resource.  Requests using GET should only retrieve data and should have no other effect. |
| `head` | The HEAD method asks for a response identical to that of a GET request, but without the response body.  This is useful for retrieving meta-information written in response headers, without having to transport the entire content. |
| `post` | The POST method requests that the server accept the entity enclosed in the request as a new subordinate of the web resource identified by the URI.  The data POSTed might be, for example, an annotation for existing resources; a message for a bulletin board, newsgroup, mailing list, or comment thread; a block of data that is the result of submitting a web form to a data-handling process; or an item to add to a database |
| `put` | The PUT method requests that the enclosed entity be stored under the supplied URI.  If the URI refers to an already existing resource, it is modified; if the URI does not point to an existing resource, then the server can create the resource with that URI. |
| `connect` | The CONNECT method converts the request connection to a transparent TCP/IP tunnel.  This is usually to facilitate SSL-encrypted communication (HTTPS) through an unencrypted HTTP proxy. |
| `options` | The OPTIONS method returns the HTTP methods that the server supports for the specified URL.  This can be used to check the functionality of a web server by requesting '\*' instead of a specific resource. |
| `trace` | The TRACE method echoes the received request so that a client can see what (if any) changes or additions have been made by intermediate servers. |
| `copy` |  |
| `lock` |  |
| `mkcol` |  |
| `move` |  |
| `propfind` |  |
| `proppatch` |  |
| `search` |  |
| `unlock` |  |
| `bind` |  |
| `rebind` |  |
| `unbind` |  |
| `acl` |  |
| `report` |  |
| `mkactivity` |  |
| `checkout` |  |
| `merge` |  |
| `msearch` |  |
| `notify` |  |
| `subscribe` |  |
| `unsubscribe` |  |
| `patch` |  |
| `purge` |  |
| `mkcalendar` |  |
| `link` |  |
| `unlink` |  |

##### [Description](boost__beast__http__verb.html#beast.ref.boost__beast__http__verb.description)

Each verb corresponds to a particular method string used in HTTP request
messages.