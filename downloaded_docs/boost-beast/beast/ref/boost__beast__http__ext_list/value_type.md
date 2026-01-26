##### [http::ext\_list::value\_type](value_type.html "http::ext_list::value_type")

The type of each element in the list.

###### [Synopsis](value_type.html#beast.ref.boost__beast__http__ext_list.value_type.synopsis)

```programlisting
using value_type = std::pair< string_view, param_list >;
```

###### [Types](value_type.html#beast.ref.boost__beast__http__ext_list.value_type.types)

| Name | Description |
| --- | --- |
| **[const\_iterator](../boost__beast__http__param_list/const_iterator.html "http::param_list::const_iterator")** | A constant iterator to the list. |
| **[value\_type](../boost__beast__http__param_list/value_type.html "http::param_list::value_type")** | The type of each element in the list. |

###### [Member Functions](value_type.html#beast.ref.boost__beast__http__ext_list.value_type.member_functions)

| Name | Description |
| --- | --- |
| **[begin](../boost__beast__http__param_list/begin.html "http::param_list::begin")** | Return a const iterator to the beginning of the list. |
| **[cbegin](../boost__beast__http__param_list/cbegin.html "http::param_list::cbegin")** | Return a const iterator to the beginning of the list. |
| **[cend](../boost__beast__http__param_list/cend.html "http::param_list::cend")** | Return a const iterator to the end of the list. |
| **[end](../boost__beast__http__param_list/end.html "http::param_list::end")** | Return a const iterator to the end of the list. |
| **[param\_list](../boost__beast__http__param_list/param_list.html "http::param_list::param_list")** | Default constructor.  — Construct a list. |

This container allows iteration of the parameter list in an HTTP extension.
The parameter list is a series of name/value pairs with each pair starting
with a semicolon. The value is optional.

If a parsing error is encountered while iterating the string, the behavior
of the container will be as if a string containing only characters up to
but excluding the first invalid character was used to construct the list.

###### [BNF](value_type.html#beast.ref.boost__beast__http__ext_list.value_type.bnf)

```programlisting
param-list  = *( OWS ";" OWS param )
param       = token OWS [ "=" OWS ( token / quoted- string ) ]
```

To use this class, construct with the string to be parsed and then use
[`begin`](../boost__beast__http__param_list/begin.html "http::param_list::begin") and [`end`](../boost__beast__http__param_list/end.html "http::param_list::end"), or range-for to iterate each
item:

###### [Example](value_type.html#beast.ref.boost__beast__http__ext_list.value_type.example)

```programlisting
for ( auto const & param : param_list{ ";level=9;no_context_takeover;bits=15" })
{
    std::cout << ";" << param.first;
    if (! param.second.empty())
        std::cout << "=" << param.second;
    std::cout << "\n" ;
}
```

###### [Description](value_type.html#beast.ref.boost__beast__http__ext_list.value_type.description)

The first element of the pair is the extension token, and the second element
of the pair is an iterable container holding the extension's name/value
parameters.