#### [detect\_ssl](boost__beast__detect_ssl.html "detect_ssl")

Detect a TLS client handshake on a stream.

##### [Synopsis](boost__beast__detect_ssl.html#beast.ref.boost__beast__detect_ssl.synopsis)

Defined in header `<boost/beast/core/detect_ssl.hpp>`

```programlisting
template<
    class SyncReadStream,
    class DynamicBuffer>
bool
detect_ssl(
    SyncReadStream& stream,
    DynamicBuffer& buffer,
    error_code& ec);
```

##### [Description](boost__beast__detect_ssl.html#beast.ref.boost__beast__detect_ssl.description)

This function reads from a stream to determine if a client handshake message
is being received.

The call blocks until one of the following is true:

* A TLS client opening handshake is detected,
* The received data is invalid for a TLS client handshake, or
* An error occurs.

The algorithm, known as a *composed operation*, is implemented
in terms of calls to the next layer's `read_some`
function.

Bytes read from the stream will be stored in the passed dynamic buffer, which
may be used to perform the TLS handshake if the detector returns true, or
be otherwise consumed by the caller based on the expected protocol.

##### [Parameters](boost__beast__detect_ssl.html#beast.ref.boost__beast__detect_ssl.parameters)

| Name | Description |
| --- | --- |
| `stream` | The stream to read from. This type must meet the requirements of *SyncReadStream*. |
| `buffer` | The dynamic buffer to use. This type must meet the requirements of *DynamicBuffer*. |
| `ec` | Set to the error if any occurred. |

##### [Return Value](boost__beast__detect_ssl.html#beast.ref.boost__beast__detect_ssl.return_value)

`true` if the buffer contains
a TLS client handshake and no error occurred, otherwise `false`.