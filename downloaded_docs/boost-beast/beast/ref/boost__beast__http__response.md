#### [http::response](boost__beast__http__response.html "http::response")

A typical HTTP response.

##### [Synopsis](boost__beast__http__response.html#beast.ref.boost__beast__http__response.synopsis)

Defined in header `<boost/beast/http/message.hpp>`

```programlisting
template<
    class Body,
    class Fields = fields>
using response = message< false, Body, Fields >;
```

##### [Types](boost__beast__http__response.html#beast.ref.boost__beast__http__response.types)

| Name | Description |
| --- | --- |
| **[allocator\_type](boost__beast__http__message/allocator_type.html "http::message::allocator_type")** | The type of allocator used. |
| **[body\_type](boost__beast__http__message/body_type.html "http::message::body_type")** | The type providing the body traits. |
| **[const\_iterator](boost__beast__http__message/const_iterator.html "http::message::const_iterator")** | A constant iterator to the field sequence. |
| **[fields\_type](boost__beast__http__message/fields_type.html "http::message::fields_type")** | The type representing the fields. |
| **[header\_type](boost__beast__http__message/header_type.html "http::message::header_type")** | The base class used to hold the header portion of the message. |
| **[is\_request](boost__beast__http__message/is_request.html "http::message::is_request")** | Indicates if the header is a request or response. |
| **[iterator](boost__beast__http__message/iterator.html "http::message::iterator")** | A constant iterator to the field sequence. |
| **[key\_compare](boost__beast__http__message/key_compare.html "http::message::key_compare")** | A strictly less predicate for comparing keys, using a case-insensitive comparison. |
| **[writer](boost__beast__http__message/writer.html "http::message::writer")** | The algorithm used to serialize the header. |

##### [Member Functions](boost__beast__http__response.html#beast.ref.boost__beast__http__response.member_functions)

| Name | Description |
| --- | --- |
| **[at](boost__beast__http__message/at.html "http::message::at")** | Returns the value for a field, or throws an exception. |
| **[base](boost__beast__http__message/base.html "http::message::base")** | Returns the header portion of the message. |
| **[begin](boost__beast__http__message/begin.html "http::message::begin")** | Return a const iterator to the beginning of the field sequence. |
| **[body](boost__beast__http__message/body.html "http::message::body")** | Returns the body. |
| **[cbegin](boost__beast__http__message/cbegin.html "http::message::cbegin")** | Return a const iterator to the beginning of the field sequence. |
| **[cend](boost__beast__http__message/cend.html "http::message::cend")** | Return a const iterator to the end of the field sequence. |
| **[chunked](boost__beast__http__message/chunked.html "http::message::chunked")** | Returns `true` if the chunked Transfer-Encoding is specified.  — Set or clear the chunked Transfer-Encoding. |
| **[clear](boost__beast__http__message/clear.html "http::message::clear")** | Remove all fields from the container. |
| **[contains](boost__beast__http__message/contains.html "http::message::contains")** | Returns `true` if there is a field with the specified name. |
| **[content\_length](boost__beast__http__message/content_length.html "http::message::content_length")** | Set or clear the Content-Length field. |
| **[count](boost__beast__http__message/count.html "http::message::count")** | Return the number of fields with the specified name. |
| **[end](boost__beast__http__message/end.html "http::message::end")** | Return a const iterator to the end of the field sequence. |
| **[equal\_range](boost__beast__http__message/equal_range.html "http::message::equal_range")** | Returns a range of iterators to the fields with the specified name.  — Returns a range of iterators to the fields with the specified name. |
| **[erase](boost__beast__http__message/erase.html "http::message::erase")** | Remove a field.  — Remove all fields with the specified name. |
| **[find](boost__beast__http__message/find.html "http::message::find")** | Returns an iterator to the case-insensitive matching field.  — Returns an iterator to the case-insensitive matching field name. |
| **[get\_allocator](boost__beast__http__message/get_allocator.html "http::message::get_allocator")** | Return a copy of the allocator associated with the container. |
| **[has\_content\_length](boost__beast__http__message/has_content_length.html "http::message::has_content_length")** | Returns `true` if the Content-Length field is present. |
| **[insert](boost__beast__http__message/insert.html "http::message::insert")** | Insert a field.  — |
| **[keep\_alive](boost__beast__http__message/keep_alive.html "http::message::keep_alive")** | Returns `true` if the message semantics indicate keep-alive.  — Set the keep-alive message semantic option. |
| **[key\_comp](boost__beast__http__message/key_comp.html "http::message::key_comp")** | Returns a copy of the key comparison function. |
| **[message](boost__beast__http__message/message.html "http::message::message")** | Constructor.  — Construct a message. |
| **[method](boost__beast__http__message/method.html "http::message::method")** | Return the request-method verb. |
| **[method\_string](boost__beast__http__message/method_string.html "http::message::method_string")** | Return the request-method as a string. |
| **[need\_eof](boost__beast__http__message/need_eof.html "http::message::need_eof")** | Returns `true` if the message semantics require an end of file. |
| **[operator=](boost__beast__http__message/operator_eq_.html "http::message::operator=")** | Assignment. |
| **[operator[]](boost__beast__http__message/operator__lb__rb_.html "http::message::operator[]")** | Returns the value for a field, or `""` if it does not exist.  — Returns the value for a case-insensitive matching header, or `""` if it does not exist. |
| **[payload\_size](boost__beast__http__message/payload_size.html "http::message::payload_size")** | Returns the payload size of the body in octets if possible. |
| **[prepare\_payload](boost__beast__http__message/prepare_payload.html "http::message::prepare_payload")** | Prepare the message payload fields for the body. |
| **[reason](boost__beast__http__message/reason.html "http::message::reason")** | Return the response reason-phrase. |
| **[result](boost__beast__http__message/result.html "http::message::result")** | The response status-code result. |
| **[result\_int](boost__beast__http__message/result_int.html "http::message::result_int")** | The response status-code expressed as an integer. |
| **[set](boost__beast__http__message/set.html "http::message::set")** | Set a field value, removing any other instances of that field.  — |
| **[swap](boost__beast__http__message/swap.html "http::message::swap")** | Return a buffer sequence representing the trailers. |
| **[target](boost__beast__http__message/target.html "http::message::target")** | Returns the request-target string. |
| **[version](boost__beast__http__message/version.html "http::message::version")** | Return the HTTP-version. |

