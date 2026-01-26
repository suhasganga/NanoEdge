##### [test::basic\_stream::~basic\_stream](_dtor_basic_stream.html "test::basic_stream::~basic_stream")

Destructor.

###### [Synopsis](_dtor_basic_stream.html#beast.ref.boost__beast__test__basic_stream._dtor_basic_stream.synopsis)

```programlisting
~basic_stream();
```

###### [Description](_dtor_basic_stream.html#beast.ref.boost__beast__test__basic_stream._dtor_basic_stream.description)

If an asynchronous read operation is pending, it will simply be discarded
with no notification to the completion handler.

If a connection is established while the stream is destroyed, the peer
will see the error `net::error::connection_reset`
when performing any reads or writes.