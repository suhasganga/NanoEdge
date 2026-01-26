### [BodyWriter](BodyWriter.html "BodyWriter")

A **BodyWriter** provides an [online
algorithm](https://en.wikipedia.org/wiki/Online_algorithm) to obtain a sequence of zero or more buffers from a body
during serialization. The implementation creates an instance of this type
when needed, and calls into it one or more times to retrieve buffers holding
body octets. The interface of **BodyWriter**
is intended to obtain buffers for these scenarios:

* A body that does not entirely fit in memory.
* A body produced incrementally from coroutine output.
* A body represented by zero or more buffers already in memory.
* A body whose size is not known ahead of time.
* Body data generated dynamically from other threads.
* Body data computed algorithmically.

##### [Associated Types](BodyWriter.html#beast.concepts.BodyWriter.associated_types)

* [`is_body_writer`](../ref/boost__beast__http__is_body_writer.html "http::is_body_writer")
* [*Body*](Body.html "Body")

##### [Requirements](BodyWriter.html#beast.concepts.BodyWriter.requirements)

|  |  |
| --- | --- |
| [Warning] | Warning |
| These requirements may undergo non-backward compatible changes in subsequent versions. |

In this table:

* `W` denotes a type meeting
  the requirements of **BodyWriter**.
* `B` denotes a [*Body*](Body.html "Body")
  where `std::is_same<W, B::writer>::value ==
  true`.
* `a` denotes a value of
  type `W`.
* `h` denotes a const value
  of type `header<isRequest,
  Fields>
  const&`.
* `v` denotes a possibly
  const value of type `Body::value_type&`.
* `ec` is a value of type
  [`error_code&`](../ref/boost__beast__error_code.html "error_code").
* `W<T>`
  is the type `boost::optional<std::pair<T, bool>>`.

**Table 1.40. Valid expressions**

| Expression | Type | Semantics, Pre/Post-conditions |
| --- | --- | --- |
| `W::const_buffers_type` |  | A type which meets the requirements of [*ConstBufferSequence*](../../../../../../doc/html/boost_asio/reference/ConstBufferSequence.html). This is the type of buffer returned by `W::get`. |
| `W{h,v};` |  | Constructible from `h` and `v`. The lifetime of `h` and `v` are guaranteed to end no earlier than after the `W` is destroyed. The writer shall not access the contents of `h` or `v` before the first call to `init`, permitting lazy construction of the message.  The constructor may optionally require that `h` and `v` are `const` references, with these consequences:  \* If `W` requires that `h` and `v` are const references, then the corresponding serializer constructors for messages with this body type will will accept a const reference to a message, otherwise:  \* If `W` requires that `h` and `v` are non-const references, then the corresponding serializer constructors for messages with this body type will require a non-const reference to a message. |
| `a.init(ec)` |  | Called once to fully initialize the object before any calls to `get`. The message body becomes valid before entering this function, and remains valid until the writer is destroyed. The function will ensure that `!ec` is `true` if there was no error or set to the appropriate error code if there was one. |
| `a.get(ec)` | `W<W::const_buffers_type>` | Called one or more times after `init` succeeds. This function returns `boost::none` if all buffers representing the body have been returned in previous calls or if it sets `ec` to indicate an error. Otherwise, if there are buffers remaining the function should return a pair with the first element containing a non-zero length buffer sequence representing the next set of octets in the body, while the second element is a `bool` meaning `true` if there may be additional buffers returned on a subsequent call, or `false` if the buffer returned on this call is the last buffer representing the body. The function will ensure that `!ec` is `true` if there was no error or set to the appropriate error code if there was one. |

  

##### [Exemplar](BodyWriter.html#beast.concepts.BodyWriter.exemplar)

```programlisting
struct BodyWriter
{
public:
    /// The type of buffer returned by `get`.
    using const_buffers_type = net::const_buffer;

    /** Construct the writer.

        @param h The header for the message being serialized

        @param body The body being serialized
    */
    template<bool isRequest, class Fields>
    BodyWriter(header<isRequest, Fields> const& h, value_type const& body);

    /** Initialize the writer.

        This is called after construction and before the first
        call to `get`. The message is valid and complete upon
        entry.

        @param ec Set to the error, if any occurred.
    */
    void
    init(error_code& ec)
    {
        // The specification requires this to indicate "no error"
        ec = {};
    }

    /** Returns the next buffer in the body.

        @li If the return value is `boost::none` (unseated optional) and
            `ec` does not contain an error, this indicates the end of the
            body, no more buffers are present.

        @li If the optional contains a value, the first element of the
            pair represents a <em>ConstBufferSequence</em> containing one or
            more octets of the body data. The second element indicates
            whether or not there are additional octets of body data.
            A value of `true` means there is more data, and that the
            implementation will perform a subsequent call to `get`.
            A value of `false` means there is no more body data.

        @li If `ec` contains an error code, the return value is ignored.

        @param ec Set to the error, if any occurred.
    */
    boost::optional<std::pair<const_buffers_type, bool>>
    get(error_code& ec)
    {
        // The specification requires this to indicate "no error"
        ec = {};

        return boost::none; // for exposition only
    }
};
```

##### [Models](BodyWriter.html#beast.concepts.BodyWriter.models)

* [`basic_dynamic_body::writer`](../ref/boost__beast__http__basic_dynamic_body/writer.html "http::basic_dynamic_body::writer")
* [`basic_file_body::writer`](../ref/boost__beast__http__basic_file_body__writer.html "http::basic_file_body::writer")
* [`basic_string_body::writer`](../ref/boost__beast__http__basic_string_body/writer.html "http::basic_string_body::writer")
* [`buffer_body::writer`](../ref/boost__beast__http__buffer_body/writer.html "http::buffer_body::writer")
* [`empty_body::writer`](../ref/boost__beast__http__empty_body/writer.html "http::empty_body::writer")
* [`span_body::writer`](../ref/boost__beast__http__span_body/writer.html "http::span_body::writer")
* [`vector_body::writer`](../ref/boost__beast__http__vector_body/writer.html "http::vector_body::writer")