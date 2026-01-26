##### [basic\_stream::executor\_type](executor_type.html "basic_stream::executor_type")

The type of the executor associated with the stream.

###### [Synopsis](executor_type.html#beast.ref.boost__beast__basic_stream.executor_type.synopsis)

```programlisting
using executor_type = beast::executor_type< socket_type >;
```

###### [Description](executor_type.html#beast.ref.boost__beast__basic_stream.executor_type.description)

This will be the type of executor used to invoke completion handlers which
do not have an explicit associated executor.