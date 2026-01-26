#### [test::run](boost__beast__test__run.html "test::run")

Run an I/O context.

##### [Synopsis](boost__beast__test__run.html#beast.ref.boost__beast__test__run.synopsis)

Defined in header `<boost/beast/_experimental/test/handler.hpp>`

```programlisting
void
run(
    net::io_context& ioc);
```

##### [Description](boost__beast__test__run.html#beast.ref.boost__beast__test__run.description)

This function runs and dispatches handlers on the specified I/O context,
until one of the following conditions is true:

* The I/O context runs out of work.

##### [Parameters](boost__beast__test__run.html#beast.ref.boost__beast__test__run.parameters)

| Name | Description |
| --- | --- |
| `ioc` | The I/O context to run |