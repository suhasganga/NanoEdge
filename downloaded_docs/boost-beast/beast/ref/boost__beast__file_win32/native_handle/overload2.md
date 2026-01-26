###### [file\_win32::native\_handle (2 of 2 overloads)](overload2.html "file_win32::native_handle (2 of 2 overloads)")

Set the native handle associated with the file.

###### [Synopsis](overload2.html#beast.ref.boost__beast__file_win32.native_handle.overload2.synopsis)

```programlisting
void
native_handle(
    native_handle_type h);
```

###### [Description](overload2.html#beast.ref.boost__beast__file_win32.native_handle.overload2.description)

If the file is open it is first closed.

###### [Parameters](overload2.html#beast.ref.boost__beast__file_win32.native_handle.overload2.parameters)

| Name | Description |
| --- | --- |
| `h` | The native file handle to assign. |