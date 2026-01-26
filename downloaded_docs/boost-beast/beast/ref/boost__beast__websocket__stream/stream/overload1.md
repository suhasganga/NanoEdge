###### [websocket::stream::stream (1 of 3 overloads)](overload1.html "websocket::stream::stream (1 of 3 overloads)")

Constructor.

###### [Synopsis](overload1.html#beast.ref.boost__beast__websocket__stream.stream.overload1.synopsis)

```programlisting
stream(
    stream&&);
```

###### [Description](overload1.html#beast.ref.boost__beast__websocket__stream.stream.overload1.description)

If `NextLayer` is move
constructible, this function will move-construct a new stream from the
existing stream.

After the move, the only valid operation on the moved-from object is
destruction.