##### [websocket::stream::set\_option](set_option.html "websocket::stream::set_option")

Set the option value.

```programlisting
template<
    class Option>
void
set_option(
    Option opt);
  » more...
```

Set the timeout option.

```programlisting
void
set_option(
    timeout const& opt);
  » more...
```

Set the permessage-deflate extension options.

```programlisting
void
set_option(
    permessage_deflate const& o);
  » more...
```