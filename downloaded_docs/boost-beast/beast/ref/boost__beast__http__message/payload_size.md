##### [http::message::payload\_size](payload_size.html "http::message::payload_size")

Returns the payload size of the body in octets if possible.

###### [Synopsis](payload_size.html#beast.ref.boost__beast__http__message.payload_size.synopsis)

```programlisting
boost::optional< std::uint64_t >
payload_size() const;
```

###### [Description](payload_size.html#beast.ref.boost__beast__http__message.payload_size.description)

This function invokes the *Body* algorithm to measure
the number of octets in the serialized body container. If there is no body,
this will return zero. Otherwise, if the body exists but is not known ahead
of time, `boost::none` is returned (usually indicating
that a chunked Transfer-Encoding will be used).

###### [Remarks](payload_size.html#beast.ref.boost__beast__http__message.payload_size.remarks)

The value of the Content-Length field in the message is not inspected.