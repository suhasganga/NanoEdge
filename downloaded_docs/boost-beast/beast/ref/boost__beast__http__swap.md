#### [http::swap](boost__beast__http__swap.html "http::swap")

Swap two header objects.

```programlisting
template<
    bool isRequest,
    class Fields>
void
swap(
    header< isRequest, Fields >& m1,
    header< isRequest, Fields >& m2);
  » more...
```

Swap two message objects.

```programlisting
template<
    bool isRequest,
    class Body,
    class Fields>
void
swap(
    message< isRequest, Body, Fields >& m1,
    message< isRequest, Body, Fields >& m2);
  » more...
```