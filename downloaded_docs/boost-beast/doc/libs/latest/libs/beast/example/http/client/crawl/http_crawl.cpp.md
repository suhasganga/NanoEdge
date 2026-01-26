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
// Example: HTTP crawl (asynchronous)
//
//------------------------------------------------------------------------------
#include "urls\_large\_data.hpp"
#include 
#include 
#include 
#include 
#include 
#include 
#include 
#include 
#include 
#include 
#include 
#include 
#include 
#include 
#include 
#include 
#include 
#include 
#include 
namespace chrono = std::chrono; // from 
namespace beast = boost::beast; // from 
namespace http = beast::http; // from 
namespace net = boost::asio; // from 
using tcp = net::ip::tcp; // from 
//------------------------------------------------------------------------------
// This structure aggregates statistics on all the sites
class crawl\_report
{
net::strand<
net::io\_context::executor\_type> strand\_;
std::atomic index\_;
std::vector const& hosts\_;
std::size\_t count\_ = 0;
public:
crawl\_report(net::io\_context& ioc)
: strand\_(ioc.get\_executor())
, index\_(0)
, hosts\_(urls\_large\_data())
{
}
// Run an aggregation function on the strand.
// This allows synchronization without a mutex.
template
void
aggregate(F const& f)
{
net::post(
strand\_,
[&, f]
{
f(\*this);
if(count\_ % 100 == 0)
{
std::cerr <<
"Progress: " << count\_ << " of " << hosts\_.size() << "\n";
//std::cerr << \*this;
}
++count\_;
});
}
// Returns the next host to check
char const\*
get\_host()
{
auto const n = index\_++;
if(n >= hosts\_.size())
return nullptr;
return hosts\_[n];
}
// Counts the number of timer failures
std::size\_t timer\_failures = 0;
// Counts the number of name resolution failures
std::size\_t resolve\_failures = 0;
// Counts the number of connection failures
std::size\_t connect\_failures = 0;
// Counts the number of write failures
std::size\_t write\_failures = 0;
// Counts the number of read failures
std::size\_t read\_failures = 0;
// Counts the number of success reads
std::size\_t success = 0;
// Counts the number received of each status code
std::map status\_codes;
};
std::ostream&
operator<<(std::ostream& os, crawl\_report const& report)
{
// Print the report
os <<
"Crawl report\n" <<
" Failure counts\n" <<
" Timer : " << report.timer\_failures << "\n" <<
" Resolve : " << report.resolve\_failures << "\n" <<
" Connect : " << report.connect\_failures << "\n" <<
" Write : " << report.write\_failures << "\n" <<
" Read : " << report.read\_failures << "\n" <<
" Success : " << report.success << "\n" <<
" Status codes\n"
;
for(auto const& result : report.status\_codes)
os <<
" " << std::setw(3) << result.first << ": " << result.second <<
" (" << http::obsolete\_reason(static\_cast(result.first)) << ")\n";
os.flush();
return os;
}
//------------------------------------------------------------------------------
// Performs HTTP GET requests and aggregates the results into a report
class worker : public std::enable\_shared\_from\_this
{
enum
{
// Use a small timeout to keep things lively
timeout = 5
};
crawl\_report& report\_;
net::strand ex\_;
tcp::resolver resolver\_;
beast::tcp\_stream stream\_;
beast::flat\_buffer buffer\_; // (Must persist between reads)
http::request req\_;
http::response res\_;
public:
worker(worker&&) = default;
// Resolver and socket require an io\_context
worker(
crawl\_report& report,
net::io\_context& ioc)
: report\_(report)
, ex\_(net::make\_strand(ioc.get\_executor()))
, resolver\_(ex\_)
, stream\_(ex\_)
{
// Set up the common fields of the request
req\_.version(11);
req\_.method(http::verb::get);
req\_.target("/");
req\_.set(http::field::user\_agent, BOOST\_BEAST\_VERSION\_STRING);
}
// Start the asynchronous operation
void
run()
{
do\_get\_host();
}
void
do\_get\_host()
{
// Grab another host
auto const host = report\_.get\_host();
// nullptr means no more work
if(! host)
return;
// The Host HTTP field is required
req\_.set(http::field::host, host);
// Set up an HTTP GET request message
// Look up the domain name
resolver\_.async\_resolve(
host,
"http",
beast::bind\_front\_handler(
&worker::on\_resolve,
shared\_from\_this()));
}
void
on\_resolve(
beast::error\_code ec,
tcp::resolver::results\_type results)
{
if(ec)
{
report\_.aggregate(
[](crawl\_report& rep)
{
++rep.resolve\_failures;
});
return do\_get\_host();
}
// Set a timeout on the operation
stream\_.expires\_after(std::chrono::seconds(10));
// Make the connection on the IP address we get from a lookup
stream\_.async\_connect(
results,
beast::bind\_front\_handler(
&worker::on\_connect,
shared\_from\_this()));
}
void
on\_connect(beast::error\_code ec, tcp::resolver::results\_type::endpoint\_type)
{
if(ec)
{
report\_.aggregate(
[](crawl\_report& rep)
{
++rep.connect\_failures;
});
return do\_get\_host();
}
// Set a timeout on the operation
stream\_.expires\_after(std::chrono::seconds(10));
// Send the HTTP request to the remote host
http::async\_write(
stream\_,
req\_,
beast::bind\_front\_handler(
&worker::on\_write,
shared\_from\_this()));
}
void
on\_write(
beast::error\_code ec,
std::size\_t bytes\_transferred)
{
boost::ignore\_unused(bytes\_transferred);
if(ec)
{
report\_.aggregate(
[](crawl\_report& rep)
{
++rep.write\_failures;
});
return do\_get\_host();
}
// Receive the HTTP response
res\_ = {};
http::async\_read(
stream\_,
buffer\_,
res\_,
beast::bind\_front\_handler(
&worker::on\_read,
shared\_from\_this()));
}
void
on\_read(
beast::error\_code ec,
std::size\_t bytes\_transferred)
{
boost::ignore\_unused(bytes\_transferred);
if(ec)
{
report\_.aggregate(
[](crawl\_report& rep)
{
++rep.read\_failures;
});
return do\_get\_host();
}
auto const code = res\_.result\_int();
report\_.aggregate(
[code](crawl\_report& rep)
{
++rep.success;
++rep.status\_codes[code];
});
// Gracefully close the socket
stream\_.socket().shutdown(tcp::socket::shutdown\_both, ec);
stream\_.close();
// If we get here then the connection is closed gracefully
do\_get\_host();
}
};
class timer
{
using clock\_type = chrono::system\_clock;
clock\_type::time\_point when\_;
public:
using duration = clock\_type::duration;
timer()
: when\_(clock\_type::now())
{
}
duration
elapsed() const
{
return clock\_type::now() - when\_;
}
};
int main(int argc, char\* argv[])
{
// Check command line arguments.
if (argc != 2)
{
std::cerr <<
"Usage: http-crawl \n" <<
"Example:\n" <<
" http-crawl 100\n";
return EXIT\_FAILURE;
}
auto const threads = std::max(1, std::atoi(argv[1]));
// The io\_context is used to aggregate the statistics
net::io\_context ioc;
// The report holds the aggregated statistics
crawl\_report report{ioc};
timer t;
// Create and launch the worker threads.
std::vector workers;
workers.reserve(threads + 1);
for(int i = 0; i < threads; ++i)
{
// Each worker will eventually add some data to the aggregated
// report. Outstanding work is tracked in each worker to
// represent the forthcoming delivery of this data by that
// worker.
auto reporting\_work = net::require(
ioc.get\_executor(),
net::execution::outstanding\_work.tracked);
workers.emplace\_back(
[&report, reporting\_work] {
// We use a separate io\_context for each worker because
// the asio resolver simulates asynchronous operation using
// a dedicated worker thread per io\_context, and we want to
// do a lot of name resolutions in parallel.
net::io\_context ioc;
std::make\_shared(report, ioc)->run();
ioc.run();
});
}
// Add another thread to run the main io\_context which
// is used to aggregate the statistics
workers.emplace\_back(
[&ioc]
{
ioc.run();
});
// Now block until all threads exit
for(std::size\_t i = 0; i < workers.size(); ++i)
workers[i].join();
std::cout <<
"Elapsed time: " << chrono::duration\_cast(t.elapsed()).count() << " seconds\n";
std::cout << report;
return EXIT\_SUCCESS;
}