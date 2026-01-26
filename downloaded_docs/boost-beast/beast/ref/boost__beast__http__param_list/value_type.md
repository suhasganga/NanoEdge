##### [http::param\_list::value\_type](value_type.html "http::param_list::value_type")

The type of each element in the list.

###### [Synopsis](value_type.html#beast.ref.boost__beast__http__param_list.value_type.synopsis)

```programlisting
using value_type = std::pair< string_view, string_view >;
```

###### [Description](value_type.html#beast.ref.boost__beast__http__param_list.value_type.description)

The first string in the pair is the name of the parameter, and the second
string in the pair is its value (which may be empty).