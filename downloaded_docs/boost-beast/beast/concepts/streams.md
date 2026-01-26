### [Streams](streams.html "Streams")

A stream in the context of Beast and networking, represents a full-duplex
connection between two programs or hosts, where data represented as bytes
may be received reliably in the same order they were written. Streams may
support any combination of synchronous and/or asynchronous reading and writing.

Stream concepts are based on named requirements in networking:

##### [Stream](streams.html#beast.concepts.streams.Stream)

A type modeling **Stream** meets either or both
of the following requirements:

* **AsyncStream**
* **SyncStream**

##### [AsyncStream](streams.html#beast.concepts.streams.AsyncStream)

A type modeling **AsyncStream** meets the following
requirements:

* [*AsyncReadStream*](../../../../../../doc/html/boost_asio/reference/AsyncReadStream.html)
* [*AsyncWriteStream*](../../../../../../doc/html/boost_asio/reference/AsyncWriteStream.html)

##### [SyncStream](streams.html#beast.concepts.streams.SyncStream)

A type modeling **SyncStream** meets the following
requirements:

* [*SyncReadStream*](../../../../../../doc/html/boost_asio/reference/SyncReadStream.html)
* [*SyncWriteStream*](../../../../../../doc/html/boost_asio/reference/SyncWriteStream.html)