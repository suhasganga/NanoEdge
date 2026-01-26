##### [basic\_stream::~basic\_stream](_dtor_basic_stream.html "basic_stream::~basic_stream")

Destructor.

###### [Synopsis](_dtor_basic_stream.html#beast.ref.boost__beast__basic_stream._dtor_basic_stream.synopsis)

```programlisting
~basic_stream();
```

###### [Description](_dtor_basic_stream.html#beast.ref.boost__beast__basic_stream._dtor_basic_stream.description)

This function destroys the stream, cancelling any outstanding asynchronous
operations associated with the socket as if by calling cancel.