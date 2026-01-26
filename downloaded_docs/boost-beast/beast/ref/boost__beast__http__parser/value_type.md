##### [http::parser::value\_type](value_type.html "http::parser::value_type")

The type of message returned by the parser.

###### [Synopsis](value_type.html#beast.ref.boost__beast__http__parser.value_type.synopsis)

```programlisting
using value_type = message< isRequest, Body, basic_fields< Allocator > >;
```

###### [Types](value_type.html#beast.ref.boost__beast__http__parser.value_type.types)

| Name | Description |
| --- | --- |
| **[allocator\_type](../boost__beast__http__message/allocator_type.html "http::message::allocator_type")** | The type of allocator used. |
| **[body\_type](../boost__beast__http__message/body_type.html "http::message::body_type")** | The type providing the body traits. |
| **[const\_iterator](../boost__beast__http__message/const_iterator.html "http::message::const_iterator")** | A constant iterator to the field sequence. |
| **[fields\_type](../boost__beast__http__message/fields_type.html "http::message::fields_type")** | The type representing the fields. |
| **[header\_type](../boost__beast__http__message/header_type.html "http::message::header_type")** | The base class used to hold the header portion of the message. |
| **[is\_request](../boost__beast__http__message/is_request.html "http::message::is_request")** | Indicates if the header is a request or response. |
| **[iterator](../boost__beast__http__message/iterator.html "http::message::iterator")** | A constant iterator to the field sequence. |
| **[key\_compare](../boost__beast__http__message/key_compare.html "http::message::key_compare")** | A strictly less predicate for comparing keys, using a case-insensitive comparison. |
| **[writer](../boost__beast__http__message/writer.html "http::message::writer")** | The algorithm used to serialize the header. |

###### [Member Functions](value_type.html#beast.ref.boost__beast__http__parser.value_type.member_functions)

| Name | Description |
| --- | --- |
| **[at](../boost__beast__http__message/at.html "http::message::at")** | Returns the value for a field, or throws an exception. |
| **[base](../boost__beast__http__message/base.html "http::message::base")** | Returns the header portion of the message. |
| **[begin](../boost__beast__http__message/begin.html "http::message::begin")** | Return a const iterator to the beginning of the field sequence. |
| **[body](../boost__beast__http__message/body.html "http::message::body")** | Returns the body. |
| **[cbegin](../boost__beast__http__message/cbegin.html "http::message::cbegin")** | Return a const iterator to the beginning of the field sequence. |
| **[cend](../boost__beast__http__message/cend.html "http::message::cend")** | Return a const iterator to the end of the field sequence. |
| **[chunked](../boost__beast__http__message/chunked.html "http::message::chunked")** | Returns `true` if the chunked Transfer-Encoding is specified.  — Set or clear the chunked Transfer-Encoding. |
| **[clear](../boost__beast__http__message/clear.html "http::message::clear")** | Remove all fields from the container. |
| **[contains](../boost__beast__http__message/contains.html "http::message::contains")** | Returns `true` if there is a field with the specified name. |
| **[content\_length](../boost__beast__http__message/content_length.html "http::message::content_length")** | Set or clear the Content-Length field. |
| **[count](../boost__beast__http__message/count.html "http::message::count")** | Return the number of fields with the specified name. |
| **[end](../boost__beast__http__message/end.html "http::message::end")** | Return a const iterator to the end of the field sequence. |
| **[equal\_range](../boost__beast__http__message/equal_range.html "http::message::equal_range")** | Returns a range of iterators to the fields with the specified name.  — Returns a range of iterators to the fields with the specified name. |
| **[erase](../boost__beast__http__message/erase.html "http::message::erase")** | Remove a field.  — Remove all fields with the specified name. |
| **[find](../boost__beast__http__message/find.html "http::message::find")** | Returns an iterator to the case-insensitive matching field.   — Returns an iterator to the case-insensitive matching field name. |
| **[get\_allocator](../boost__beast__http__message/get_allocator.html "http::message::get_allocator")** | Return a copy of the allocator associated with the container. |
| **[has\_content\_length](../boost__beast__http__message/has_content_length.html "http::message::has_content_length")** | Returns `true` if the Content-Length field is present. |
| **[insert](../boost__beast__http__message/insert.html "http::message::insert")** | Insert a field.  — |
| **[keep\_alive](../boost__beast__http__message/keep_alive.html "http::message::keep_alive")** | Returns `true` if the message semantics indicate keep-alive.  — Set the keep-alive message semantic option. |
| **[key\_comp](../boost__beast__http__message/key_comp.html "http::message::key_comp")** | Returns a copy of the key comparison function. |
| **[message](../boost__beast__http__message/message.html "http::message::message")** | Constructor.  — Construct a message. |
| **[method](../boost__beast__http__message/method.html "http::message::method")** | Return the request-method verb. |
| **[method\_string](../boost__beast__http__message/method_string.html "http::message::method_string")** | Return the request-method as a string. |
| **[need\_eof](../boost__beast__http__message/need_eof.html "http::message::need_eof")** | Returns `true` if the message semantics require an end of file. |
| **[operator=](../boost__beast__http__message/operator_eq_.html "http::message::operator=")** | Assignment. |
| **[operator[]](../boost__beast__http__message/operator__lb__rb_.html "http::message::operator[]")** | Returns the value for a field, or `""` if it does not exist.  — Returns the value for a case-insensitive matching header, or `""` if it does not exist. |
| **[payload\_size](../boost__beast__http__message/payload_size.html "http::message::payload_size")** | Returns the payload size of the body in octets if possible. |
| **[prepare\_payload](../boost__beast__http__message/prepare_payload.html "http::message::prepare_payload")** | Prepare the message payload fields for the body. |
| **[reason](../boost__beast__http__message/reason.html "http::message::reason")** | Return the response reason-phrase. |
| **[result](../boost__beast__http__message/result.html "http::message::result")** | The response status-code result. |
| **[result\_int](../boost__beast__http__message/result_int.html "http::message::result_int")** | The response status-code expressed as an integer. |
| **[set](../boost__beast__http__message/set.html "http::message::set")** | Set a field value, removing any other instances of that field.  — |
| **[swap](../boost__beast__http__message/swap.html "http::message::swap")** | Return a buffer sequence representing the trailers. |
| **[target](../boost__beast__http__message/target.html "http::message::target")** | Returns the request-target string. |
| **[version](../boost__beast__http__message/version.html "http::message::version")** | Return the HTTP-version. |

