#### [test::handler](boost__beast__test__handler.html "test::handler")

A CompletionHandler used for testing.

##### [Synopsis](boost__beast__test__handler.html#beast.ref.boost__beast__test__handler.synopsis)

Defined in header `<boost/beast/_experimental/test/handler.hpp>`

```programlisting
class handler
```

##### [Member Functions](boost__beast__test__handler.html#beast.ref.boost__beast__test__handler.member_functions)

| Name | Description |
| --- | --- |
| **[handler](boost__beast__test__handler/handler.html "test::handler::handler") [constructor]** |  |
| **[operator()](boost__beast__test__handler/operator_lp__rp_.html "test::handler::operator()")** |  |
| **[~handler](boost__beast__test__handler/_dtor_handler.html "test::handler::~handler") [destructor]** |  |

##### [Description](boost__beast__test__handler.html#beast.ref.boost__beast__test__handler.description)

This completion handler is used by tests to ensure correctness of behavior.
It is designed as a single type to reduce template instantiations, with configurable
settings through constructor arguments. Typically this type will be used
in type lists and not instantiated directly; instances of this class are
returned by the helper functions listed below.

##### [See Also](boost__beast__test__handler.html#beast.ref.boost__beast__test__handler.see_also)

[`success_handler`](boost__beast__test__success_handler.html "test::success_handler"), [`fail_handler`](boost__beast__test__fail_handler.html "test::fail_handler"), [`any_handler`](boost__beast__test__any_handler.html "test::any_handler")