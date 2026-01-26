##### [test::handler::operator()](operator_lp__rp_.html "test::handler::operator()")

```programlisting
template<
    class... Args>
void
operator()(
    error_code ec,
    Args&& ...);
  » more...

void
operator()();
  » more...

template<
    class Arg0,
    class... Args,
    class = typename std::enable_if<            ! std::is_convertible<Arg0, error_code>::value>::type>
void
operator()(
    Arg0&&,
    Args&& ...);
  » more...
```