##### [http::ext\_list::find](find.html "http::ext_list::find")

Find a token in the list.

###### [Synopsis](find.html#beast.ref.boost__beast__http__ext_list.find.synopsis)

```programlisting
const_iterator
find(
    string_view const& s);
```

###### [Parameters](find.html#beast.ref.boost__beast__http__ext_list.find.parameters)

| Name | Description |
| --- | --- |
| `s` | The token to find. A case-insensitive comparison is used. |

###### [Return Value](find.html#beast.ref.boost__beast__http__ext_list.find.return_value)

An iterator to the matching token, or [`end()`](end.html "http::ext_list::end")
if no token exists.