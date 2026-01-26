### [SSL/TLS Shutdown](ssl_tls_shutdown.html "SSL/TLS Shutdown")

A secure SSL/TLS connection requires a proper shutdown process to securely
indicate the [*EOF*](https://en.wikipedia.org/wiki/End-of-file)
condition. This process prevents a type of attack known as a [*truncation
attack*](https://en.wikipedia.org/wiki/Transport_Layer_Security#Truncation_attack) in which an attacker can close the underlying transport
layer and control the length of the last message in the SSL/TLS connection.
A shutdown process consists of exchanging `close_notify`
message between two parties. In [Boost.Asio](../../../../../../libs/asio/index.html)
these steps happen by calling `shutdown()` or `async_shutdown()` on `ssl::stream`
object.

#### [error::stream\_truncated](ssl_tls_shutdown.html#beast.using_io.ssl_tls_shutdown.error_stream_truncated "error::stream_truncated")

There are SSL/TLS implementations that don't perform a proper shutdown
process and simply close the underlying transport layer instead. As a result,
the EOF condition in these applications is not cryptographically secure
and should not be relied upon. However, there are scenarios where an HTTPS
client or server doesn't need EOF for determining the end of the last message:

* The HTTP message has a `Content-Length`
  header, and the body is fully received (a known body length).
* The HTTP message uses chunked transfer encoding, and the final chunk
  is received.
* The HTTP message doesn't contain a body, such as any response with
  a 1xx (Informational), 204 (No Content), or 304 (Not Modified) status
  code.

In such scenarios, `http::read`
or `http::async_read` operations succeed as they
don't need EOF to complete. However, the next operation on the stream would
fail with an [`net::ssl::error::stream_truncated`](../../../../../../doc/html/boost_asio/reference/ssl__error__stream_errors.html) error.

For example, let's assume we are using Beast for communicating with an
HTTPS server that doesn't perform a proper SSL/TLS shutdown:

```programlisting
// Receive the HTTP response
http::read(stream, buffer, res);

// Gracefully shutdown the SSL/TLS connection
error_code ec;
stream.shutdown(ec);
// Non-compliant servers don't participate in the SSL/TLS shutdown process and
// close the underlying transport layer. This causes the shutdown operation to
// complete with a `stream_truncated` error. One might decide not to log such
// errors as there are many non-compliant servers in the wild.
if(ec != net::ssl::error::stream_truncated)
    log(ec);
```

###### [Non-Compliant Peers and Unknown Body Length](ssl_tls_shutdown.html#beast.using_io.ssl_tls_shutdown.error_stream_truncated.non_compliant_peers_and_unknown_)

This is a rare case and indeed a security issue when HTTPS servers don't
perform a proper SSL/TLS shutdown procedure and send an HTTP response message
that relies on EOF to determine the end of the body. This is a security
concern because without an SSL/TLS shutdown procedure, the EOF is not cryptographically
secure, leaving the message body vulnerable to truncation attacks.

The following is an example that can read an HTTP response from such a
server:

```programlisting
// Use an HTTP response parser to have more control
http::response_parser<http::dynamic_body> parser;

error_code ec;
// Receive the HTTP response until the end or until an error occurs
http::read(stream, buffer, parser, ec);

// Try to manually commit the EOF, the resulting message body would be
// vulnerable to truncation attacks.
if(parser.need_eof() && ec == net::ssl::error::stream_truncated)
    parser.put_eof(ec); // Override the error_code

if(ec)
    throw system_error{ec};

// Access the HTTP response inside the parser
std::cout << parser.get() << std::endl;

// Gracefully shutdown the SSL/TLS connection
stream.shutdown(ec); // Override the error_code
// Non-compliant servers don't participate in the SSL/TLS shutdown process and
// close the underlying transport layer. This causes the shutdown operation to
// complete with a `stream_truncated` error. One might decide not to log such
// errors as there are many non-compliant servers in the wild.
if(ec != net::ssl::error::stream_truncated)
    log(ec);
```