###### [http::message::keep\_alive (1 of 2 overloads)](overload1.html "http::message::keep_alive (1 of 2 overloads)")

Returns `true` if the message
semantics indicate keep-alive.

###### [Synopsis](overload1.html#beast.ref.boost__beast__http__message.keep_alive.overload1.synopsis)

```programlisting
bool
keep_alive() const;
```

###### [Description](overload1.html#beast.ref.boost__beast__http__message.keep_alive.overload1.description)

The value depends on the version in the message, which must be set to
the final value before this function is called or else the return value
is unreliable.