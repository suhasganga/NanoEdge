##### [http::token\_list::exists](exists.html "http::token_list::exists")

Return `true` if a token is
present in the list.

###### [Synopsis](exists.html#beast.ref.boost__beast__http__token_list.exists.synopsis)

```programlisting
bool
exists(
    string_view const& s);
```

###### [Parameters](exists.html#beast.ref.boost__beast__http__token_list.exists.parameters)

| Name | Description |
| --- | --- |
| `s` | The token to find. A case-insensitive comparison is used. |