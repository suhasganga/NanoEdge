###### [file::native\_handle (2 of 2 overloads)](overload2.html "file::native_handle (2 of 2 overloads)")

(Inherited from [`file_stdio`](../../boost__beast__file_stdio.html "file_stdio"))

Set the native handle associated with the file.

###### [Synopsis](overload2.html#beast.ref.boost__beast__file.native_handle.overload2.synopsis)

```programlisting
void
native_handle(
    std::FILE* f);
```

###### [Description](overload2.html#beast.ref.boost__beast__file.native_handle.overload2.description)

If the file is open it is first closed.

###### [Parameters](overload2.html#beast.ref.boost__beast__file.native_handle.overload2.parameters)

| Name | Description |
| --- | --- |
| `f` | The native file handle to assign. |