## [Release Notes](release_notes.html "Release Notes")

#### [Boost 1.90](release_notes.html#beast.release_notes.boost_1_90)

**API Changes**

* [#3042](https://github.com/boostorg/beast/issues/3042) `http::parser` rejects non-standard trailer fields
  by default. *Actions Required*:

  + If your code relies on a non-standard trailer field, consider setting
    [`http::parser::merge_all_trailers`](ref/boost__beast__http__parser/merge_all_trailers/overload2.html "http::parser::merge_all_trailers (2 of 2 overloads)") after
    you have validated the `Trailer`
    header field in the header section of the message.
* [#3042](https://github.com/boostorg/beast/issues/3042) `http::basic_parser` uses a dedicated callback
  for trailer fields. *Actions Required*:

  + Custom parsers derived from `http::basic_parser`
    must override the new virtual function [`http::basic_parser::on_trailer_field_impl`](ref/boost__beast__http__basic_parser/on_trailer_field_impl.html "http::basic_parser::on_trailer_field_impl") which
    is invoked for each field received while parsing the trailer section
    of a chunked HTTP message.
* [#3042](https://github.com/boostorg/beast/issues/3042) `http::field` constants are updated. *Actions
  Required*:

  + Most removed constants were unrelated to the HTTP protocol. If your
    code used one of them, please use the corresponding string literal
    value.

**Fixes**

* [#3034](https://github.com/boostorg/beast/issues/3034) Fixed allocator move/copy assignment in `flat_buffer`
  and `multi_buffer`
* [#3028](https://github.com/boostorg/beast/issues/3028) Fixed websocket permessage-deflate error on partial message consumption
* [#3032](https://github.com/boostorg/beast/issues/3032) `http::buffer_body` ignores empty chunks

**Improvements**

* [#3039](https://github.com/boostorg/beast/issues/3039) Added `http::basic_fields::contains` member function
* [#3050](https://github.com/boostorg/beast/issues/3050) Removed dependency on Boost.Preprocessor
* [#3048](https://github.com/boostorg/beast/issues/3048) Removed dependency on Boost.StaticAssert

#### [Boost 1.89](release_notes.html#beast.release_notes.boost_1_89)

**Fixes**

* [#3002](https://github.com/boostorg/beast/issues/3002) Conditionally defined `immediate_executor_type`
  in `async_base`
* [#2999](https://github.com/boostorg/beast/issues/2999) Used `handshake_timeout`
  for closing handshake during read operations
* [#3003](https://github.com/boostorg/beast/issues/3003) Added missing `cstdint`
  header to `detail/cpu_info.hpp`
* [#3016](https://github.com/boostorg/beast/issues/3016) Fixed `std::is_trivial` deprecation warnings
* [#3019](https://github.com/boostorg/beast/issues/3019) Fixed `-Wmaybe-uninitialized`
  warnings

**Improvements**

* [#3005](https://github.com/boostorg/beast/issues/3005) Replaced `detail/work_guard.hpp`
  with `net::executor_work_guard`
* [#3016](https://github.com/boostorg/beast/issues/3016) Fixed portability issues for building tests in MinGW

**Documentation**

* [#3009](https://github.com/boostorg/beast/issues/3009) Removed moved sections from documentation
* [#3009](https://github.com/boostorg/beast/issues/3009) Removed superfluous log messages from tests

#### [Boost 1.88](release_notes.html#beast.release_notes.boost_1_88)

**Fixes**

* [#2962](https://github.com/boostorg/beast/issues/2962) Fixed out-of-bounds access in `iequals`
  function

**Improvements**

* [#2974](https://github.com/boostorg/beast/issues/2974) Updated SSL examples to verify peer certificate hostname
* [#2954](https://github.com/boostorg/beast/issues/2954) Refactored CMakeLists
* [#2955](https://github.com/boostorg/beast/issues/2955) Removed Boost.Scope dependency from examples
* [#2716](https://github.com/boostorg/beast/issues/2716) WebSockets: Peer pings are counted as activity for `idle_timeout`

**Documentation**

* [#2918](https://github.com/boostorg/beast/issues/2918) Added new examples for Unix domain sockets
* [#2910](https://github.com/boostorg/beast/issues/2910) Added SSL/TLS Certificate section to documentation
* [#2730](https://github.com/boostorg/beast/issues/2730) Improved documentation of `websocket::stream::async_close`

#### [Boost 1.87](release_notes.html#beast.release_notes.boost_1_87)

**API Changes**

* [#2920](https://github.com/boostorg/beast/issues/2920) Added `error_code`
  overload for `basic_fields::insert()`
* [#2911](https://github.com/boostorg/beast/issues/2911) Added overload for `websocket::stream::get_status`
  to query permessage-deflate status

**Fixes**

* [#2926](https://github.com/boostorg/beast/issues/2926) Fixed use-after-move in calls to `net::dispatch`
  within `http::basic_stream`, which caused `bad_executor` exceptions on timeouts
* [#2915](https://github.com/boostorg/beast/issues/2915) Removed mutating operations in initiating functions
* [#2915](https://github.com/boostorg/beast/issues/2915) Fixed cancellation handling in `teardown_tcp_op`
* [#2920](https://github.com/boostorg/beast/issues/2920) Set `state_` in
  `basic_parser` before calling
  `on_finish_impl`
* [#2939](https://github.com/boostorg/beast/issues/2939) Removed static specifier from `clamp`
  functions
* [#2903](https://github.com/boostorg/beast/issues/2903) Addressed `-Wattributes`
  warnings in tests
* [#2944](https://github.com/boostorg/beast/issues/2944) Addressed unreachable code warning in tests

**Improvements**

* [#2940](https://github.com/boostorg/beast/issues/2940) Added forward declaration headers for types in `beast::http`
  namespace
* [#2920](https://github.com/boostorg/beast/issues/2920) Enabled `http::parser` to use `basic_fields::insert()` with `error_code`
  overload
* [#2920](https://github.com/boostorg/beast/issues/2920) Applied `header_limit_`
  in `http::basic_parser` to trailer headers
* [#2920](https://github.com/boostorg/beast/issues/2920) Improved `http::basic_parser` to return `http::error::header_limit` earlier
* [#2905](https://github.com/boostorg/beast/issues/2905) Added support for modular boost build structure

#### [Boost 1.86](release_notes.html#beast.release_notes.boost_1_86)

**API Changes**

* [#2878](https://github.com/boostorg/beast/issues/2878) Added HTTP status code **418 I'm a teapot**

**Fixes**

* [#2879](https://github.com/boostorg/beast/issues/2879) Narrowing conversion in `read_size_hint_db()`
* [#2893](https://github.com/boostorg/beast/issues/2893) Overloads that are ambiguous when using default completion tokens
* [#2517](https://github.com/boostorg/beast/issues/2517) Misplaced static\_assert in `http::basic_fields`
  move-assignment operator
* [#2880](https://github.com/boostorg/beast/issues/2880) Underflow of `bytes_transferred`
  in WebSocket partial write operations
* [#2879](https://github.com/boostorg/beast/issues/2879) `websocket::stream::read_size_hint()`
  does not exceed `read_message_max`
* [#2877](https://github.com/boostorg/beast/issues/2877) Various warnings in tests
* [#2872](https://github.com/boostorg/beast/issues/2872) Error handling in SSL shutdown operations in examples
* [#2869](https://github.com/boostorg/beast/issues/2869) Annotate fallthrough case in zlib
* [#2866](https://github.com/boostorg/beast/issues/2866) Handling of expired timers in `basic_stream::ops::transfer_op`
* [#2864](https://github.com/boostorg/beast/issues/2864) Ambiguity in `test::basic_stream`
  constructor overloads
* [#2861](https://github.com/boostorg/beast/issues/2861) Partial parsing of the final chunk in `http::parser`

**Improvements**

* [#2897](https://github.com/boostorg/beast/issues/2897) Graceful shutdown in `server_flex_awaitable`
  example
* [#2897](https://github.com/boostorg/beast/issues/2897) Simplified awaitable examples
* [#2888](https://github.com/boostorg/beast/issues/2888) Added fuzzing targets
* [#2875](https://github.com/boostorg/beast/issues/2875) Removed superfluous uses of `std::bind`
  in some examples
* [#2875](https://github.com/boostorg/beast/issues/2875) `ssl_stream` does
  not use `flat_stream`

**Documentation**

* [#2875](https://github.com/boostorg/beast/issues/2875) `ssl_stream` and
  `flat_stream` marked as deprecated
* [#2875](https://github.com/boostorg/beast/issues/2875) `net::ssl::stream` is canonical in snippets and examples
* [#2872](https://github.com/boostorg/beast/issues/2872) Added `SSL/TLS Shutdown
  Procedure` section

#### [Boost 1.85](release_notes.html#beast.release_notes.boost_1_85)

**API Changes**

* [#2811](https://github.com/boostorg/beast/issues/2811) The status code list has been updated to conform with the IANA
  registry

**Fixes**

* [#2803](https://github.com/boostorg/beast/issues/2803) Unreachable code warning in `buffers_cat.hpp`
* [#2778](https://github.com/boostorg/beast/issues/2778) Connection error handling in `websocker_server_awaitable`
  example
* [#2739](https://github.com/boostorg/beast/issues/2739) Concurrent calls to `async_write`
  in advanced server examples
* [#2810](https://github.com/boostorg/beast/issues/2810) zlib name conflicts with minizip
* [#2818](https://github.com/boostorg/beast/issues/2818) host string should be updated after `SSL_set_tlsext_host_name()`

**Improvements**

* [#2782](https://github.com/boostorg/beast/issues/2782) `asio::associator` is specialized for `bind_wrapper` and `bind_front_wrapper`
* [#2646](https://github.com/boostorg/beast/issues/2646) Add non-allocating overload for error category message function

**Documentation**

* [#2789](https://github.com/boostorg/beast/issues/2789) Specifies when calling `http::message::prepare_payload()` is optional
* [#2799](https://github.com/boostorg/beast/issues/2799) Operations affected by `basic_stream::expires_after()`
* [#2808](https://github.com/boostorg/beast/issues/2808) `teardown()`
  and `async_teardown()`
  are customization points
* [#2814](https://github.com/boostorg/beast/issues/2814) Moving or copying `http::serializer`
  after first usage is undefined behaviour
* [#2817](https://github.com/boostorg/beast/issues/2817) `websocket::permessage_deflate` should be configured
  before performing the WebSocket handshake
* [#2816](https://github.com/boostorg/beast/issues/2816) `bytes_transferred`
  in http reads operations reports the number of bytes consumed by the HTTP
  parser

#### [Boost 1.84](release_notes.html#beast.release_notes.boost_1_84)

**API Changes**

* Remove deprecated allocation and invocation hooks

**Features**

* Support for `immediate_executor`

**Fixes**

* [#2766](https://github.com/boostorg/beast/issues/2766) Use the explicit type std::size\_t when completing transfer\_op
* [#2727](https://github.com/boostorg/beast/issues/2727) Replaced `BOOST_ASIO_INITFN_RESULT_TYPE`
  with `BOOST_ASIO_INITFN_AUTO_RES`
* [#2715](https://github.com/boostorg/beast/issues/2715) `server-flex-awaitable` example resets parser

**Documentation**

* [#2713](https://github.com/boostorg/beast/issues/2713) Corrected the `websocket::stream::async_ping/pong`
  handler requirement
* [#2755](https://github.com/boostorg/beast/issues/2755) Update documentation for `websocket::stream::async_write_some`

#### [Boost 1.83](release_notes.html#beast.release_notes.boost_1_83)

**Fixes**

* [#2680](https://github.com/boostorg/beast/issues/2680) aligned\_storage unused for C+23
* [#2653](https://github.com/boostorg/beast/issues/2653) MSVC literal `not` error
* [#2661](https://github.com/boostorg/beast/issues/2661) ssl\_stream ambiguity error on clang
* [#2649](https://github.com/boostorg/beast/issues/2649) Jamefile uses openssl.jam

#### [Boost 1.82](release_notes.html#beast.release_notes.boost_1_82)

**Features**

* [#2475](https://github.com/boostorg/beast/issues/2475) Add `error_code`s
  use source\_location

**Fixes**

* [#2602](https://github.com/boostorg/beast/issues/2602) tcp\_stream uses the correct executor of the timer.
* [#2638](https://github.com/boostorg/beast/issues/2638) `std::placeholders` ambiguity fix.

**Improvements**

* error\_categories use numeric ids
* `file_body` support seek

#### [Boost 1.81](release_notes.html#beast.release_notes.boost_1_81)

**Features**

* Add `buffers_generator`
* Add [`http::message_generator`](ref/boost__beast__http__message_generator.html "http::message_generator")
* Add [`buffer_ref`](ref/boost__beast__buffer_ref.html "buffer_ref")
* Support for per-operation cancellation

**Fixes**

* [#2439](https://github.com/boostorg/beast/issues/2439) Fix CVE-2018-25032 in zlib streams
* [#264](https://github.com/boostorg/beast/issues/264) Websocket support continue in upgrade
* [#471](https://github.com/boostorg/beast/issues/471) Unquote takes s by reference

**Improvements**

* [#2104](https://github.com/boostorg/beast/issues/2104) C++20 awaitable examples.
* [#226](https://github.com/boostorg/beast/issues/226), [#227](https://github.com/boostorg/beast/issues/227) per-message compression options
* [#2449](https://github.com/boostorg/beast/issues/2449) websocket timeout option api
* [#2468](https://github.com/boostorg/beast/issues/2468) multiple content length error

**Miscellaneous**

* Use `span` from Boost.Core
* Use `static_string` from
  Boost.StaticString
* `serializer::is_done` is `const`
* Support for default-completion and rebind
* [#2469](https://github.com/boostorg/beast/issues/2469) s390x architecture support

**Documentation**

* [#891](https://github.com/boostorg/beast/issues/891) Feature table for buffers
* [#516](https://github.com/boostorg/beast/issues/516) Case-insensitivity for fields is stated
* [#298](https://github.com/boostorg/beast/issues/298) api version is documented

#### [Boost 1.80](release_notes.html#beast.release_notes.boost_1_80)

**Miscellaneous**

* [#2363](https://github.com/boostorg/beast/issues/2363) Remove `BOOST_BEAST_USE_STD_STRING_VIEW`
* [#2417](https://github.com/boostorg/beast/issues/2417) use boost::core::string\_view. This improves inter-conversion between
  string\_view implementations. Some observable differences for users:

  + `core::string_view` no longer supports
    the `.to_string()` or `.clear()`
    extensions from Utility
  + code that relied on `.max_size()`
    returning `.size(),` needs to be fixed to use `.size()` instead
  + `remove_suffix()`
    and `remove_prefix()` were more lenient than the standard
    specs; be sure you don't rely on it clamping the argument to valid
    range
  + `BOOST_NO_CXX11_EXPLICIT_CONVERSION_OPERATORS`
    no longer suppresses conversions to `std::string`

#### [Boost 1.79](release_notes.html#beast.release_notes.boost_1_79)

**Fixes**

* [#2391](https://github.com/boostorg/beast/issues/2391) Add missing include for file\_body test.
* [#2364](https://github.com/boostorg/beast/issues/2364) Fix WebSocket handshake response on failure.
* [#2280](https://github.com/boostorg/beast/issues/2280) (related) Fix open append mode for file\_posix.
* [#2280](https://github.com/boostorg/beast/issues/2280) Fix open append mode for file\_win32.
* [#2280](https://github.com/boostorg/beast/issues/2280) Fix file open with append/append\_existing flag on Windows
* [#2354](https://github.com/boostorg/beast/issues/2354) Fix clang-cl UTF8 path handling for `file_win32`.
* [#2354](https://github.com/boostorg/beast/issues/2354) Fix clang-cl UTF8 path handling for `file_stdio`.

**Miscellaneous**

* [#2375](https://github.com/boostorg/beast/issues/2375) Add ARM64 builds to drone CI
* [#2217](https://github.com/boostorg/beast/issues/2217) Fix async\_base documentation link
* [#2280](https://github.com/boostorg/beast/issues/2280) Add tests for file open in append/append\_existing mode
* [#2351](https://github.com/boostorg/beast/issues/2351) Update CI to include gcc 11, clang 12, msvc 14.3
* [#2350](https://github.com/boostorg/beast/issues/2350) Add individual tests to CMake workflow

#### [Boost 1.78](release_notes.html#beast.release_notes.boost_1_78)

**Fixes**

* Fix CVE-2016-9840 in zlib implementation.
* Fix TLS SNI handling in websocket\_client\_async\_ssl example.
* [#2313](https://github.com/boostorg/beast/issues/2313) Fix reuse of sliding window in WebSocket permessage\_deflate.
* Fix accept error handling in http\_server\_async example.

**Miscellaneous**

* Remove test framework's dependency on RTTI.
* Move library-specific docca configuration to Beast.
* Remove dependency on RTTI in `test::stream`.
* Fix missing includes in test headers.

#### [Boost 1.77](release_notes.html#beast.release_notes.boost_1_77)

**Fixes**

* [#2233](https://github.com/boostorg/beast/issues/2233) Remove use of POSIX-only constant.

**Miscellaneous**

* Fixes to tests.
* Improvements and fixes in Github and Drone CI.
* Accommodate Docca updates.
* Update example root certificates.
* Add example of reading large response body.
* Remove Travis CI.
* Update CMakeLists.txt

#### [Boost 1.76](release_notes.html#beast.release_notes.boost_1_76)

**Fixes**

* [#2139](https://github.com/boostorg/beast/issues/2139) Add executor rebind to test::stream.
* Fix unused variable compiler warning in WebSocket async shutdown.

**Improvements**

* [#2124](https://github.com/boostorg/beast/issues/2124) Floating point support no longer required to use Beast.
* Reduce size of websockety compiled code by using a common buffers type
  for all operations.
* HTTP Parser has improved detection of incorrect use.

**Miscellaneous**

* [#2140](https://github.com/boostorg/beast/issues/2140) Add cxxstd tag to library metadata.
* Move to Drone CI.
* Minor documentation formatting improvements.
* CML now finds required Boost::thread library during in-tree build.

#### [Boost 1.75](release_notes.html#beast.release_notes.boost_1_75)

**Fixes**

* Eliminate spurious unused parameter warning in `detect_ssl`.
* Update Websocket examples to set the SNI for TLS connections.
* [#2023](https://github.com/boostorg/beast/issues/2023) websocket async\_shutdown will now shutdown the underlying TLS transport.
* [#2011](https://github.com/boostorg/beast/issues/2011) File open with append\_existing flag now works correctly in posix
  environments.
* [#2039](https://github.com/boostorg/beast/issues/2039) Windows builds now link to bcrypt as required by the filesystem
  library.
* [#2063](https://github.com/boostorg/beast/issues/2063) Logic error fixed in `advanced_server_flex`
  example.
* [#1582](https://github.com/boostorg/beast/issues/1582) Fix unreachable code error on MSVC.
* [#2070](https://github.com/boostorg/beast/issues/2070) Fix http body behaviour when body\_limit it none.
* [#2065](https://github.com/boostorg/beast/issues/2065) Fix behaviour of `basic_stream`
  when a zero-length write is requested.
* [#2080](https://github.com/boostorg/beast/issues/2080) Add enums representing Sec-\* HTTP headers.
* [#2085](https://github.com/boostorg/beast/issues/2085) Fix `nullptr` implicit
  cast on `fields::set()`.
* [#2029](https://github.com/boostorg/beast/issues/2029) Fix C++20 tests for `basic_stream`.

**Miscellaneous**

* Add handler tracking to asynchronous operations:

  + Define the preprocessor macro `BOOST_ASIO_ENABLE_HANDLER_TRACKING`
    to enable Asio handler tracking in Boost.Beast asynchronous operations.
    Please see [asio
    handler tracking](../../../../../doc/html/boost_asio/overview/core/handler_tracking.html) for details.
* Add Bishop-Fox 2020 Security Assessment.

#### [Boost 1.74](release_notes.html#beast.release_notes.boost_1_74)

**API Changes**

* The API to Asio has undergone changes. Please refer to the Asio release
  notes for details.
* Beast has been updated to track and respect developer choices in the use
  of Asio. In particular:

  + Define `BOOST_ASIO_NO_DEPRECATED`
    to disallow deprecated invocation hooks.
  + Define `BOOST_ASIO_NO_TS_EXECUTORS`
    to ensure that executors conform to the [Standard
    Executors](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2019/p0443r11.html) proposal.
  + Define `BOOST_ASIO_USE_TS_EXECUTOR_AS_DEFAULT`
    to select [Networking
    TS](https://cplusplus.github.io/networking-ts/draft.pdf) style executors by default. If this macro is not defined,
    Asio default executors will be the [Standard
    Executors](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2019/p0443r11.html) implementation.
* [#1897](https://github.com/boostorg/beast/issues/1897) Parser `body_limit`
  is optional (API Change) *Actions Required*

  + The signature of `basic_parser<>::body_limit(n)` has changed. It now accepts an optional
    `std::uint64_t`. The caller may indicate
    that no body limit is required by calling `body_limit(boost::none)`. The default limits remain in place
    in order to maintain 'safe by default' behaviour.
* [#1934](https://github.com/boostorg/beast/issues/1934) Remove deprecated interfaces (API Change) *Actions Required*

  + The macro `BOOST_BEAST_NO_DEPRECATED`
    will no longer be noticed by Beast. The only way to enable deprecated
    functionality is now the macro `BOOST_BEAST_ALLOW_DEPRECATED`
    which is undefined by default. That is, all deprecated behaviour
    is disabled by default.
  + The following deprecated functions have been removed:

    - `websocket::async_accept_ex`
    - `websocket::async_handshake_ex`
    - `websocket::accept_ex`
    - `websocket::handshake_ex` Programs still
      using these names should be refactored to use the `decorator` feature and the
      remaining handshake and accept functions.
  + `websocket::role_type` has been removed. Users
    should use `beast::role_type`
    instead.
  + `handler_ptr` has been
    removed. Users should use `net::bind_handler`
    and/or `bind_front_handler`
    instead.
  + Code that depends on `mutable_data_type`
    should be refactored to use `mutable_buffers_type`.
    Classes affected are:

    - `buffers_adaptor`
    - `flat_buffer`
    - `flat_static_buffer`
    - `multi_buffer`
    - `static_buffer`
  + The `reset` function
    has been removed from `flat_static_buffer`.
    Use the `clear` function
    instead.
  + The `core/type_traits.hpp` public header has been removed
    and along with it the type trait `is_completion_handler`.
    Beast uses the CompletionHandler correctness checks provided by Asio.
    In a c++20 environment, these convert to concept checks.
  + The error code enum `invalid_code_lenths`
    (sic) was a synonym of `invalid_code_lengths`.
    Affected programs should be modified to use `invalid_code_lengths`.
  + The file `core/buffers_adapter.hpp` has been removed along with
    the deprecated alias typename `buffers_adapter`.
    Affected programs should use  `core/buffers_adapator.hpp`
    and the type `buffers_adaptor`.
* [#1956](https://github.com/boostorg/beast/issues/1956) Deprecate `string_param`
  (API Change) *Actions Required* `string_param`,
  which was previously the argument type when setting field values has been
  replaced by `string_view`.
  Because of this, it is no longer possible to set message field values directly
  as integrals. Users are requied to convert numeric arguments to a string
  type prior to calling `fields::set`
  et. al. Beast provides the non-allocating `to_static_string()` function for this purpose. To set Content-Length
  field manually, call `message::content_length`.

**Fixes**

* [#1913](https://github.com/boostorg/beast/issues/1913) Fix standalone compilation error with `std::string_view`
* [#1925](https://github.com/boostorg/beast/issues/1925) [#1916](https://github.com/boostorg/beast/issues/1916) Fix compile errors on Visual Studio with /std:c++latest
* [#1924](https://github.com/boostorg/beast/issues/1924) Fix c++20 deprecation warning in `span_body`
* [#1920](https://github.com/boostorg/beast/issues/1920) Fix use `buffered_read_stream`
  with `use_awaitable`
* [#1918](https://github.com/boostorg/beast/issues/1918) Fix `async_detect_ssl`
  with `use_awaitable`
* [#1944](https://github.com/boostorg/beast/issues/1944) Fix `FILE` namespace
  qualification
* [#1942](https://github.com/boostorg/beast/issues/1942) Fix http read `bytes_transferred`
* [#1943](https://github.com/boostorg/beast/issues/1943) Fix `basic_stream`
  `expires_after`
* [#1980](https://github.com/boostorg/beast/issues/1980) Fix `max` compile
  error
* [#1949](https://github.com/boostorg/beast/issues/1949) `iless` and `iequal` take part in Heterogeneous Lookup

**Miscellaneous**

* [#1907](https://github.com/boostorg/beast/issues/1907) OpenSSL 1.0.2 or later is required when using SSL/TLS streams.
  This is a requirement inherited from Boost.Asio.
* Additional tests have been added to ensure correct integration with C++20
  coroutines when avaialable.

#### [Boost 1.73](release_notes.html#beast.release_notes.boost_1_73)

**API Changes**

* Nested `mutable_data_type`
  in Beast dynamic buffers is deprecated. Affected types:

  + `buffers_adaptor`
  + `flat_buffer`
  + `flat_static_buffer`
  + `multi_buffer`
  + `static_buffer`

**Changes Required**

* Use nested `mutable_buffers_type`
  instead of `mutable_data_type`,
  or define `BOOST_BEAST_ALLOW_DEPRECATED`

**Miscellaneous**

* Update root certificates in examples

**Fixes**

* [#1880](https://github.com/boostorg/beast/issues/1880) Fix Content-Length parsing
* [#1852](https://github.com/boostorg/beast/issues/1852) Fix examples to dispatch to strand
* [#1875](https://github.com/boostorg/beast/issues/1875) Ensure `basic_stream::close`
  will not throw
* [#1863](https://github.com/boostorg/beast/issues/1863) Field digest is endian-independent
* [#1853](https://github.com/boostorg/beast/issues/1853) Fix ostream flush
* [#1831](https://github.com/boostorg/beast/issues/1831) `flat_buffer::shrink_to_fit` is `noexcept`
* [#1828](https://github.com/boostorg/beast/issues/1828) Fix erase field
* [#1822](https://github.com/boostorg/beast/issues/1822) Examples use strands correctly
* [#1818](https://github.com/boostorg/beast/issues/1818) `file_body` returns
  `short_read` on eof during
  read
* [#1786](https://github.com/boostorg/beast/issues/1786) Fix bug in win32 `file_body`
* [#1260](https://github.com/boostorg/beast/issues/1260) Add accessor function to File member of `basic_file_body`
* [#793](https://github.com/boostorg/beast/issues/793) `file_win32` supports
  UTF-8 paths
* [#793](https://github.com/boostorg/beast/issues/793) `file_stdio` supports
  unicode paths
* [#1786](https://github.com/boostorg/beast/issues/1786) `file_win32` bodies
  respect `http::serializer::split`
* Correct `buffer_bytes` documentation
* Fix missing include in sha1.hpp
* Fix ostream warning
* Update broken links in README
* Translate some win32 errors to net error codes
* Moved-from dynamic buffers do not clear if different allocator
* Fix compilation macro documentation
* Clarify end-of-file behaviour in `File::read`
  docs
* ostream\_buffer satisfies preconditions of DynamicBuffer\_v1::commit
* Fix release build of docs
* Fix `echo-op` test
* Fix non-msvc cmake

#### [Boost 1.72](release_notes.html#beast.release_notes.boost_1_72)

**Examples**

* Add async-ssl-system-executor http client example
* Add async-ssl-system-executor websocket client example

**Features**

* Async init-fns use the executor's default token
* Use automatically deduced return types for all async operations (since
  C++14)
* Support Concepts for completion token params

**Fixes**

* [#1664](https://github.com/boostorg/beast/issues/1664) Add default dtors to satisfy -Wnon-virtual-dtor
* [#1682](https://github.com/boostorg/beast/issues/1682) Multiple I/O of the same type is not supported
* [#1687](https://github.com/boostorg/beast/issues/1687) Fix signed/unsigned mismatch in file\_stdio::seek
* [#1688](https://github.com/boostorg/beast/issues/1688) basic\_stream dtor cannot throw
* [#1734](https://github.com/boostorg/beast/issues/1734) Fix leftovers in basic\_parser corner case:
* [#1751](https://github.com/boostorg/beast/issues/1751) https\_get example sends the Host header
* [#1754](https://github.com/boostorg/beast/issues/1754) Fix async\_close error code when async\_read times out
* [#1782](https://github.com/boostorg/beast/issues/1782) root\_certificates.hpp is not for production
* Fix data race in websocket examples
* Fix data race in http server examples
* Squelch spurious websocket timer assert
* Use the executor type in basic\_stream timer

#### [Boost 1.71](release_notes.html#beast.release_notes.boost_1_71)

**Improvements**

* [#1280](https://github.com/boostorg/beast/issues/1280) Add 1-element specialization for `buffers_cat`
* [#1556](https://github.com/boostorg/beast/issues/1556) Set parser status and flags even if body limit has been reached
* [#1567](https://github.com/boostorg/beast/issues/1567) Relax requirements for vector\_body
* [#1568](https://github.com/boostorg/beast/issues/1568) `detect_ssl` uses
  `bool` instead of `tribool`
* [#1574](https://github.com/boostorg/beast/issues/1574) Replace `static_string`
  in HTTP parser
* [#1606](https://github.com/boostorg/beast/issues/1606) Use `steady_timer`
  type
* [#1611](https://github.com/boostorg/beast/issues/1611) Make chat websocket javascript client more user friendly
* [#1613](https://github.com/boostorg/beast/issues/1613) Remove redundant use of `static_string`
* [#1636](https://github.com/boostorg/beast/issues/1636) Improve performance of `http::string_to_verb`
* Preserve `operation_aborted`
  on partial message
* Remove unused `<experimental/unit_test/thread.hpp>`
* Reduce the number of instantiations of `filter_token_list`
* Add idle ping suspend test
* Remove the use of `bind_executor`
  in `basic_stream`
* Remove redundant template in service\_base
* Remove the use of `static_string`
  from `http::fields`
* Enable split compilation in http::basic\_fields
* Remove redundant instation of `static_string`
  in websocket
* Remove redundant use of `asio::coroutine`
  in `flat_stream`
* More split compilation in rfc7230.hpp
* More split compilation in websocket/detail/mask.hpp
* Simplify generation of sec-websocket-key

**Fixes**

* [#1332](https://github.com/boostorg/beast/issues/1332) `allocator_traits::construct`
  is used for user-defined types
* [#1559](https://github.com/boostorg/beast/issues/1559) Member `get_executor`
  const-correctness
* [#1569](https://github.com/boostorg/beast/issues/1569) Fix `async_detect_ssl`
  handler type
* [#1570](https://github.com/boostorg/beast/issues/1570) Launder pointers
* [#1578](https://github.com/boostorg/beast/issues/1578) Fix min/max on MSVC
* [#1586](https://github.com/boostorg/beast/issues/1586) Fix uninitalized memory use in deflate\_stream
* [#1593](https://github.com/boostorg/beast/issues/1593) Fix UB in websocket close tests
* [#1594](https://github.com/boostorg/beast/issues/1594) Fix data race in test stream
* [#1599](https://github.com/boostorg/beast/issues/1599) Fix moved-from executor in idle ping timeout
* [#1607](https://github.com/boostorg/beast/issues/1607) Remove uses of the deprecated `buffers`
  function
* [#1612](https://github.com/boostorg/beast/issues/1612) Remove uses of deprecated methods in websocket tests
* [#1620](https://github.com/boostorg/beast/issues/1620) Clean up typo in chat websocket javascript client
* [#1621](https://github.com/boostorg/beast/issues/1621) Fix `flat_buffer`
  copy members
* Silence gcc-8 warning
* Fix `buffers_cat` iterator
  tests
* Don't pessimize-move
* Qualify calls to `beast::iequals`
  in basic\_parser.ipp
* Fix UB in websocket read tests
* Simplify websocket::detail::prng
* Don't over-allocate in http::basic\_fields

**Documentation**

* Documentation is built with SaxonHE instead of xsltproc

#### [Boost 1.70](release_notes.html#beast.release_notes.boost_1_70)

|  |  |
| --- | --- |
| [Tip] | Tip |
| The namespace alias `net` is used throughout for `boost::asio`. |

**New Features**

* All composed operations use the new [`net::async_initiate`](../../../../../doc/html/boost_asio/reference/async_initiate.html) internally.
* New `tcp_stream` and `basic_stream` support:

  + Timeouts, [`async_read_some`](ref/boost__beast__basic_stream/async_read_some.html "basic_stream::async_read_some"), [`async_write_some`](ref/boost__beast__basic_stream/async_write_some.html "basic_stream::async_write_some") complete
    with [`error::timeout`](ref/boost__beast__error.html "error") on expiration.
  + Traffic-shaping policies [`simple`](ref/boost__beast__simple_rate_policy.html "simple_rate_policy") and [`unlimited`](ref/boost__beast__unlimited_rate_policy.html "unlimited_rate_policy"), or a user-defined
    [*RatePolicy*](concepts/RatePolicy.html "RatePolicy").
  + Supports [P1322R0](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2018/p1322r0.html).
* `websocket::stream` supports

  + Configurable handshake timeout
  + Configurable idle timeout
  + Automatic idle pings
* [`ssl_stream`](ref/boost__beast__ssl_stream.html "ssl_stream")
  is a public interface
* ( [#1305](https://github.com/boostorg/beast/issues/1305)) Better `flat_buffer`,
  `flat_static_buffer`, `multi_buffer`, and `static_buffer`:

  + Revise all reference documentation
  + Move construction does not always invalidate buffers
  + non-const `data()`
    returns a mutable buffer sequence
  + Add `cdata()`
    to also return constant readable bytes
  + Eligible member functions are declared `noexcept`
* ( [#1345](https://github.com/boostorg/beast/issues/1345)) Better `flat_buffer`,
  `multi_buffer`

  + Add `clear`, `reserve()`,
    `max_size()`,
    `shrink_to_fit()`
  + Respect Allocator `max_size()`
  + Specify exception safety
* ( [#1384](https://github.com/boostorg/beast/issues/1384)) New functions `bind_front_handler`
* Better `static_buffer`,
  `flat_static_buffer`

  + Add `clear()`
  + More members are `noexcept`
  + Specify exception safety
* Faster `http::string_to_field`
* Dynamic buffer `clear` operations
  perserve capacity.
* New file <boost/beast/core/buffer\_traits.hpp>

  + New variadic `is_const_buffer_sequence`
  + New variadic `is_mutable_buffer_sequence`
  + New trait `buffers_iterator_type`
  + New trait `buffers_type`
* New classes `async_base`,
  `stable_async_base`

  + Handle boilerplate for writing composed operations
  + New `allocate_stable`
    is preferred over `handler_ptr`
* New `buffer_bytes` replacement
  for `net::buffer_size`
* New:

  + `saved_handler`
  + `buffers_range_ref`
  + `executor_type`
  + `get_lowest_layer`,
    `lowest_layer_type`
  + `close_socket`, `beast_close_socket`
  + `error`, `condition`
* These interfaces are now public (were experimental): [`flat_stream`](ref/boost__beast__flat_stream.html "flat_stream"), [`detect_ssl`](ref/boost__beast__detect_ssl.html "detect_ssl"), [`async_detect_ssl`](ref/boost__beast__async_detect_ssl.html "async_detect_ssl").
* Websocket streams use PCG as the fast random number generator, for increased
  security.

**Documentation**

* WebSocket reference documentation is revised
* Updated [Networking Refresher](using_io/asio_refresher.html "Refresher")
* Revised [Asynchronous
  Echo](using_io/writing_composed_operations/echo.html "Echo 💡")
* Rewritten [**Detect SSL Handshake**](using_io/writing_composed_operations/detect_ssl.html "Detect SSL 💡")

**API Changes**

* The [*Fields*](concepts/Fields.html "Fields")
  concept is deprecated and will be removed in a future version. *Actions
  Required*: Do not rely on the *Fields* concept.
* `handler_ptr` is deprecated.
  *Actions Required*: Use `stable_async_base`
  and `allocate_stable` instead.
* On Windows, Visual Studio 2017 or later is required
* OpenSSL is required to build the examples and tests
* HTTP stream algorithms return the number of bytes transferred from the
  stream. Previously, they returned the number of bytes consumed by the parser.
  *Actions Required*:

  + Callers depending on the return value of `http::read`
    or `http::async_read` overloads should adjust
    the usage of the returned value as needed.
* Metafunctions `has_get_executor`,
  `is_sync_stream`, `is_sync_read_stream`, `is_sync_write_stream`,
  `is_async_stream`, `is_async_read_stream`, and `is_async_write_stream` are in stream\_traits.hpp.
  *Actions Required*: Include stream\_traits.hpp as needed.
* `basic_parser` is abstract.
  *Actions Required*

  + Change uses of the `basic_parser`
    type to omit the `Derived`
    template parameter
  + Classes derived from `basic_parser`
    no longer need to friend the base.
  + Virtual functions in the derived class may be marked `override`.
* Metafunction `is_file` is
  in file\_base.hpp. *Actions Required*: Include file\_base.hpp
  as needed.
* `flat_static_buffer::reset()`
  is deprecated. *Actions Required*:

  + call `clear()`
    instead.
* `buffers_adapter` is spelled
  `buffers_adaptor`. *Actions
  Required*:

  + Replace `buffers_adapter`
    with `buffers_adaptor`,
    or define `BOOST_BEAST_ALLOW_DEPRECATED`.
* `buffers` is spelled `make_printable`. *Actions Required*:

  + Replace `buffers` with
    `make_printable`, and
    include "make\_printable.hpp" instead of "ostream.hpp".
* `file_mode::append_new` is removed, as it makes no
  sense. *Actions Required*:

  + Replace `file_mode::append_new`
    with either `file_mode::append`
    or `file_mode::append_existing` as needed.
* `role_type` is moved from
  `websocket` to `beast`
* `buffers_range_ref` is preferred
  to `std::reference_wrapper`. *Actions
  Required*:

  + Call `buffers_range_ref`
    with the buffer, instead of calling `buffers_range`
    with a reference wrapper constructed from the buffer.
* Nested `lowest_layer` and
  `lowest_layer_type` are removed.
  *Actions Required*: Use the free function `get_lowest_layer` and the type trait
  `lowest_layer_type` instead.
* WebSocket decorator is a socket option:

  + Overloads of the following functions which accept a Decorator are
    deprecated:

    - `accept`, `accept_ex`
    - `handshake`,
      `handshake_ex`
    - `async_accept`,
      `async_accept_ex`
    - `async_handshake`,
      `async_handshake_ex`
* ( [#1375](https://github.com/boostorg/beast/issues/1375)) The value returned from `basic_parser::content_length`
  no longer changes as the body of the message is received. *Actions
  Required*: Call `basic_parser::content_length_remaining`
  instead of `basic_parser::content_length`
  in order to determine the remaining number of bytes in the body.

**Examples**

* All example programs are updated:

  + Use `tcp_stream` with
    timeouts (HTTP)
  + Use `ssl_stream`
  + Set timeouts for WebSocket streams.
  + Use `bind_front_handler`
* ( [#1100](https://github.com/boostorg/beast/issues/1100)) http-crawl clears the response before each read
* ( [#1347](https://github.com/boostorg/beast/issues/1347)) echo-op is rewritten
* ( [#1401](https://github.com/boostorg/beast/issues/1401)) Examples use `flat_buffer`
* Advanced servers use HTTP parser interfaces for reading
* detect-ssl is rewritten
* New example [example/websocket/server/chat-multi](../../../example/websocket/server/chat-multi)
* `async_echo` works with move-only
  handlers
* cppcon2018 example is removed

**Fixes**

* ( [#38](https://github.com/boostorg/beast/issues/38)) Better treatment of SSL short reads
* ( [#1223](https://github.com/boostorg/beast/issues/1223)) HTTP read counts bytes correctly when an error occurs
* ( [#1247](https://github.com/boostorg/beast/issues/1247)) Update `ssl_stream`
  for Asio changes
* ( [#1279](https://github.com/boostorg/beast/issues/1279)) Enable explicit instantiations of `websocket::stream`
* ( [#1290](https://github.com/boostorg/beast/issues/1290)) Don't use deprecated Asio interfaces
* ( [#1306](https://github.com/boostorg/beast/issues/1306)) `http::message` is not-a `boost::empty_value`
* ( [#1306](https://github.com/boostorg/beast/issues/1306)) `test::stream` has fewer dependencies
* ( [#1358](https://github.com/boostorg/beast/issues/1358)) Destroy abandoned websocket ops on shutdown
* ( [#1365](https://github.com/boostorg/beast/issues/1365)) Handler wrappers decay parameters sooner
* ( [#1408](https://github.com/boostorg/beast/issues/1408)) `session_alloc`
  is thread-safe
* ( [#1414](https://github.com/boostorg/beast/issues/1414)) Boost.System is header-only
* ( [#1418](https://github.com/boostorg/beast/issues/1418)) `test::stream` maintains a handler work guard
* ( [#1445](https://github.com/boostorg/beast/issues/1445)) Fix posix\_file::close handling of EINTR
* ( [#1460](https://github.com/boostorg/beast/issues/1460)) Large WebSocket Upgrade response no longer overflows
* Reusing an HTTP parser returns an error
* Handler bind wrappers use the associated allocator
* `buffers_cat` correctly skips
  empty buffers when iterated
* `ostream` does not overflow
  or exceed the dynamic buffer's maximum size
* Fixes to `test::stream::async_read`
* `file_mode::append_existing` works correctly
* A handler work guard is maintained on paused websocket operations
* All behavior of default-constructed iterators is conforming

#### [Boost 1.69](release_notes.html#beast.release_notes.boost_1_69)

**New Videos**

**New Features**

* ( [#1133](https://github.com/boostorg/beast/issues/1133)) Add `BOOST_BEAST_USE_STD_STRING_VIEW`

**Examples**

* New WebSocket server and browser-based client: example/cppcon2018

**Fixes**

* ( [#1245](https://github.com/boostorg/beast/issues/1245)) Fix a rare case of incorrect UTF8 validation
* ( [#1237](https://github.com/boostorg/beast/issues/1237)) Verify certificates in client examples
* ( [#1233](https://github.com/boostorg/beast/issues/1233)) Use [`boost::empty_value`](../../../../../doc/html/core/empty_value.html)
* ( [#1091](https://github.com/boostorg/beast/issues/1091)) Fix timer on websocket upgrade in examples
* ( [#1270](https://github.com/boostorg/beast/issues/1270)) [`basic_fields`](ref/boost__beast__http__basic_fields.html "http::basic_fields") uses intrusive base
  hooks
* ( [#1267](https://github.com/boostorg/beast/issues/1267)) Fix parsing of out-of-bounds hex values
* ( [#1263](https://github.com/boostorg/beast/issues/1263)) Fix uninitialized comparison in buffers iterator
* ( [#1288](https://github.com/boostorg/beast/issues/1288)) Remove extraneous strand from example
* Workaround for http-server-fast and libstdc++
* Partial support for `BOOST_NO_EXCEPTIONS`

**Experimental**

* Add `timeout_socket`

#### [Boost 1.68](release_notes.html#beast.release_notes.boost_1_68)

This version fixes a missing executor work guard in all composed operations
used in the implementation. Users who are experiencing crashes related to asynchronous
completion handlers are encouraged to upgrade. Also included is an improved
mechanism for generating random numbers used to mask outgoing websocket frames
when operating in the client mode. This resolves a vulnerability described
in the Beast Hybrid Assessment Report from Bishop Fox.

**New Features**

The include directory `<beast/experimental>` contains features which are not part of
the stable public interface but are available anyway. They may change in future
versions.

* ( [#1108](https://github.com/boostorg/beast/issues/1108)) New [`flat_stream`](ref/boost__beast__flat_stream.html "flat_stream") for working around
  an SSL stream performance limitation
* ( [#1151](https://github.com/boostorg/beast/issues/1151), [#595](https://github.com/boostorg/beast/issues/595)) New [`http::icy_stream`](ref/boost__beast__http__icy_stream.html "http::icy_stream") stream filter allows
  parsing ICY HTTP response handshakes
* New [`ssl_stream`](ref/boost__beast__ssl_stream.html "ssl_stream")
  for better SSL performance and move constructability
* New [`test::connect`](ref/boost__beast__test__error.html "test::error"),
  [`test::error`](ref/boost__beast__test__error.html "test::error"),
  [`test::fail_count`](ref/boost__beast__test__error.html "test::error"),
  and [`test::stream`](ref/boost__beast__test__error.html "test::error")
  utilities for writing unit tests.
* New [`http::is_mutable_body_writer`](ref/boost__beast__http__is_mutable_body_writer.html "http::is_mutable_body_writer") metafunction
* New [`websocket::seed_prng`](ref/boost__beast__websocket__seed_prng.html "websocket::seed_prng") for manually providing
  entropy to the PRNG
* New [`websocket::stream::secure_prng`](ref/boost__beast__websocket__stream/secure_prng.html "websocket::stream::secure_prng") to control whether
  the connection uses a secure PRNG

**Improvements**

* Generated WebSocket masks use a secure PRNG by default
* Improvements to [`buffers_adaptor`](ref/boost__beast__buffers_adaptor.html "buffers_adaptor")
* ( [#1188](https://github.com/boostorg/beast/issues/1188)) Set "/permissive-" for MSVC builds
* ( [#1109](https://github.com/boostorg/beast/issues/1109)) Use a shared string for example HTTP server doc roots
* ( [#1079](https://github.com/boostorg/beast/issues/1079)) Add `handler_ptr::has_value`

**Fixes**

* ( [#1073](https://github.com/boostorg/beast/issues/1073)) Fix race in advanced server examples
* ( [#1076](https://github.com/boostorg/beast/issues/1076)) Use executor\_work\_guard in composed operations
* ( [#1079](https://github.com/boostorg/beast/issues/1079)) Remove spurious assert
* ( [#1113](https://github.com/boostorg/beast/issues/1113)) Add `const` and
  non-`const` overloads for message
  based HTTP writes
* ( [#1119](https://github.com/boostorg/beast/issues/1119)) Fix unused variable warning
* ( [#1121](https://github.com/boostorg/beast/issues/1121)) Examples use the root certificate which matches the fingerprint
* ( [#1141](https://github.com/boostorg/beast/issues/1141)) Tidy up composed operation doc
* ( [#1186](https://github.com/boostorg/beast/issues/1186)) Check error in example set\_option
* ( [#1210](https://github.com/boostorg/beast/issues/1210)) Fix http\_server\_stackless\_ssl.cpp example
* ( [#1211](https://github.com/boostorg/beast/issues/1211)) Fix parse\_dec algorithm
* ( [#1214](https://github.com/boostorg/beast/issues/1214)) Silence ubsan false positive
* Tidy up websocket stream javadocs
* Fix move-only arguments in [`bind_handler`](ref/boost__beast__bind_handler.html "bind_handler")
* Fix [`http::parser`](ref/boost__beast__http__parser.html "http::parser") constructor javadoc
* Fix [`buffers_adaptor`](ref/boost__beast__buffers_adaptor.html "buffers_adaptor") iterator value
  type
* Fix [`buffers_adaptor::max_size`](ref/boost__beast__buffers_adaptor/max_size.html "buffers_adaptor::max_size")
* Fix [`buffers_prefix`](ref/boost__beast__buffers_prefix.html "buffers_prefix") iterator decrement
* Fix [*Fields*](concepts/Fields.html "Fields"),
  [*FieldsWriter*](concepts/FieldsWriter.html "FieldsWriter")
  concept docs
* Fix [*BodyReader*](concepts/BodyReader.html "BodyReader")
  constructor requirements doc

**Breaking Changes**

* Remove deprecated `serializer::reader_impl`
* Remove deprecated [*Body*](concepts/Body.html "Body")
  `reader` and `writer` ctor signatures

#### [Boost 1.67](release_notes.html#beast.release_notes.boost_1_67)

This version fixes significant defects in [`websocket::stream`](ref/boost__beast__websocket__stream.html "websocket::stream") which can lead to asserts or
undefined behavior. Users are encouraged to update to the latest Boost release.

**New Features**

* Move-only completion handlers are supported throughout the library
* ( [#899](https://github.com/boostorg/beast/issues/899)) Advanced server examples support idle websocket pings and timeouts
* ( [#849](https://github.com/boostorg/beast/issues/849)) WebSocket permessage-deflate support is now a compile-time feature.
  This adds an additional `bool`
  template parameter to [`websocket::stream`](ref/boost__beast__websocket__stream.html "websocket::stream") When `deflateSupported`
  is `true`, the stream will be
  capable of negotiating the permessage-deflate websocket extension per the
  configured run-time settings. When `deflateSupported`
  is `false`, the stream will
  never negotiate the permessage-deflate websocket extension. Furthermore,
  all of the code necessary for implementing the permessage-deflate extension
  will be excluded from function instantiations. Programs which set `deflateSupported` to `false`
  when instantiating streams will be smaller.
* ( [#949](https://github.com/boostorg/beast/issues/949)) WebSocket error codes are revised. New [error
  codes](ref/boost__beast__websocket__error.html "websocket::error") are added for more fine-grained failure outcomes. Messages
  for error codes are more verbose to help pinpoint the problem. Error codes
  are now also mapped to newly added [error
  conditions](ref/boost__beast__websocket__condition.html "websocket::condition") to simplify comparisons. The error codes `websocket::error::failed` and `websocket::error::handshake_failed`
  are removed. Actions required: Code which explicitly compares `error_code` values against the constant
  `websocket::error::handshake_failed` should compare against
  [`websocket::condition::handshake_failed`](ref/boost__beast__websocket__condition.html "websocket::condition") instead. Code
  which explicitly compares error\_code values against the constant `websocket::error::failed` should compare against [`websocket::condition::protocol_violation`](ref/boost__beast__websocket__condition.html "websocket::condition") instead.

**Improvements**

* ( [#857](https://github.com/boostorg/beast/issues/857)) [`http::basic_fields`](ref/boost__beast__http__basic_fields.html "http::basic_fields") uses less storage
* ( [#894](https://github.com/boostorg/beast/issues/894)) [`http::basic_fields`](ref/boost__beast__http__basic_fields.html "http::basic_fields") exception specifiers
  are provided
* Implementation no longer uses deprecated `asio::null_buffers`
* Add `<boost/beast/websocket/stream_fwd.hpp>`
* ( [#955](https://github.com/boostorg/beast/issues/955)) The asynchronous SSL detector example uses a stackless coroutine
* [`bind_handler`](ref/boost__beast__bind_handler.html "bind_handler")
  works with boost placeholders
* Examples set `reuse_address(true)`
* ( [#1026](https://github.com/boostorg/beast/issues/1026)) Advanced servers support clean shutdown via SIGINT or SIGTERM
* Some basic\_fields operations now give the strong exception guarantee

**Fixes**

* Fix "warning: ‘const’ type qualifier on return type has no effect"
* ( [#916](https://github.com/boostorg/beast/issues/916)) Tidy up `ssl_stream`
  special members
* ( [#918](https://github.com/boostorg/beast/issues/918)) Calls to `<algorithm>` are protected from macros
* ( [#954](https://github.com/boostorg/beast/issues/954)) The control callback is invoked on the proper executor
* ( [#994](https://github.com/boostorg/beast/issues/994)) Fix iterator version of [`http::basic_fields::erase`](ref/boost__beast__http__basic_fields/erase/overload1.html "http::basic_fields::erase (1 of 3 overloads)")
* ( [#992](https://github.com/boostorg/beast/issues/992)) Fix use-after-move in example request handlers
* ( [#988](https://github.com/boostorg/beast/issues/988)) Type check completion handlers
* ( [#985](https://github.com/boostorg/beast/issues/985)) Tidy up [`bind_handler`](ref/boost__beast__bind_handler.html "bind_handler") doc
* Fix memory leak in advanced server examples
* ( [#1000](https://github.com/boostorg/beast/issues/1000)) Fix soft-mutex assert in websocket stream. This resolves the
  assert `"ws_.wr_block_ == tok_"`.
* ( [#1019](https://github.com/boostorg/beast/issues/1019)) Fix fallthrough warnings
* ( [#1024](https://github.com/boostorg/beast/issues/1024)) Fix teardown for TIME\_WAIT
* ( [#1030](https://github.com/boostorg/beast/issues/1030)) Fix big-endian websocket masking
* Safe treatment of zero-length string arguments in basic\_fields
* ( [#1043](https://github.com/boostorg/beast/issues/1043)) Examples clear the HTTP message before reading
* ( [#1012](https://github.com/boostorg/beast/issues/1012)) Add asio\_handler\_invoke overloads for stream algorithms
* Add Access-Control-Expose-Headers field constant

**API Changes**

* Remove unintended public members of `handler_ptr`.
  Actions required: don't call non-public members.
* `handler_ptr` is a move-only
  type, with `unique_ptr` semantics.
  Actions required: user-defined composed operations using `handler_ptr` to manage state can only
  be moved, not copied.
* `handler_ptr` gives the strong
  exception guarantee. The constructor signature for managed objects constructed
  by `handler_ptr` now receives
  a `const` reference to the handler.
  Actions required: Change the constructor signature for state objects used
  with `handler_ptr` to receive
  a `const` reference to the handler.
* ( [#896](https://github.com/boostorg/beast/issues/896)) [`http::basic_fields`](ref/boost__beast__http__basic_fields.html "http::basic_fields") does not support
  fancy pointers
* [`http::parser`](ref/boost__beast__http__parser.html "http::parser")
  is no longer **MoveConstructible**
* ( [#930](https://github.com/boostorg/beast/issues/930)) `http::serializer::reader_impl` is deprecated and will be
  removed in the next release. Actions required: Call [`http::serializer::writer_impl`](ref/boost__beast__http__serializer/writer_impl.html "http::serializer::writer_impl") instead of `serializer::reader_impl`.
* ( [#884](https://github.com/boostorg/beast/issues/884)) The [*BodyReader*](concepts/BodyReader.html "BodyReader")
  and [*BodyWriter*](concepts/BodyWriter.html "BodyWriter")
  concept constructor requirements have changed. They now require the header
  and body elements to be passed as distinct [`http::header`](ref/boost__beast__http__header.html "http::header") and `value_type`
  objects. This enables the composition of body types. The previous single-argument
  constructors are deprecated and will be removed in the next version. Actions
  required: Change user-defined instances of [*BodyReader*](concepts/BodyReader.html "BodyReader")
  or [*BodyWriter*](concepts/BodyWriter.html "BodyWriter")
  constructor signatures to the two-argument form. Alternatively. define
  the macro `BOOST_BEAST_ALLOW_DEPRECATED`
  in the project (which will cause both the new and the deprecated signatures
  to be accepted).
* [`websocket::stream::control_callback`](ref/boost__beast__websocket__stream/control_callback.html "websocket::stream::control_callback") now copies or
  moves the function object.
* ( [#1014](https://github.com/boostorg/beast/issues/1014)) DynamicBuffer input areas are not mutable. Actions required:
  do not attempt to write to input areas of dynamic buffers.
* ( [#941](https://github.com/boostorg/beast/issues/941)) `get_lowest_layer`
  is now a type alias. Actions required: Replace instances of `typename get_lowest_layer<T>::type`
  with `get_lowest_layer<T>`.

#### [Boost 1.66](release_notes.html#beast.release_notes.boost_1_66)

* Initial release