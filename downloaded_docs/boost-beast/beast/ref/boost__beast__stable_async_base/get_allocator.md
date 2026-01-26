##### [stable\_async\_base::get\_allocator](get_allocator.html "stable_async_base::get_allocator")

(Inherited from [`async_base`](../boost__beast__async_base.html "async_base"))

Returns the allocator associated with this object.

###### [Synopsis](get_allocator.html#beast.ref.boost__beast__stable_async_base.get_allocator.synopsis)

```programlisting
allocator_type
get_allocator() const;
```

###### [Description](get_allocator.html#beast.ref.boost__beast__stable_async_base.get_allocator.description)

If a class derived from [`boost::beast::async_base`](../boost__beast__async_base.html "async_base") is a completion handler,
then the object returned from this function will be used as the associated
allocator of the derived class.