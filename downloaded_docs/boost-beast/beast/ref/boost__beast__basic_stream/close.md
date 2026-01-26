##### [basic\_stream::close](close.html "basic_stream::close")

Close the timed stream.

###### [Synopsis](close.html#beast.ref.boost__beast__basic_stream.close.synopsis)

```programlisting
void
close();
```

###### [Description](close.html#beast.ref.boost__beast__basic_stream.close.description)

This cancels all of the outstanding asynchronous operations as if by calling
[`cancel`](cancel.html "basic_stream::cancel"), and closes the underlying
socket.