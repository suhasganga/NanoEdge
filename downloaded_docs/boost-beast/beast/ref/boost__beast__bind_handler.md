#### [bind\_handler](boost__beast__bind_handler.html "bind_handler")

Bind parameters to a completion handler, creating a new handler.

##### [Synopsis](boost__beast__bind_handler.html#beast.ref.boost__beast__bind_handler.synopsis)

Defined in header `<boost/beast/core/bind_handler.hpp>`

```programlisting
template<
    class Handler,
    class... Args>
implementation-defined
bind_handler(
    Handler&& handler,
    Args&&... args);
```

##### [Description](boost__beast__bind_handler.html#beast.ref.boost__beast__bind_handler.description)

This function creates a new handler which, when invoked, calls the original
handler with the list of bound arguments. Any parameters passed in the invocation
will be substituted for placeholders present in the list of bound arguments.
Parameters which are not matched to placeholders are silently discarded.

The passed handler and arguments are forwarded into the returned handler,
whose associated allocator and associated executor will be the same as those
of the original handler.

##### [Example](boost__beast__bind_handler.html#beast.ref.boost__beast__bind_handler.example)

This function posts the invocation of the specified completion handler with
bound arguments:

```programlisting
template < class AsyncReadStream, class ReadHandler>
void
signal_aborted (AsyncReadStream& stream, ReadHandler&& handler)
{
    net::post(
        stream.get_executor(),
        bind_handler (std::forward <ReadHandler> (handler),
            net::error::operation_aborted, 0));
}
```

##### [Parameters](boost__beast__bind_handler.html#beast.ref.boost__beast__bind_handler.parameters)

| Name | Description |
| --- | --- |
| `handler` | The handler to wrap. The implementation takes ownership of the handler by performing a decay-copy. |
| `args` | A list of arguments to bind to the handler. The arguments are forwarded into the returned object. These arguments may include placeholders, which will operate in a fashion identical to a call to `std::bind`. |