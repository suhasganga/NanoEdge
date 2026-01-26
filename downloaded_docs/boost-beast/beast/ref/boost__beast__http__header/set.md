##### [http::header::set](set.html "http::header::set")

Set a field value, removing any other instances of that field.

```programlisting
void
set(
    field name,
    string_view value);
  » more...

void
set(
    string_view name,
    string_view value);
  » more...
```

```programlisting
void
set(
    field,
    std::nullptr_t) = delete;
  » more...

void
set(
    string_view,
    std::nullptr_t) = delete;
  » more...
```