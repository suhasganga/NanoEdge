### [FieldsWriter](FieldsWriter.html "FieldsWriter")

A **FieldsWriter** provides a algorithm to obtain
a sequence of buffers representing the complete serialized HTTP/1 header
for a set of fields. The implementation constructs an instance of this type
when needed, and calls into it once to retrieve the buffers.

##### [Associated Types](FieldsWriter.html#beast.concepts.FieldsWriter.associated_types)

* [*FieldsWriter*](FieldsWriter.html "FieldsWriter")

##### [Requirements](FieldsWriter.html#beast.concepts.FieldsWriter.requirements)

|  |  |
| --- | --- |
| [Warning] | Warning |
| These requirements may undergo non-backward compatible changes in subsequent versions. |

In this table:

* `W` denotes a type that
  meets the requirements of **FieldsWriter**.
* `F` denotes a [*Fields*](Fields.html "Fields")
  where `std::is_same<W, F::writer>::value ==
  true`.
* `a` is a value of type
  `W`.
* `f` is a value of type
  `F`.
* `v` is an `unsigned` value representing the HTTP version.
* `c` is an `unsigned` representing the HTTP status-code.
* `m` is a value of type
  [`verb`](../ref/boost__beast__http__verb.html "http::verb").

**Table 1.44. Valid expressions**

| expression | type | semantics, pre/post-conditions |
| --- | --- | --- |
| `W::const_buffers_type` |  | A type which meets the requirements of [*ConstBufferSequence*](../../../../../../doc/html/boost_asio/reference/ConstBufferSequence.html). This is the type of buffer returned by `W::get`. |
| `W{f,v,m}` |  | The implementation calls this constructor to indicate that the fields being serialized form part of an HTTP request. The lifetime of `f` is guaranteed to end no earlier than after the `W` is destroyed. |
| `W{f,v,c}` |  | The implementation calls this constructor to indicate that the fields being serialized form part of an HTTP response. The lifetime of `f` is guaranteed to end no earlier than after the `W` is destroyed. |
| `W{f}` |  | The implementation calls this constructor to indicate that the fields being serialized form part of a chunked encoding final-chunk trailer. The lifetime of `f` is guaranteed to end no earlier than after the `W` is destroyed. |
| `a.get()` | `W::const_buffers_type` | Called once after construction, this function returns a constant buffer sequence containing the serialized representation of the HTTP request or response including the final carriage return linefeed sequence (`"\r\n"`).  Copies may be made of the returned sequence, but the underlying memory is still owned by the writer. The implementation will destroy all copies of the buffer sequence before destroying `a`. |

  

##### [Exemplar](FieldsWriter.html#beast.concepts.FieldsWriter.exemplar)

```programlisting
struct FieldsWriter
{
    // The type of buffers returned by `get`
    struct const_buffers_type;

    // Constructor for requests
    FieldsWriter(Fields const& f, unsigned version, verb method);

    // Constructor for responses
    FieldsWriter(Fields const& f, unsigned version, unsigned status);

    // Returns the serialized header buffers
    const_buffers_type
    get();
};
```

##### [Models](FieldsWriter.html#beast.concepts.FieldsWriter.models)

* [`basic_fields::writer`](../ref/boost__beast__http__basic_fields/writer.html "http::basic_fields::writer")