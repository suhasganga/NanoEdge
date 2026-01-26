##### [test::basic\_stream::close](close.html "test::basic_stream::close")

Close the stream.

###### [Synopsis](close.html#beast.ref.boost__beast__test__basic_stream.close.synopsis)

```programlisting
void
close();
```

###### [Description](close.html#beast.ref.boost__beast__test__basic_stream.close.description)

The other end of the connection will see `error::eof`
after reading all the remaining data.