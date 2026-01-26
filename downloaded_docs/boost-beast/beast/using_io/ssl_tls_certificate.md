### [SSL/TLS Certificate](ssl_tls_certificate.html "SSL/TLS Certificate")

##### [Certificate Authority](ssl_tls_certificate.html#beast.using_io.ssl_tls_certificate.certificate_authority)

A Certificate Authority (CA) is a trusted entity that signs digital certificates,
enabling users to verify their authenticity. Rather than storing every individual
certificate for each server (which would be impractical due to the sheer
volume and frequent renewals), users can store a limited set of root certificates
to authenticate server certificates as needed.

Boost.Asio provides various methods for loading certificate authority certificates:

* [`net::ssl::context::add_certificate_authority`](../../../../../../doc/html/boost_asio/reference/ssl__context/add_certificate_authority.html)
* [`net::ssl::context::add_verify_path`](../../../../../../doc/html/boost_asio/reference/ssl__context/add_verify_path.html)
* [`net::ssl::context::load_verify_file`](../../../../../../doc/html/boost_asio/reference/ssl__context/load_verify_file.html)
* [`net::ssl::context::set_default_verify_paths`](../../../../../../doc/html/boost_asio/reference/ssl__context/set_default_verify_paths.html)

It is important to set up peer verification so that the TLS/SSL handshake
fails if certificate verification is unsuccessful:

```programlisting
// Verify the remote server's certificate
ctx.set_verify_mode(net::ssl::verify_peer);
```

A client must also verify that the hostname or IP address in the certificate
matches the expected one. The [`net::ssl::host_name_verification`](../../../../../../doc/html/boost_asio/reference/ssl__host_name_verification.html)
helper function object can perform this verification according to the rules
described in RFC 6125:

```programlisting
// Verify the remote server's Hostname or IP address
stream.set_verify_callback(
    net::ssl::host_name_verification("host.name"));
```

A server can also request and verify a client certificate to authenticate
the client:

```programlisting
// Verify the remote client's certificate
ctx.set_verify_mode(
    net::ssl::verify_peer |
    net::ssl::verify_fail_if_no_peer_cert);
```

##### [Server Certificate](ssl_tls_certificate.html#beast.using_io.ssl_tls_certificate.server_certificate)

A Server Certificate is a digital certificate that confirms a server's identity
as the legitimate destination for a client. It contains a verifiable signature
that ensures it was issued by a trusted certificate authority (CA).

When a server certificate is issued by an intermediate certificate authority,
and the client lacks those intermediate certificates, the server should provide
all the relevant certificates to the client. This allows the client to verify
the final certificate in the chain against the root certificate.

The following Boost.Asio methods can be used for loading a certificate or
a certificate chain:

* [`net::ssl::context::use_certificate`](../../../../../../doc/html/boost_asio/reference/ssl__context/use_certificate.html)
* [`net::ssl::context::use_certificate_file`](../../../../../../doc/html/boost_asio/reference/ssl__context/use_certificate_file.html)
* [`net::ssl::context::use_certificate_chain`](../../../../../../doc/html/boost_asio/reference/ssl__context/use_certificate_chain.html)
* [`net::ssl::context::use_certificate_chain_file`](../../../../../../doc/html/boost_asio/reference/ssl__context/use_certificate_chain_file.html)

##### [Client Certificate](ssl_tls_certificate.html#beast.using_io.ssl_tls_certificate.client_certificate)

A server can authenticate clients by requiring and verifying their certificates,
preventing access for those without a valid certificate and private key.
The server enforces this by modifying peer verification settings:

```programlisting
// Verify the remote client's certificate
ctx.set_verify_mode(
    net::ssl::verify_peer |
    net::ssl::verify_fail_if_no_peer_cert);
```

If used, the necessary CA certificates must be loaded into the server's SSL
context to enable verification of the client's certificate.

##### [Common Name and Subject Alternative Name](ssl_tls_certificate.html#beast.using_io.ssl_tls_certificate.common_name_and_subject_alternat)

The Subject Alternative Name (SAN) is an extension in X.509 certificates
that allows multiple domain names, subdomains, or IP addresses to be associated
with a single SSL/TLS certificate. Before that it was the Common Name field
in the certificate subject which could contain a single hostname.

