##### [zlib::deflate\_stream::tune](tune.html "zlib::deflate_stream::tune")

Fine tune internal compression parameters.

###### [Synopsis](tune.html#beast.ref.boost__beast__zlib__deflate_stream.tune.synopsis)

```programlisting
void
tune(
    int good_length,
    int max_lazy,
    int nice_length,
    int max_chain);
```

###### [Description](tune.html#beast.ref.boost__beast__zlib__deflate_stream.tune.description)

Compression parameters should only be tuned by someone who understands
the algorithm used by zlib's deflate for searching for the best matching
string, and even then only by the most fanatic optimizer trying to squeeze
out the last compressed bit for their specific input data. Read the deflate.c
source code (ZLib) for the meaning of the max\_lazy, good\_length, nice\_length,
and max\_chain parameters.