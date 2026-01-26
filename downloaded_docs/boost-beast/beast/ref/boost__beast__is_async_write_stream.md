#### [is\_async\_write\_stream](boost__beast__is_async_write_stream.html "is_async_write_stream")

Determine if `T` meets the
requirements of *AsyncWriteStream*.

##### [Synopsis](boost__beast__is_async_write_stream.html#beast.ref.boost__beast__is_async_write_stream.synopsis)

Defined in header `<boost/beast/core/stream_traits.hpp>`

```programlisting
template<
    class T>
using is_async_write_stream = see-below;
```

##### [Description](boost__beast__is_async_write_stream.html#beast.ref.boost__beast__is_async_write_stream.description)

Metafunctions are used to perform compile time checking of template types.
This type will be `std::true_type` if `T`
meets the requirements, else the type will be `std::false_type`.

##### [Example](boost__beast__is_async_write_stream.html#beast.ref.boost__beast__is_async_write_stream.example)

Use with `static_assert`:

```programlisting
template < class AsyncWriteStream>
void f(AsyncWriteStream& stream)
{
    static_assert (is_async_write_stream<AsyncWriteStream>::value,
        "AsyncWriteStream type requirements not met" );
...
```

Use with `std::enable_if` (SFINAE):

```programlisting
template < class AsyncWriteStream>
typename std::enable_if<is_async_write_stream<AsyncWriteStream>::value>::type
f(AsyncWriteStream& stream);
```