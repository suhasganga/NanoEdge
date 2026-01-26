#### [http::fields](boost__beast__http__fields.html "http::fields")

A typical HTTP header fields container.

##### [Synopsis](boost__beast__http__fields.html#beast.ref.boost__beast__http__fields.synopsis)

Defined in header `<boost/beast/http/fields.hpp>`

```programlisting
using fields = basic_fields< std::allocator< char > >;
```

##### [Types](boost__beast__http__fields.html#beast.ref.boost__beast__http__fields.types)

| Name | Description |
| --- | --- |
| **[allocator\_type](boost__beast__http__basic_fields/allocator_type.html "http::basic_fields::allocator_type")** | The type of allocator used. |
| **[const\_iterator](boost__beast__http__basic_fields/const_iterator.html "http::basic_fields::const_iterator")** | A constant iterator to the field sequence. |
| **[iterator](boost__beast__http__basic_fields/iterator.html "http::basic_fields::iterator")** | A constant iterator to the field sequence. |
| **[key\_compare](boost__beast__http__basic_fields/key_compare.html "http::basic_fields::key_compare")** | A strictly less predicate for comparing keys, using a case-insensitive comparison. |
| **[value\_type](boost__beast__http__basic_fields__value_type.html "http::basic_fields::value_type")** | The type of element used to represent a field. |
| **[writer](boost__beast__http__basic_fields/writer.html "http::basic_fields::writer")** | The algorithm used to serialize the header. |

##### [Member Functions](boost__beast__http__fields.html#beast.ref.boost__beast__http__fields.member_functions)

| Name | Description |
| --- | --- |
| **[at](boost__beast__http__basic_fields/at.html "http::basic_fields::at")** | Returns the value for a field, or throws an exception. |
| **[basic\_fields](boost__beast__http__basic_fields/basic_fields.html "http::basic_fields::basic_fields")** | Constructor.  — Move constructor.  — Copy constructor. |
| **[begin](boost__beast__http__basic_fields/begin.html "http::basic_fields::begin")** | Return a const iterator to the beginning of the field sequence. |
| **[cbegin](boost__beast__http__basic_fields/cbegin.html "http::basic_fields::cbegin")** | Return a const iterator to the beginning of the field sequence. |
| **[cend](boost__beast__http__basic_fields/cend.html "http::basic_fields::cend")** | Return a const iterator to the end of the field sequence. |
| **[clear](boost__beast__http__basic_fields/clear.html "http::basic_fields::clear")** | Remove all fields from the container. |
| **[contains](boost__beast__http__basic_fields/contains.html "http::basic_fields::contains")** | Returns `true` if there is a field with the specified name. |
| **[count](boost__beast__http__basic_fields/count.html "http::basic_fields::count")** | Return the number of fields with the specified name. |
| **[end](boost__beast__http__basic_fields/end.html "http::basic_fields::end")** | Return a const iterator to the end of the field sequence. |
| **[equal\_range](boost__beast__http__basic_fields/equal_range.html "http::basic_fields::equal_range")** | Returns a range of iterators to the fields with the specified name.  — Returns a range of iterators to the fields with the specified name. |
| **[erase](boost__beast__http__basic_fields/erase.html "http::basic_fields::erase")** | Remove a field.  — Remove all fields with the specified name. |
| **[find](boost__beast__http__basic_fields/find.html "http::basic_fields::find")** | Returns an iterator to the case-insensitive matching field.  — Returns an iterator to the case-insensitive matching field name. |
| **[get\_allocator](boost__beast__http__basic_fields/get_allocator.html "http::basic_fields::get_allocator")** | Return a copy of the allocator associated with the container. |
| **[insert](boost__beast__http__basic_fields/insert.html "http::basic_fields::insert")** | Insert a field.  — |
| **[key\_comp](boost__beast__http__basic_fields/key_comp.html "http::basic_fields::key_comp")** | Returns a copy of the key comparison function. |
| **[operator=](boost__beast__http__basic_fields/operator_eq_.html "http::basic_fields::operator=")** | Move assignment.  — Copy assignment. |
| **[operator[]](boost__beast__http__basic_fields/operator__lb__rb_.html "http::basic_fields::operator[]")** | Returns the value for a field, or `""` if it does not exist.  — Returns the value for a case-insensitive matching header, or `""` if it does not exist. |
| **[set](boost__beast__http__basic_fields/set.html "http::basic_fields::set")** | Set a field value, removing any other instances of that field.  — |
| **[swap](boost__beast__http__basic_fields/swap.html "http::basic_fields::swap")** | Return a buffer sequence representing the trailers. |
| **[~basic\_fields](boost__beast__http__basic_fields/_dtor_basic_fields.html "http::basic_fields::~basic_fields") [destructor]** | Destructor. |

