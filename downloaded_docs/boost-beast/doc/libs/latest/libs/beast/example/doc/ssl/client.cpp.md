//
// Copyright (c) 2025 Mohammad Nejati
//
// Distributed under the Boost Software License, Version 1.0. (See accompanying
// file LICENSE\_1\_0.txt or copy at http://www.boost.org/LICENSE\_1\_0.txt)
//
// Official repository: https://github.com/boostorg/beast
//
#include 
#include 
#include 
#include 
#include 
#if defined(BOOST\_ASIO\_HAS\_CO\_AWAIT)
namespace beast = boost::beast;
namespace http = beast::http;
namespace net = boost::asio;
namespace ssl = net::ssl;
void
print\_exception(std::exception\_ptr eptr)
{
if(eptr)
{
try
{
std::rethrow\_exception(eptr);
}
catch(std::exception& e)
{
std::cerr << e.what() << std::endl;
}
}
}
net::awaitable
request(ssl::context& ctx)
{
auto executor = co\_await net::this\_coro::executor;
net::ip::tcp::endpoint endpoint{ {}, 8080 };
ssl::stream stream{ executor, ctx };
// Connect TCP socket
co\_await stream.lowest\_layer().async\_connect(endpoint);
// Set Server Name Indication (SNI)
if(!SSL\_set\_tlsext\_host\_name(stream.native\_handle(), "localhost"))
{
throw beast::system\_error(
static\_cast(::ERR\_get\_error()),
net::error::get\_ssl\_category());
}
// Set a callback to verify that the hostname in the server
// certificate matches the expected value
stream.set\_verify\_callback(ssl::host\_name\_verification("localhost"));
// Perform the SSL handshake
co\_await stream.async\_handshake(ssl::stream\_base::client);
// Write an HTTP GET request
http::request req{ http::verb::get, "/", 11 };
req.set(http::field::host, "localhost");
req.set(http::field::user\_agent, BOOST\_BEAST\_VERSION\_STRING);
co\_await http::async\_write(stream, req);
// Read the response
beast::flat\_buffer buf;
http::response res;
co\_await http::async\_read(stream, buf, res);
// Print the response body
std::cout << res.body();
// Gracefully shutdown the SSL stream
auto [ec] = co\_await stream.async\_shutdown(net::as\_tuple);
if(ec && ec != ssl::error::stream\_truncated)
throw boost::system::system\_error(ec);
}
int
main()
{
try
{
// The io\_context is required for all I/O
net::io\_context ioc;
// The SSL context is required, and holds certificates,
// configurations and session related data
ssl::context ctx{ ssl::context::sslv23 };
// https://docs.openssl.org/3.4/man3/SSL\_CTX\_set\_options/
ctx.set\_options(
ssl::context::no\_sslv2 | ssl::context::default\_workarounds |
ssl::context::single\_dh\_use);
// set up the peer verification mode so that the TLS/SSL handshake fails
// if the certificate verification is unsuccessful
ctx.set\_verify\_mode(ssl::verify\_peer);
// The servers's certificate will be verified against this
// certificate authority.
ctx.load\_verify\_file("ca.crt");
// In a real application, the passphrase would be read from
// a secure place, such as a key vault.
ctx.set\_password\_callback([](auto, auto) { return "123456"; });
// Client certificate and private key (if server request for).
ctx.use\_certificate\_chain\_file("client.crt");
ctx.use\_private\_key\_file("client.key", ssl::context::pem);
net::co\_spawn(ioc, request(ctx), print\_exception);
ioc.run();
}
catch(std::exception& e)
{
std::cerr << e.what() << std::endl;
}
}
#else
int
main(int, char\*[])
{
std::printf("awaitables require C++20\n");
return EXIT\_FAILURE;
}
#endif