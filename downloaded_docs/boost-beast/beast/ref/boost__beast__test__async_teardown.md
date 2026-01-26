#### [test::async\_teardown](boost__beast__test__async_teardown.html "test::async_teardown")

##### [Synopsis](boost__beast__test__async_teardown.html#beast.ref.boost__beast__test__async_teardown.synopsis)

Defined in header `<boost/beast/_experimental/test/stream.hpp>`

```programlisting
template<
    class Executor,
    class TeardownHandler>
void
async_teardown(
    role_type role,
    basic_stream< Executor >& s,
    TeardownHandler&& handler);
```