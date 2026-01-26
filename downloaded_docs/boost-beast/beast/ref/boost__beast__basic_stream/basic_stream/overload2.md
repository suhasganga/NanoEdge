###### [basic\_stream::basic\_stream (2 of 3 overloads)](overload2.html "basic_stream::basic_stream (2 of 3 overloads)")

Constructor.

###### [Synopsis](overload2.html#beast.ref.boost__beast__basic_stream.basic_stream.overload2.synopsis)

```programlisting
template<
    class RatePolicy_,
    class... Args>
basic_stream(
    RatePolicy_&& policy,
    Args&&... args);
```

###### [Description](overload2.html#beast.ref.boost__beast__basic_stream.basic_stream.overload2.description)

This constructor creates the stream with the specified rate policy, and
forwards all remaining arguments to the underlying socket. The socket
then needs to be open and connected or accepted before data can be sent
or received on it.

###### [Parameters](overload2.html#beast.ref.boost__beast__basic_stream.basic_stream.overload2.parameters)

| Name | Description |
| --- | --- |
| `policy` | The rate policy object to use. The stream will take ownership of this object by decay-copy. |
| `args` | A list of parameters forwarded to the constructor of the underlying socket. |