##### [Protected Member Functions](boost__beast__http__response.html#beast.ref.boost__beast__http__response.protected_member_functions)

| Name | Description |
| --- | --- |
| **[get\_chunked\_impl](boost__beast__http__message/get_chunked_impl.html "http::message::get_chunked_impl")** | Returns the chunked Transfer-Encoding setting. |
| **[get\_keep\_alive\_impl](boost__beast__http__message/get_keep_alive_impl.html "http::message::get_keep_alive_impl")** | Returns the keep-alive setting. |
| **[get\_method\_impl](boost__beast__http__message/get_method_impl.html "http::message::get_method_impl")** | Returns the request-method string. |
| **[get\_reason\_impl](boost__beast__http__message/get_reason_impl.html "http::message::get_reason_impl")** | Returns the response reason-phrase string. |
| **[get\_target\_impl](boost__beast__http__message/get_target_impl.html "http::message::get_target_impl")** | Returns the request-target string. |
| **[has\_content\_length\_impl](boost__beast__http__message/has_content_length_impl.html "http::message::has_content_length_impl")** | Returns `true` if the Content-Length field is present. |
| **[set\_chunked\_impl](boost__beast__http__message/set_chunked_impl.html "http::message::set_chunked_impl")** | Adjusts the chunked Transfer-Encoding value. |
| **[set\_content\_length\_impl](boost__beast__http__message/set_content_length_impl.html "http::message::set_content_length_impl")** | Sets or clears the Content-Length field. |
| **[set\_keep\_alive\_impl](boost__beast__http__message/set_keep_alive_impl.html "http::message::set_keep_alive_impl")** | Adjusts the Connection field. |
| **[set\_method\_impl](boost__beast__http__message/set_method_impl.html "http::message::set_method_impl")** | Set or clear the method string. |
| **[set\_reason\_impl](boost__beast__http__message/set_reason_impl.html "http::message::set_reason_impl")** | Set or clear the reason string. |
| **[set\_target\_impl](boost__beast__http__message/set_target_impl.html "http::message::set_target_impl")** | Set or clear the target string. |

##### [Static Members](boost__beast__http__response.html#beast.ref.boost__beast__http__response.static_members)

| Name | Description |
| --- | --- |
| **[max\_name\_size](boost__beast__http__message/max_name_size.html "http::message::max_name_size")** | Maximum field name size. |
| **[max\_value\_size](boost__beast__http__message/max_value_size.html "http::message::max_value_size")** | Maximum field value size. |

This container is derived from the `Fields`
template type. To understand all of the members of this class it is necessary
to view the declaration for the `Fields`
type. When using the default fields container, those declarations are in
[`fields`](boost__beast__http__fields.html "http::fields").

A message can be a request or response, depending on the `isRequest`
template argument value. Requests and responses have different types; functions
may be overloaded based on the type if desired.

The `Body` template argument
type determines the model used to read or write the content body of the message.

Newly constructed messages objects have version set to HTTP/1.1. Newly constructed
response objects also have result code set to [`status::ok`](boost__beast__http__status.html "http::status").

##### [Template Parameters](boost__beast__http__response.html#beast.ref.boost__beast__http__response.template_parameters)

| Type | Description |
| --- | --- |
| `isRequest` | `true` if this represents a request, or `false` if this represents a response. Some class data members are conditionally present depending on this value. |
| `Body` | A type meeting the requirements of Body. |
| `Fields` | The type of container used to hold the field value pairs. |