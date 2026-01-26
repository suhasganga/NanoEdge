#### [test::fail\_handler](boost__beast__test__fail_handler.html "test::fail_handler")

Return a test CompletionHandler which requires a specific error code.

##### [Synopsis](boost__beast__test__fail_handler.html#beast.ref.boost__beast__test__fail_handler.synopsis)

Defined in header `<boost/beast/_experimental/test/handler.hpp>`

```programlisting
handler
fail_handler(
    error_code ec,
    boost::source_location loc = BOOST_CURRENT_LOCATION);
```

##### [Description](boost__beast__test__fail_handler.html#beast.ref.boost__beast__test__fail_handler.description)

This handler can be invoked with any signature whose first parameter is an
[`error_code`](boost__beast__error_code.html "error_code").
The handler fails the test if:

* The handler is destroyed without being invoked.
* The handler is invoked with an error code different from what is specified.

##### [Parameters](boost__beast__test__fail_handler.html#beast.ref.boost__beast__test__fail_handler.parameters)

| Name | Description |
| --- | --- |
| `ec` | The error code to specify. |