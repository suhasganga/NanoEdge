##### [zlib::deflate\_stream::reset](reset.html "zlib::deflate_stream::reset")

Reset the stream and compression settings.

```programlisting
void
reset(
    int level,
    int windowBits,
    int memLevel,
    Strategy strategy);
  » more...
```

Reset the stream without deallocating memory.

```programlisting
void
reset();
  » more...
```