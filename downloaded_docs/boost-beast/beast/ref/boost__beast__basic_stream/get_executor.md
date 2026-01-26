##### [basic\_stream::get\_executor](get_executor.html "basic_stream::get_executor")

Get the executor associated with the object.

###### [Synopsis](get_executor.html#beast.ref.boost__beast__basic_stream.get_executor.synopsis)

```programlisting
executor_type
get_executor();
```

###### [Description](get_executor.html#beast.ref.boost__beast__basic_stream.get_executor.description)

This function may be used to obtain the executor object that the stream
uses to dispatch completion handlers without an assocaited executor.

###### [Return Value](get_executor.html#beast.ref.boost__beast__basic_stream.get_executor.return_value)

A copy of the executor that stream will use to dispatch handlers.