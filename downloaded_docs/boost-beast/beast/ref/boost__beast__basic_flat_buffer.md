#### [basic\_flat\_buffer](boost__beast__basic_flat_buffer.html "basic_flat_buffer")

A dynamic buffer providing buffer sequences of length one.

##### [Synopsis](boost__beast__basic_flat_buffer.html#beast.ref.boost__beast__basic_flat_buffer.synopsis)

Defined in header `<boost/beast/core/flat_buffer.hpp>`

```programlisting
template<
    class Allocator>
class basic_flat_buffer
```

##### [Types](boost__beast__basic_flat_buffer.html#beast.ref.boost__beast__basic_flat_buffer.types)

| Name | Description |
| --- | --- |
| **[allocator\_type](boost__beast__basic_flat_buffer/allocator_type.html "basic_flat_buffer::allocator_type")** | The type of allocator used. |
| **[const\_buffers\_type](boost__beast__basic_flat_buffer/const_buffers_type.html "basic_flat_buffer::const_buffers_type")** | The ConstBufferSequence used to represent the readable bytes. |
| **[mutable\_buffers\_type](boost__beast__basic_flat_buffer/mutable_buffers_type.html "basic_flat_buffer::mutable_buffers_type")** | The MutableBufferSequence used to represent the writable bytes. |

##### [Member Functions](boost__beast__basic_flat_buffer.html#beast.ref.boost__beast__basic_flat_buffer.member_functions)

| Name | Description |
| --- | --- |
| **[basic\_flat\_buffer](boost__beast__basic_flat_buffer/basic_flat_buffer.html "basic_flat_buffer::basic_flat_buffer") [constructor]** | Constructor.  — Move Constructor.  — Copy Constructor. |
| **[capacity](boost__beast__basic_flat_buffer/capacity.html "basic_flat_buffer::capacity")** | Return the maximum number of bytes, both readable and writable, that can be held without requiring an allocation. |
| **[cdata](boost__beast__basic_flat_buffer/cdata.html "basic_flat_buffer::cdata")** | Returns a constant buffer sequence representing the readable bytes. |
| **[clear](boost__beast__basic_flat_buffer/clear.html "basic_flat_buffer::clear")** | Set the size of the readable and writable bytes to zero. |
| **[commit](boost__beast__basic_flat_buffer/commit.html "basic_flat_buffer::commit")** | Append writable bytes to the readable bytes. |
| **[consume](boost__beast__basic_flat_buffer/consume.html "basic_flat_buffer::consume")** | Remove bytes from beginning of the readable bytes. |
| **[data](boost__beast__basic_flat_buffer/data.html "basic_flat_buffer::data")** | Returns a constant buffer sequence representing the readable bytes.  — Returns a mutable buffer sequence representing the readable bytes. |
| **[get\_allocator](boost__beast__basic_flat_buffer/get_allocator.html "basic_flat_buffer::get_allocator")** | Returns a copy of the allocator used. |
| **[max\_size](boost__beast__basic_flat_buffer/max_size.html "basic_flat_buffer::max_size")** | Set the maximum allowed capacity.  — Return the maximum number of bytes, both readable and writable, that can ever be held. |
| **[operator=](boost__beast__basic_flat_buffer/operator_eq_.html "basic_flat_buffer::operator=")** | Move Assignment.  — Copy Assignment.  — Copy assignment. |
| **[prepare](boost__beast__basic_flat_buffer/prepare.html "basic_flat_buffer::prepare")** | Returns a mutable buffer sequence representing writable bytes. |
| **[reserve](boost__beast__basic_flat_buffer/reserve.html "basic_flat_buffer::reserve")** | Guarantee a minimum capacity. |
| **[shrink\_to\_fit](boost__beast__basic_flat_buffer/shrink_to_fit.html "basic_flat_buffer::shrink_to_fit")** | Request the removal of unused capacity. |
| **[size](boost__beast__basic_flat_buffer/size.html "basic_flat_buffer::size")** | Returns the number of readable bytes. |
| **[~basic\_flat\_buffer](boost__beast__basic_flat_buffer/_dtor_basic_flat_buffer.html "basic_flat_buffer::~basic_flat_buffer") [destructor]** | Destructor. |

##### [Friends](boost__beast__basic_flat_buffer.html#beast.ref.boost__beast__basic_flat_buffer.friends)

| Name | Description |
| --- | --- |
| **[swap](boost__beast__basic_flat_buffer/swap.html "basic_flat_buffer::swap")** | Exchange two dynamic buffers. |

##### [Description](boost__beast__basic_flat_buffer.html#beast.ref.boost__beast__basic_flat_buffer.description)

A dynamic buffer encapsulates memory storage that may be automatically resized
as required, where the memory is divided into two regions: readable bytes
followed by writable bytes. These memory regions are internal to the dynamic
buffer, but direct access to the elements is provided to permit them to be
efficiently used with I/O operations.

Objects of this type meet the requirements of *DynamicBuffer*
and have the following additional properties:

* A mutable buffer sequence representing the readable bytes is returned
  by [`data`](boost__beast__basic_flat_buffer/data.html "basic_flat_buffer::data") when `this`
  is non-const.
* A configurable maximum buffer size may be set upon construction. Attempts
  to exceed the buffer size will throw `std::length_error`.
* Buffer sequences representing the readable and writable bytes, returned
  by [`data`](boost__beast__basic_flat_buffer/data.html "basic_flat_buffer::data") and [`prepare`](boost__beast__basic_flat_buffer/prepare.html "basic_flat_buffer::prepare"), will have a type of
  net::const\_buffer or net::mutable\_buffer.

Upon construction, a maximum size for the buffer may be specified. If this
limit is exceeded, the `std::length_error`
exception will be thrown.

##### [Remarks](boost__beast__basic_flat_buffer.html#beast.ref.boost__beast__basic_flat_buffer.remarks)

This class is designed for use with algorithms that take dynamic buffers
as parameters, and are optimized for the case where the input sequence or
output sequence is stored in a single contiguous buffer.