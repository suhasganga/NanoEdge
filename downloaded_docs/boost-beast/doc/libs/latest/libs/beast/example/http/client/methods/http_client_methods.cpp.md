//
// Copyright (c) 2016-2019 Vinnie Falco (vinnie dot falco at gmail dot com)
//
// Distributed under the Boost Software License, Version 1.0. (See accompanying
// file LICENSE\_1\_0.txt or copy at http://www.boost.org/LICENSE\_1\_0.txt)
//
// Official repository: https://github.com/boostorg/beast
//
//------------------------------------------------------------------------------
//
// Example: HTTP client, synchronous for every method on httpbin
//
//------------------------------------------------------------------------------
//[example\_http\_client\_methods
#include 
#include 
#include 
#include 
#include 
#include 
#include 
#include 
namespace beast = boost::beast; // from 
namespace http = beast::http; // from 
namespace net = boost::asio; // from 
using tcp = net::ip::tcp; // from 
// perform a get request
void do\_get(beast::tcp\_stream & stream,
http::request & req,
beast::flat\_buffer buffer,
http::response & res)
{
req.target("/get");
req.method(beast::http::verb::get);
http::write(stream, req);
http::read(stream, buffer, res);
}
// perform a head request
void do\_head(beast::tcp\_stream & stream,
http::request & req,
beast::flat\_buffer buffer,
http::response & res)
{
// we reuse the get endpoint
req.target("/get");
req.method(beast::http::verb::head);
http::write(stream, req);
/\* the head response will send back a content-length
\* without a body. The other requests don't set content-length when not
\* sending a body back.
\*
\* the response parser doesn't know that we sent head,
\* so we need to manually make sure we're only reading the header
\* otherwise we're waiting forever for data.
\*/
http::response\_parser p;
http::read\_header(stream, buffer, p);
// move the result over
res = p.release();
}
// perform a patch request
void do\_patch(beast::tcp\_stream & stream,
http::request & req,
beast::flat\_buffer buffer,
http::response & res)
{
req.target("/patch");
req.method(beast::http::verb::patch);
req.body() = "Some random patch data";
req.prepare\_payload(); // set content-length based on the body
http::write(stream, req);
http::read(stream, buffer, res);
}
// perform a put request
void do\_put(beast::tcp\_stream & stream,
http::request & req,
beast::flat\_buffer buffer,
http::response & res)
{
req.target("/put");
req.method(beast::http::verb::put);
req.body() = "Some random put data";
req.prepare\_payload(); // set content-length based on the body
http::write(stream, req);
http::read(stream, buffer, res);
}
// perform a post request
void do\_post(beast::tcp\_stream & stream,
http::request & req,
beast::flat\_buffer buffer,
http::response & res)
{
req.target("/post");
req.method(beast::http::verb::post);
req.body() = "Some random post data";
req.prepare\_payload(); // set content-length based on the body
http::write(stream, req);
http::read(stream, buffer, res);
}
// perform a delete request
void do\_delete(beast::tcp\_stream & stream,
http::request & req,
beast::flat\_buffer buffer,
http::response & res)
{
req.target("/delete");
req.method(beast::http::verb::delete\_);
// NOTE: delete doesn't require a body
req.body() = "Some random delete data";
req.prepare\_payload(); // set content-length based on the body
http::write(stream, req);
http::read(stream, buffer, res);
}
// Performs an HTTP request against httpbin.cpp.al and prints request & response
int main(int argc, char\*\* argv)
{
try
{
// Check command line arguments.
if(argc != 2)
{
std::cerr <<
"Usage: http-client-method  \n" <<
"Example:\n" <<
" http-client-method get\n" <<
" http-client-method post\n";
return EXIT\_FAILURE;
}
for (char \* c = argv[1]; \*c != '\0'; c++)
\*c = static\_cast(std::tolower(\*c));
beast::string\_view method{argv[1]};
// The io\_context is required for all I/O
net::io\_context ioc;
// These objects perform our I/O
tcp::resolver resolver(ioc);
beast::tcp\_stream stream(ioc);
// Look up the domain name
auto const results = resolver.resolve("httpbin.cpp.al", "http");
// Make the connection on the IP address we get from a lookup
stream.connect(results);
// Set up an HTTP GET request message
http::request req;
req.set(http::field::host, "httpbin.cpp.al");
req.set(http::field::user\_agent, BOOST\_BEAST\_VERSION\_STRING);
// This buffer is used for reading and must be persisted
beast::flat\_buffer buffer;
// Declare a container to hold the response
http::response res;
if (method == "get")
do\_get(stream, req, buffer, res);
else if (method == "head")
do\_head(stream, req, buffer, res);
else if (method == "patch")
do\_patch(stream, req, buffer, res);
else if (method == "put")
do\_put(stream, req, buffer, res);
else if (method == "post")
do\_post(stream, req, buffer, res);
else if (method == "delete")
do\_delete(stream, req, buffer, res);
else
{
std::cerr << "Unknown method: " << method << std::endl;
return EXIT\_FAILURE;
}
// Write the message to standard out
std::cout << "Request send:\n-----------------------------\n"
<< req << std::endl;
// Write the message to standard out
std::cout << "\n\nResponse received:\n-----------------------------\n"
<< res << std::endl;
// Gracefully close the socket
beast::error\_code ec;
stream.socket().shutdown(tcp::socket::shutdown\_both, ec);
// not\_connected happens sometimes
// so don't bother reporting it.
//
if(ec && ec != beast::errc::not\_connected)
throw beast::system\_error{ec};
// If we get here then the connection is closed gracefully
}
catch(std::exception const& e)
{
std::cerr << "Error: " << e.what() << std::endl;
return EXIT\_FAILURE;
}
return EXIT\_SUCCESS;
}
//]