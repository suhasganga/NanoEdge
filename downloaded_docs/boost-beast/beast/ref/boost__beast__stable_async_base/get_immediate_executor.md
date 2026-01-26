##### [stable\_async\_base::get\_immediate\_executor](get_immediate_executor.html "stable_async_base::get_immediate_executor")

(Inherited from [`async_base`](../boost__beast__async_base.html "async_base"))

Returns the immediate executor associated with this handler.

###### [Synopsis](get_immediate_executor.html#beast.ref.boost__beast__stable_async_base.get_immediate_executor.synopsis)

```programlisting
net::associated_immediate_executor_t< Handler, typename net::executor_work_guard< Executor1 >::executor_type >
get_immediate_executor() const;
```

###### [Description](get_immediate_executor.html#beast.ref.boost__beast__stable_async_base.get_immediate_executor.description)

If the handler has none it returns asios default immediate executor based
on the executor of the object.

If a class derived from [`boost::beast::async_base`](../boost__beast__async_base.html "async_base") is a completion handler,
then the object returned from this function will be used as the associated
immediate executor of the derived class.