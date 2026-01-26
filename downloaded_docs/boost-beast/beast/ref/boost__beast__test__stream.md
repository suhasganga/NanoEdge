#### [test::stream](boost__beast__test__stream.html "test::stream")

##### [Synopsis](boost__beast__test__stream.html#beast.ref.boost__beast__test__stream.synopsis)

Defined in header `<boost/beast/_experimental/test/stream.hpp>`

```programlisting
using stream = basic_stream<>;
```

##### [Types](boost__beast__test__stream.html#beast.ref.boost__beast__test__stream.types)

| Name | Description |
| --- | --- |
| **[buffer\_type](boost__beast__test__basic_stream/buffer_type.html "test::basic_stream::buffer_type")** |  |
| **[executor\_type](boost__beast__test__basic_stream/executor_type.html "test::basic_stream::executor_type")** | The type of the executor associated with the object. |
| **[rebind\_executor](boost__beast__test__basic_stream__rebind_executor.html "test::basic_stream::rebind_executor")** | Rebinds the socket type to another executor. |

##### [Member Functions](boost__beast__test__stream.html#beast.ref.boost__beast__test__stream.member_functions)

| Name | Description |
| --- | --- |
| **[append](boost__beast__test__basic_stream/append.html "test::basic_stream::append")** | Appends a string to the pending input data. |
| **[async\_read\_some](boost__beast__test__basic_stream/async_read_some.html "test::basic_stream::async_read_some")** | Start an asynchronous read. |
| **[async\_write\_some](boost__beast__test__basic_stream/async_write_some.html "test::basic_stream::async_write_some")** | Start an asynchronous write. |
| **[basic\_stream](boost__beast__test__basic_stream/basic_stream.html "test::basic_stream::basic_stream")** | Move Constructor.  — Construct a stream. |
| **[buffer](boost__beast__test__basic_stream/buffer.html "test::basic_stream::buffer")** | Direct input buffer access. |
| **[clear](boost__beast__test__basic_stream/clear.html "test::basic_stream::clear")** | Clear the pending input area. |
| **[close](boost__beast__test__basic_stream/close.html "test::basic_stream::close")** | Close the stream. |
| **[close\_remote](boost__beast__test__basic_stream/close_remote.html "test::basic_stream::close_remote")** | Close the other end of the stream. |
| **[connect](boost__beast__test__basic_stream/connect.html "test::basic_stream::connect")** | Establish a connection. |
| **[get\_executor](boost__beast__test__basic_stream/get_executor.html "test::basic_stream::get_executor")** | Return the executor associated with the object. |
| **[nread](boost__beast__test__basic_stream/nread.html "test::basic_stream::nread")** | Return the number of reads. |
| **[nread\_bytes](boost__beast__test__basic_stream/nread_bytes.html "test::basic_stream::nread_bytes")** | Return the number of bytes read. |
| **[nwrite](boost__beast__test__basic_stream/nwrite.html "test::basic_stream::nwrite")** | Return the number of writes. |
| **[nwrite\_bytes](boost__beast__test__basic_stream/nwrite_bytes.html "test::basic_stream::nwrite_bytes")** | Return the number of bytes written. |
| **[operator=](boost__beast__test__basic_stream/operator_eq_.html "test::basic_stream::operator=")** | Move Assignment. |
| **[operator==](boost__beast__test__basic_stream/operator_eq__eq_.html "test::basic_stream::operator==")** |  |
| **[read\_size](boost__beast__test__basic_stream/read_size.html "test::basic_stream::read_size")** | Set the maximum number of bytes returned by read\_some. |
| **[read\_some](boost__beast__test__basic_stream/read_some.html "test::basic_stream::read_some")** | Read some data from the stream. |
| **[str](boost__beast__test__basic_stream/str.html "test::basic_stream::str")** | Returns a string view representing the pending input data. |
| **[write\_size](boost__beast__test__basic_stream/write_size.html "test::basic_stream::write_size")** | Set the maximum number of bytes returned by write\_some. |
| **[write\_some](boost__beast__test__basic_stream/write_some.html "test::basic_stream::write_some")** | Write some data to the stream. |
| **[~basic\_stream](boost__beast__test__basic_stream/_dtor_basic_stream.html "test::basic_stream::~basic_stream") [destructor]** | Destructor. |

An instance of this class simulates a traditional socket, while also providing
features useful for unit testing. Each endpoint maintains an independent
buffer called the input area. Writes from one endpoint append data to the
peer's pending input area. When an endpoint performs a read and data is present
in the input area, the data is delivered to the blocking or asynchronous
operation. Otherwise the operation is blocked or deferred until data is made
available, or until the endpoints become disconnected.

These streams may be used anywhere an algorithm accepts a reference to a
synchronous or asynchronous read or write stream. It is possible to use a
test stream in a call to `net::read_until`,
or in a call to [`boost::beast::http::async_write`](boost__beast__http__async_write.html "http::async_write") for example.

As with Boost.Asio I/O objects, a [`stream`](boost__beast__test__stream.html "test::stream") constructs with a reference
to the `net::io_context` to use for handling asynchronous
I/O. For asynchronous operations, the stream follows the same rules as a
traditional asio socket with respect to how completion handlers for asynchronous
operations are performed.

To facilitate testing, these streams support some additional features:

* The input area, represented by a [`beast::basic_flat_buffer`](boost__beast__basic_flat_buffer.html "basic_flat_buffer"), may be directly
  accessed by the caller to inspect the contents before or after the remote
  endpoint writes data. This allows a unit test to verify that the received
  data matches.
* Data may be manually appended to the input area. This data will delivered
  in the next call to [`stream::read_some`](boost__beast__test__basic_stream/read_some.html "test::basic_stream::read_some") or [`stream::async_read_some`](boost__beast__test__basic_stream/async_read_some.html "test::basic_stream::async_read_some"). This allows
  predefined test vectors to be set up for testing read algorithms.
* The stream may be constructed with a fail count. The stream will eventually
  fail with a predefined error after a certain number of operations, where
  the number of operations is controlled by the test. When a test loops
  over a range of operation counts, it is possible to exercise every possible
  point of failure in the algorithm being tested. When used correctly the
  technique allows the tests to reach a high percentage of code coverage.

##### [Thread Safety](boost__beast__test__stream.html#beast.ref.boost__beast__test__stream.thread_safety)

*Distinct**objects:*Safe.

*Shared**objects:*Unsafe. The application
must also ensure that all asynchronous operations are performed within the
same implicit or explicit strand.