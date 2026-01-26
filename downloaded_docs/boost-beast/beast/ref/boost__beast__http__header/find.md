##### [http::header::find](find.html "http::header::find")

Returns an iterator to the case-insensitive matching field.

```programlisting
const_iterator
find(
    field name) const;
  » more...
```

Returns an iterator to the case-insensitive matching field name.

```programlisting
const_iterator
find(
    string_view name) const;
  » more...
```