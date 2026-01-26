### [Decorator](decorator.html "Decorator")

For programs which need to modify either the outgoing WebSocket HTTP Upgrade
request, the outgoing WebSocket HTTP Upgrade response, or both, the stream
supports an optional property called a *decorator*. This
is a function pointer or callable object which is invoked before the implementation
sends an HTTP message. The decorator receives a modifiable reference to the
message, allowing for modifications. The interface to this system uses:

**Table 1.33. WebSocket Decorator Interface**

| Name | Description |
| --- | --- |
| [`request_type`](../ref/boost__beast__websocket__request_type.html "websocket::request_type") | This is the type of the object passed to the decorator to represent HTTP Upgrade requests. |
| [`response_type`](../ref/boost__beast__websocket__response_type.html "websocket::response_type") | This is the type of the object passed to the decorator to represent HTTP Upgrade response. |
| [`stream_base::decorator`](../ref/boost__beast__websocket__stream_base__decorator.html "websocket::stream_base::decorator") | Objects of this type are used to hold a decorator to be set on the stream using `set_option`. |
| [`stream::set_option`](../ref/boost__beast__websocket__stream/set_option.html "websocket::stream::set_option") | This function is used to set a `stream_base::decorator` on the stream. |

  

This declares a normal function which decorates outgoing HTTP requests:

```programlisting
void set_user_agent(request_type& req)
{
    // Set the User-Agent on the request
    req.set(http::field::user_agent, "My User Agent");
}
```

When using a decorator, it must be set on the stream before any handshaking
takes place. This sets the decorator on the stream, to be used for all subsequent
calls to accept or handshake:

```programlisting
stream<tcp_stream> ws(ioc);

// The function `set_user_agent` will be invoked with
// every upgrade request before it is sent by the stream.

ws.set_option(stream_base::decorator(&set_user_agent));
```

Alternatively, a function object may be used. Small function objects will
not incur a memory allocation. The follow code declares and sets a function
object as a decorator:

```programlisting
struct set_server
{
    void operator()(response_type& res)
    {
        // Set the Server field on the response
        res.set(http::field::user_agent, "My Server");
    }
};

ws.set_option(stream_base::decorator(set_server{}));
```

A lambda may be used in place of a named function object:

```programlisting
ws.set_option(stream_base::decorator(
    [](response_type& res)
    {
        // Set the Server field on the response
        res.set(http::field::user_agent, "My Server");
    }));
```

It also possible for a single decorator to handle both requests and responses,
if it is overloaded for both types either as a generic lambda (C++14 and
later) or as a class as shown here:

```programlisting
struct set_message_fields
{
    void operator()(request_type& req)
    {
        // Set the User-Agent on the request
        req.set(http::field::user_agent, "My User Agent");
    }

    void operator()(response_type& res)
    {
        // Set the Server field on the response
        res.set(http::field::user_agent, "My Server");
    }
};

ws.set_option(stream_base::decorator(set_message_fields{}));
```

The implementation takes ownership by decay-copy of the invocable object
used as the decorator. Move-only types are possible:

```programlisting
struct set_auth
{
    std::unique_ptr<std::string> key;

    void operator()(request_type& req)
    {
        // Set the authorization field
        req.set(http::field::authorization, *key);
    }
};

// The stream takes ownership of the decorator object
ws.set_option(stream_base::decorator(
    set_auth{boost::make_unique<std::string>("Basic QWxhZGRpbjpPcGVuU2VzYW1l")}));
```

|  |  |
| --- | --- |
| [Important] | Important |
| Undefined behavior results if the decorator modifies the fields specific to perform the WebSocket Upgrade, such as the Upgrade or Connection fields. |