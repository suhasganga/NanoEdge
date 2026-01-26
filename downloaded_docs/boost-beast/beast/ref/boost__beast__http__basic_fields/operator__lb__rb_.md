##### [http::basic\_fields::operator[]](operator__lb__rb_.html "http::basic_fields::operator[]")

Returns the value for a field, or `""`
if it does not exist.

```programlisting
string_view const
operator[](
    field name) const;
  » more...
```

Returns the value for a case-insensitive matching header, or `""` if it does not exist.

```programlisting
string_view const
operator[](
    string_view name) const;
  » more...
```