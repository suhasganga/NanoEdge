##### [http::parser::put](put.html "http::parser::put")

(Inherited from [`http::basic_parser`](../boost__beast__http__basic_parser.html "http::basic_parser"))

Write a buffer sequence to the parser.

###### [Synopsis](put.html#beast.ref.boost__beast__http__parser.put.synopsis)

```programlisting
template<
    class ConstBufferSequence>
std::size_t
put(
    ConstBufferSequence const& buffers,
    error_code& ec);
```

###### [Description](put.html#beast.ref.boost__beast__http__parser.put.description)

This function attempts to incrementally parse the HTTP message data stored
in the caller provided buffers. Upon success, a positive return value indicates
that the parser made forward progress, consuming that number of bytes.

In some cases there may be an insufficient number of octets in the input
buffer in order to make forward progress. This is indicated by the code
[`error::need_more`](../boost__beast__http__error.html "http::error").
When this happens, the caller should place additional bytes into the buffer
sequence and call [`put`](put.html "http::parser::put") again.

The error code [`error::need_more`](../boost__beast__http__error.html "http::error") is special. When this
error is returned, a subsequent call to [`put`](put.html "http::parser::put") may succeed if the buffers
have been updated. Otherwise, upon error the parser may not be restarted.

###### [Parameters](put.html#beast.ref.boost__beast__http__parser.put.parameters)

| Name | Description |
| --- | --- |
| `buffers` | An object meeting the requirements of *ConstBufferSequence* that represents the next chunk of message data. If the length of this buffer sequence is one, the implementation will not allocate additional memory. The class [`beast::basic_flat_buffer`](../boost__beast__basic_flat_buffer.html "basic_flat_buffer") is provided as one way to meet this requirement |
| `ec` | Set to the error, if any occurred. |

###### [Return Value](put.html#beast.ref.boost__beast__http__parser.put.return_value)

The number of octets consumed in the buffer sequence. The caller should
remove these octets even if the error is set.