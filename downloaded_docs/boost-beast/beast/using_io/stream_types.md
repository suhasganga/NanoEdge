### [Streams](stream_types.html "Streams")

A [*Stream*](../concepts/streams.html "Streams")
is a communication channel where data is reliably transferred as an ordered
sequence of bytes. Streams are either synchronous or asynchronous, and may
allow reading, writing, or both. Note that a particular type may model more
than one concept. For example, the networking types [`tcp::socket`](../../../../../../doc/html/boost_asio/reference/ip__tcp/socket.html)
and [`net::ssl::stream`](../../../../../../doc/html/boost_asio/reference/ssl__stream.html)
support both [*SyncStream*](../concepts/streams.html#beast.concepts.streams.SyncStream)
and [*AsyncStream*](../concepts/streams.html#beast.concepts.streams.AsyncStream).
All stream algorithms in Beast are declared as template functions using these
concepts:

**Table 1.4. Stream Concepts**

| Concept | Description |
| --- | --- |
| [*SyncReadStream*](../../../../../../doc/html/boost_asio/reference/SyncReadStream.html) | Supports buffer-oriented blocking reads. |
| [*SyncWriteStream*](../../../../../../doc/html/boost_asio/reference/SyncWriteStream.html) | Supports buffer-oriented blocking writes. |
| [*SyncStream*](../concepts/streams.html#beast.concepts.streams.SyncStream) | A stream supporting buffer-oriented blocking reads and writes. |
| [*AsyncReadStream*](../../../../../../doc/html/boost_asio/reference/AsyncReadStream.html) | Supports buffer-oriented asynchronous reads. |
| [*AsyncWriteStream*](../../../../../../doc/html/boost_asio/reference/AsyncWriteStream.html) | Supports buffer-oriented asynchronous writes. |
| [*AsyncStream*](../concepts/streams.html#beast.concepts.streams.AsyncStream) | A stream supporting buffer-oriented asynchronous reads and writes. |

  

These template metafunctions check whether a given type meets the requirements
for the various stream concepts, and some additional useful utilities. The
library uses these type checks internally and also provides them as public
interfaces so users may use the same techniques to augment their own code.
The use of these type checks helps provide more concise errors during compilation:

**Table 1.5. Type Traits and Metafunctions**

| Name | Description |
| --- | --- |
| [`executor_type`](../ref/boost__beast__executor_type.html "executor_type") | An alias for the type of object returned by `get_executor`. |
| [`has_get_executor`](../ref/boost__beast__has_get_executor.html "has_get_executor") | Determine if the `get_executor` member function is present. |
| [`is_async_read_stream`](../ref/boost__beast__is_async_read_stream.html "is_async_read_stream") | Determine if a type meets the requirements of [*AsyncReadStream*](../../../../../../doc/html/boost_asio/reference/AsyncReadStream.html). |
| [`is_async_stream`](../ref/boost__beast__is_async_stream.html "is_async_stream") | Determine if a type meets the requirements of both [*AsyncReadStream*](../../../../../../doc/html/boost_asio/reference/AsyncReadStream.html) and [*AsyncWriteStream*](../../../../../../doc/html/boost_asio/reference/AsyncWriteStream.html). |
| [`is_async_write_stream`](../ref/boost__beast__is_async_write_stream.html "is_async_write_stream") | Determine if a type meets the requirements of [*AsyncWriteStream*](../../../../../../doc/html/boost_asio/reference/AsyncWriteStream.html). |
| [`is_sync_read_stream`](../ref/boost__beast__is_sync_read_stream.html "is_sync_read_stream") | Determine if a type meets the requirements of [*SyncReadStream*](../../../../../../doc/html/boost_asio/reference/SyncReadStream.html). |
| [`is_sync_stream`](../ref/boost__beast__is_sync_stream.html "is_sync_stream") | Determine if a type meets the requirements of both [*SyncReadStream*](../../../../../../doc/html/boost_asio/reference/SyncReadStream.html) and [*SyncWriteStream*](../../../../../../doc/html/boost_asio/reference/SyncWriteStream.html). |
| [`is_sync_write_stream`](../ref/boost__beast__is_sync_write_stream.html "is_sync_write_stream") | Determine if a type meets the requirements of [*SyncWriteStream*](../../../../../../doc/html/boost_asio/reference/SyncWriteStream.html). |

  

Using the type checks with `static_assert`
on function or class template types will provide users with helpful error
messages and prevent undefined behaviors. This example shows how a template
function which writes to a synchronous stream may check its argument:

```programlisting
template<class SyncWriteStream>
void write_string(SyncWriteStream& stream, string_view s)
{
    static_assert(is_sync_write_stream<SyncWriteStream>::value,
        "SyncWriteStream type requirements not met");
    net::write(stream, net::const_buffer(s.data(), s.size()));
}
```