###### [Protected Member Functions](value_type.html#beast.ref.boost__beast__http__parser.value_type.protected_member_functions)

| Name | Description |
| --- | --- |
| **[get\_chunked\_impl](../boost__beast__http__message/get_chunked_impl.html "http::message::get_chunked_impl")** | Returns the chunked Transfer-Encoding setting. |
| **[get\_keep\_alive\_impl](../boost__beast__http__message/get_keep_alive_impl.html "http::message::get_keep_alive_impl")** | Returns the keep-alive setting. |
| **[get\_method\_impl](../boost__beast__http__message/get_method_impl.html "http::message::get_method_impl")** | Returns the request-method string. |
| **[get\_reason\_impl](../boost__beast__http__message/get_reason_impl.html "http::message::get_reason_impl")** | Returns the response reason-phrase string. |
| **[get\_target\_impl](../boost__beast__http__message/get_target_impl.html "http::message::get_target_impl")** | Returns the request-target string. |
| **[has\_content\_length\_impl](../boost__beast__http__message/has_content_length_impl.html "http::message::has_content_length_impl")** | Returns `true` if the Content-Length field is present. |
| **[set\_chunked\_impl](../boost__beast__http__message/set_chunked_impl.html "http::message::set_chunked_impl")** | Adjusts the chunked Transfer-Encoding value. |
| **[set\_content\_length\_impl](../boost__beast__http__message/set_content_length_impl.html "http::message::set_content_length_impl")** | Sets or clears the Content-Length field. |
| **[set\_keep\_alive\_impl](../boost__beast__http__message/set_keep_alive_impl.html "http::message::set_keep_alive_impl")** | Adjusts the Connection field. |
| **[set\_method\_impl](../boost__beast__http__message/set_method_impl.html "http::message::set_method_impl")** | Set or clear the method string. |
| **[set\_reason\_impl](../boost__beast__http__message/set_reason_impl.html "http::message::set_reason_impl")** | Set or clear the reason string. |
| **[set\_target\_impl](../boost__beast__http__message/set_target_impl.html "http::message::set_target_impl")** | Set or clear the target string. |

###### [Static Members](value_type.html#beast.ref.boost__beast__http__parser.value_type.static_members)

| Name | Description |
| --- | --- |
| **[max\_name\_size](../boost__beast__http__message/max_name_size.html "http::message::max_name_size")** | Maximum field name size. |
| **[max\_value\_size](../boost__beast__http__message/max_value_size.html "http::message::max_value_size")** | Maximum field value size. |

