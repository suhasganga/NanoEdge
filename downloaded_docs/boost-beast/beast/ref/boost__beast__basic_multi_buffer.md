#### [basic\_multi\_buffer](boost__beast__basic_multi_buffer.html "basic_multi_buffer")

A dynamic buffer providing sequences of variable length.

##### [Synopsis](boost__beast__basic_multi_buffer.html#beast.ref.boost__beast__basic_multi_buffer.synopsis)

Defined in header `<boost/beast/core/multi_buffer.hpp>`

```programlisting
template<
    class Allocator>
class basic_multi_buffer
```

##### [Types](boost__beast__basic_multi_buffer.html#beast.ref.boost__beast__basic_multi_buffer.types)

| Name | Description |
| --- | --- |
| **[allocator\_type](boost__beast__basic_multi_buffer/allocator_type.html "basic_multi_buffer::allocator_type")** | The type of allocator used. |
| **[const\_buffers\_type](boost__beast__basic_multi_buffer/const_buffers_type.html "basic_multi_buffer::const_buffers_type")** | The ConstBufferSequence used to represent the readable bytes. |
| **[mutable\_buffers\_type](boost__beast__basic_multi_buffer/mutable_buffers_type.html "basic_multi_buffer::mutable_buffers_type")** | The MutableBufferSequence used to represent the writable bytes. |

##### [Member Functions](boost__beast__basic_multi_buffer.html#beast.ref.boost__beast__basic_multi_buffer.member_functions)

| Name | Description |
| --- | --- |
| **[basic\_multi\_buffer](boost__beast__basic_multi_buffer/basic_multi_buffer.html "basic_multi_buffer::basic_multi_buffer") [constructor]** | Constructor.  — Move Constructor.  — Copy Constructor. |
| **[capacity](boost__beast__basic_multi_buffer/capacity.html "basic_multi_buffer::capacity")** | Return the maximum number of bytes, both readable and writable, that can be held without requiring an allocation. |
| **[cdata](boost__beast__basic_multi_buffer/cdata.html "basic_multi_buffer::cdata")** | Returns a constant buffer sequence representing the readable bytes. |
| **[clear](boost__beast__basic_multi_buffer/clear.html "basic_multi_buffer::clear")** | Set the size of the readable and writable bytes to zero. |
| **[commit](boost__beast__basic_multi_buffer/commit.html "basic_multi_buffer::commit")** | Append writable bytes to the readable bytes. |
| **[consume](boost__beast__basic_multi_buffer/consume.html "basic_multi_buffer::consume")** | Remove bytes from beginning of the readable bytes. |
| **[data](boost__beast__basic_multi_buffer/data.html "basic_multi_buffer::data")** | Returns a constant buffer sequence representing the readable bytes.  — Returns a mutable buffer sequence representing the readable bytes. |
| **[get\_allocator](boost__beast__basic_multi_buffer/get_allocator.html "basic_multi_buffer::get_allocator")** | Returns a copy of the allocator used. |
| **[max\_size](boost__beast__basic_multi_buffer/max_size.html "basic_multi_buffer::max_size")** | Set the maximum allowed capacity.  — Return the maximum number of bytes, both readable and writable, that can ever be held. |
| **[operator=](boost__beast__basic_multi_buffer/operator_eq_.html "basic_multi_buffer::operator=")** | Move Assignment.  — Copy Assignment. |
| **[prepare](boost__beast__basic_multi_buffer/prepare.html "basic_multi_buffer::prepare")** | Returns a mutable buffer sequence representing writable bytes. |
| **[reserve](boost__beast__basic_multi_buffer/reserve.html "basic_multi_buffer::reserve")** | Guarantee a minimum capacity. |
| **[shrink\_to\_fit](boost__beast__basic_multi_buffer/shrink_to_fit.html "basic_multi_buffer::shrink_to_fit")** | Reallocate the buffer to fit the readable bytes exactly. |
| **[size](boost__beast__basic_multi_buffer/size.html "basic_multi_buffer::size")** | Returns the number of readable bytes. |
| **[~basic\_multi\_buffer](boost__beast__basic_multi_buffer/_dtor_basic_multi_buffer.html "basic_multi_buffer::~basic_multi_buffer") [destructor]** | Destructor. |

##### [Friends](boost__beast__basic_multi_buffer.html#beast.ref.boost__beast__basic_multi_buffer.friends)

| Name | Description |
| --- | --- |
| **[swap](boost__beast__basic_multi_buffer/swap.html "basic_multi_buffer::swap")** | Exchange two dynamic buffers. |

##### [Description](boost__beast__basic_multi_buffer.html#beast.ref.boost__beast__basic_multi_buffer.description)

A dynamic buffer encapsulates memory storage that may be automatically resized
as required, where the memory is divided into two regions: readable bytes
followed by writable bytes. These memory regions are internal to the dynamic
buffer, but direct access to the elements is provided to permit them to be
efficiently used with I/O operations.

The implementation uses a sequence of one or more byte arrays of varying
sizes to represent the readable and writable bytes. Additional byte array
objects are appended to the sequence to accommodate changes in the desired
size. The behavior and implementation of this container is most similar to
`std::deque`.

Objects of this type meet the requirements of *DynamicBuffer*
and have the following additional properties:

* A mutable buffer sequence representing the readable bytes is returned
  by [`data`](boost__beast__basic_multi_buffer/data.html "basic_multi_buffer::data") when `this`
  is non-const.
* Buffer sequences representing the readable and writable bytes, returned
  by [`data`](boost__beast__basic_multi_buffer/data.html "basic_multi_buffer::data") and [`prepare`](boost__beast__basic_multi_buffer/prepare.html "basic_multi_buffer::prepare"), may have length greater
  than one.
* A configurable maximum size may be set upon construction and adjusted
  afterwards. Calls to [`prepare`](boost__beast__basic_multi_buffer/prepare.html "basic_multi_buffer::prepare") that would exceed this
  size will throw `std::length_error`.
* Sequences previously obtained using [`data`](boost__beast__basic_multi_buffer/data.html "basic_multi_buffer::data") remain valid after calls
  to [`prepare`](boost__beast__basic_multi_buffer/prepare.html "basic_multi_buffer::prepare") or [`commit`](boost__beast__basic_multi_buffer/commit.html "basic_multi_buffer::commit").

##### [Template Parameters](boost__beast__basic_multi_buffer.html#beast.ref.boost__beast__basic_multi_buffer.template_parameters)

| Type | Description |
| --- | --- |
| `Allocator` | The allocator to use for managing memory. |