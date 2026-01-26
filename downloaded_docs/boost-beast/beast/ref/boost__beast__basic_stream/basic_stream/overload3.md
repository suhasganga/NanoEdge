###### [basic\_stream::basic\_stream (3 of 3 overloads)](overload3.html "basic_stream::basic_stream (3 of 3 overloads)")

Move constructor.

###### [Synopsis](overload3.html#beast.ref.boost__beast__basic_stream.basic_stream.overload3.synopsis)

```programlisting
basic_stream(
    basic_stream&& other);
```

###### [Parameters](overload3.html#beast.ref.boost__beast__basic_stream.basic_stream.overload3.parameters)

| Name | Description |
| --- | --- |
| `other` | The other object from which the move will occur. |

###### [Remarks](overload3.html#beast.ref.boost__beast__basic_stream.basic_stream.overload3.remarks)

Following the move, the moved-from object is in the same state as if
newly constructed.