#### [test::any\_handler](boost__beast__test__any_handler.html "test::any_handler")

Return a test CompletionHandler which requires invocation.

##### [Synopsis](boost__beast__test__any_handler.html#beast.ref.boost__beast__test__any_handler.synopsis)

Defined in header `<boost/beast/_experimental/test/handler.hpp>`

```programlisting
handler
any_handler(
    boost::source_location loc = BOOST_CURRENT_LOCATION);
```

##### [Description](boost__beast__test__any_handler.html#beast.ref.boost__beast__test__any_handler.description)

The returned handler can be invoked with any signature. The handler fails
the test if:

* The handler is destroyed without being invoked.