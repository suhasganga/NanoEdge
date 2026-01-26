#### [make\_printable](boost__beast__make_printable.html "make_printable")

Helper to permit a buffer sequence to be printed to a std::ostream.

##### [Synopsis](boost__beast__make_printable.html#beast.ref.boost__beast__make_printable.synopsis)

Defined in header `<boost/beast/core/make_printable.hpp>`

```programlisting
template<
    class ConstBufferSequence>
implementation-defined
make_printable(
    ConstBufferSequence const& buffers);
```

##### [Description](boost__beast__make_printable.html#beast.ref.boost__beast__make_printable.description)

This function is used to wrap a buffer sequence to allow it to be interpreted
as characters and written to a `std::ostream`
such as `std::cout`. No character translation is performed;
unprintable and null characters will be transferred as-is to the output stream.

##### [Example](boost__beast__make_printable.html#beast.ref.boost__beast__make_printable.example)

This function prints the size and contents of a buffer sequence to standard
output:

```programlisting
template < class ConstBufferSequence>
void
print (ConstBufferSequence const & buffers)
{
    std::cout <<
        "Buffer size: " << buffer_bytes(buffers) << " bytes\n"
        "Buffer data: '" << make_printable(buffers) << "'\n" ;
}
```

##### [Parameters](boost__beast__make_printable.html#beast.ref.boost__beast__make_printable.parameters)

| Name | Description |
| --- | --- |
| `buffers` | An object meeting the requirements of *ConstBufferSequence* to be streamed. The implementation will make a copy of this object. Ownership of the underlying memory is not transferred, the application is still responsible for managing its lifetime. |