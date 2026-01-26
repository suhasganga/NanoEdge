#### [http::header](boost__beast__http__header.html "http::header")

A container for an HTTP request or response header.

##### [Synopsis](boost__beast__http__header.html#beast.ref.boost__beast__http__header.synopsis)

Defined in header `<boost/beast/http/message.hpp>`

```programlisting
template<
    bool isRequest,
    class Fields = fields>
class header :
    public http::basic_fields< std::allocator< char > >
```

##### [Types](boost__beast__http__header.html#beast.ref.boost__beast__http__header.types)

| Name | Description |
| --- | --- |
| **[allocator\_type](boost__beast__http__header/allocator_type.html "http::header::allocator_type")** | The type of allocator used. |
| **[const\_iterator](boost__beast__http__header/const_iterator.html "http::header::const_iterator")** | A constant iterator to the field sequence. |
| **[fields\_type](boost__beast__http__header/fields_type.html "http::header::fields_type")** | The type representing the fields. |
| **[is\_request](boost__beast__http__header/is_request.html "http::header::is_request")** | Indicates if the header is a request or response. |
| **[iterator](boost__beast__http__header/iterator.html "http::header::iterator")** | A constant iterator to the field sequence. |
| **[key\_compare](boost__beast__http__header/key_compare.html "http::header::key_compare")** | A strictly less predicate for comparing keys, using a case-insensitive comparison. |
| **[writer](boost__beast__http__header/writer.html "http::header::writer")** | The algorithm used to serialize the header. |

##### [Member Functions](boost__beast__http__header.html#beast.ref.boost__beast__http__header.member_functions)

| Name | Description |
| --- | --- |
| **[at](boost__beast__http__header/at.html "http::header::at")** | Returns the value for a field, or throws an exception. |
| **[begin](boost__beast__http__header/begin.html "http::header::begin")** | Return a const iterator to the beginning of the field sequence. |
| **[cbegin](boost__beast__http__header/cbegin.html "http::header::cbegin")** | Return a const iterator to the beginning of the field sequence. |
| **[cend](boost__beast__http__header/cend.html "http::header::cend")** | Return a const iterator to the end of the field sequence. |
| **[clear](boost__beast__http__header/clear.html "http::header::clear")** | Remove all fields from the container. |
| **[contains](boost__beast__http__header/contains.html "http::header::contains")** | Returns `true` if there is a field with the specified name. |
| **[count](boost__beast__http__header/count.html "http::header::count")** | Return the number of fields with the specified name. |
| **[end](boost__beast__http__header/end.html "http::header::end")** | Return a const iterator to the end of the field sequence. |
| **[equal\_range](boost__beast__http__header/equal_range.html "http::header::equal_range")** | Returns a range of iterators to the fields with the specified name.  — Returns a range of iterators to the fields with the specified name. |
| **[erase](boost__beast__http__header/erase.html "http::header::erase")** | Remove a field.  — Remove all fields with the specified name. |
| **[find](boost__beast__http__header/find.html "http::header::find")** | Returns an iterator to the case-insensitive matching field.  — Returns an iterator to the case-insensitive matching field name. |
| **[get\_allocator](boost__beast__http__header/get_allocator.html "http::header::get_allocator")** | Return a copy of the allocator associated with the container. |
| **[header](boost__beast__http__header/header.html "http::header::header") [constructor]** | Constructor. |
| **[insert](boost__beast__http__header/insert.html "http::header::insert")** | Insert a field.  — |
| **[key\_comp](boost__beast__http__header/key_comp.html "http::header::key_comp")** | Returns a copy of the key comparison function. |
| **[method](boost__beast__http__header/method.html "http::header::method")** | Return the request-method verb.  — Set the request-method. |
| **[method\_string](boost__beast__http__header/method_string.html "http::header::method_string")** | Return the request-method as a string.  — Set the request-method. |
| **[operator=](boost__beast__http__header/operator_eq_.html "http::header::operator=")** | Assignment. |
| **[operator[]](boost__beast__http__header/operator__lb__rb_.html "http::header::operator[]")** | Returns the value for a field, or `""` if it does not exist.  — Returns the value for a case-insensitive matching header, or `""` if it does not exist. |
| **[reason](boost__beast__http__header/reason.html "http::header::reason")** | Return the response reason-phrase.  — Set the response reason-phrase (deprecated) |
| **[result](boost__beast__http__header/result.html "http::header::result")** | The response status-code result.  — Set the response status-code.  — Set the response status-code as an integer. |
| **[result\_int](boost__beast__http__header/result_int.html "http::header::result_int")** | The response status-code expressed as an integer. |
| **[set](boost__beast__http__header/set.html "http::header::set")** | Set a field value, removing any other instances of that field.  — |
| **[swap](boost__beast__http__header/swap.html "http::header::swap")** | Return a buffer sequence representing the trailers. |
| **[target](boost__beast__http__header/target.html "http::header::target")** | Returns the request-target string.  — Set the request-target string. |
| **[version](boost__beast__http__header/version.html "http::header::version")** | Return the HTTP-version.  — Set the HTTP-version. |

