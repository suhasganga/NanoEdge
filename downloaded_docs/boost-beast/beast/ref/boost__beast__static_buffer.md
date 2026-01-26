#### [static\_buffer](boost__beast__static_buffer.html "static_buffer")

A dynamic buffer providing a fixed size, circular buffer.

##### [Synopsis](boost__beast__static_buffer.html#beast.ref.boost__beast__static_buffer.synopsis)

Defined in header `<boost/beast/core/static_buffer.hpp>`

```programlisting
template<
    std::size_t N>
class static_buffer :
    public static_buffer_base
```

##### [Types](boost__beast__static_buffer.html#beast.ref.boost__beast__static_buffer.types)

| Name | Description |
| --- | --- |
| **[const\_buffers\_type](boost__beast__static_buffer/const_buffers_type.html "static_buffer::const_buffers_type")** | The ConstBufferSequence used to represent the readable bytes. |
| **[mutable\_buffers\_type](boost__beast__static_buffer/mutable_buffers_type.html "static_buffer::mutable_buffers_type")** | The MutableBufferSequence used to represent the writable bytes. |

##### [Member Functions](boost__beast__static_buffer.html#beast.ref.boost__beast__static_buffer.member_functions)

| Name | Description |
| --- | --- |
| **[base](boost__beast__static_buffer/base.html "static_buffer::base")** | Returns the [`static_buffer_base`](boost__beast__static_buffer_base.html "static_buffer_base") portion of this object. |
| **[capacity](boost__beast__static_buffer/capacity.html "static_buffer::capacity")** | Return the maximum sum of input and output sizes that can be held without an allocation. |
| **[cdata](boost__beast__static_buffer/cdata.html "static_buffer::cdata")** | Returns a constant buffer sequence representing the readable bytes. |
| **[clear](boost__beast__static_buffer/clear.html "static_buffer::clear")** | Clear the readable and writable bytes to zero. |
| **[commit](boost__beast__static_buffer/commit.html "static_buffer::commit")** | Append writable bytes to the readable bytes. |
| **[consume](boost__beast__static_buffer/consume.html "static_buffer::consume")** | Remove bytes from beginning of the readable bytes. |
| **[data](boost__beast__static_buffer/data.html "static_buffer::data")** | Returns a constant buffer sequence representing the readable bytes.  — Returns a mutable buffer sequence representing the readable bytes. |
| **[max\_size](boost__beast__static_buffer/max_size.html "static_buffer::max_size")** | Return the maximum sum of the input and output sequence sizes. |
| **[operator=](boost__beast__static_buffer/operator_eq_.html "static_buffer::operator=")** | Assignment. |
| **[prepare](boost__beast__static_buffer/prepare.html "static_buffer::prepare")** | Returns a mutable buffer sequence representing writable bytes. |
| **[size](boost__beast__static_buffer/size.html "static_buffer::size")** | Returns the number of readable bytes. |
| **[static\_buffer](boost__beast__static_buffer/static_buffer.html "static_buffer::static_buffer") [constructor]** | Constructor. |

##### [Description](boost__beast__static_buffer.html#beast.ref.boost__beast__static_buffer.description)

A dynamic buffer encapsulates memory storage that may be automatically resized
as required, where the memory is divided into two regions: readable bytes
followed by writable bytes. These memory regions are internal to the dynamic
buffer, but direct access to the elements is provided to permit them to be
efficiently used with I/O operations.

Objects of this type meet the requirements of *DynamicBuffer*
and have the following additional properties:

* A mutable buffer sequence representing the readable bytes is returned
  by [`data`](boost__beast__static_buffer/data.html "static_buffer::data") when `this`
  is non-const.
* Buffer sequences representing the readable and writable bytes, returned
  by [`data`](boost__beast__static_buffer/data.html "static_buffer::data") and [`prepare`](boost__beast__static_buffer/prepare.html "static_buffer::prepare"), may have length up
  to two.
* All operations execute in constant time.

##### [Template Parameters](boost__beast__static_buffer.html#beast.ref.boost__beast__static_buffer.template_parameters)

| Type | Description |
| --- | --- |
| `N` | The number of bytes in the internal buffer. |

##### [Remarks](boost__beast__static_buffer.html#beast.ref.boost__beast__static_buffer.remarks)

To reduce the number of template instantiations when passing objects of this
type in a deduced context, the signature of the receiving function should
use [`static_buffer_base`](boost__beast__static_buffer_base.html "static_buffer_base") instead.

##### [See Also](boost__beast__static_buffer.html#beast.ref.boost__beast__static_buffer.see_also)

[`static_buffer_base`](boost__beast__static_buffer_base.html "static_buffer_base")