#### [buffers\_to\_string](boost__beast__buffers_to_string.html "buffers_to_string")

Return a string representing the contents of a buffer sequence.

##### [Synopsis](boost__beast__buffers_to_string.html#beast.ref.boost__beast__buffers_to_string.synopsis)

Defined in header `<boost/beast/core/buffers_to_string.hpp>`

```programlisting
template<
    class ConstBufferSequence>
std::string
buffers_to_string(
    ConstBufferSequence const& buffers);
```

##### [Description](boost__beast__buffers_to_string.html#beast.ref.boost__beast__buffers_to_string.description)

This function returns a string representing an entire buffer sequence. Nulls
and unprintable characters in the buffer sequence are inserted to the resulting
string as-is. No character conversions are performed.

##### [Parameters](boost__beast__buffers_to_string.html#beast.ref.boost__beast__buffers_to_string.parameters)

| Name | Description |
| --- | --- |
| `buffers` | The buffer sequence to convert |

##### [Example](boost__beast__buffers_to_string.html#beast.ref.boost__beast__buffers_to_string.example)

This function writes a buffer sequence converted to a string to `std::cout`.

```programlisting
template < class ConstBufferSequence>
void print(ConstBufferSequence const & buffers)
{
    std::cout << buffers_to_string(buffers) << std::endl;
}
```