#### [flat\_static\_buffer](boost__beast__flat_static_buffer.html "flat_static_buffer")

A *DynamicBuffer* with a fixed size internal buffer using
no memory allocations.

##### [Synopsis](boost__beast__flat_static_buffer.html#beast.ref.boost__beast__flat_static_buffer.synopsis)

Defined in header `<boost/beast/core/flat_static_buffer.hpp>`

```programlisting
template<
    std::size_t N>
class flat_static_buffer :
    public flat_static_buffer_base
```

##### [Types](boost__beast__flat_static_buffer.html#beast.ref.boost__beast__flat_static_buffer.types)

| Name | Description |
| --- | --- |
| **[const\_buffers\_type](boost__beast__flat_static_buffer/const_buffers_type.html "flat_static_buffer::const_buffers_type")** | The ConstBufferSequence used to represent the readable bytes. |
| **[mutable\_buffers\_type](boost__beast__flat_static_buffer/mutable_buffers_type.html "flat_static_buffer::mutable_buffers_type")** | The MutableBufferSequence used to represent the writable bytes. |

##### [Member Functions](boost__beast__flat_static_buffer.html#beast.ref.boost__beast__flat_static_buffer.member_functions)

| Name | Description |
| --- | --- |
| **[base](boost__beast__flat_static_buffer/base.html "flat_static_buffer::base")** | Returns the [`flat_static_buffer_base`](boost__beast__flat_static_buffer_base.html "flat_static_buffer_base") portion of this object. |
| **[capacity](boost__beast__flat_static_buffer/capacity.html "flat_static_buffer::capacity")** | Return the maximum sum of input and output sizes that can be held without an allocation. |
| **[cdata](boost__beast__flat_static_buffer/cdata.html "flat_static_buffer::cdata")** | Returns a constant buffer sequence representing the readable bytes. |
| **[clear](boost__beast__flat_static_buffer/clear.html "flat_static_buffer::clear")** | Clear the readable and writable bytes to zero. |
| **[commit](boost__beast__flat_static_buffer/commit.html "flat_static_buffer::commit")** | Append writable bytes to the readable bytes. |
| **[consume](boost__beast__flat_static_buffer/consume.html "flat_static_buffer::consume")** | Remove bytes from beginning of the readable bytes. |
| **[data](boost__beast__flat_static_buffer/data.html "flat_static_buffer::data")** | Returns a constant buffer sequence representing the readable bytes.  — Returns a mutable buffer sequence representing the readable bytes. |
| **[flat\_static\_buffer](boost__beast__flat_static_buffer/flat_static_buffer.html "flat_static_buffer::flat_static_buffer") [constructor]** | Constructor. |
| **[max\_size](boost__beast__flat_static_buffer/max_size.html "flat_static_buffer::max_size")** | Return the maximum sum of the input and output sequence sizes. |
| **[operator=](boost__beast__flat_static_buffer/operator_eq_.html "flat_static_buffer::operator=")** | Assignment. |
| **[prepare](boost__beast__flat_static_buffer/prepare.html "flat_static_buffer::prepare")** | Returns a mutable buffer sequence representing writable bytes. |
| **[size](boost__beast__flat_static_buffer/size.html "flat_static_buffer::size")** | Returns the number of readable bytes. |

##### [Protected Member Functions](boost__beast__flat_static_buffer.html#beast.ref.boost__beast__flat_static_buffer.protected_member_functions)

| Name | Description |
| --- | --- |
| **[reset](boost__beast__flat_static_buffer/reset.html "flat_static_buffer::reset")** | Reset the pointed-to buffer. |

##### [Description](boost__beast__flat_static_buffer.html#beast.ref.boost__beast__flat_static_buffer.description)

Buffer sequences representing the readable and writable bytes, returned by
[`data`](boost__beast__flat_static_buffer/data.html "flat_static_buffer::data") and [`prepare`](boost__beast__flat_static_buffer/prepare.html "flat_static_buffer::prepare"), will have a type of net::const\_buffer
or net::mutable\_buffer.

##### [Template Parameters](boost__beast__flat_static_buffer.html#beast.ref.boost__beast__flat_static_buffer.template_parameters)

| Type | Description |
| --- | --- |
| `N` | The number of bytes in the internal buffer. |

##### [Remarks](boost__beast__flat_static_buffer.html#beast.ref.boost__beast__flat_static_buffer.remarks)

To reduce the number of template instantiations when passing objects of this
type in a deduced context, the signature of the receiving function should
use [`flat_static_buffer_base`](boost__beast__flat_static_buffer_base.html "flat_static_buffer_base") instead.

##### [See Also](boost__beast__flat_static_buffer.html#beast.ref.boost__beast__flat_static_buffer.see_also)

[`flat_static_buffer_base`](boost__beast__flat_static_buffer_base.html "flat_static_buffer_base")