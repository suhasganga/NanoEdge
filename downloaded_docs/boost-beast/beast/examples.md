## [Examples](examples.html "Examples")

Source code and build scripts for these programs are located in the [example](../../../example) directory.

### [Clients](examples.html#beast.examples.clients "Clients")

These HTTP clients submit a GET request to a server specified on the command
line, and prints the resulting response. The crawl client asynchronously
fetches the document root of the 10,000 top ranked domains, this may be used
to evaluate robustness. All asynchronous clients support timeouts.

| Description | Source File | Source File (using SSL) |
| --- | --- | --- |
| HTTP, synchronous | [http\_client\_sync.cpp](../../../example/http/client/sync/http_client_sync.cpp) | [http\_client\_sync\_ssl.cpp](../../../example/http/client/sync-ssl/http_client_sync_ssl.cpp) |
| HTTP, asynchronous | [http\_client\_async.cpp](../../../example/http/client/async/http_client_async.cpp) | [http\_client\_async\_ssl.cpp](../../../example/http/client/async-ssl/http_client_async_ssl.cpp) |
| HTTP, asynchronous Unix domain sockets | [http\_client\_async\_local.cpp](../../../example/http/client/async-local/http_client_async_local.cpp) |  |
| HTTP, asynchronous using [`net::system_executor`](../../../../../doc/html/boost_asio/reference/system_executor.html) |  | [http\_client\_async\_ssl\_system\_executor.cpp](../../../example/http/client/async-ssl-system-executor/http_client_async_ssl_system_executor.cpp) |
| HTTP, coroutine | [http\_client\_coro.cpp](../../../example/http/client/coro/http_client_coro.cpp) | [http\_client\_coro\_ssl.cpp](../../../example/http/client/coro-ssl/http_client_coro_ssl.cpp) |
| HTTP, C++20 coroutine | [http\_client\_awaitable.cpp](../../../example/http/client/awaitable/http_client_awaitable.cpp) | [http\_client\_awaitable\_ssl.cpp](../../../example/http/client/awaitable-ssl/http_client_awaitable_ssl.cpp) |
| HTTP crawl (asynchronous) | [http\_crawl.cpp](../../../example/http/client/crawl/http_crawl.cpp) |  |
| HTTP json\_body (synchronous) | [json\_client.cpp](../../../example/http/client/body/json_client.hpp) |
| HTTP client for all methods (synchronous) | [http\_client\_methods.cpp](../../../example/http/client/methods/http_client_methods.cpp) |

These WebSocket clients connect to a server and send a message, then receive
a message and print the response before disconnecting. All asynchronous clients
support timeouts.

| Description | Source File | Source File (using SSL) |
| --- | --- | --- |
| WebSocket, synchronous | [websocket\_client\_sync.cpp](../../../example/websocket/client/sync/websocket_client_sync.cpp) | [websocket\_client\_sync\_ssl.cpp](../../../example/websocket/client/sync-ssl/websocket_client_sync_ssl.cpp) |
| WebSocket, asynchronous | [websocket\_client\_async.cpp](../../../example/websocket/client/async/websocket_client_async.cpp) | [websocket\_client\_async\_ssl.cpp](../../../example/websocket/client/async-ssl/websocket_client_async_ssl.cpp) |
| WebSocket, asynchronous Unix domain sockets | [websocket\_client\_async\_local.cpp](../../../example/websocket/client/async-local/websocket_client_async_local.cpp) |  |
| WebSocket, asynchronous using [`net::system_executor`](../../../../../doc/html/boost_asio/reference/system_executor.html) |  | [websocket\_client\_async\_ssl\_system\_executor.cpp](../../../example/websocket/client/async-ssl-system-executor/websocket_client_async_ssl_system_executor.cpp) |
| WebSocket, coroutine | [websocket\_client\_coro.cpp](../../../example/websocket/client/coro/websocket_client_coro.cpp) | [websocket\_client\_coro\_ssl.cpp](../../../example/websocket/client/coro-ssl/websocket_client_coro_ssl.cpp) |
| WebSocket, C++20 coroutine | [websocket\_client\_awaitable.cpp](../../../example/websocket/client/awaitable/websocket_client_awaitable.cpp) |  |

### [Servers](examples.html#beast.examples.servers "Servers")

These HTTP servers deliver files from a root directory specified on the command
line. All asynchronous servers support timeouts.

| Description | Source File | Source File (using SSL) |
| --- | --- | --- |
| HTTP, synchronous | [http\_server\_sync.cpp](../../../example/http/server/sync/http_server_sync.cpp) | [http\_server\_sync\_ssl.cpp](../../../example/http/server/sync-ssl/http_server_sync_ssl.cpp) |
| HTTP, asynchronous | [http\_server\_async.cpp](../../../example/http/server/async/http_server_async.cpp) | [http\_server\_async\_ssl.cpp](../../../example/http/server/async-ssl/http_server_async_ssl.cpp) |
| HTTP, asynchronous Unix domain sockets | [http\_server\_async\_local.cpp](../../../example/http/server/async-local/http_server_async_local.cpp) |  |
| HTTP, coroutine | [http\_server\_coro.cpp](../../../example/http/server/coro/http_server_coro.cpp) | [http\_server\_coro\_ssl.cpp](../../../example/http/server/coro-ssl/http_server_coro_ssl.cpp) |
| HTTP, stackless coroutine | [http\_server\_stackless.cpp](../../../example/http/server/stackless/http_server_stackless.cpp) | [http\_server\_stackless\_ssl.cpp](../../../example/http/server/stackless-ssl/http_server_stackless_ssl.cpp) |
| HTTP, C++ 20 coroutine | [http\_server\_awaitable.cpp](../../../example/http/server/awaitable/http_server_awaitable.cpp) |  |
| HTTP, fast (optimized for speed) | [http\_server\_fast.cpp](../../../example/http/server/fast/http_server_fast.cpp) |  |
| HTTP, small (optimized for space) | [http\_server\_small.cpp](../../../example/http/server/small/http_server_small.cpp) |  |
| HTTP, flex (plain + SSL) |  | [http\_server\_flex.cpp](../../../example/http/server/flex/http_server_flex.cpp) |

