##### [async\_base::immediate\_executor\_type](immediate_executor_type.html "async_base::immediate_executor_type")

The type of the immediate executor associated with this object.

###### [Synopsis](immediate_executor_type.html#beast.ref.boost__beast__async_base.immediate_executor_type.synopsis)

```programlisting
using immediate_executor_type = implementation-defined;
```

###### [Description](immediate_executor_type.html#beast.ref.boost__beast__async_base.immediate_executor_type.description)

If a class derived from [`boost::beast::async_base`](../boost__beast__async_base.html "async_base") is a completion handler,
then the associated immediage executor of the derived class will be this
type.