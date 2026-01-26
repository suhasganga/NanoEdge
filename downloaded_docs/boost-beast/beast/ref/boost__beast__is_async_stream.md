#### [is\_async\_stream](boost__beast__is_async_stream.html "is_async_stream")

Determine if `T` meets the
requirements of **AsyncStream**.

##### [Synopsis](boost__beast__is_async_stream.html#beast.ref.boost__beast__is_async_stream.synopsis)

Defined in header `<boost/beast/core/stream_traits.hpp>`

```programlisting
template<
    class T>
using is_async_stream = see-below;
```

##### [Description](boost__beast__is_async_stream.html#beast.ref.boost__beast__is_async_stream.description)

Metafunctions are used to perform compile time checking of template types.
This type will be `std::true_type` if `T`
meets the requirements, else the type will be `std::false_type`.

##### [Example](boost__beast__is_async_stream.html#beast.ref.boost__beast__is_async_stream.example)

Use with `static_assert`:

```programlisting
template < class AsyncStream>
void f(AsyncStream& stream)
{
    static_assert (is_async_stream<AsyncStream>::value,
        "AsyncStream type requirements not met" );
...
```

Use with `std::enable_if` (SFINAE):

```programlisting
template < class AsyncStream>
typename std::enable_if<is_async_stream<AsyncStream>::value>::type
f(AsyncStream& stream);
```