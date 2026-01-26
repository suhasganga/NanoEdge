#### [static\_buffer\_base](boost__beast__static_buffer_base.html "static_buffer_base")

A dynamic buffer providing a fixed size, circular buffer.

##### [Synopsis](boost__beast__static_buffer_base.html#beast.ref.boost__beast__static_buffer_base.synopsis)

Defined in header `<boost/beast/core/static_buffer.hpp>`

```programlisting
class static_buffer_base
```

##### [Types](boost__beast__static_buffer_base.html#beast.ref.boost__beast__static_buffer_base.types)

| Name | Description |
| --- | --- |
| **[const\_buffers\_type](boost__beast__static_buffer_base/const_buffers_type.html "static_buffer_base::const_buffers_type")** | The ConstBufferSequence used to represent the readable bytes. |
| **[mutable\_buffers\_type](boost__beast__static_buffer_base/mutable_buffers_type.html "static_buffer_base::mutable_buffers_type")** | The MutableBufferSequence used to represent the writable bytes. |

##### [Member Functions](boost__beast__static_buffer_base.html#beast.ref.boost__beast__static_buffer_base.member_functions)

| Name | Description |
| --- | --- |
| **[capacity](boost__beast__static_buffer_base/capacity.html "static_buffer_base::capacity")** | Return the maximum number of bytes, both readable and writable, that can be held without requiring an allocation. |
| **[cdata](boost__beast__static_buffer_base/cdata.html "static_buffer_base::cdata")** | Returns a constant buffer sequence representing the readable bytes. |
| **[clear](boost__beast__static_buffer_base/clear.html "static_buffer_base::clear")** | Clear the readable and writable bytes to zero. |
| **[commit](boost__beast__static_buffer_base/commit.html "static_buffer_base::commit")** | Append writable bytes to the readable bytes. |
| **[consume](boost__beast__static_buffer_base/consume.html "static_buffer_base::consume")** | Remove bytes from beginning of the readable bytes. |
| **[data](boost__beast__static_buffer_base/data.html "static_buffer_base::data")** | Returns a constant buffer sequence representing the readable bytes.  — Returns a mutable buffer sequence representing the readable bytes. |
| **[max\_size](boost__beast__static_buffer_base/max_size.html "static_buffer_base::max_size")** | Return the maximum number of bytes, both readable and writable, that can ever be held. |
| **[prepare](boost__beast__static_buffer_base/prepare.html "static_buffer_base::prepare")** | Returns a mutable buffer sequence representing writable bytes. |
| **[size](boost__beast__static_buffer_base/size.html "static_buffer_base::size")** | Returns the number of readable bytes. |
| **[static\_buffer\_base](boost__beast__static_buffer_base/static_buffer_base.html "static_buffer_base::static_buffer_base") [constructor]** | Constructor. |

##### [Description](boost__beast__static_buffer_base.html#beast.ref.boost__beast__static_buffer_base.description)

A dynamic buffer encapsulates memory storage that may be automatically resized
as required, where the memory is divided into two regions: readable bytes
followed by writable bytes. These memory regions are internal to the dynamic
buffer, but direct access to the elements is provided to permit them to be
efficiently used with I/O operations.

Objects of this type meet the requirements of *DynamicBuffer*
and have the following additional properties:

* A mutable buffer sequence representing the readable bytes is returned
  by [`data`](boost__beast__static_buffer_base/data.html "static_buffer_base::data") when `this`
  is non-const.
* Buffer sequences representing the readable and writable bytes, returned
  by [`data`](boost__beast__static_buffer_base/data.html "static_buffer_base::data") and [`prepare`](boost__beast__static_buffer_base/prepare.html "static_buffer_base::prepare"), may have length up
  to two.
* All operations execute in constant time.
* Ownership of the underlying storage belongs to the derived class.

##### [Remarks](boost__beast__static_buffer_base.html#beast.ref.boost__beast__static_buffer_base.remarks)

Variables are usually declared using the template class [`static_buffer`](boost__beast__static_buffer.html "static_buffer"); however, to reduce
the number of template instantiations, objects should be passed [`static_buffer_base`](boost__beast__static_buffer_base.html "static_buffer_base")& .

##### [See Also](boost__beast__static_buffer_base.html#beast.ref.boost__beast__static_buffer_base.see_also)

[`static_buffer`](boost__beast__static_buffer.html "static_buffer")