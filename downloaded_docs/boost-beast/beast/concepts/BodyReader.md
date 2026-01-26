### [BodyReader](BodyReader.html "BodyReader")

A **BodyReader** provides an online algorithm
to transfer a series of zero or more buffers containing parsed body octets
into a message container. The [`parser`](../ref/boost__beast__http__parser.html "http::parser") creates an instance of this
type when needed, and calls into it zero or more times to transfer buffers.
The interface of **BodyReader** is intended
to allow the conversion of buffers into these scenarios for representation:

* Storing a body in a dynamic buffer
* Storing a body in a user defined container with a custom allocator
* Transformation of incoming body data before storage, for example to compress
  it first.
* Saving body data to a file

##### [Associated Types](BodyReader.html#beast.concepts.BodyReader.associated_types)

* [`is_body_reader`](../ref/boost__beast__http__is_body_reader.html "http::is_body_reader")
* [*Body*](Body.html "Body")

##### [Requirements](BodyReader.html#beast.concepts.BodyReader.requirements)

|  |  |
| --- | --- |
| [Warning] | Warning |
| These requirements may undergo non-backward compatible changes in subsequent versions. |

In this table:

* `R` denotes a type meeting
  the requirements of **BodyReader**.
* `B` denotes a [*Body*](Body.html "Body")
  where `std::is_same<R, B::reader>::value ==
  true`.
* `a` denotes a value of
  type `R`.
* `b` is an object whose
  type meets the requirements of [*ConstBufferSequence*](../../../../../../doc/html/boost_asio/reference/ConstBufferSequence.html)
* `h` denotes a value of
  type `header<isRequest,
  Fields>&`.
* `v` denotes a value of
  type `Body::value_type&`.
* `n` is a value of type
  `boost::optional<std::uint64_t>`.
* `ec` is a value of type
  [`error_code&`](../ref/boost__beast__error_code.html "error_code").

**Table 1.39. Valid expressions**

| Expression | Type | Semantics, Pre/Post-conditions |
| --- | --- | --- |
| `R{h,v};` |  | Constructible from `h` and `v`. The lifetime of `h` and `v` is guaranteed to end no earlier than after the `R` is destroyed. The reader shall not access the contents of `h` or `v` before the first call to `init`, permitting lazy construction of the message. |
| `a.init(n, ec)` |  | Called once to fully initialize the object before any calls to `put`. The message body is valid before entering this function, and remains valid until the reader is destroyed. The value of `n` will be set to the content length of the body if known, otherwise `n` will be equal to `boost::none`. Implementations of **BodyReader** may use this information to optimize allocation.  The function will ensure that `!ec` is `true` if there was no error or set to the appropriate error code if there was one. |
| `a.put(b,ec)` | `std::size_t` | This function is called to append some or all of the buffers specified by `b` into the body representation. The number of bytes inserted from `b` is returned. If the number of bytes inserted is less than the total input, the remainder of the input will be presented in the next call to `put`. The function will ensure that `!ec` is `true` if there was no error or set to the appropriate error code if there was one. |
| `a.finish(ec)` |  | This function is called when no more body octets are remaining. The function will ensure that `!ec` is `true` if there was no error or set to the appropriate error code if there was one. |
| `is_body_reader<B>` | `std::true_type` | An alias for `std::true_type` for `B`, otherwise an alias for `std::false_type`. |

  

##### [Exemplar](BodyReader.html#beast.concepts.BodyReader.exemplar)

```programlisting
struct BodyReader
{
    /** Construct the reader.

        @param h The header for the message being parsed

        @param body The body to store the parsed results into
    */
    template<bool isRequest, class Fields>
    BodyReader(header<isRequest, Fields>& h, value_type& body);

    /** Initialize the reader.

        This is called after construction and before the first
        call to `put`. The message is valid and complete upon
        entry.

        @param ec Set to the error, if any occurred.
    */
    void
    init(
        boost::optional<std::uint64_t> const& content_length,
        error_code& ec)
    {
        boost::ignore_unused(content_length);

        // The specification requires this to indicate "no error"
        ec = {};
    }

    /** Store buffers.

        This is called zero or more times with parsed body octets.

        @param buffers The constant buffer sequence to store.

        @param ec Set to the error, if any occurred.

        @return The number of bytes transferred from the input buffers.
    */
    template<class ConstBufferSequence>
    std::size_t
    put(ConstBufferSequence const& buffers, error_code& ec)
    {
        // The specification requires this to indicate "no error"
        ec = {};

        return buffer_bytes(buffers);
    }

    /** Called when the body is complete.

        @param ec Set to the error, if any occurred.
    */
    void
    finish(error_code& ec)
    {
        // The specification requires this to indicate "no error"
        ec = {};
    }
};
```

##### [Models](BodyReader.html#beast.concepts.BodyReader.models)

* [`basic_dynamic_body::reader`](../ref/boost__beast__http__basic_dynamic_body/reader.html "http::basic_dynamic_body::reader")
* [`basic_file_body::reader`](../ref/boost__beast__http__basic_file_body__reader.html "http::basic_file_body::reader")
* [`basic_string_body::reader`](../ref/boost__beast__http__basic_string_body/reader.html "http::basic_string_body::reader")
* [`buffer_body::reader`](../ref/boost__beast__http__buffer_body/reader.html "http::buffer_body::reader")
* [`empty_body::reader`](../ref/boost__beast__http__empty_body/reader.html "http::empty_body::reader")
* [`span_body::reader`](../ref/boost__beast__http__span_body/reader.html "http::span_body::reader")
* [`vector_body::reader`](../ref/boost__beast__http__vector_body/reader.html "http::vector_body::reader")