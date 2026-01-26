#### [rate\_policy\_access](boost__beast__rate_policy_access.html "rate_policy_access")

Helper class to assist implementing a *RatePolicy*.

##### [Synopsis](boost__beast__rate_policy_access.html#beast.ref.boost__beast__rate_policy_access.synopsis)

Defined in header `<boost/beast/core/rate_policy.hpp>`

```programlisting
class rate_policy_access
```

##### [Description](boost__beast__rate_policy_access.html#beast.ref.boost__beast__rate_policy_access.description)

This class is used by the implementation to gain access to the private members
of a user-defined object meeting the requirements of *RatePolicy*.
To use it, simply declare it as a friend in your class:

##### [Example](boost__beast__rate_policy_access.html#beast.ref.boost__beast__rate_policy_access.example)

```programlisting
class custom_rate_policy
{
    friend class beast::rate_policy_access;
    ...
```

* *RatePolicy*

##### [See Also](boost__beast__rate_policy_access.html#beast.ref.boost__beast__rate_policy_access.see_also)

[`beast::basic_stream`](boost__beast__basic_stream.html "basic_stream")