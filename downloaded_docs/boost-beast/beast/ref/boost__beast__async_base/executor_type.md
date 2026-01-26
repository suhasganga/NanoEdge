##### [async\_base::executor\_type](executor_type.html "async_base::executor_type")

The type of executor associated with this object.

###### [Synopsis](executor_type.html#beast.ref.boost__beast__async_base.executor_type.synopsis)

```programlisting
using executor_type = implementation-defined;
```

###### [Description](executor_type.html#beast.ref.boost__beast__async_base.executor_type.description)

If a class derived from [`boost::beast::async_base`](../boost__beast__async_base.html "async_base") is a completion handler,
then the associated executor of the derived class will be this type.