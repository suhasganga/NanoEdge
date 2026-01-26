On this page

This page describes the available functions to assist with working with binary
data.

## base64[​](#base64 "Direct link to base64")

`base64(data, maxLength)` encodes raw binary data using the base64 encoding into
a string with a maximum length defined by `maxLength`.

**Arguments:**

* `data` is the binary data to be encoded.
* `maxLength` is the intended maximum length of the encoded string.

**Return value:**

Return value type is `string`.

**Example:**

```prism-code
SELECT base64(rnd_bin(), 20);  
-- `rnd_bin` can be used to generate random binary data.
```

| base64 |
| --- |
| q7QDHliR4V1OsAEUVCFwDDTerbI= |

## See also[​](#see-also "Direct link to See also")

[`rnd_bin`](/docs/query/functions/random-value-generator/#rnd_bin) can be
used to generate random binary data.