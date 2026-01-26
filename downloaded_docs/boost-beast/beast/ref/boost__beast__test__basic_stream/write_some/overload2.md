###### [test::basic\_stream::write\_some (2 of 2 overloads)](overload2.html "test::basic_stream::write_some (2 of 2 overloads)")

Write some data to the stream.

###### [Synopsis](overload2.html#beast.ref.boost__beast__test__basic_stream.write_some.overload2.synopsis)

```programlisting
template<
    class ConstBufferSequence>
std::size_t
write_some(
    ConstBufferSequence const& buffers,
    error_code& ec);
```

###### [Description](overload2.html#beast.ref.boost__beast__test__basic_stream.write_some.overload2.description)

This function is used to write data on the stream. The function call
will block until one or more bytes of data has been written successfully,
or until an error occurs.

###### [Parameters](overload2.html#beast.ref.boost__beast__test__basic_stream.write_some.overload2.parameters)

| Name | Description |
| --- | --- |
| `buffers` | The data to be written. |
| `ec` | Set to indicate what error occurred, if any. |

###### [Return Value](overload2.html#beast.ref.boost__beast__test__basic_stream.write_some.overload2.return_value)

The number of bytes written.

###### [Remarks](overload2.html#beast.ref.boost__beast__test__basic_stream.write_some.overload2.remarks)

The `write_some` operation
may not transmit all of the data to the peer. Consider using the function
`net::write` if you need to ensure that all
data is written before the blocking operation completes.