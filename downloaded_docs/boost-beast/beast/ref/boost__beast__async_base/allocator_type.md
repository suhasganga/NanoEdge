##### [async\_base::allocator\_type](allocator_type.html "async_base::allocator_type")

The type of allocator associated with this object.

###### [Synopsis](allocator_type.html#beast.ref.boost__beast__async_base.allocator_type.synopsis)

```programlisting
using allocator_type = net::associated_allocator_t< Handler, Allocator >;
```

###### [Description](allocator_type.html#beast.ref.boost__beast__async_base.allocator_type.description)

If a class derived from [`boost::beast::async_base`](../boost__beast__async_base.html "async_base") is a completion handler,
then the associated allocator of the derived class will be this type.