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
handle\_session(ssl::stream stream)
{
// Perform the SSL handshake
co\_await stream.async\_handshake(ssl::stream\_base::server);
// Read and discard a request
beast::flat\_buffer buf;
http::request req;
co\_await http::async\_read(stream, buf, req);
// Write the response
http::response res;
res.body() = "Hello!";
co\_await http::async\_write(stream, res);
// Gracefully shutdown the SSL stream
auto [ec] = co\_await stream.async\_shutdown(net::as\_tuple);
if(ec && ec != ssl::error::stream\_truncated)
throw boost::system::system\_error(ec);
}
net::awaitable
acceptor(ssl::context& ctx)
{
auto executor = co\_await net::this\_coro::executor;
net::ip::tcp::endpoint endpoint{ {}, 8080 };
net::ip::tcp::acceptor acceptor{ executor, endpoint };
for(;;)
{
net::co\_spawn(
executor,
handle\_session({ co\_await acceptor.async\_accept(), ctx }),
print\_exception);
}
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
// Comment this line to disable client certificate request.
ctx.set\_verify\_mode(
ssl::verify\_peer | ssl::verify\_fail\_if\_no\_peer\_cert);
// The client's certificate will be verified against this
// certificate authority.
ctx.load\_verify\_file("ca.crt");
// In a real application, the passphrase would be read from
// a secure place, such as a key vault.
ctx.set\_password\_callback([](auto, auto) { return "123456"; });
// Server certificate and private key.
ctx.use\_certificate\_chain\_file("server.crt");
ctx.use\_private\_key\_file("server.key", ssl::context::pem);
// DH parameters for DHE-based cipher suites
ctx.use\_tmp\_dh\_file("dh4096.pem");
net::co\_spawn(ioc, acceptor(ctx), print\_exception);
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