This container is derived from the `Fields`
template type. To understand all of the members of this class it is necessary
to view the declaration for the `Fields`
type. When using the default fields container, those declarations are in
[`fields`](../boost__beast__http__fields.html "http::fields").

A message can be a request or response, depending on the `isRequest` template argument value. Requests
and responses have different types; functions may be overloaded based on
the type if desired.

The `Body` template argument
type determines the model used to read or write the content body of the
message.

Newly constructed messages objects have version set to HTTP/1.1. Newly
constructed response objects also have result code set to [`status::ok`](../boost__beast__http__status.html "http::status").

###### [Template Parameters](value_type.html#beast.ref.boost__beast__http__parser.value_type.template_parameters)

| Type | Description |
| --- | --- |
| `isRequest` | `true` if this represents a request, or `false` if this represents a response. Some class data members are conditionally present depending on this value. |
| `Body` | A type meeting the requirements of Body. |
| `Fields` | The type of container used to hold the field value pairs. |

###### [Types](value_type.html#beast.ref.boost__beast__http__parser.value_type.types0)

| Name | Description |
| --- | --- |
| **[allocator\_type](../boost__beast__http__basic_fields/allocator_type.html "http::basic_fields::allocator_type")** | The type of allocator used. |
| **[const\_iterator](../boost__beast__http__basic_fields/const_iterator.html "http::basic_fields::const_iterator")** | A constant iterator to the field sequence. |
| **[iterator](../boost__beast__http__basic_fields/iterator.html "http::basic_fields::iterator")** | A constant iterator to the field sequence. |
| **[key\_compare](../boost__beast__http__basic_fields/key_compare.html "http::basic_fields::key_compare")** | A strictly less predicate for comparing keys, using a case-insensitive comparison. |
| **[value\_type](../boost__beast__http__basic_fields__value_type.html "http::basic_fields::value_type")** | The type of element used to represent a field. |
| **[writer](../boost__beast__http__basic_fields/writer.html "http::basic_fields::writer")** | The algorithm used to serialize the header. |

###### [Member Functions](value_type.html#beast.ref.boost__beast__http__parser.value_type.member_functions0)

| Name | Description |
| --- | --- |
| **[at](../boost__beast__http__basic_fields/at.html "http::basic_fields::at")** | Returns the value for a field, or throws an exception. |
| **[basic\_fields](../boost__beast__http__basic_fields/basic_fields.html "http::basic_fields::basic_fields")** | Constructor.  — Move constructor.  — Copy constructor. |
| **[begin](../boost__beast__http__basic_fields/begin.html "http::basic_fields::begin")** | Return a const iterator to the beginning of the field sequence. |
| **[cbegin](../boost__beast__http__basic_fields/cbegin.html "http::basic_fields::cbegin")** | Return a const iterator to the beginning of the field sequence. |
| **[cend](../boost__beast__http__basic_fields/cend.html "http::basic_fields::cend")** | Return a const iterator to the end of the field sequence. |
| **[clear](../boost__beast__http__basic_fields/clear.html "http::basic_fields::clear")** | Remove all fields from the container. |
| **[contains](../boost__beast__http__basic_fields/contains.html "http::basic_fields::contains")** | Returns `true` if there is a field with the specified name. |
| **[count](../boost__beast__http__basic_fields/count.html "http::basic_fields::count")** | Return the number of fields with the specified name. |
| **[end](../boost__beast__http__basic_fields/end.html "http::basic_fields::end")** | Return a const iterator to the end of the field sequence. |
| **[equal\_range](../boost__beast__http__basic_fields/equal_range.html "http::basic_fields::equal_range")** | Returns a range of iterators to the fields with the specified name.  — Returns a range of iterators to the fields with the specified name. |
| **[erase](../boost__beast__http__basic_fields/erase.html "http::basic_fields::erase")** | Remove a field.  — Remove all fields with the specified name. |
| **[find](../boost__beast__http__basic_fields/find.html "http::basic_fields::find")** | Returns an iterator to the case-insensitive matching field.   — Returns an iterator to the case-insensitive matching field name. |
| **[get\_allocator](../boost__beast__http__basic_fields/get_allocator.html "http::basic_fields::get_allocator")** | Return a copy of the allocator associated with the container. |
| **[insert](../boost__beast__http__basic_fields/insert.html "http::basic_fields::insert")** | Insert a field.  — |
| **[key\_comp](../boost__beast__http__basic_fields/key_comp.html "http::basic_fields::key_comp")** | Returns a copy of the key comparison function. |
| **[operator=](../boost__beast__http__basic_fields/operator_eq_.html "http::basic_fields::operator=")** | Move assignment.  — Copy assignment. |
| **[operator[]](../boost__beast__http__basic_fields/operator__lb__rb_.html "http::basic_fields::operator[]")** | Returns the value for a field, or `""` if it does not exist.  — Returns the value for a case-insensitive matching header, or `""` if it does not exist. |
| **[set](../boost__beast__http__basic_fields/set.html "http::basic_fields::set")** | Set a field value, removing any other instances of that field.  — |
| **[swap](../boost__beast__http__basic_fields/swap.html "http::basic_fields::swap")** | Return a buffer sequence representing the trailers. |
| **[~basic\_fields](../boost__beast__http__basic_fields/_dtor_basic_fields.html "http::basic_fields::~basic_fields") [destructor]** | Destructor. |

