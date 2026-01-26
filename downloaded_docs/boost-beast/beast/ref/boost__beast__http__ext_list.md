#### [http::ext\_list](boost__beast__http__ext_list.html "http::ext_list")

A list of extensions in a comma separated HTTP field value.

##### [Synopsis](boost__beast__http__ext_list.html#beast.ref.boost__beast__http__ext_list.synopsis)

Defined in header `<boost/beast/http/rfc7230.hpp>`

```programlisting
class ext_list
```

##### [Types](boost__beast__http__ext_list.html#beast.ref.boost__beast__http__ext_list.types)

| Name | Description |
| --- | --- |
| **[const\_iterator](boost__beast__http__ext_list/const_iterator.html "http::ext_list::const_iterator")** | A constant iterator to the list. |
| **[value\_type](boost__beast__http__ext_list/value_type.html "http::ext_list::value_type")** | The type of each element in the list. |

##### [Member Functions](boost__beast__http__ext_list.html#beast.ref.boost__beast__http__ext_list.member_functions)

| Name | Description |
| --- | --- |
| **[begin](boost__beast__http__ext_list/begin.html "http::ext_list::begin")** | Return a const iterator to the beginning of the list. |
| **[cbegin](boost__beast__http__ext_list/cbegin.html "http::ext_list::cbegin")** | Return a const iterator to the beginning of the list. |
| **[cend](boost__beast__http__ext_list/cend.html "http::ext_list::cend")** | Return a const iterator to the end of the list. |
| **[end](boost__beast__http__ext_list/end.html "http::ext_list::end")** | Return a const iterator to the end of the list. |
| **[exists](boost__beast__http__ext_list/exists.html "http::ext_list::exists")** | Return `true` if a token is present in the list. |
| **[ext\_list](boost__beast__http__ext_list/ext_list.html "http::ext_list::ext_list") [constructor]** | Construct a list. |
| **[find](boost__beast__http__ext_list/find.html "http::ext_list::find")** | Find a token in the list. |

##### [Description](boost__beast__http__ext_list.html#beast.ref.boost__beast__http__ext_list.description)

This container allows iteration of the extensions in an HTTP field value.
The extension list is a comma separated list of token parameter list pairs.

If a parsing error is encountered while iterating the string, the behavior
of the container will be as if a string containing only characters up to
but excluding the first invalid character was used to construct the list.

##### [BNF](boost__beast__http__ext_list.html#beast.ref.boost__beast__http__ext_list.bnf)

```programlisting
ext-list    = *( "," OWS ) ext *( OWS "," [ OWS ext ] )
ext         = token param-list
param-list  = *( OWS ";" OWS param )
param       = token OWS [ "=" OWS ( token / quoted- string ) ]
```

To use this class, construct with the string to be parsed and then use [`begin`](boost__beast__http__ext_list/begin.html "http::ext_list::begin")
and [`end`](boost__beast__http__ext_list/end.html "http::ext_list::end"), or range-for to iterate each
item:

##### [Example](boost__beast__http__ext_list.html#beast.ref.boost__beast__http__ext_list.example)

```programlisting
for ( auto const & ext : ext_list{ "none, 7z;level=9, zip;no_context_takeover;bits=15" })
{
    std::cout << ext.first << "\n" ;
    for ( auto const & param : ext.second)
    {
        std::cout << ";" << param.first;
        if (! param.second.empty())
            std::cout << "=" << param.second;
        std::cout << "\n" ;
    }
}
```