##### [Protected Member Functions](boost__beast__http__header.html#beast.ref.boost__beast__http__header.protected_member_functions)

| Name | Description |
| --- | --- |
| **[get\_chunked\_impl](boost__beast__http__header/get_chunked_impl.html "http::header::get_chunked_impl")** | Returns the chunked Transfer-Encoding setting. |
| **[get\_keep\_alive\_impl](boost__beast__http__header/get_keep_alive_impl.html "http::header::get_keep_alive_impl")** | Returns the keep-alive setting. |
| **[get\_method\_impl](boost__beast__http__header/get_method_impl.html "http::header::get_method_impl")** | Returns the request-method string. |
| **[get\_reason\_impl](boost__beast__http__header/get_reason_impl.html "http::header::get_reason_impl")** | Returns the response reason-phrase string. |
| **[get\_target\_impl](boost__beast__http__header/get_target_impl.html "http::header::get_target_impl")** | Returns the request-target string. |
| **[has\_content\_length\_impl](boost__beast__http__header/has_content_length_impl.html "http::header::has_content_length_impl")** | Returns `true` if the Content-Length field is present. |
| **[set\_chunked\_impl](boost__beast__http__header/set_chunked_impl.html "http::header::set_chunked_impl")** | Adjusts the chunked Transfer-Encoding value. |
| **[set\_content\_length\_impl](boost__beast__http__header/set_content_length_impl.html "http::header::set_content_length_impl")** | Sets or clears the Content-Length field. |
| **[set\_keep\_alive\_impl](boost__beast__http__header/set_keep_alive_impl.html "http::header::set_keep_alive_impl")** | Adjusts the Connection field. |
| **[set\_method\_impl](boost__beast__http__header/set_method_impl.html "http::header::set_method_impl")** | Set or clear the method string. |
| **[set\_reason\_impl](boost__beast__http__header/set_reason_impl.html "http::header::set_reason_impl")** | Set or clear the reason string. |
| **[set\_target\_impl](boost__beast__http__header/set_target_impl.html "http::header::set_target_impl")** | Set or clear the target string. |

##### [Static Members](boost__beast__http__header.html#beast.ref.boost__beast__http__header.static_members)

| Name | Description |
| --- | --- |
| **[max\_name\_size](boost__beast__http__header/max_name_size.html "http::header::max_name_size")** | Maximum field name size. |
| **[max\_value\_size](boost__beast__http__header/max_value_size.html "http::header::max_value_size")** | Maximum field value size. |

##### [Description](boost__beast__http__header.html#beast.ref.boost__beast__http__header.description)

This container is derived from the `Fields`
template type. To understand all of the members of this class it is necessary
to view the declaration for the `Fields`
type. When using the default fields container, those declarations are in
[`fields`](boost__beast__http__fields.html "http::fields").

Newly constructed header objects have version set to HTTP/1.1. Newly constructed
response objects also have result code set to [`status::ok`](boost__beast__http__status.html "http::status").

A `header` includes the start-line
and header-fields.