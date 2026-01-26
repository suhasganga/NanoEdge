## [Design Choices](design_choices.html "Design Choices")

The implementations were originally driven by business needs of cryptocurrency
server applications (e.g. [rippled](https://github.com/ripple/rippled)),
written in C++. These needs were not met by existing solutions so Beast was
written from scratch as a solution. Beast's design philosophy avoids flaws
exhibited by other libraries:

* Don't try to do too much.
* Don't sacrifice performance.
* Mimic [Boost.Asio](../../../../../libs/asio/index.html); familiarity
  breeds confidence.
* Role-symmetric interfaces; client and server the same (or close to it).
* Leave important decisions, such as allocating memory or managing flow control,
  to the user.

Beast uses the [*DynamicBuffer*](concepts/DynamicBuffer.html "DynamicBuffer")
concept presented in the [Networking
TS](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2018/n4771.pdf), and relies heavily on the [*ConstBufferSequence*](../../../../../doc/html/boost_asio/reference/ConstBufferSequence.html)
and [*MutableBufferSequence*](../../../../../doc/html/boost_asio/reference/MutableBufferSequence.html)
concepts for passing buffers to functions. The authors have found the dynamic
buffer and buffer sequence interfaces to be optimal for interacting with Asio,
and for other tasks such as incremental parsing of data in buffers (for example,
parsing websocket frames stored in a [`static_buffer`](ref/boost__beast__static_buffer.html "static_buffer")).

During the development of Beast the authors have studied other software packages
and in particular the comments left during the Boost Review process of other
packages offering similar functionality. In this section and the FAQs that
follow we attempt to answer those questions that are also applicable to Beast.

For HTTP we model the message to maximize flexibility of implementation strategies
while allowing familiar verbs such as **`read`**
and **`write`**.
The HTTP interface is further driven by the needs of the WebSocket module,
as a WebSocket session requires a HTTP Upgrade handshake exchange at the start.
Other design goals:

* Keep it simple.
* Stay low level; don't invent a whole web server or client.
* Allow for customizations, if the user needs it.

The following video presentation was delivered at [CppCon](https://cppcon.org/)
in 2016. It provides a light introduction to some of the earliest interfaces
of Beast (which have since changed).