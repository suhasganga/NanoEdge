###### [test::handler::operator() (3 of 3 overloads)](overload3.html "test::handler::operator() (3 of 3 overloads)")

###### [Synopsis](overload3.html#beast.ref.boost__beast__test__handler.operator_lp__rp_.overload3.synopsis)

```programlisting
template<
    class Arg0,
    class... Args,
    class = typename std::enable_if<            ! std::is_convertible<Arg0, error_code>::value>::type>
void
operator()(
    Arg0&&,
    Args&& ...);
```