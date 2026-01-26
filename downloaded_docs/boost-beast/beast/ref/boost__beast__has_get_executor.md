#### [has\_get\_executor](boost__beast__has_get_executor.html "has_get_executor")

Determine if `T` has the `get_executor` member function.

##### [Synopsis](boost__beast__has_get_executor.html#beast.ref.boost__beast__has_get_executor.synopsis)

Defined in header `<boost/beast/core/stream_traits.hpp>`

```programlisting
template<
    class T>
using has_get_executor = see-below;
```

##### [Description](boost__beast__has_get_executor.html#beast.ref.boost__beast__has_get_executor.description)

Metafunctions are used to perform compile time checking of template types.
This type will be `std::true_type` if `T`
has the member function with the correct signature, else type will be `std::false_type`.

##### [Example](boost__beast__has_get_executor.html#beast.ref.boost__beast__has_get_executor.example)

Use with tag dispatching:

```programlisting
template < class T>
void maybe_hello(T const & t, std::true_type)
{
    net::post(
        t.get_executor(),
        []
        {
            std::cout << "Hello, world!" << std::endl;
        });
}

template < class T>
void maybe_hello(T const &, std::false_type)
{
    // T does not have get_executor
}

template < class T>
void maybe_hello(T const & t)
{
    maybe_hello(t, has_get_executor<T>{});
}
```

Use with `static_assert`:

```programlisting
struct stream
{
    using executor_type = net::io_context::executor_type;
    executor_type get_executor() noexcept;
};

static_assert(has_get_executor<stream>::value, "Missing get_executor member" );
```