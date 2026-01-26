### [Fields](Fields.html "Fields")

An instance of **Fields** is a container for
holding HTTP header fields and their values. The implementation also calls
upon the container to store the request target and non-standard strings for
method and obsolete reason phrase as needed. Types which meet these requirements
can always be serialized.

##### [Associated Types](Fields.html#beast.concepts.Fields.associated_types)

* [`is_fields`](../ref/boost__beast__http__is_fields.html "http::is_fields")
* [*FieldsWriter*](FieldsWriter.html "FieldsWriter")

##### [Requirements](Fields.html#beast.concepts.Fields.requirements)

In this table:

* `F` denotes a type that
  meets the requirements of **Fields**.
* `W` denotes a type meeting
  the requirements of [*FieldsWriter*](FieldsWriter.html "FieldsWriter").
* `a` denotes a value of
  type `F`.
* `c` denotes a (possibly
  const) value of type `F`.
* `b` is a value of type
  `bool`
* `n` is a value of type
  `boost::optional<std::uint64_t>`.
* `s` is a value of type
  [`string_view`](../ref/boost__beast__string_view.html "string_view").
* `v` is a value of type
  `unsigned int`
  representing the HTTP-version.

**Table 1.43. Valid expressions**

| Expression | Type | Semantics, Pre/Post-conditions |
| --- | --- | --- |
| `F::writer` | `W` | A type which meets the requirements of [*FieldsWriter*](FieldsWriter.html "FieldsWriter"). |
| `c.get_method_impl()` | `string_view` | Returns the method text. The implementation only calls this function for request headers when retrieving the method text previously set with a call to `set_method_impl` using a non-empty string. |
| `c.get_target_impl()` | `string_view` | Returns the target string. The implementation only calls this function for request headers. |
| `c.get_reason_impl()` | `string_view` | Returns the obsolete request text. The implementation only calls this for response headers when retrieving the reason text previously set with a call to `set_reason_impl` using a non-empty string. |
| `c.get_chunked_impl()` | `bool` | Returns `true` if the [**Transfer-Encoding**](https://tools.ietf.org/html/rfc7230#section-3.3.1) field value indicates that the payload is chunk encoded. Both of these conditions must be true:  * The Transfer-Encoding field is present in the message. * The last item in value of the field is "chunked". |
| `c.get_keep_alive_impl(v)` | `bool` | Returns `true` if the semantics of the [**Connection**](https://tools.ietf.org/html/rfc7230#section-6.1) field and version indicate that the connection should remain open after the corresponding response is transmitted or received:  * If `(v   < 11)` the function returns `true` if the "keep-alive"   token is present in the Connection field value. Otherwise the   function returns `false`. * If `(v   == 11)`, the function returns `false` if the "close"   token is present in the Connection field value. Otherwise the   function returns `true`. |
| `c.has_content_length()` | `bool` | Returns `true` if the [**Content-Length**](https://tools.ietf.org/html/rfc7230#section-3.3.2) field is present. |
| `a.set_method_impl(s)` |  | Stores a copy of `s` as the method text, or erases the previously stored value if `s` is empty. The implementation only calls this function for request headers. This function may throw `std::invalid_argument` if the operation is not supported by the container. |
| `a.set_target_impl(s)` |  | Stores a copy of `s` as the target, or erases the previously stored value if `s` is empty. The implementation only calls this function for request headers. This function may throw `std::invalid_argument` if the operation is not supported by the container. |
| `a.set_reason_impl(s)` |  | Stores a copy of `s` as the reason text, or erases the previously stored value of the reason text if `s` is empty. The implementation only calls this function for request headers. This function may throw `std::invalid_argument` if the operation is not supported by the container. |
| `a.set_chunked_impl(b)` |  | Adjusts the [**Transfer-Encoding**](https://tools.ietf.org/html/rfc7230#section-3.3.1) field value as follows:  * If `b` is `true`, the "chunked"   token is appended to the list of encodings if it does not already   appear last in the list. If the Transfer-Encoding field is   absent, the field will be inserted to the container with the   value "chunked". * If `b` is `false,   the "chunked" token is removed from the list of encodings   if it appears last in the list. If the result of the removal   leaves the list of encodings empty, the Transfer-Encoding field   shall not appear when the associated [*FieldsWriter*](FieldsWriter.html "FieldsWriter")   serializes the fields.  If the result of adjusting the field value produces an empty string, the field is removed from the container. |
| `a.set_content_length_impl(n)` |  | Adjusts the [**Content-Length**](https://tools.ietf.org/html/rfc7230#section-3.3.2) field value as follows:  * If `n` contains   a value, the Content-Length field will be set to the text representation   of the value. Any previous Content-Length fields are removed   from the container. * If `n` does not   contain a value, any present Content-Length fields are removed   from the container. |
| `a.set_keep_alive_impl(v,b)` |  | Adjusts the [**Connection**](https://tools.ietf.org/html/rfc7230#section-6.1) field value depending on the values of `v` and `b`. The field value is treated as [*connection-option*](https://tools.ietf.org/html/rfc7230#section-6.1) (rfc7230).  * If `(v   < 11   && b)`, then all "close"   tokens present in the value are removed, and the "keep-alive"   token is added to the value if it is not already present. * If `(v   < 11   && !   b)`,   then all "close" and "keep-alive" tokens   present in the value are removed. * If `(v   == 11   && b)`, then all "keep-alive"   and "close" tokens present in the value are removed. * If `(v   == 11   && !   b)`,   then all "keep-alive" tokens present in the value   are removed, and the "close" token is added to the   value if it is not already present.  If the result of adjusting the field value produces an empty string, the field is removed from the container. |

  

##### [Exemplar](Fields.html#beast.concepts.Fields.exemplar)

```programlisting
class Fields
{
public:
    /// Constructed as needed when fields are serialized
    struct writer;

protected:
    /** Returns the request-method string.

        @note Only called for requests.
    */
    string_view
    get_method_impl() const;

    /** Returns the request-target string.

        @note Only called for requests.
    */
    string_view
    get_target_impl() const;

    /** Returns the response reason-phrase string.

        @note Only called for responses.
    */
    string_view
    get_reason_impl() const;

    /** Returns the chunked Transfer-Encoding setting
    */
    bool
    get_chunked_impl() const;

    /** Returns the keep-alive setting
    */
    bool
    get_keep_alive_impl(unsigned version) const;

    /** Returns `true` if the Content-Length field is present.
    */
    bool
    has_content_length_impl() const;

    /** Set or clear the method string.

        @note Only called for requests.
    */
    void
    set_method_impl(string_view s);

    /** Set or clear the target string.

        @note Only called for requests.
    */
    void
    set_target_impl(string_view s);

    /** Set or clear the reason string.

        @note Only called for responses.
    */
    void
    set_reason_impl(string_view s);

    /** Sets or clears the chunked Transfer-Encoding value
    */
    void
    set_chunked_impl(bool value);

    /** Sets or clears the Content-Length field
    */
    void
    set_content_length_impl(boost::optional<std::uint64_t>);

    /** Adjusts the Connection field
    */
    void
    set_keep_alive_impl(unsigned version, bool keep_alive);
};

static_assert(is_fields<Fields>::value,
    "Fields type requirements not met");
```

##### [Models](Fields.html#beast.concepts.Fields.models)

* [`basic_fields`](../ref/boost__beast__http__basic_fields.html "http::basic_fields")
* [`fields`](../ref/boost__beast__http__fields.html "http::fields")