These WebSocket servers echo back any message received, keeping the session
open until the client disconnects. All asynchronous servers support timeouts.

| Description | Source File | Source File (using SSL) |
| --- | --- | --- |
| WebSocket, synchronous | [websocket\_server\_sync.cpp](../../../example/websocket/server/sync/websocket_server_sync.cpp) | [websocket\_server\_sync\_ssl.cpp](../../../example/websocket/server/sync-ssl/websocket_server_sync_ssl.cpp) |
| WebSocket, asynchronous | [websocket\_server\_async.cpp](../../../example/websocket/server/async/websocket_server_async.cpp) | [websocket\_server\_async\_ssl.cpp](../../../example/websocket/server/async-ssl/websocket_server_async_ssl.cpp) |
| WebSocket, asynchronous Unix domain sockets | [websocket\_server\_async\_local.cpp](../../../example/websocket/server/async-local/websocket_server_async_local.cpp) |  |
| WebSocket, coroutine | [websocket\_server\_coro.cpp](../../../example/websocket/server/coro/websocket_server_coro.cpp) | [websocket\_server\_coro\_ssl.cpp](../../../example/websocket/server/coro-ssl/websocket_server_coro_ssl.cpp) |
| WebSocket, stackless coroutine | [websocket\_server\_stackless.cpp](../../../example/websocket/server/stackless/websocket_server_stackless.cpp) | [websocket\_server\_stackless\_ssl.cpp](../../../example/websocket/server/stackless-ssl/websocket_server_stackless_ssl.cpp) |
| WebSocket, C++ 20 coroutine | [websocket\_server\_awaitable.cpp](../../../example/websocket/server/awaitable/websocket_server_awaitable.cpp) |  |
| WebSocket, fast (suited for benchmarks) | [websocket\_server\_fast.cpp](../../../example/websocket/server/fast/websocket_server_fast.cpp) |  |

### [Servers (Advanced)](examples.html#beast.examples.servers_advanced "Servers (Advanced)")

These servers offer both HTTP and WebSocket services on the same port, and
illustrate the implementation of advanced features.

| Description | Features | Sources |
| --- | --- | --- |
| Advanced | * Timeouts * Multi-threaded * HTTP pipelining * Parser-oriented HTTP reading * Dual protocols: HTTP and WebSocket * Clean exit via SIGINT (CTRL+C) or SIGTERM (kill) | [advanced\_server.cpp](../../../example/advanced/server/advanced_server.cpp) |
| Advanced, flex (plain + SSL) | * Timeouts * Multi-threaded * HTTP pipelining * Parser-oriented HTTP reading * Dual protocols: HTTP and WebSocket * Flexible ports: plain and SSL on the same port * Clean exit via SIGINT (CTRL+C) or SIGTERM (kill) | [advanced\_server\_flex.cpp](../../../example/advanced/server-flex/advanced_server_flex.cpp) |
| Advanced, flex (plain + SSL) with awaitable | * Timeouts * Multi-threaded * HTTP pipelining * Parser-oriented HTTP reading * Dual protocols: HTTP and WebSocket * Flexible ports: plain and SSL on the same port * Clean exit via SIGINT (CTRL+C) or SIGTERM (kill) * Usage of cancellation\_signals | [advanced\_server\_flex\_awaitable.cpp](../../../example/advanced/server-flex-awaitable/advanced_server_flex_awaitable.cpp) |
| Chat Server, multi-threaded | * Multi-threaded * Broadcasting Messages * Multi-user Chat Server * JavaScript Browser Client * Parser-oriented HTTP reading * Dual protocols: HTTP and WebSocket * Clean exit via SIGINT (CTRL+C) or SIGTERM (kill) | [chat-multi](../../../example/websocket/server/chat-multi) |

### [Chat Server 🎦](examples.html#beast.examples.chat_server "Chat Server 🎦")

This example demonstrates a websocket chat server, allowing multiple users
to connect and participate in live, group messaging. It comes with a tiny
front end implemented in JavaScript and HTML5 which runs in any browser.
The example is accompanied by a one hour presentation which provides a discussion
of networking concepts, followed by in-depth explanation of how the client
and server are constructed. This talk was delivered at [CppCon
2018](https://cppcon.org). The source code in the Beast example contains improvements
to the original program.

**Table 1.1. Chat WebSocket Server and JavaScript Client**

| Component | Features | Sources |
| --- | --- | --- |
| Server | * C++ * Timeouts * Multi-threaded * Broadcast to multiple peers * Dual protocols: HTTP and WebSocket * Clean exit via SIGINT (CTRL+C) or SIGTERM (kill) | [chat-multi](../../../example/websocket/server/chat-multi) |
| Client | * JavaScript / HTML5 * Runs in the browser * Delivered by the server * Only 60 lines total including UI * Completely portable graphics | [chat\_client.html](../../../example/websocket/server/chat-multi/chat_client.html) |