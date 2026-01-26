##### [test::basic\_stream::close\_remote](close_remote.html "test::basic_stream::close_remote")

Close the other end of the stream.

###### [Synopsis](close_remote.html#beast.ref.boost__beast__test__basic_stream.close_remote.synopsis)

```programlisting
void
close_remote();
```

###### [Description](close_remote.html#beast.ref.boost__beast__test__basic_stream.close_remote.description)

This end of the connection will see `error::eof`
after reading all the remaining data.