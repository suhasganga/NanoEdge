### [BuffersGenerator](BuffersGenerator.html "BuffersGenerator")

A **BuffersGenerator** provides a generalized
interface for generating serialized data for sequential processing.

The generator will be asked to produce buffers. The consuming code will signal
how much of the data has been consumed, and repeatedly query for buffers
until no more data is available, or the generator indicates an error condition.

In this way, serializers can be adapted as **BuffersGenerator**,
for example [`http::message_generator`](../ref/boost__beast__http__message_generator.html "http::message_generator") which provides
a type-erased interface for a variety of concrete http message types.

Overloads of [`write`](../ref/boost__beast__write.html "write") and [`async_write`](../ref/boost__beast__async_write.html "async_write") operations are provided
as free functions. These operations will consume the output of a **BuffersGenerator** and process the data by writing them
to a [*SyncWriteStream*](../../../../../../doc/html/boost_asio/reference/SyncWriteStream.html)
or [*AsyncWriteStream*](../../../../../../doc/html/boost_asio/reference/AsyncWriteStream.html)
respectively.

##### [Associated Types](BuffersGenerator.html#beast.concepts.BuffersGenerator.associated_types)

* [`is_buffers_generator`](../ref/boost__beast__is_buffers_generator.html "is_buffers_generator")
* [*ConstBufferSequence*](../../../../../../doc/html/boost_asio/reference/ConstBufferSequence.html)

##### [Requirements](BuffersGenerator.html#beast.concepts.BuffersGenerator.requirements)

In this table:

* `G` denotes a type meeting
  the requirements of **BuffersGenerator**.
* `g` denotes a value of
  type `G`.
* `c` denotes a possibly-const
  value of type `G`.
* `n` is a value of type
  `std::size_t`.
* `ec` is a value of type
  [`error_code&`](../ref/boost__beast__error_code.html "error_code").

**Table 1.41. Valid expressions**

| Expression | Type | Semantics, Pre/Post-conditions |
| --- | --- | --- |
| `G::const_buffers_type` |  | A type which meets the requirements of [*ConstBufferSequence*](../../../../../../doc/html/boost_asio/reference/ConstBufferSequence.html). This is the type of buffer returned by `g.prepare(ec)`. |
| `c.is_done()` | `bool` | Called to ask the generator for its completion status.  A generator has completed when no new buffer will be produced and previously produced buffers have been fully consumed.  **Note:** The result of invoking `prepare` on `g` once it has completed is unspecified. |
| `g.prepare(ec)` | `G::const_buffers_type` | Called to ask the generator to produce buffers containing data for processing.  The returned value is the [*ConstBufferSequence*](../../../../../../doc/html/boost_asio/reference/ConstBufferSequence.html) representing unconsumed data.  The function will ensure that `ec.failed()` is `false` if there was no error or set to the appropriate error code if there was one.  If no unconsumed data is available, this operation shall make progress to eventually reach completion.  The result of invoking `prepare` after completion or encountered error(s) is defined by the generator implementation. It can not be assumed to be meaningful or safe to do so, in general.  The capacity of the buffer returned is defined by the generator implementation.  **Note:** Any buffers obtained by previous calls to `prepare` are invalidated. |
| `g.consume(n)` |  | This function is called to signal that the consumer (caller) of the generator has processed part of the data returned by the previous call to `prepare`.  The value of `n` indicates how much of the data processed (in bytes).  When `n` exceeds the number of bytes returned from the last call to `prepare`, `consume` shall behave as if `n` was equal to that number.  Remaining unconsumed data will be returned from subsequent calls to `prepare`.  **Note:** Any buffers obtained by previous calls to `prepare` are invalidated. |
| `is_buffers_generator<G>` | `std::bool_constant` | An alias for `std::true_type` for `G`, otherwise an alias for `std::false_type`. |

  

##### [Exemplar](BuffersGenerator.html#beast.concepts.BuffersGenerator.exemplar)

```programlisting
// A buffer sequence generator
struct BuffersGenerator
{
    using const_buffers_type = net::const_buffer;

    bool is_done() const;
    const_buffers_type prepare( error_code& ec );
    void consume( std::size_t n );
};

static_assert(
    is_buffers_generator<BuffersGenerator>::value, "");
```

##### [Models](BuffersGenerator.html#beast.concepts.BuffersGenerator.models)

* [`http::message_generator`](../ref/boost__beast__http__message_generator.html "http::message_generator")

##### [Algorithms](BuffersGenerator.html#beast.concepts.BuffersGenerator.algorithms)

* [`async_write`](../ref/boost__beast__async_write.html "async_write")
* [`write`](../ref/boost__beast__write.html "write")