## [Introduction](introduction.html "Introduction")

Beast is a C++ header-only library serving as a foundation for writing interoperable
networking libraries by providing **low-level HTTP/1, WebSocket,
and networking protocol** vocabulary types and algorithms using the
consistent asynchronous model of [Boost.Asio](../../../../../libs/asio/index.html).

This library is designed for:

* **Symmetry:** Algorithms are role-agnostic;
  build clients, servers, or both.
* **Ease of Use:** [Boost.Asio](../../../../../libs/asio/index.html)
  users will immediately understand Beast.
* **Flexibility:** Users make the important
  decisions such as buffer or thread management.
* **Performance:** Build applications handling
  thousands of connections or more.
* **Basis for Further Abstraction.** Components
  are well-suited for building upon.

This library is not a client or server, but it can be used to build those things.
Many examples are provided, including clients and servers, which may be used
as a starting point for writing your own program.

#### [Motivation](introduction.html#beast.introduction.motivation)

Beast empowers users to create their own libraries, clients, and servers using
HTTP/1 and WebSocket. Code will be easier and faster to implement, understand,
and maintain, because Beast takes care of the low-level protocol details. The
HTTP and WebSocket protocols drive most of the World Wide Web. Every web browser
implements these protocols to load webpages and to enable client side programs
(often written in JavaScript) to communicate interactively. C++ benefits greatly
from having a standardized implementation of these protocols.

### [Requirements](introduction.html#beast.introduction.requirements "Requirements")

|  |  |
| --- | --- |
| [Important] | Important |
| This library is for programmers familiar with [Boost.Asio](../../../../../libs/asio/index.html). Users who wish to use asynchronous interfaces should already know how to create concurrent network programs using callbacks or coroutines. |

Beast requires:

* **C++11:** Robust support for most language
  features.
* **Boost:** Beast only works with Boost,
  not stand-alone Asio
* **OpenSSL:** Version 1.0.2 or higher. Required
  to build the tests, examples, and to use TLS/Secure sockets.

Tested with these compilers: msvc-14+, gcc 5.0+, clang 3.6+.

Sources are **header-only**. Adding additional
libraries to the linking step for your programs to use Beast is normally
not necessary, except for these cases:

* When using coroutines created by calling [`boost::asio::spawn`](../../../../../doc/html/boost_asio/reference/spawn.html), you will need to add
  the [Boost.Coroutine](../../../../../libs/coroutine/index.html)
  library to your program.
* When using [`boost::asio::ssl::stream`](../../../../../doc/html/boost_asio/reference/ssl__stream.html), you will need to add
  the [OpenSSL](https://www.openssl.org/) library to
  your program.

Please visit the [Boost documentation](../../../../../more/getting_started.html)
for instructions on how to build and link with Boost libraries for your particular
environment system.

### [Reporting Bugs](introduction.html#beast.introduction.reporting_bugs "Reporting Bugs")

To report bugs or get help using Beast, GitHub issues are preferred. Please
visit <https://github.com/boostorg/beast/issues>
to ask a question, report a defect, or request a feature. If you prefer to
keep your issue or question confidential please email the author at [vinnie.falco@gmail.com](mailto:vinnie.falco%40gmail.com).

### [Credits](introduction.html#beast.introduction.credits "Credits")

Boost.Asio is the inspiration behind which all of the interfaces and implementation
strategies are built. Some parts of the documentation are written to closely
resemble the wording and presentation of Boost.Asio documentation. Credit
goes to [Christopher Kohlhoff](https://github.com/chriskohlhoff)
for his wonderful Asio library and the ideas in [**C++ Extensions for Networking**](http://cplusplus.github.io/networking-ts/draft.pdf) which power
Beast.

Beast would not be possible without the support of [Ripple](https://www.ripple.com)
during the library's early development, or the ideas, time and patience contributed
by [David Schwartz](https://github.com/JoelKatz), [Edward Hennis](https://github.com/ximinez), [Howard
Hinnant](https://github.com/howardhinnant), [Miguel Portilla](https://github.com/miguelportilla),
[Nik Bougalis](https://github.com/nbougalis), [Scott
Determan](https://github.com/seelabs) and [Scott Schurr](https://github.com/scottschurr).
Many thanks to [Agustín Bergé](https://github.com/K-ballo),
[Glen Fernandes](http://www.boost.org/users/people/glen_fernandes.html),
and [Peter Dimov](https://github.com/pdimov) for tirelessly
answering questions on the [C++ Language
Slack Workspace](https://slack.cpp.al/).

Thanks to [Damian Jarek](https://github.com/djarek) for
his generous participation and source code contributions.

Thanks to [Richard Hodges](https://github.com/madmongo1)
(hodges.r@gmail.com) for maintaining Beast on behalf of the [C++
Alliance](https://cppalliance.org).

Many thanks to [Jetbrains s.r.o.](https://www.jetbrains.com)
for generously providing the Beast development team with All Product Developmnent
Licenses.