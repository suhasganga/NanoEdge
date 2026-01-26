##### [http::message::writer](writer.html "http::message::writer")

(Inherited from [`http::basic_fields`](../boost__beast__http__basic_fields.html "http::basic_fields"))

The algorithm used to serialize the header.

###### [Synopsis](writer.html#beast.ref.boost__beast__http__message.writer.synopsis)

```programlisting
using writer = { bool operator()(string_view lhs, value_type const &rhs) const noexcept { if(lhs.size()< rhs.name_string().size()) return true;if(lhs.size() > rhs.name_string().size()) return false;return iless::operator()(lhs, rhs.name_string());} bool operator()(value_type const &lhs, string_view rhs) const noexcept { if(lhs.name_string().size()< rhs.size()) return true;if(lhs.name_string().size() > rhs.size()) return false;return iless::operator()(lhs.name_string(), rhs);} bool operator()(value_type const &lhs, value_type const &rhs) const noexcept { if(lhs.name_string().size()< rhs.name_string().size()) return true;if(lhs.name_string().size() > rhs.name_string().size()) return false;return iless::operator()(lhs.name_string(), rhs.name_string());} } implementation-defined;
```