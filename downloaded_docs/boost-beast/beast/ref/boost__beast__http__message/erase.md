##### [http::message::erase](erase.html "http::message::erase")

Remove a field.

```programlisting
const_iterator
erase(
    const_iterator pos);
  » more...
```

Remove all fields with the specified name.

```programlisting
std::size_t
erase(
    field name);
  » more...

std::size_t
erase(
    string_view name);
  » more...
```