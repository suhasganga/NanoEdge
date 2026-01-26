##### [websocket::stream::~stream](_dtor_stream.html "websocket::stream::~stream")

Destructor.

###### [Synopsis](_dtor_stream.html#beast.ref.boost__beast__websocket__stream._dtor_stream.synopsis)

```programlisting
~stream();
```

###### [Description](_dtor_stream.html#beast.ref.boost__beast__websocket__stream._dtor_stream.description)

Destroys the stream and all associated resources.

###### [Remarks](_dtor_stream.html#beast.ref.boost__beast__websocket__stream._dtor_stream.remarks)

A stream object must not be destroyed while there are pending asynchronous
operations associated with it.