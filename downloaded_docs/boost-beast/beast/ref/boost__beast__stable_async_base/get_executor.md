##### [stable\_async\_base::get\_executor](get_executor.html "stable_async_base::get_executor")

(Inherited from [`async_base`](../boost__beast__async_base.html "async_base"))

Returns the executor associated with this object.

###### [Synopsis](get_executor.html#beast.ref.boost__beast__stable_async_base.get_executor.synopsis)

```programlisting
executor_type
get_executor() const;
```

###### [Description](get_executor.html#beast.ref.boost__beast__stable_async_base.get_executor.description)

If a class derived from [`boost::beast::async_base`](../boost__beast__async_base.html "async_base") is a completion handler,
then the object returned from this function will be used as the associated
executor of the derived class.