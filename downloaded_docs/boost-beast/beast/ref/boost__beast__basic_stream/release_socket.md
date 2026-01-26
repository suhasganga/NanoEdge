##### [basic\_stream::release\_socket](release_socket.html "basic_stream::release_socket")

Release ownership of the underlying socket.

###### [Synopsis](release_socket.html#beast.ref.boost__beast__basic_stream.release_socket.synopsis)

```programlisting
socket_type
release_socket();
```

###### [Description](release_socket.html#beast.ref.boost__beast__basic_stream.release_socket.description)

This function causes all outstanding asynchronous connect, read, and write
operations to be canceled as if by a call to [`cancel`](cancel.html "basic_stream::cancel"). Ownership of the underlying
socket is then transferred to the caller.