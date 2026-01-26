##### [http::message::set\_reason\_impl](set_reason_impl.html "http::message::set_reason_impl")

(Inherited from [`http::basic_fields`](../boost__beast__http__basic_fields.html "http::basic_fields"))

Set or clear the reason string.

###### [Synopsis](set_reason_impl.html#beast.ref.boost__beast__http__message.set_reason_impl.synopsis)

```programlisting
void
set_reason_impl(
    string_view s);
```

###### [Remarks](set_reason_impl.html#beast.ref.boost__beast__http__message.set_reason_impl.remarks)

Only called for responses.