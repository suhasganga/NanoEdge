##### [basic\_stream::cancel](cancel.html "basic_stream::cancel")

Cancel all asynchronous operations associated with the socket.

###### [Synopsis](cancel.html#beast.ref.boost__beast__basic_stream.cancel.synopsis)

```programlisting
void
cancel();
```

###### [Description](cancel.html#beast.ref.boost__beast__basic_stream.cancel.description)

This function causes all outstanding asynchronous connect, read, and write
operations to finish immediately. Completion handlers for cancelled operations
will receive the error `net::error::operation_aborted`.
Completion handlers not yet invoked whose operations have completed, will
receive the error corresponding to the result of the operation (which may
indicate success).