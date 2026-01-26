#### [is\_sync\_stream](boost__beast__is_sync_stream.html "is_sync_stream")

Determine if `T` meets the
requirements of **SyncStream**.

##### [Synopsis](boost__beast__is_sync_stream.html#beast.ref.boost__beast__is_sync_stream.synopsis)

Defined in header `<boost/beast/core/stream_traits.hpp>`

```programlisting
template<
    class T>
using is_sync_stream = see-below;
```

##### [Description](boost__beast__is_sync_stream.html#beast.ref.boost__beast__is_sync_stream.description)

Metafunctions are used to perform compile time checking of template types.
This type will be `std::true_type` if `T`
meets the requirements, else the type will be `std::false_type`.

##### [Example](boost__beast__is_sync_stream.html#beast.ref.boost__beast__is_sync_stream.example)

Use with `static_assert`:

```programlisting
template < class SyncStream>
void f(SyncStream& stream)
{
    static_assert (is_sync_stream<SyncStream>::value,
        "SyncStream type requirements not met" );
...
```

Use with `std::enable_if` (SFINAE):

```programlisting
template < class SyncStream>
typename std::enable_if<is_sync_stream<SyncStream>::value>::type
f(SyncStream& stream);
```