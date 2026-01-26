#### [http::string\_to\_verb](boost__beast__http__string_to_verb.html "http::string_to_verb")

Converts a string to the request method verb.

##### [Synopsis](boost__beast__http__string_to_verb.html#beast.ref.boost__beast__http__string_to_verb.synopsis)

Defined in header `<boost/beast/http/verb.hpp>`

```programlisting
verb
string_to_verb(
    string_view s);
```

##### [Description](boost__beast__http__string_to_verb.html#beast.ref.boost__beast__http__string_to_verb.description)

If the string does not match a known request method, [`verb::unknown`](boost__beast__http__verb.html "http::verb") is returned.