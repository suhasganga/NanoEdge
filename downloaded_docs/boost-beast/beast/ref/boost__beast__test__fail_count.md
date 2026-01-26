#### [test::fail\_count](boost__beast__test__fail_count.html "test::fail_count")

A countdown to simulated failure.

##### [Synopsis](boost__beast__test__fail_count.html#beast.ref.boost__beast__test__fail_count.synopsis)

Defined in header `<boost/beast/_experimental/test/fail_count.hpp>`

```programlisting
class fail_count
```

##### [Member Functions](boost__beast__test__fail_count.html#beast.ref.boost__beast__test__fail_count.member_functions)

| Name | Description |
| --- | --- |
| **[fail](boost__beast__test__fail_count/fail.html "test::fail_count::fail")** | Throw an exception on the Nth failure.  — Set an error code on the Nth failure. |
| **[fail\_count](boost__beast__test__fail_count/fail_count.html "test::fail_count::fail_count") [constructor]** | — Construct a counter. |

##### [Description](boost__beast__test__fail_count.html#beast.ref.boost__beast__test__fail_count.description)

On the Nth operation, the class will fail with the specified error code,
or the default error code of [`error::test_failure`](boost__beast__test__error.html "test::error").

Instances of this class may be used to build objects which are specifically
designed to aid in writing unit tests, for interfaces which can throw exceptions
or return [`error_code`](boost__beast__error_code.html "error_code") values representing failure.