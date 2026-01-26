#### [is\_sync\_read\_stream](boost__beast__is_sync_read_stream.html "is_sync_read_stream")

Determine if at type meets the requirements of *SyncReadStream*.

##### [Synopsis](boost__beast__is_sync_read_stream.html#beast.ref.boost__beast__is_sync_read_stream.synopsis)

Defined in header `<boost/beast/core/stream_traits.hpp>`

```programlisting
template<
    class T>
using is_sync_read_stream = see-below;
```

##### [Description](boost__beast__is_sync_read_stream.html#beast.ref.boost__beast__is_sync_read_stream.description)

Metafunctions are used to perform compile time checking of template types.
This type will be `std::true_type` if `T`
meets the requirements, else the type will be `std::false_type`.

##### [Example](boost__beast__is_sync_read_stream.html#beast.ref.boost__beast__is_sync_read_stream.example)

Use with `static_assert`:

```programlisting
template < class SyncReadStream>
void f(SyncReadStream& stream)
{
    static_assert (is_sync_read_stream<SyncReadStream>::value,
        "SyncReadStream type requirements not met" );
...
```

Use with `std::enable_if` (SFINAE):

```programlisting
template < class SyncReadStream>
typename std::enable_if<is_sync_read_stream<SyncReadStream>::value>::type
f(SyncReadStream& stream);
```