#### [test::success\_handler](boost__beast__test__success_handler.html "test::success_handler")

Return a test CompletionHandler which requires success.

##### [Synopsis](boost__beast__test__success_handler.html#beast.ref.boost__beast__test__success_handler.synopsis)

Defined in header `<boost/beast/_experimental/test/handler.hpp>`

```programlisting
handler
success_handler(
    boost::source_location loc = BOOST_CURRENT_LOCATION);
```

##### [Description](boost__beast__test__success_handler.html#beast.ref.boost__beast__test__success_handler.description)

The returned handler can be invoked with any signature whose first parameter
is an [`error_code`](boost__beast__error_code.html "error_code").
The handler fails the test if:

* The handler is destroyed without being invoked, or
* The handler is invoked with a non-successful error code.