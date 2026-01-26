##### [saved\_handler::invoke](invoke.html "saved_handler::invoke")

Unconditionally invoke the stored completion handler.

###### [Synopsis](invoke.html#beast.ref.boost__beast__saved_handler.invoke.synopsis)

```programlisting
void
invoke();
```

###### [Description](invoke.html#beast.ref.boost__beast__saved_handler.invoke.description)

Requires this->[`has_value()`](has_value.html "saved_handler::has_value")
== true . Any dynamic memory used is deallocated before the stored completion
handler is invoked. The executor work guard is also reset before the invocation.