[RFC
6125](https://datatracker.ietf.org/doc/html/rfc6125#appendix-B.2) recommends that if a certificate includes a SAN dNSName field,
the client must ignore the subject CN field. Some modern browsers, such as
Google Chrome, check only the SAN section in an SSL/TLS certificate and reject
certificates that contain only the CN field.

##### [Private Key](ssl_tls_certificate.html#beast.using_io.ssl_tls_certificate.private_key)

The private key of a certificate is required during the SSL/TLS handshake
to prove that the certificate's provider is its rightful owner

The following Boost.Asio methods can be used for loading a private key:

* [`net::ssl::context::use_private_key`](../../../../../../doc/html/boost_asio/reference/ssl__context/use_private_key.html)
* [`net::ssl::context::use_private_key_file`](../../../../../../doc/html/boost_asio/reference/ssl__context/use_private_key_file.html)
* [`net::ssl::context::use_rsa_private_key`](../../../../../../doc/html/boost_asio/reference/ssl__context/use_rsa_private_key.html)
* [`net::ssl::context::use_rsa_private_key_file`](../../../../../../doc/html/boost_asio/reference/ssl__context/use_rsa_private_key_file.html)

If the private key is secured with a password, the [net::ssl::context::set\_password\_callback](../../../../../../doc/html/boost_asio/reference/ssl__context/set_password_callback.html)
allows specifying a callable object to retrieve the password.

##### [Self-Signed and Self-Issued Certificates](ssl_tls_certificate.html#beast.using_io.ssl_tls_certificate.self_signed_and_self_issued_cert)

A self-issued certificate is a certificate where the issuer and subject are
the same entity.

A self-signed certificate is a self-issued certificate in which the digital
signature can be verified using the public key within the certificate.

|  |  |
| --- | --- |
| [Warning] | Warning |
| Installing an untrusted, self-issued, or self-signed CA certificate poses a significant security risk, as there are no restrictions on the domains for which it can issue certificates. This allows attackers to generate fraudulent certificates for any public domain, enabling man-in-the-middle attacks if they gain access to your network. |

##### [Diffie-Hellman (DH) Parameters](ssl_tls_certificate.html#beast.using_io.ssl_tls_certificate.diffie_hellman_dh_parameters)

Diffie-Hellman (DH) key exchange is a cryptographic protocol that allows
two parties to securely establish a shared secret over an insecure communication
channel. The key exchange process involves both parties agreeing on a set
of parameters, known as Diffie-Hellman parameters, which include a large
prime number `p` and a generator
`g`. Since generating these
parameters is a computationally expensive task, a user might prefer to provide
a precomputed value at startup.

The following Boost.Asio methods can be used for loading DH parameters:

* [`net::ssl::context::use_tmp_dh`](../../../../../../doc/html/boost_asio/reference/ssl__context/use_tmp_dh.html)
* [`net::ssl::context::use_tmp_dh_file`](../../../../../../doc/html/boost_asio/reference/ssl__context/use_tmp_dh_file.html)

If no DH parameter is provided, OpenSSL will refuse to perform any handshake
that uses DHE-based cipher suites but will still work with other cipher suites,
such as those based on ECDHE.

##### [A Self-Issued Certificate Example](ssl_tls_certificate.html#beast.using_io.ssl_tls_certificate.a_self_issued_certificate_exampl)

In the following example, we will generate a self-signed CA certificate and
use it to issue both server and client certificates.

* Generate a CA certificate:

```programlisting
openssl req -new -newkey rsa:4096 -keyout ca.key -x509 -out ca.crt -subj "/CN=localhost" -days 365
```

* Generate a Server CSR:

```programlisting
openssl req -new -newkey rsa:4096 -keyout server.key -out server.csr -subj "/CN=localhost" -addext "subjectAltName=DNS:localhost,IP:127.0.0.1"
```

* Sign the Server CSR using our CA:

```programlisting
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -copy_extensions copy -days 365 -out server.crt
```

* Generate a Client CSR:

```programlisting
openssl req -new -newkey rsa:4096 -keyout client.key -out client.csr -subj "/CN=client.1"
```

* Sign the Client CSR using our CA:

```programlisting
openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -days 365 -out client.crt
```

* Generate a DH parameters file:

```programlisting
openssl dhparam -out dh4096.pem 4096
```

Server example: [server.cpp](../../../../example/doc/ssl/server.cpp)

Note that the server is configured in such a way that it requests and verifies
the client certificate. You can disable this by commenting out the related
line in the example.

You can test the server using this cURL command:

```programlisting
curl https://localhost:8080 --cacert ca.crt --cert client.crt --key client.key
```

Also, you can use the client example: [client.cpp](../../../../example/doc/ssl/client.cpp)