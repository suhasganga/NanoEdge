##### [websocket::stream::get\_option](get_option.html "websocket::stream::get_option")

Get the option value.

```programlisting
template<
    class Option>
void
get_option(
    Option& opt);
  » more...
```

Get the timeout option.

```programlisting
void
get_option(
    timeout& opt);
  » more...
```

Get the permessage-deflate extension options.

```programlisting
void
get_option(
    permessage_deflate& o);
  » more...
```