### [DynamicBuffer](DynamicBuffer.html "DynamicBuffer")

A dynamic buffer encapsulates memory storage that may be automatically resized
as required, where the memory is divided into an input sequence followed
by an output sequence. These memory regions are internal to the dynamic buffer,
but direct access to the elements is provided to permit them to be efficiently
used with I/O operations, such as the send or receive operations of a socket.
Data written to the output sequence of a dynamic buffer object is appended
to the input sequence of the same object.

The interface to this concept is intended to permit the following implementation
strategies:

* A single contiguous octet array, which is reallocated as necessary to
  accommodate changes in the size of the octet sequence. This is the implementation
  approach currently offered by [`flat_buffer`](../ref/boost__beast__flat_buffer.html "flat_buffer").
* A sequence of one or more octet arrays, where each array is of the same
  size. Additional octet array objects are appended to the sequence to
  accommodate changes in the size of the octet sequence.
* A sequence of one or more octet arrays of varying sizes. Additional octet
  array objects are appended to the sequence to accommodate changes in
  the size of the character sequence. This is the implementation approach
  currently offered by [`multi_buffer`](../ref/boost__beast__multi_buffer.html "multi_buffer").

##### [Associated With](DynamicBuffer.html#beast.concepts.DynamicBuffer.associated_with)

* `boost::asio::is_dynamic_buffer`
* [*ConstBufferSequence*](../../../../../../doc/html/boost_asio/reference/ConstBufferSequence.html)
* [*MutableBufferSequence*](../../../../../../doc/html/boost_asio/reference/MutableBufferSequence.html)

##### [Requirements](DynamicBuffer.html#beast.concepts.DynamicBuffer.requirements)

* `D` denotes a dynamic buffer
  class.
* `a` denotes a value of
  type `D`.
* `c` denotes a (possibly
  const) value of type `D`.
* `n` denotes a value of
  type `std::size_t`.
* `T` denotes a type meeting
  the requirements for [*ConstBufferSequence*](../../../../../../doc/html/boost_asio/reference/ConstBufferSequence.html).
* `U` denotes a type meeting
  the requirements for [*MutableBufferSequence*](../../../../../../doc/html/boost_asio/reference/MutableBufferSequence.html).

**Table 1.42. Valid expressions**

| Expression | Type | Semantics, Pre/Post-conditions |
| --- | --- | --- |
| `D::const_buffers_type` | `T` | This type represents the memory associated with the input sequence. |
| `D::mutable_buffers_type` | `U` | This type represents the memory associated with the output sequence. |
| `c.size()` | `std::size_t` | Returns the size, in bytes, of the input sequence. |
| `c.max_size()` | `std::size_t` | Returns the permitted maximum of the sum of the sizes of the input sequence and output sequence. |
| `c.capacity()` | `std::size_t` | Returns the maximum sum of the sizes of the input sequence and output sequence that the dynamic buffer can hold without requiring reallocation. |
| `c.data()` | `D::const_buffers_type` | Returns a constant buffer sequence u that represents the memory associated with the input sequence, and where `buffer_size(u) == size()`. |
| `a.prepare(n)` | `D::mutable_buffers_type` | Returns a mutable buffer sequence u representing the output sequence, and where `buffer_size(u) == n`. The dynamic buffer reallocates memory as required. All constant or mutable buffer sequences previously obtained using `data()` or `prepare()` are invalidated.  Throws: `length_error` if `size() + n` exceeds `max_size()`. |
| `a.commit(n)` |  | Appends `n` bytes from the start of the output sequence to the end of the input sequence. The remainder of the output sequence is discarded. If `n` is greater than the size of the output sequence, the entire output sequence is appended to the input sequence. All constant or mutable buffer sequences previously obtained using `data()` or `prepare()` are invalidated. |
| `a.consume(n)` |  | Removes `n` bytes from beginning of the input sequence. If `n` is greater than the size of the input sequence, the entire input sequence is removed. All constant or mutable buffer sequences previously obtained using `data()` or `prepare()` are invalidated. |

  

##### [Models](DynamicBuffer.html#beast.concepts.DynamicBuffer.models)

* [`basic_flat_buffer`](../ref/boost__beast__basic_flat_buffer.html "basic_flat_buffer")
* [`basic_multi_buffer`](../ref/boost__beast__basic_multi_buffer.html "basic_multi_buffer")
* [`flat_buffer`](../ref/boost__beast__flat_buffer.html "flat_buffer")
* [`flat_static_buffer`](../ref/boost__beast__flat_static_buffer.html "flat_static_buffer")
* [`flat_static_buffer_base`](../ref/boost__beast__flat_static_buffer_base.html "flat_static_buffer_base")
* [`static_buffer`](../ref/boost__beast__static_buffer.html "static_buffer")
* [`static_buffer_base`](../ref/boost__beast__static_buffer_base.html "static_buffer_base")
* [`multi_buffer`](../ref/boost__beast__multi_buffer.html "multi_buffer")