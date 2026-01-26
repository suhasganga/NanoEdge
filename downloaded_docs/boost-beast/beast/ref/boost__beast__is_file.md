#### [is\_file](boost__beast__is_file.html "is_file")

Determine if `T` meets the
requirements of *File*.

##### [Synopsis](boost__beast__is_file.html#beast.ref.boost__beast__is_file.synopsis)

Defined in header `<boost/beast/core/file_base.hpp>`

```programlisting
template<
    class T>
struct is_file :
    public std::integral_constant< bool,... >
```

##### [Description](boost__beast__is_file.html#beast.ref.boost__beast__is_file.description)

Metafunctions are used to perform compile time checking of template types.
This type will be `std::true_type` if `T`
meets the requirements, else the type will be `std::false_type`.

##### [Example](boost__beast__is_file.html#beast.ref.boost__beast__is_file.example)

Use with `static_assert`:

```programlisting
template < class File>
void f(File& file)
{
    static_assert (is_file<File>::value,
        "File type requirements not met" );
...
```

Use with `std::enable_if` (SFINAE):

```programlisting
template < class File>
typename std::enable_if<is_file<File>::value>::type
f(File& file);
```