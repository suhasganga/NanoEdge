#### [is\_async\_read\_stream](boost__beast__is_async_read_stream.html "is_async_read_stream")

Determine if `T` meets the
requirements of *AsyncReadStream*.

##### [Synopsis](boost__beast__is_async_read_stream.html#beast.ref.boost__beast__is_async_read_stream.synopsis)

Defined in header `<boost/beast/core/stream_traits.hpp>`

```programlisting
template<
    class T>
using is_async_read_stream = see-below;
```

##### [Description](boost__beast__is_async_read_stream.html#beast.ref.boost__beast__is_async_read_stream.description)

Metafunctions are used to perform compile time checking of template types.
This type will be `std::true_type` if `T`
meets the requirements, else the type will be `std::false_type`.

##### [Example](boost__beast__is_async_read_stream.html#beast.ref.boost__beast__is_async_read_stream.example)

Use with `static_assert`:

```programlisting
template < class AsyncReadStream>
void f(AsyncReadStream& stream)
{
    static_assert (is_async_read_stream<AsyncReadStream>::value,
        "AsyncReadStream type requirements not met" );
...
```

Use with `std::enable_if` (SFINAE):

```programlisting
template < class AsyncReadStream>
typename std::enable_if<is_async_read_stream<AsyncReadStream>::value>::type
f(AsyncReadStream& stream);
```