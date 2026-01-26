##### [http::message::equal\_range](equal_range.html "http::message::equal_range")

Returns a range of iterators to the fields with the specified name.

```programlisting
std::pair< const_iterator, const_iterator >
equal_range(
    field name) const;
  » more...
```

Returns a range of iterators to the fields with the specified name.

```programlisting
std::pair< const_iterator, const_iterator >
equal_range(
    string_view name) const;
  » more...
```