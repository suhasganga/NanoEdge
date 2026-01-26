##### [http::basic\_fields::writer](writer.html "http::basic_fields::writer")

The algorithm used to serialize the header.

###### [Synopsis](writer.html#beast.ref.boost__beast__http__basic_fields.writer.synopsis)

```programlisting
using writer = { bool operator()( string_view lhs, value_type const &rhs) const noexcept { if(lhs.size()< rhs.name_string().size()) return true; if(lhs.size() > rhs.name_string().size()) return false; return iless::operator()(lhs, rhs.name_string()); } bool operator()( value_type const &lhs, string_view rhs) const noexcept { if(lhs.name_string().size()< rhs.size()) return true; if(lhs.name_string().size() > rhs.size()) return false; return iless::operator()(lhs.name_string(), rhs); } bool operator()( value_type const &lhs, value_type const &rhs) const noexcept { if(lhs.name_string().size()< rhs.name_string().size()) return true; if(lhs.name_string().size() > rhs.name_string().size()) return false; return iless::operator()(lhs.name_string(), rhs.name_string()); } } implementation-defined;
```

###### [Member Functions](writer.html#beast.ref.boost__beast__http__basic_fields.writer.member_functions)

| Name | Description |
| --- | --- |
| **[name](../boost__beast__http__basic_fields__value_type/name.html "http::basic_fields::value_type::name")** | Returns the field enum, which can be [`boost::beast::http::field::unknown`](../boost__beast__http__field.html "http::field"). |
| **[name\_string](../boost__beast__http__basic_fields__value_type/name_string.html "http::basic_fields::value_type::name_string")** | Returns the field name as a string. |
| **[operator=](../boost__beast__http__basic_fields__value_type/operator_eq_.html "http::basic_fields::value_type::operator=")** | Assignment (deleted) |
| **[value](../boost__beast__http__basic_fields__value_type/value.html "http::basic_fields::value_type::value")** | Returns the value of the field. |
| **[value\_type](../boost__beast__http__basic_fields__value_type/value_type.html "http::basic_fields::value_type::value_type")** | Constructor (deleted) |

###### [Protected Member Functions](writer.html#beast.ref.boost__beast__http__basic_fields.writer.protected_member_functions)

| Name | Description |
| --- | --- |
| **[value\_type](../boost__beast__http__basic_fields__value_type/value_type.html "http::basic_fields::value_type::value_type")** |  |

###### [Member Functions](writer.html#beast.ref.boost__beast__http__basic_fields.writer.member_functions0)

| Name | Description |
| --- | --- |
| **[name](../boost__beast__http__basic_fields__value_type/name.html "http::basic_fields::value_type::name")** | Returns the field enum, which can be [`boost::beast::http::field::unknown`](../boost__beast__http__field.html "http::field"). |
| **[name\_string](../boost__beast__http__basic_fields__value_type/name_string.html "http::basic_fields::value_type::name_string")** | Returns the field name as a string. |
| **[operator=](../boost__beast__http__basic_fields__value_type/operator_eq_.html "http::basic_fields::value_type::operator=")** | Assignment (deleted) |
| **[value](../boost__beast__http__basic_fields__value_type/value.html "http::basic_fields::value_type::value")** | Returns the value of the field. |
| **[value\_type](../boost__beast__http__basic_fields__value_type/value_type.html "http::basic_fields::value_type::value_type")** | Constructor (deleted) |

###### [Protected Member Functions](writer.html#beast.ref.boost__beast__http__basic_fields.writer.protected_member_functions0)

| Name | Description |
| --- | --- |
| **[value\_type](../boost__beast__http__basic_fields__value_type/value_type.html "http::basic_fields::value_type::value_type")** |  |

###### [Member Functions](writer.html#beast.ref.boost__beast__http__basic_fields.writer.member_functions1)

| Name | Description |
| --- | --- |
| **[name](../boost__beast__http__basic_fields__value_type/name.html "http::basic_fields::value_type::name")** | Returns the field enum, which can be [`boost::beast::http::field::unknown`](../boost__beast__http__field.html "http::field"). |
| **[name\_string](../boost__beast__http__basic_fields__value_type/name_string.html "http::basic_fields::value_type::name_string")** | Returns the field name as a string. |
| **[operator=](../boost__beast__http__basic_fields__value_type/operator_eq_.html "http::basic_fields::value_type::operator=")** | Assignment (deleted) |
| **[value](../boost__beast__http__basic_fields__value_type/value.html "http::basic_fields::value_type::value")** | Returns the value of the field. |
| **[value\_type](../boost__beast__http__basic_fields__value_type/value_type.html "http::basic_fields::value_type::value_type")** | Constructor (deleted) |

###### [Protected Member Functions](writer.html#beast.ref.boost__beast__http__basic_fields.writer.protected_member_functions1)

| Name | Description |
| --- | --- |
| **[value\_type](../boost__beast__http__basic_fields__value_type/value_type.html "http::basic_fields::value_type::value_type")** |  |

###### [Member Functions](writer.html#beast.ref.boost__beast__http__basic_fields.writer.member_functions2)

| Name | Description |
| --- | --- |
| **[name](../boost__beast__http__basic_fields__value_type/name.html "http::basic_fields::value_type::name")** | Returns the field enum, which can be [`boost::beast::http::field::unknown`](../boost__beast__http__field.html "http::field"). |
| **[name\_string](../boost__beast__http__basic_fields__value_type/name_string.html "http::basic_fields::value_type::name_string")** | Returns the field name as a string. |
| **[operator=](../boost__beast__http__basic_fields__value_type/operator_eq_.html "http::basic_fields::value_type::operator=")** | Assignment (deleted) |
| **[value](../boost__beast__http__basic_fields__value_type/value.html "http::basic_fields::value_type::value")** | Returns the value of the field. |
| **[value\_type](../boost__beast__http__basic_fields__value_type/value_type.html "http::basic_fields::value_type::value_type")** | Constructor (deleted) |

###### [Protected Member Functions](writer.html#beast.ref.boost__beast__http__basic_fields.writer.protected_member_functions2)

| Name | Description |
| --- | --- |
| **[value\_type](../boost__beast__http__basic_fields__value_type/value_type.html "http::basic_fields::value_type::value_type")** |  |