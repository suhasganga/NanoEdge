#### [async\_detect\_ssl](boost__beast__async_detect_ssl.html "async_detect_ssl")

Detect a TLS/SSL handshake asynchronously on a stream.

##### [Synopsis](boost__beast__async_detect_ssl.html#beast.ref.boost__beast__async_detect_ssl.synopsis)

Defined in header `<boost/beast/core/detect_ssl.hpp>`

```programlisting
template<
    class AsyncReadStream,
    class DynamicBuffer,
    class CompletionToken = net::default_completion_token_t<beast::executor_type<AsyncReadStream>>>
DEDUCED
async_detect_ssl(
    AsyncReadStream& stream,
    DynamicBuffer& buffer,
    CompletionToken&& token = net::default_completion_token_t< beast::executor_type< AsyncReadStream > >{});
```

##### [Description](boost__beast__async_detect_ssl.html#beast.ref.boost__beast__async_detect_ssl.description)

This function reads asynchronously from a stream to determine if a client
handshake message is being received.

This call always returns immediately. The asynchronous operation will continue
until one of the following conditions is true:

* A TLS client opening handshake is detected,
* The received data is invalid for a TLS client handshake, or
* An error occurs.

The algorithm, known as a *composed asynchronous operation*,
is implemented in terms of calls to the next layer's `async_read_some`
function. The program must ensure that no other calls to `async_read_some`
are performed until this operation completes.

Bytes read from the stream will be stored in the passed dynamic buffer, which
may be used to perform the TLS handshake if the detector returns true, or
be otherwise consumed by the caller based on the expected protocol.

##### [Parameters](boost__beast__async_detect_ssl.html#beast.ref.boost__beast__async_detect_ssl.parameters)

| Name | Description |
| --- | --- |
| `stream` | The stream to read from. This type must meet the requirements of *AsyncReadStream*. |
| `buffer` | The dynamic buffer to use. This type must meet the requirements of *DynamicBuffer*. |
| `token` | The completion token used to determine the method used to provide the result of the asynchronous operation. If this is a completion handler, the implementation takes ownership of the handler by performing a decay-copy, and the equivalent function signature of the handler must be:   ```table-programlisting void handler(     error_code const & error,    // Set to the error, if any     bool result                 // The result of the detector ); ```   If the handler has an associated immediate executor, an immediate completion will be dispatched to it. Otherwise, the handler will not be invoked from within this function. Invocation of the handler will be performed in a manner equivalent to using `net::post`. |