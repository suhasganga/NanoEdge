#### [http::basic\_file\_body::value\_type](boost__beast__http__basic_file_body__value_type.html "http::basic_file_body::value_type")

The type of the [`message::body`](boost__beast__http__message/body.html "http::message::body") member.

##### [Synopsis](boost__beast__http__basic_file_body__value_type.html#beast.ref.boost__beast__http__basic_file_body__value_type.synopsis)

Defined in header `<boost/beast/http/basic_file_body.hpp>`

```programlisting
class value_type
```

##### [Member Functions](boost__beast__http__basic_file_body__value_type.html#beast.ref.boost__beast__http__basic_file_body__value_type.member_functions)

| Name | Description |
| --- | --- |
| **[close](boost__beast__http__basic_file_body__value_type/close.html "http::basic_file_body::value_type::close")** | Close the file if open. |
| **[file](boost__beast__http__basic_file_body__value_type/file.html "http::basic_file_body::value_type::file")** | Return the file. |
| **[is\_open](boost__beast__http__basic_file_body__value_type/is_open.html "http::basic_file_body::value_type::is_open")** | Returns `true` if the file is open. |
| **[open](boost__beast__http__basic_file_body__value_type/open.html "http::basic_file_body::value_type::open")** | Open a file at the given path with the specified mode. |
| **[operator=](boost__beast__http__basic_file_body__value_type/operator_eq_.html "http::basic_file_body::value_type::operator=")** | Move assignment. |
| **[reset](boost__beast__http__basic_file_body__value_type/reset.html "http::basic_file_body::value_type::reset")** | Set the open file. |
| **[seek](boost__beast__http__basic_file_body__value_type/seek.html "http::basic_file_body::value_type::seek")** | Set the cursor position of the file. |
| **[size](boost__beast__http__basic_file_body__value_type/size.html "http::basic_file_body::value_type::size")** | Returns the size of the file if open. |
| **[value\_type](boost__beast__http__basic_file_body__value_type/value_type.html "http::basic_file_body::value_type::value_type") [constructor]** | Constructor. |
| **[~value\_type](boost__beast__http__basic_file_body__value_type/_dtor_value_type.html "http::basic_file_body::value_type::~value_type") [destructor]** | Destructor. |

##### [Description](boost__beast__http__basic_file_body__value_type.html#beast.ref.boost__beast__http__basic_file_body__value_type.description)

Messages declared using [`basic_file_body`](boost__beast__http__basic_file_body.html "http::basic_file_body") will have this type
for the body member. This rich class interface allow the file to be opened
with the file handle maintained directly in the object, which is attached
to the message.