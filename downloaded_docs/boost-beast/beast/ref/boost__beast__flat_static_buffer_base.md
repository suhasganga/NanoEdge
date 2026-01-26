#### [flat\_static\_buffer\_base](boost__beast__flat_static_buffer_base.html "flat_static_buffer_base")

A dynamic buffer using a fixed size internal buffer using no memory allocations.

##### [Synopsis](boost__beast__flat_static_buffer_base.html#beast.ref.boost__beast__flat_static_buffer_base.synopsis)

Defined in header `<boost/beast/core/flat_static_buffer.hpp>`

```programlisting
class flat_static_buffer_base
```

##### [Types](boost__beast__flat_static_buffer_base.html#beast.ref.boost__beast__flat_static_buffer_base.types)

| Name | Description |
| --- | --- |
| **[const\_buffers\_type](boost__beast__flat_static_buffer_base/const_buffers_type.html "flat_static_buffer_base::const_buffers_type")** | The ConstBufferSequence used to represent the readable bytes. |
| **[mutable\_buffers\_type](boost__beast__flat_static_buffer_base/mutable_buffers_type.html "flat_static_buffer_base::mutable_buffers_type")** | The MutableBufferSequence used to represent the writable bytes. |

##### [Member Functions](boost__beast__flat_static_buffer_base.html#beast.ref.boost__beast__flat_static_buffer_base.member_functions)

| Name | Description |
| --- | --- |
| **[capacity](boost__beast__flat_static_buffer_base/capacity.html "flat_static_buffer_base::capacity")** | Return the maximum number of bytes, both readable and writable, that can be held without requiring an allocation. |
| **[cdata](boost__beast__flat_static_buffer_base/cdata.html "flat_static_buffer_base::cdata")** | Returns a constant buffer sequence representing the readable bytes. |
| **[clear](boost__beast__flat_static_buffer_base/clear.html "flat_static_buffer_base::clear")** | Clear the readable and writable bytes to zero. |
| **[commit](boost__beast__flat_static_buffer_base/commit.html "flat_static_buffer_base::commit")** | Append writable bytes to the readable bytes. |
| **[consume](boost__beast__flat_static_buffer_base/consume.html "flat_static_buffer_base::consume")** | Remove bytes from beginning of the readable bytes. |
| **[data](boost__beast__flat_static_buffer_base/data.html "flat_static_buffer_base::data")** | Returns a constant buffer sequence representing the readable bytes.  — Returns a mutable buffer sequence representing the readable bytes. |
| **[flat\_static\_buffer\_base](boost__beast__flat_static_buffer_base/flat_static_buffer_base.html "flat_static_buffer_base::flat_static_buffer_base") [constructor]** | Constructor. |
| **[max\_size](boost__beast__flat_static_buffer_base/max_size.html "flat_static_buffer_base::max_size")** | Return the maximum number of bytes, both readable and writable, that can ever be held. |
| **[prepare](boost__beast__flat_static_buffer_base/prepare.html "flat_static_buffer_base::prepare")** | Returns a mutable buffer sequence representing writable bytes. |
| **[size](boost__beast__flat_static_buffer_base/size.html "flat_static_buffer_base::size")** | Returns the number of readable bytes. |

##### [Protected Member Functions](boost__beast__flat_static_buffer_base.html#beast.ref.boost__beast__flat_static_buffer_base.protected_member_functions)

| Name | Description |
| --- | --- |
| **[flat\_static\_buffer\_base](boost__beast__flat_static_buffer_base/flat_static_buffer_base.html "flat_static_buffer_base::flat_static_buffer_base") [constructor]** | Constructor. |
| **[reset](boost__beast__flat_static_buffer_base/reset.html "flat_static_buffer_base::reset")** | Reset the pointed-to buffer. |

##### [Description](boost__beast__flat_static_buffer_base.html#beast.ref.boost__beast__flat_static_buffer_base.description)

A dynamic buffer encapsulates memory storage that may be automatically resized
as required, where the memory is divided into two regions: readable bytes
followed by writable bytes. These memory regions are internal to the dynamic
buffer, but direct access to the elements is provided to permit them to be
efficiently used with I/O operations.

Objects of this type meet the requirements of *DynamicBuffer*
and have the following additional properties:

* A mutable buffer sequence representing the readable bytes is returned
  by [`data`](boost__beast__flat_static_buffer_base/data.html "flat_static_buffer_base::data") when `this`
  is non-const.
* Buffer sequences representing the readable and writable bytes, returned
  by [`data`](boost__beast__flat_static_buffer_base/data.html "flat_static_buffer_base::data") and [`prepare`](boost__beast__flat_static_buffer_base/prepare.html "flat_static_buffer_base::prepare"), will have a type of
  net::const\_buffer or net::mutable\_buffer.
* Ownership of the underlying storage belongs to the derived class.

##### [Remarks](boost__beast__flat_static_buffer_base.html#beast.ref.boost__beast__flat_static_buffer_base.remarks)

Variables are usually declared using the template class [`flat_static_buffer`](boost__beast__flat_static_buffer.html "flat_static_buffer"); however, to
reduce the number of template instantiations, objects should be passed [`flat_static_buffer_base`](boost__beast__flat_static_buffer_base.html "flat_static_buffer_base")&
.

##### [See Also](boost__beast__flat_static_buffer_base.html#beast.ref.boost__beast__flat_static_buffer_base.see_also)

[`flat_static_buffer`](boost__beast__flat_static_buffer.html "flat_static_buffer")