#### [flat\_stream](boost__beast__flat_stream.html "flat_stream")

(Deprecated: This wrapper is no longer needed; Asio linearizes scatter/gather
I/O in ssl::stream.) Stream wrapper to improve write performance.

##### [Synopsis](boost__beast__flat_stream.html#beast.ref.boost__beast__flat_stream.synopsis)

Defined in header `<boost/beast/core/flat_stream.hpp>`

```programlisting
template<
    class NextLayer>
class flat_stream
```

##### [Types](boost__beast__flat_stream.html#beast.ref.boost__beast__flat_stream.types)

| Name | Description |
| --- | --- |
| **[executor\_type](boost__beast__flat_stream/executor_type.html "flat_stream::executor_type")** | The type of the executor associated with the object. |
| **[next\_layer\_type](boost__beast__flat_stream/next_layer_type.html "flat_stream::next_layer_type")** | The type of the next layer. |

##### [Member Functions](boost__beast__flat_stream.html#beast.ref.boost__beast__flat_stream.member_functions)

| Name | Description |
| --- | --- |
| **[async\_read\_some](boost__beast__flat_stream/async_read_some.html "flat_stream::async_read_some")** | Start an asynchronous read. |
| **[async\_write\_some](boost__beast__flat_stream/async_write_some.html "flat_stream::async_write_some")** | Start an asynchronous write. |
| **[flat\_stream](boost__beast__flat_stream/flat_stream.html "flat_stream::flat_stream") [constructor]** | — Constructor. |
| **[get\_executor](boost__beast__flat_stream/get_executor.html "flat_stream::get_executor")** | Get the executor associated with the object. |
| **[next\_layer](boost__beast__flat_stream/next_layer.html "flat_stream::next_layer")** | Get a reference to the next layer. |
| **[operator=](boost__beast__flat_stream/operator_eq_.html "flat_stream::operator=")** |  |
| **[read\_some](boost__beast__flat_stream/read_some.html "flat_stream::read_some")** | Read some data from the stream. |
| **[write\_some](boost__beast__flat_stream/write_some.html "flat_stream::write_some")** | Write some data to the stream. |
| **[~flat\_stream](boost__beast__flat_stream/_dtor_flat_stream.html "flat_stream::~flat_stream") [destructor]** | Destructor. |

##### [Description](boost__beast__flat_stream.html#beast.ref.boost__beast__flat_stream.description)

This wrapper flattens writes for buffer sequences having length greater than
1 and total size below a predefined amount, using a dynamic memory allocation.
It is primarily designed to overcome a performance limitation of the current
version of `net::ssl::stream`,
which does not use OpenSSL's scatter/gather interface for its low-level read
some and write some operations.

It is normally not necessary to use this class directly if you are already
using [`ssl_stream`](boost__beast__ssl_stream.html "ssl_stream").
The following examples shows how to use this class with the ssl stream that
comes with networking:

##### [Example](boost__beast__flat_stream.html#beast.ref.boost__beast__flat_stream.example)

To use the [`flat_stream`](boost__beast__flat_stream.html "flat_stream") template with SSL streams,
declare a variable of the correct type. Parameters passed to the constructor
will be forwarded to the next layer's constructor:

```programlisting
flat_stream<net::ssl::stream<ip::tcp::socket>> fs{ioc, ctx};
```

Alternatively you can write

```programlisting
ssl::stream<ip::tcp::socket> ss{ioc, ctx};
flat_stream<net::ssl::stream<ip::tcp::socket>&> fs{ss};
```

The resulting stream may be passed to any stream algorithms which operate
on synchronous or asynchronous read or write streams, examples include:

* `net::read`, `net::async_read`
* `net::write`, `net::async_write`
* `net::read_until`, `net::async_read_until`

The stream may also be used as a template parameter in other stream wrappers,
such as for websocket:

```programlisting
websocket::stream<flat_stream<net::ssl::stream<ip::tcp::socket>>> ws{ioc, ctx};
```

##### [Template Parameters](boost__beast__flat_stream.html#beast.ref.boost__beast__flat_stream.template_parameters)

| Type | Description |
| --- | --- |
| `NextLayer` | The type representing the next layer, to which data will be read and written during operations. For synchronous operations, the type must support the **SyncStream** concept. For asynchronous operations, the type must support the **AsyncStream** concept. This type will usually be some variation of `net::ssl::stream`. |

##### [See Also](boost__beast__flat_stream.html#beast.ref.boost__beast__flat_stream.see_also)

* <https://github.com/boostorg/asio/issues/100>
* <https://github.com/boostorg/beast/issues/1108>
* <https://stackoverflow.com/questions/38198638/openssl-ssl-write-from-multiple-buffers-ssl-writev>
* <https://stackoverflow.com/questions/50026167/performance-drop-on-port-from-beast-1-0-0-b66-to-boost-1-67-0-beast>