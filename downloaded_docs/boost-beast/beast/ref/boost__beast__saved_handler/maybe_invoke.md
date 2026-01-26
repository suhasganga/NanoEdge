##### [saved\_handler::maybe\_invoke](maybe_invoke.html "saved_handler::maybe_invoke")

Conditionally invoke the stored completion handler.

###### [Synopsis](maybe_invoke.html#beast.ref.boost__beast__saved_handler.maybe_invoke.synopsis)

```programlisting
bool
maybe_invoke();
```

###### [Description](maybe_invoke.html#beast.ref.boost__beast__saved_handler.maybe_invoke.description)

Invokes the stored completion handler if this->[`has_value()`](has_value.html "saved_handler::has_value")
== true , otherwise does nothing. Any dynamic memory used is deallocated
before the stored completion handler is invoked. The executor work guard
is also reset before the invocation.

###### [Return Value](maybe_invoke.html#beast.ref.boost__beast__saved_handler.maybe_invoke.return_value)

`true` if the invocation took
place.