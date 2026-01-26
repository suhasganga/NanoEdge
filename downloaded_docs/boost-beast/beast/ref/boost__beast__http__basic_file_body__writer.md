#### [http::basic\_file\_body::writer](boost__beast__http__basic_file_body__writer.html "http::basic_file_body::writer")

Algorithm for retrieving buffers when serializing.

##### [Synopsis](boost__beast__http__basic_file_body__writer.html#beast.ref.boost__beast__http__basic_file_body__writer.synopsis)

Defined in header `<boost/beast/http/basic_file_body.hpp>`

```programlisting
class writer
```

##### [Types](boost__beast__http__basic_file_body__writer.html#beast.ref.boost__beast__http__basic_file_body__writer.types)

| Name | Description |
| --- | --- |
| **[const\_buffers\_type](boost__beast__http__basic_file_body__writer/const_buffers_type.html "http::basic_file_body::writer::const_buffers_type")** |  |

##### [Member Functions](boost__beast__http__basic_file_body__writer.html#beast.ref.boost__beast__http__basic_file_body__writer.member_functions)

| Name | Description |
| --- | --- |
| **[get](boost__beast__http__basic_file_body__writer/get.html "http::basic_file_body::writer::get")** |  |
| **[init](boost__beast__http__basic_file_body__writer/init.html "http::basic_file_body::writer::init")** |  |
| **[writer](boost__beast__http__basic_file_body__writer/writer.html "http::basic_file_body::writer::writer") [constructor]** |  |

##### [Description](boost__beast__http__basic_file_body__writer.html#beast.ref.boost__beast__http__basic_file_body__writer.description)

Objects of this type are created during serialization to extract the buffers
representing the body.