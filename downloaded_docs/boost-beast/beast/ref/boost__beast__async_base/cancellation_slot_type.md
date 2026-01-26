##### [async\_base::cancellation\_slot\_type](cancellation_slot_type.html "async_base::cancellation_slot_type")

The type of cancellation\_slot associated with this object.

###### [Synopsis](cancellation_slot_type.html#beast.ref.boost__beast__async_base.cancellation_slot_type.synopsis)

```programlisting
using cancellation_slot_type = beast::detail::filtering_cancellation_slot< net::associated_cancellation_slot_t< Handler > >;
```

###### [Description](cancellation_slot_type.html#beast.ref.boost__beast__async_base.cancellation_slot_type.description)

If a class derived from [`async_base`](../boost__beast__async_base.html "async_base") is a completion handler,
then the associated cancellation\_slot of the derived class will be this
type.

The default type is a filtering cancellation slot, that only allows terminal
cancellation.