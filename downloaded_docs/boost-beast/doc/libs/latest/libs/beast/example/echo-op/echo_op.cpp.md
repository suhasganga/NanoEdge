//
// Copyright (c) 2016-2019 Vinnie Falco (vinnie dot falco at gmail dot com)
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
#include 
namespace net = boost::asio;
namespace beast = boost::beast;
//[example\_core\_echo\_op\_1
template<
class AsyncStream,
class DynamicBuffer,
class CompletionToken>
auto
async\_echo (AsyncStream& stream, DynamicBuffer& buffer, CompletionToken&& token)
//]
->
typename net::async\_result<
typename std::decay::type,
void(beast::error\_code)>::return\_type;
//------------------------------------------------------------------------------
//[example\_core\_echo\_op\_2
/\*\* Asynchronously read a line and echo it back.
This function is used to asynchronously read a line ending
in a newline (`"\n"`) from the stream, and then write
it back.
This call always returns immediately. The asynchronous operation
will continue until one of the following conditions is true:
@li A line was read in and written back on the stream
@li An error occurs.
The algorithm, known as a *composed asynchronous operation*,
is implemented in terms of calls to the stream's `async\_read\_some`
and `async\_write\_some` function. The program must ensure that no
other reads or writes are performed until this operation completes.
Since the length of the line is not known ahead of time, the
implementation may read additional characters that lie past the
first line. These characters are stored in the dynamic buffer\_.
The same dynamic buffer must be presented again in each call,
to provide the implementation with any leftover bytes.
@param stream The stream to operate on. The type must meet the
requirements of *AsyncReadStream* and @AsyncWriteStream
@param buffer A dynamic buffer to hold implementation-defined
temporary data. Ownership is not transferred; the caller is
responsible for ensuring that the lifetime of this object is
extended least until the completion handler is invoked.
@param token The handler to be called when the operation completes.
The implementation takes ownership of the handler by performing a decay-copy.
The handler must be invocable with this signature:
@code
void handler(
beast::error\_code error // Result of operation.
);
@endcode
Regardless of whether the asynchronous operation completes immediately or
not, the handler will not be invoked from within this function. Invocation
of the handler will be performed in a manner equivalent to using
`net::post`.
\*/
template<
class AsyncStream,
class DynamicBuffer,
class CompletionToken>
auto
async\_echo (
AsyncStream& stream,
DynamicBuffer& buffer, /\*< Unlike Asio, we pass by non-const reference instead of rvalue-ref >\*/
CompletionToken&& token) ->
typename net::async\_result< /\*< `async\_result` deduces the return type from the completion handler >\*/
typename std::decay::type,
void(beast::error\_code) /\*< The completion handler signature goes here >\*/
>::return\_type;
//]
//[example\_core\_echo\_op\_3
template
class echo\_op;
// This example uses the Asio's stackless "fauxroutines", implemented
// using a macro-based solution. It makes the code easier to write and
// easier to read. This include file defines the necessary macros and types.
#include 
// Read a line and echo it back
//
template<
class AsyncStream,
class DynamicBuffer,
class CompletionToken>
auto
async\_echo(
AsyncStream& stream,
DynamicBuffer& buffer,
CompletionToken&& token) ->
typename net::async\_result<
typename std::decay::type,
void(beast::error\_code)>::return\_type /\*< The completion handler signature goes here >\*/
{
// Perform some type checks using static assert, this helps
// with more friendly error messages when passing the wrong types.
static\_assert(
beast::is\_async\_stream::value,
"AsyncStream type requirements not met");
static\_assert(
net::is\_dynamic\_buffer::value,
"DynamicBuffer type requirements not met");
// This class template deduces the actual handler type from a
// CompletionToken, captures a local reference to the handler,
// and creates the `async\_result` object which becomes the
// return value of this initiating function.
net::async\_completion init(token);
// The helper macro BOOST\_ASIO\_HANDLER\_TYPE converts the completion
// token type into a concrete handler type of the correct signature.
using handler\_type = BOOST\_ASIO\_HANDLER\_TYPE(CompletionToken, void(beast::error\_code));
// The class template `async\_base` holds the caller's completion
// handler for us, and provides all of the boilerplate for forwarding
// the associated allocator and associated executor from the caller's
// handler to our operation. It also maintains a `net::executor\_work\_guard`
// for the executor associated with the stream. This work guard is
// inexpensive, and prevents the execution context from running out
// of work. It is usually necessary although rarely it can be skipped
// depending on the operation (this echo example needs it because it
// performs more than one asynchronous operation in a row).
// We declare this type alias to make the code easier to read.
using base\_type = beast::async\_base<
handler\_type, /\*< The type of the completion handler obtained from the token >\*/
beast::executor\_type /\*< The type of executor used by the stream to dispatch asynchronous operations >\*/
>;
// This nested class implements the echo composed operation as a
// stateful completion handler. We derive from `async\_base` to
// take care of boilerplate and we derived from asio::coroutine to
// allow the reenter and yield keywords to work.
struct echo\_op : base\_type, boost::asio::coroutine
{
AsyncStream& stream\_;
DynamicBuffer& buffer\_;
echo\_op(
AsyncStream& stream,
DynamicBuffer& buffer,
handler\_type&& handler)
: base\_type(
std::move(handler), /\*< The `async\_base` helper takes ownership of the handler, >\*/
stream.get\_executor()) /\*< and also needs to know which executor to use. >\*/
, stream\_(stream)
, buffer\_(buffer)
{
// Launch the operation directly from the constructor. We
// pass `false` for `cont` to indicate that the calling
// thread does not represent a continuation of our
// asynchronous control flow.
(\*this)({}, 0, false);
}
// If a newline is present in the buffer sequence, this function returns
// the number of characters from the beginning of the buffer up to the
// newline, including the newline character. Otherwise it returns zero.
std::size\_t
find\_newline(typename DynamicBuffer::const\_buffers\_type const& buffers)
{
// The `buffers\_iterator` class template provides random-access
// iterators into a buffer sequence. Use the standard algorithm
// to look for the new line if it exists.
auto begin = net::buffers\_iterator<
typename DynamicBuffer::const\_buffers\_type>::begin(buffers);
auto end = net::buffers\_iterator<
typename DynamicBuffer::const\_buffers\_type>::end(buffers);
auto result = std::find(begin, end, '\n');
if(result == end)
return 0; // not found
return result + 1 - begin;
}
// This is the entry point of our completion handler. Every time an
// asynchronous operation completes, this function will be invoked.
void
operator()(
beast::error\_code ec,
std::size\_t bytes\_transferred = 0,
bool cont = true) /\*< Second and subsequent invocations will seee `cont=true`. \*/
{
// The `reenter` keyword transfers control to the last
// yield point, or to the beginning of the scope if
// this is the first time.
reenter(\*this)
{
for(;;)
{
std::size\_t pos;
// Search for a newline in the readable bytes of the buffer
pos = find\_newline(buffer\_.data());
// If we don't have the newline, then read more
if(pos == 0)
{
std::size\_t bytes\_to\_read;
// Determine the number of bytes to read,
// using available capacity in the buffer first.
bytes\_to\_read = std::min(
std::max(512, // under 512 is too little,
buffer\_.capacity() - buffer\_.size()),
std::min(65536, // and over 65536 is too much.
buffer\_.max\_size() - buffer\_.size()));
// Read some data into our dynamic buffer\_. We transfer
// ownership of the composed operation by using the
// `std::move(\*this)` idiom. The `yield` keyword causes
// the function to return immediately after the initiating
// function returns.
yield stream\_.async\_read\_some(
buffer\_.prepare(bytes\_to\_read), std::move(\*this));
// After the `async\_read\_some` completes, control is
// transferred to this line by the `reenter` keyword.
// Move the bytes read from the writable area to the
// readable area.
buffer\_.commit(bytes\_transferred);
// If an error occurs, deliver it to the caller's completion handler.
if(ec)
break;
// Keep looping until we get the newline
continue;
}
// We have our newline, so send the first `pos` bytes of the
// buffers. The function `buffers\_prefix` returns the front part
// of the buffers we want.
yield net::async\_write(stream\_,
beast::buffers\_prefix(pos, buffer\_.data()), std::move(\*this));
// After the `async\_write` completes, our completion handler will
// be invoked with the error and the number of bytes transferred,
// and the `reenter` statement above will cause control to jump
// to the following line. The variable `pos` is no longer valid
// (remember that we returned from the function using `yield` above)
// but we can use `bytes\_transferred` to know how much of the buffer
// to consume. With "real" coroutines this will be easier and more
// natural.
buffer\_.consume(bytes\_transferred);
// The loop terminates here, and we will either deliver a
// successful result or an error to the caller's completion handler.
break;
}
// When a composed operation completes immediately, it must not
// directly invoke the completion handler otherwise it could
// lead to unfairness, starvation, or stack overflow. Therefore,
// if cont == false (meaning, that the call stack still includes
// the frame of the initiating function) then we need to use
// `net::post` to cause us to be called again after the initiating
// function. The function `async\_base::invoke` takes care of
// calling the final completion handler, using post if the
// first argument is false, otherwise invoking it directly.
this->complete(cont, ec);
}
}
};
// Create the composed operation and launch it. This is a constructor
// call followed by invocation of operator(). We use BOOST\_ASIO\_HANDLER\_TYPE
// to convert the completion token into the correct handler type,
// allowing user-defined specializations of the async\_result template
// to be used.
echo\_op(stream, buffer, std::move(init.completion\_handler));
// This hook lets the caller see a return value when appropriate.
// For example this might return std::future if
// CompletionToken is net::use\_future, or this might
// return an error code if CompletionToken specifies a coroutine.
return init.result.get();
}
// Including this file undefines the macros used by the stackless fauxroutines.
#include 
//]
struct move\_only\_handler
{
move\_only\_handler() = default;
move\_only\_handler(move\_only\_handler&&) = default;
move\_only\_handler(move\_only\_handler const&) = delete;
void operator()(beast::error\_code ec)
{
if(ec)
std::cerr << ": " << ec.message() << std::endl;
}
};
int main(int argc, char\*\* argv)
{
if(argc != 3)
{
std::cerr
<< "Usage: echo-op  \n"
<< "Example:\n"
<< " echo-op 0.0.0.0 8080\n";
return EXIT\_FAILURE;
}
namespace net = boost::asio;
auto const address = net::ip::make\_address(argv[1]);
auto const port = static\_cast(std::atoi(argv[2]));
using endpoint\_type = net::ip::tcp::endpoint;
// Create a listening socket, accept a connection, perform
// the echo, and then shut everything down and exit.
net::io\_context ioc;
net::ip::tcp::acceptor acceptor{ioc};
endpoint\_type ep(address, port);
acceptor.open(ep.protocol());
acceptor.set\_option(net::socket\_base::reuse\_address(true));
acceptor.bind(ep);
acceptor.listen();
auto sock = acceptor.accept();
beast::flat\_buffer buffer;
async\_echo(sock, buffer, move\_only\_handler{});
ioc.run();
return EXIT\_SUCCESS;
}