##### [Protected Member Functions](boost__beast__http__fields.html#beast.ref.boost__beast__http__fields.protected_member_functions)

| Name | Description |
| --- | --- |
| **[get\_chunked\_impl](boost__beast__http__basic_fields/get_chunked_impl.html "http::basic_fields::get_chunked_impl")** | Returns the chunked Transfer-Encoding setting. |
| **[get\_keep\_alive\_impl](boost__beast__http__basic_fields/get_keep_alive_impl.html "http::basic_fields::get_keep_alive_impl")** | Returns the keep-alive setting. |
| **[get\_method\_impl](boost__beast__http__basic_fields/get_method_impl.html "http::basic_fields::get_method_impl")** | Returns the request-method string. |
| **[get\_reason\_impl](boost__beast__http__basic_fields/get_reason_impl.html "http::basic_fields::get_reason_impl")** | Returns the response reason-phrase string. |
| **[get\_target\_impl](boost__beast__http__basic_fields/get_target_impl.html "http::basic_fields::get_target_impl")** | Returns the request-target string. |
| **[has\_content\_length\_impl](boost__beast__http__basic_fields/has_content_length_impl.html "http::basic_fields::has_content_length_impl")** | Returns `true` if the Content-Length field is present. |
| **[set\_chunked\_impl](boost__beast__http__basic_fields/set_chunked_impl.html "http::basic_fields::set_chunked_impl")** | Adjusts the chunked Transfer-Encoding value. |
| **[set\_content\_length\_impl](boost__beast__http__basic_fields/set_content_length_impl.html "http::basic_fields::set_content_length_impl")** | Sets or clears the Content-Length field. |
| **[set\_keep\_alive\_impl](boost__beast__http__basic_fields/set_keep_alive_impl.html "http::basic_fields::set_keep_alive_impl")** | Adjusts the Connection field. |
| **[set\_method\_impl](boost__beast__http__basic_fields/set_method_impl.html "http::basic_fields::set_method_impl")** | Set or clear the method string. |
| **[set\_reason\_impl](boost__beast__http__basic_fields/set_reason_impl.html "http::basic_fields::set_reason_impl")** | Set or clear the reason string. |
| **[set\_target\_impl](boost__beast__http__basic_fields/set_target_impl.html "http::basic_fields::set_target_impl")** | Set or clear the target string. |

##### [Static Members](boost__beast__http__fields.html#beast.ref.boost__beast__http__fields.static_members)

| Name | Description |
| --- | --- |
| **[max\_name\_size](boost__beast__http__basic_fields/max_name_size.html "http::basic_fields::max_name_size")** | Maximum field name size. |
| **[max\_value\_size](boost__beast__http__basic_fields/max_value_size.html "http::basic_fields::max_value_size")** | Maximum field value size. |

##### [Friends](boost__beast__http__fields.html#beast.ref.boost__beast__http__fields.friends)

| Name | Description |
| --- | --- |
| **[swap](boost__beast__http__basic_fields/swap.html "http::basic_fields::swap")** | Swap two field containers. |

This container is designed to store the field value pairs that make up the
fields and trailers in an HTTP message. Objects of this type are iterable,
with each element holding the field name and field value.

Field names are stored as-is, but comparisons are case-insensitive. The container
behaves as a `std::multiset`; there will be a separate value
for each occurrence of the same field name. When the container is iterated
the fields are presented in the order of insertion, with fields having the
same name following each other consecutively.

Meets the requirements of *Fields*

##### [Template Parameters](boost__beast__http__fields.html#beast.ref.boost__beast__http__fields.template_parameters)

| Type | Description |
| --- | --- |
| `Allocator` | The allocator to use. |