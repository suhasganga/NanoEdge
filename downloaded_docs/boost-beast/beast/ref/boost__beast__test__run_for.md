#### [test::run\_for](boost__beast__test__run_for.html "test::run_for")

Run an I/O context for a certain amount of time.

##### [Synopsis](boost__beast__test__run_for.html#beast.ref.boost__beast__test__run_for.synopsis)

Defined in header `<boost/beast/_experimental/test/handler.hpp>`

```programlisting
template<
    class Rep,
    class Period>
void
run_for(
    net::io_context& ioc,
    std::chrono::duration< Rep, Period > elapsed);
```

##### [Description](boost__beast__test__run_for.html#beast.ref.boost__beast__test__run_for.description)

This function runs and dispatches handlers on the specified I/O context,
until one of the following conditions is true:

* The I/O context runs out of work.
* No completions occur and the specified amount of time has elapsed.

##### [Parameters](boost__beast__test__run_for.html#beast.ref.boost__beast__test__run_for.parameters)

| Name | Description |
| --- | --- |
| `ioc` | The I/O context to run |
| `elapsed` | The maximum amount of time to run for. |