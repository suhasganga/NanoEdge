##### [test::handler::handler](handler.html "test::handler::handler")

```programlisting
handler(
    boost::source_location loc = BOOST_CURRENT_LOCATION);
  » more...

explicit
handler(
    error_code ec,
    boost::source_location loc = BOOST_CURRENT_LOCATION);
  » more...

explicit
handler(
    boost::none_t,
    boost::source_location loc = BOOST_CURRENT_LOCATION);
  » more...

handler(
    handler&& other);
  » more...
```