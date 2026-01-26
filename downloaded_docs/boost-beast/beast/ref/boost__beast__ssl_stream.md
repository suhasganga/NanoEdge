#### [ssl\_stream](boost__beast__ssl_stream.html "ssl_stream")

(Deprecated: Use asio::ssl::stream instead.) Provides stream-oriented functionality
using OpenSSL

##### [Synopsis](boost__beast__ssl_stream.html#beast.ref.boost__beast__ssl_stream.synopsis)

Defined in header `<boost/beast/ssl/ssl_stream.hpp>`

```programlisting
template<
    class NextLayer>
struct ssl_stream :
    public net::ssl::stream< NextLayer >
```