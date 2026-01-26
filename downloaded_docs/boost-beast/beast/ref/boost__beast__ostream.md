#### [ostream](boost__beast__ostream.html "ostream")

Return an output stream that formats values into a *DynamicBuffer*.

##### [Synopsis](boost__beast__ostream.html#beast.ref.boost__beast__ostream.synopsis)

Defined in header `<boost/beast/core/ostream.hpp>`

```programlisting
template<
    class DynamicBuffer>
implementation-defined
ostream(
    DynamicBuffer& buffer);
```

##### [Description](boost__beast__ostream.html#beast.ref.boost__beast__ostream.description)

This function wraps the caller provided *DynamicBuffer*
into a `std::ostream` derived class, to allow `operator<<`
stream style formatting operations.

##### [Example](boost__beast__ostream.html#beast.ref.boost__beast__ostream.example)

```programlisting
ostream(buffer) << "Hello, world!" << std::endl;
```

##### [Remarks](boost__beast__ostream.html#beast.ref.boost__beast__ostream.remarks)

Calling members of the underlying buffer before the output stream is destroyed
results in undefined behavior.

##### [Parameters](boost__beast__ostream.html#beast.ref.boost__beast__ostream.parameters)

| Name | Description |
| --- | --- |
| `buffer` | An object meeting the requirements of *DynamicBuffer* into which the formatted output will be placed. |

##### [Return Value](boost__beast__ostream.html#beast.ref.boost__beast__ostream.return_value)

An object derived from `std::ostream`
which redirects output The wrapped dynamic buffer is not modified, a copy
is made instead. Ownership of the underlying memory is not transferred, the
application is still responsible for managing its lifetime. The caller is
responsible for ensuring the dynamic buffer is not destroyed for the lifetime
of the output stream.