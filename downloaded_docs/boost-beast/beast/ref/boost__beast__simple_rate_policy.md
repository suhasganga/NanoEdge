#### [simple\_rate\_policy](boost__beast__simple_rate_policy.html "simple_rate_policy")

A rate policy with simple, configurable limits on reads and writes.

##### [Synopsis](boost__beast__simple_rate_policy.html#beast.ref.boost__beast__simple_rate_policy.synopsis)

Defined in header `<boost/beast/core/rate_policy.hpp>`

```programlisting
class simple_rate_policy
```

##### [Member Functions](boost__beast__simple_rate_policy.html#beast.ref.boost__beast__simple_rate_policy.member_functions)

| Name | Description |
| --- | --- |
| **[read\_limit](boost__beast__simple_rate_policy/read_limit.html "simple_rate_policy::read_limit")** | Set the limit of bytes per second to read. |
| **[write\_limit](boost__beast__simple_rate_policy/write_limit.html "simple_rate_policy::write_limit")** | Set the limit of bytes per second to write. |

##### [Description](boost__beast__simple_rate_policy.html#beast.ref.boost__beast__simple_rate_policy.description)

This rate policy allows for simple individual limits on the amount of bytes
per second allowed for reads and writes.

* *RatePolicy*

##### [See Also](boost__beast__simple_rate_policy.html#beast.ref.boost__beast__simple_rate_policy.see_also)

[`beast::basic_stream`](boost__beast__basic_stream.html "basic_stream")