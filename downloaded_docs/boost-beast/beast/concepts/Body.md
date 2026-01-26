### [Body](Body.html "Body")

A **Body** type is supplied as a template argument
to the [`message`](../ref/boost__beast__http__message.html "http::message") class. It controls both
the type of the data member of the resulting message object, and the algorithms
used during parsing and serialization.

##### [Associated Types](Body.html#beast.concepts.Body.associated_types)

* [`is_body`](../ref/boost__beast__http__is_body.html "http::is_body")
* [*BodyReader*](BodyReader.html "BodyReader")
* [*BodyWriter*](BodyWriter.html "BodyWriter")

##### [Requirements](Body.html#beast.concepts.Body.requirements)

In this table:

* `B` is a type meeting the
  requirements of **Body**.
* `m` is a value of type
  `message<b,B,F>`
  where `b` is a `bool` value and `F`
  is a type meeting the requirements of [*Fields*](Fields.html "Fields").

**Table 1.38. Valid expressions**

| Expression | Type | Semantics, Pre/Post-conditions |
| --- | --- | --- |
| `B::value_type` |  | The return type of the `message::body` member function. If this is not movable or not copyable, the containing message will be not movable or not copyable. |
| `B::reader` |  | If present, indicates that the body can be parsed. The type must meet the requirements of [*BodyReader*](BodyReader.html "BodyReader"). The implementation constructs an object of this type to obtain buffers into which parsed body octets are placed. |
| `B::writer` |  | If present, indicates that the body is serializable. The type must meet the requirements of [*BodyWriter*](BodyWriter.html "BodyWriter"). The implementation constructs an object of this type to obtain buffers representing the message body for serialization. |
| ```programlisting B::size(   B::value_type body) ``` | `std::uint64_t` | This static member function is optional. It returns the payload size of `body` in bytes not including any chunked transfer encoding. The return value may be zero, to indicate that the message is known to have no payload. The function shall not exit via an exception.  When this function is present:  \* The function shall not fail  \* A call to [`message::payload_size`](../ref/boost__beast__http__message/payload_size.html "http::message::payload_size") will return the same value as `size`.  \* A call to [`message::prepare_payload`](../ref/boost__beast__http__message/prepare_payload.html "http::message::prepare_payload") will remove "chunked" from the Transfer-Encoding field if it appears as the last encoding, and will set the Content-Length field to the returned value.  Otherwise, when the function is omitted:  \* A call to [`message::payload_size`](../ref/boost__beast__http__message/payload_size.html "http::message::payload_size") will return `boost::none`.  \* A call to [`message::prepare_payload`](../ref/boost__beast__http__message/prepare_payload.html "http::message::prepare_payload") will erase the Content-Length field, and add "chunked" as the last encoding in the Transfer-Encoding field if it is not already present. |

  

##### [Exemplar](Body.html#beast.concepts.Body.exemplar)

```programlisting
struct Body
{
    // The type of message::body when used
    struct value_type;

    /// The algorithm used during parsing
    class reader;

    /// The algorithm used during serialization
    class writer;

    /// Returns the body's payload size
    static
    std::uint64_t
    size(value_type const& body);
};

static_assert(is_body<Body>::value, "");
```

##### [Models](Body.html#beast.concepts.Body.models)

* [`basic_dynamic_body`](../ref/boost__beast__http__basic_dynamic_body.html "http::basic_dynamic_body")
* [`basic_file_body`](../ref/boost__beast__http__basic_file_body.html "http::basic_file_body")
* [`basic_string_body`](../ref/boost__beast__http__basic_string_body.html "http::basic_string_body")
* [`buffer_body`](../ref/boost__beast__http__buffer_body.html "http::buffer_body")
* [`empty_body`](../ref/boost__beast__http__empty_body.html "http::empty_body")
* [`span_body`](../ref/boost__beast__http__span_body.html "http::span_body")
* [`vector_body`](../ref/boost__beast__http__vector_body.html "http::vector_body")