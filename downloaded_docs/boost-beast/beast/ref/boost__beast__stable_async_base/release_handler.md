##### [stable\_async\_base::release\_handler](release_handler.html "stable_async_base::release_handler")

(Inherited from [`async_base`](../boost__beast__async_base.html "async_base"))

Returns ownership of the handler associated with this object.

###### [Synopsis](release_handler.html#beast.ref.boost__beast__stable_async_base.release_handler.synopsis)

```programlisting
Handler
release_handler();
```

###### [Description](release_handler.html#beast.ref.boost__beast__stable_async_base.release_handler.description)

This function is used to transfer ownership of the handler to the caller,
by move-construction. After the move, the only valid operations on the
base object are move construction and destruction.