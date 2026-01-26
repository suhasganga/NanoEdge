#### [buffers\_adaptor](boost__beast__buffers_adaptor.html "buffers_adaptor")

Adapts a *MutableBufferSequence* into a *DynamicBuffer*.

##### [Synopsis](boost__beast__buffers_adaptor.html#beast.ref.boost__beast__buffers_adaptor.synopsis)

Defined in header `<boost/beast/core/buffers_adaptor.hpp>`

```programlisting
template<
    class MutableBufferSequence>
class buffers_adaptor
```

##### [Types](boost__beast__buffers_adaptor.html#beast.ref.boost__beast__buffers_adaptor.types)

| Name | Description |
| --- | --- |
| **[const\_buffers\_type](boost__beast__buffers_adaptor/const_buffers_type.html "buffers_adaptor::const_buffers_type")** | The ConstBufferSequence used to represent the readable bytes. |
| **[mutable\_buffers\_type](boost__beast__buffers_adaptor/mutable_buffers_type.html "buffers_adaptor::mutable_buffers_type")** | The MutableBufferSequence used to represent the writable bytes. |
| **[value\_type](boost__beast__buffers_adaptor/value_type.html "buffers_adaptor::value_type")** | The type of the underlying mutable buffer sequence. |

##### [Member Functions](boost__beast__buffers_adaptor.html#beast.ref.boost__beast__buffers_adaptor.member_functions)

| Name | Description |
| --- | --- |
| **[buffers\_adaptor](boost__beast__buffers_adaptor/buffers_adaptor.html "buffers_adaptor::buffers_adaptor") [constructor]** | Construct a buffers adaptor.  — Constructor.  — Copy Constructor. |
| **[capacity](boost__beast__buffers_adaptor/capacity.html "buffers_adaptor::capacity")** | Return the maximum number of bytes, both readable and writable, that can be held without requiring an allocation. |
| **[cdata](boost__beast__buffers_adaptor/cdata.html "buffers_adaptor::cdata")** | Returns a constant buffer sequence representing the readable bytes. |
| **[commit](boost__beast__buffers_adaptor/commit.html "buffers_adaptor::commit")** | Append writable bytes to the readable bytes. |
| **[consume](boost__beast__buffers_adaptor/consume.html "buffers_adaptor::consume")** | Remove bytes from beginning of the readable bytes. |
| **[data](boost__beast__buffers_adaptor/data.html "buffers_adaptor::data")** | Returns a constant buffer sequence representing the readable bytes.  — Returns a mutable buffer sequence representing the readable bytes. |
| **[max\_size](boost__beast__buffers_adaptor/max_size.html "buffers_adaptor::max_size")** | Return the maximum number of bytes, both readable and writable, that can ever be held. |
| **[operator=](boost__beast__buffers_adaptor/operator_eq_.html "buffers_adaptor::operator=")** | Copy Assignment. |
| **[prepare](boost__beast__buffers_adaptor/prepare.html "buffers_adaptor::prepare")** | Returns a mutable buffer sequence representing writable bytes. |
| **[size](boost__beast__buffers_adaptor/size.html "buffers_adaptor::size")** | Returns the number of readable bytes. |
| **[value](boost__beast__buffers_adaptor/value.html "buffers_adaptor::value")** | Returns the original mutable buffer sequence. |

##### [Description](boost__beast__buffers_adaptor.html#beast.ref.boost__beast__buffers_adaptor.description)

This class wraps a *MutableBufferSequence* to meet the
requirements of *DynamicBuffer*. Upon construction the
input and output sequences are empty. A copy of the mutable buffer sequence
object is stored; however, ownership of the underlying memory is not transferred.
The caller is responsible for making sure that referenced memory remains
valid for the duration of any operations.

The size of the mutable buffer sequence determines the maximum number of
bytes which may be prepared and committed.

##### [Template Parameters](boost__beast__buffers_adaptor.html#beast.ref.boost__beast__buffers_adaptor.template_parameters)

| Type | Description |
| --- | --- |
| `MutableBufferSequence` | The type of mutable buffer sequence to adapt. |