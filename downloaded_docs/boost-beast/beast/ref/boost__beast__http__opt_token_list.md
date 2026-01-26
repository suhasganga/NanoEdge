#### [http::opt\_token\_list](boost__beast__http__opt_token_list.html "http::opt_token_list")

A list of tokens in a comma separated HTTP field value.

##### [Synopsis](boost__beast__http__opt_token_list.html#beast.ref.boost__beast__http__opt_token_list.synopsis)

Defined in header `<boost/beast/http/rfc7230.hpp>`

```programlisting
using opt_token_list = detail::basic_parsed_list< detail::opt_token_list_policy >;
```

##### [Description](boost__beast__http__opt_token_list.html#beast.ref.boost__beast__http__opt_token_list.description)

This container allows iteration of a list of items in a header field value.
The input is a comma separated list of tokens.

If a parsing error is encountered while iterating the string, the behavior
of the container will be as if a string containing only characters up to
but excluding the first invalid character was used to construct the list.

##### [BNF](boost__beast__http__opt_token_list.html#beast.ref.boost__beast__http__opt_token_list.bnf)

```programlisting
token-list  = *( "," OWS ) token *( OWS "," [ OWS token ] )
```

To use this class, construct with the string to be parsed and then use `begin` and `end`,
or range-for to iterate each item:

##### [Example](boost__beast__http__opt_token_list.html#beast.ref.boost__beast__http__opt_token_list.example)

```programlisting
for ( auto const & token : token_list{ "apple, pear, banana" })
    std::cout << token << "\n" ;
```