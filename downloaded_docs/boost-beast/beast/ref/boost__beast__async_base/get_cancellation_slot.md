##### [async\_base::get\_cancellation\_slot](get_cancellation_slot.html "async_base::get_cancellation_slot")

Returns the cancellation\_slot associated with this object.

###### [Synopsis](get_cancellation_slot.html#beast.ref.boost__beast__async_base.get_cancellation_slot.synopsis)

```programlisting
cancellation_slot_type
get_cancellation_slot() const;
```

###### [Description](get_cancellation_slot.html#beast.ref.boost__beast__async_base.get_cancellation_slot.description)

If a class derived from [`async_base`](../boost__beast__async_base.html "async_base") is a completion handler,
then the object returned from this function will be used as the associated
cancellation\_slot of the derived class.