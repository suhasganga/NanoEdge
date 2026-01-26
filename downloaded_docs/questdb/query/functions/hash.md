On this page

Hash functions generate fixed-size string outputs from variable-length inputs.

These functions are useful for data integrity verification, checksums, and data anonymization.

## Supported functions[​](#supported-functions "Direct link to Supported functions")

* [`md5()`](#md5) – Generates a 128-bit (32 character) hash value
* [`sha1()`](#sha1) – Generates a 160-bit (40 character) hash value
* [`sha256()`](#sha256) – Generates a 256-bit (64 character) hash value

## Function reference[​](#function-reference "Direct link to Function reference")

### md5()[​](#md5 "Direct link to md5()")

Calculates an MD5 hash of the input value and returns it as a hexadecimal string.

**Arguments:**

* String, varchar, or binary value

**Return value:**

* A 32-character hexadecimal string representing the MD5 hash
* NULL if the input is NULL

**Examples:**

md5() with string input[Demo this query](https://demo.questdb.io/?query=SELECT%20md5('abc')%3B%0A--%20Returns%3A%20'900150983cd24fb0d6963f7d28e17f72'%0A%0ASELECT%20md5('')%3B%0A--%20Returns%3A%20'd41d8cd98f00b204e9800998ecf8427e'&executeQuery=true)

```prism-code
SELECT md5('abc');  
-- Returns: '900150983cd24fb0d6963f7d28e17f72'  
  
SELECT md5('');  
-- Returns: 'd41d8cd98f00b204e9800998ecf8427e'
```

md5() with UTF-8 input[Demo this query](https://demo.questdb.io/?query=SELECT%20md5('Hello%2C%20world!')%3B%0A--%20Returns%3A%20'6cd3556deb0da54bca060b4c39479839'&executeQuery=true)

```prism-code
SELECT md5('Hello, world!');  
-- Returns: '6cd3556deb0da54bca060b4c39479839'
```

### sha1()[​](#sha1 "Direct link to sha1()")

Calculates a SHA1 hash of the input value and returns it as a hexadecimal string.

**Arguments:**

* String, varchar, or binary value

**Return value:**

* A 40-character hexadecimal string representing the SHA1 hash
* NULL if the input is NULL

**Examples:**

sha1() with string input[Demo this query](https://demo.questdb.io/?query=SELECT%20sha1('abc')%3B%0A--%20Returns%3A%20'a9993e364706816aba3e25717850c26c9cd0d89d'%0A%0ASELECT%20sha1('')%3B%0A--%20Returns%3A%20'da39a3ee5e6b4b0d3255bfef95601890afd80709'&executeQuery=true)

```prism-code
SELECT sha1('abc');  
-- Returns: 'a9993e364706816aba3e25717850c26c9cd0d89d'  
  
SELECT sha1('');  
-- Returns: 'da39a3ee5e6b4b0d3255bfef95601890afd80709'
```

sha1() with UTF-8 input[Demo this query](https://demo.questdb.io/?query=SELECT%20sha1('Hello%2C%20world!')%3B%0A--%20Returns%3A%20'943a702d06f34599aee1f8da8ef9f7296031d699'&executeQuery=true)

```prism-code
SELECT sha1('Hello, world!');  
-- Returns: '943a702d06f34599aee1f8da8ef9f7296031d699'
```

### sha256()[​](#sha256 "Direct link to sha256()")

Calculates a SHA256 hash of the input value and returns it as a hexadecimal string.

**Arguments:**

* String, varchar, or binary value

**Return value:**

* A 64-character hexadecimal string representing the SHA256 hash
* NULL if the input is NULL

**Examples:**

sha256() with string input[Demo this query](https://demo.questdb.io/?query=SELECT%20sha256('abc')%3B%0A--%20Returns%3A%20'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'%0A%0ASELECT%20sha256('')%3B%0A--%20Returns%3A%20'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'&executeQuery=true)

```prism-code
SELECT sha256('abc');  
-- Returns: 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'  
  
SELECT sha256('');  
-- Returns: 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
```

sha256() with UTF-8 input[Demo this query](https://demo.questdb.io/?query=SELECT%20sha256('Hello%2C%20world!')%3B%0A--%20Returns%3A%20'315f5bdb76d078c43b8ac0064e4a0164612b1fce77c869345bfc94c75894edd3'&executeQuery=true)

```prism-code
SELECT sha256('Hello, world!');  
-- Returns: '315f5bdb76d078c43b8ac0064e4a0164612b1fce77c869345bfc94c75894edd3'
```

## Notes and restrictions[​](#notes-and-restrictions "Direct link to Notes and restrictions")

### Input handling[​](#input-handling "Direct link to Input handling")

* All hash functions support string, varchar, and binary inputs
* Empty strings produce a valid hash value
* NULL inputs always return NULL outputs
* UTF-8 strings are fully supported

### Thread safety[​](#thread-safety "Direct link to Thread safety")

* Hash functions are not thread-safe
* Each function instance maintains its own internal state

### Output characteristics[​](#output-characteristics "Direct link to Output characteristics")

* Output is always lowercase hexadecimal
* Output length is fixed regardless of input size:
  + MD5: 32 characters
  + SHA1: 40 characters
  + SHA256: 64 characters

### Implementation details[​](#implementation-details "Direct link to Implementation details")

* Uses Java's built-in MessageDigest implementations
* Supported algorithms are guaranteed to be available on all Java platforms
* Processes input in a single pass

### Common use cases[​](#common-use-cases "Direct link to Common use cases")

#### Data integrity verification[​](#data-integrity-verification "Direct link to Data integrity verification")

```prism-code
SELECT   
    filename,  
    sha256(content) = expected_hash as is_valid  
FROM files;
```

#### Anonymizing sensitive data[​](#anonymizing-sensitive-data "Direct link to Anonymizing sensitive data")

```prism-code
SELECT   
    md5(email) as hashed_email,  
    count(*) as user_count  
FROM users  
GROUP BY hashed_email;
```

#### Binary data hashing[​](#binary-data-hashing "Direct link to Binary data hashing")

```prism-code
SELECT   
    file_id,  
    sha1(binary_content) as content_hash  
FROM binary_files;
```