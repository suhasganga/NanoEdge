##### [http::header::get\_reason\_impl](get_reason_impl.html "http::header::get_reason_impl")

(Inherited from [`http::basic_fields`](../boost__beast__http__basic_fields.html "http::basic_fields"))

Returns the response reason-phrase string.

###### [Synopsis](get_reason_impl.html#beast.ref.boost__beast__http__header.get_reason_impl.synopsis)

```programlisting
string_view
get_reason_impl() const;
```

###### [Remarks](get_reason_impl.html#beast.ref.boost__beast__http__header.get_reason_impl.remarks)

Only called for responses.