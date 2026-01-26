#### [buffer\_ref](boost__beast__buffer_ref.html "buffer_ref")

The buffer ref provides a wrapper around beast buffers to make them usable
with asio dynamic\_buffer v1.

##### [Synopsis](boost__beast__buffer_ref.html#beast.ref.boost__beast__buffer_ref.synopsis)

Defined in header `<boost/beast/core/buffer_ref.hpp>`

```programlisting
template<
    typename Buffer>
struct buffer_ref
```

##### [Types](boost__beast__buffer_ref.html#beast.ref.boost__beast__buffer_ref.types)

| Name | Description |
| --- | --- |
| **[buffer\_type](boost__beast__buffer_ref/buffer_type.html "buffer_ref::buffer_type")** | The type of the underlying buffer. |
| **[const\_buffers\_type](boost__beast__buffer_ref/const_buffers_type.html "buffer_ref::const_buffers_type")** | The ConstBufferSequence used to represent the readable bytes. |
| **[mutable\_buffers\_type](boost__beast__buffer_ref/mutable_buffers_type.html "buffer_ref::mutable_buffers_type")** | The MutableBufferSequence used to represent the writable bytes. |

##### [Member Functions](boost__beast__buffer_ref.html#beast.ref.boost__beast__buffer_ref.member_functions)

| Name | Description |
| --- | --- |
| **[buffer\_ref](boost__beast__buffer_ref/buffer_ref.html "buffer_ref::buffer_ref") [constructor]** | Create a buffer reference around `buffer`.  — Copy the reference. |
| **[capacity](boost__beast__buffer_ref/capacity.html "buffer_ref::capacity")** | Return the maximum number of bytes, both readable and writable, that can be held without requiring an allocation. |
| **[commit](boost__beast__buffer_ref/commit.html "buffer_ref::commit")** | Move bytes from the output sequence to the input sequence. |
| **[consume](boost__beast__buffer_ref/consume.html "buffer_ref::consume")** | Remove `n` bytes from the readable byte sequence. |
| **[data](boost__beast__buffer_ref/data.html "buffer_ref::data")** | Returns a constant buffer sequence representing the readable bytes. |
| **[max\_size](boost__beast__buffer_ref/max_size.html "buffer_ref::max_size")** | Return the maximum number of bytes, both readable and writable, that can ever be held. |
| **[prepare](boost__beast__buffer_ref/prepare.html "buffer_ref::prepare")** | Get a list of buffers that represents the output sequence, with the given size. |
| **[size](boost__beast__buffer_ref/size.html "buffer_ref::size")** | Returns the number of readable bytes. |

##### [Description](boost__beast__buffer_ref.html#beast.ref.boost__beast__buffer_ref.description)

v2 is current not supported, so that `BOOST_ASIO_NO_DYNAMIC_BUFFER_V1`
mustn't be defined.

##### [Example](boost__beast__buffer_ref.html#beast.ref.boost__beast__buffer_ref.example)

```programlisting
asio::tcp::socket sock;
beast::flat_buffer fb;
asio::read_until(sock, ref(fb) '\n' );
```

##### [Template Parameters](boost__beast__buffer_ref.html#beast.ref.boost__beast__buffer_ref.template_parameters)

| Type | Description |
| --- | --- |
| `Buffer` | The underlying buffer |