###### [Protected Member Functions](value_type.html#beast.ref.boost__beast__http__parser.value_type.protected_member_functions0)

| Name | Description |
| --- | --- |
| **[get\_chunked\_impl](../boost__beast__http__basic_fields/get_chunked_impl.html "http::basic_fields::get_chunked_impl")** | Returns the chunked Transfer-Encoding setting. |
| **[get\_keep\_alive\_impl](../boost__beast__http__basic_fields/get_keep_alive_impl.html "http::basic_fields::get_keep_alive_impl")** | Returns the keep-alive setting. |
| **[get\_method\_impl](../boost__beast__http__basic_fields/get_method_impl.html "http::basic_fields::get_method_impl")** | Returns the request-method string. |
| **[get\_reason\_impl](../boost__beast__http__basic_fields/get_reason_impl.html "http::basic_fields::get_reason_impl")** | Returns the response reason-phrase string. |
| **[get\_target\_impl](../boost__beast__http__basic_fields/get_target_impl.html "http::basic_fields::get_target_impl")** | Returns the request-target string. |
| **[has\_content\_length\_impl](../boost__beast__http__basic_fields/has_content_length_impl.html "http::basic_fields::has_content_length_impl")** | Returns `true` if the Content-Length field is present. |
| **[set\_chunked\_impl](../boost__beast__http__basic_fields/set_chunked_impl.html "http::basic_fields::set_chunked_impl")** | Adjusts the chunked Transfer-Encoding value. |
| **[set\_content\_length\_impl](../boost__beast__http__basic_fields/set_content_length_impl.html "http::basic_fields::set_content_length_impl")** | Sets or clears the Content-Length field. |
| **[set\_keep\_alive\_impl](../boost__beast__http__basic_fields/set_keep_alive_impl.html "http::basic_fields::set_keep_alive_impl")** | Adjusts the Connection field. |
| **[set\_method\_impl](../boost__beast__http__basic_fields/set_method_impl.html "http::basic_fields::set_method_impl")** | Set or clear the method string. |
| **[set\_reason\_impl](../boost__beast__http__basic_fields/set_reason_impl.html "http::basic_fields::set_reason_impl")** | Set or clear the reason string. |
| **[set\_target\_impl](../boost__beast__http__basic_fields/set_target_impl.html "http::basic_fields::set_target_impl")** | Set or clear the target string. |

###### [Static Members](value_type.html#beast.ref.boost__beast__http__parser.value_type.static_members0)

| Name | Description |
| --- | --- |
| **[max\_name\_size](../boost__beast__http__basic_fields/max_name_size.html "http::basic_fields::max_name_size")** | Maximum field name size. |
| **[max\_value\_size](../boost__beast__http__basic_fields/max_value_size.html "http::basic_fields::max_value_size")** | Maximum field value size. |

###### [Friends](value_type.html#beast.ref.boost__beast__http__parser.value_type.friends)

| Name | Description |
| --- | --- |
| **[swap](../boost__beast__http__basic_fields/swap.html "http::basic_fields::swap")** | Swap two field containers. |

This container is designed to store the field value pairs that make up
the fields and trailers in an HTTP message. Objects of this type are iterable,
with each element holding the field name and field value.

Field names are stored as-is, but comparisons are case-insensitive. The
container behaves as a `std::multiset`;
there will be a separate value for each occurrence of the same field name.
When the container is iterated the fields are presented in the order of
insertion, with fields having the same name following each other consecutively.

Meets the requirements of *Fields*

###### [Template Parameters](value_type.html#beast.ref.boost__beast__http__parser.value_type.template_parameters0)

| Type | Description |
| --- | --- |
| `Allocator` | The allocator to use. |