On this page

* Each method has a security type indicating required API key permissions, shown next to the method name (e.g., [Place new order (TRADE)](/docs/binance-spot-api-docs/websocket-api/request-security#place-new-order-trade)).
* If unspecified, the security type is `NONE`.
* Except for `NONE`, all methods with a security type are considered `SIGNED` requests (i.e. including a `signature`), except for [listenKey management](/docs/binance-spot-api-docs/websocket-api/request-security#user-data-stream-requests).
* Secure methods require a valid API key to be specified and authenticated.
  + API keys can be created on the [API Management](https://www.binance.com/en/support/faq/360002502072) page of your Binance account.
  + **Both API key and secret key are sensitive.** Never share them with anyone.
    If you notice unusual activity in your account, immediately revoke all the keys and contact Binance support.
* API keys can be configured to allow access only to certain types of secure methods.
  + For example, you can have an API key with `TRADE` permission for trading,
    while using a separate API key with `USER_DATA` permission to monitor your order status.
  + By default, an API key cannot `TRADE`. You need to enable trading in API Management first.

| Security type | Description |
| --- | --- |
| `NONE` | Public market data |
| `TRADE` | Trading on the exchange, placing and canceling orders |
| `USER_DATA` | Private account information, such as order status and your trading history |
| `USER_STREAM` | Managing User Data Stream subscriptions |

### SIGNED request security[​](/docs/binance-spot-api-docs/websocket-api/request-security#signed-request-security "Direct link to SIGNED request security")

* `SIGNED` requests require an additional parameter: `signature`, authorizing the request.

#### Signature Case Sensitivity[​](/docs/binance-spot-api-docs/websocket-api/request-security#signature-case-sensitivity "Direct link to Signature Case Sensitivity")

* **HMAC:** Signatures generated using HMAC are **not case-sensitive**. This means the signature string can be verified regardless of letter casing.
* **RSA:** Signatures generated using RSA are **case-sensitive**.
* **Ed25519:** Signatures generated using ED25519 are also **case-sensitive**

Please consult [SIGNED request example (HMAC)](/docs/binance-spot-api-docs/websocket-api/request-security#signed-request-example-hmac), [SIGNED request example (RSA)](/docs/binance-spot-api-docs/websocket-api/request-security#signed-request-example-rsa), and [SIGNED request example (Ed25519)](/docs/binance-spot-api-docs/websocket-api/request-security#signed-request-example-ed25519) on how to compute signature, depending on which API key type you are using.

### Timing security[​](/docs/binance-spot-api-docs/websocket-api/request-security#timing-security "Direct link to Timing security")

* `SIGNED` requests also require a `timestamp` parameter which should be the current timestamp either in milliseconds or microseconds. (See [General API Information](/docs/binance-spot-api-docs/websocket-api/request-security#general-api-information))
* An additional optional parameter, `recvWindow`, specifies for how long the request stays valid and may only be specified in milliseconds.
  + `recvWindow` supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
  + If `recvWindow` is not sent, **it defaults to 5000 milliseconds**.
  + Maximum `recvWindow` is 60000 milliseconds.
* Request processing logic is as follows:

```prism-code
serverTime = getCurrentTime()  
if (timestamp < (serverTime + 1 second) && (serverTime - timestamp) <= recvWindow) {  
  // begin processing request  
  serverTime = getCurrentTime()  
  if (serverTime - timestamp) <= recvWindow {  
    // forward request to Matching Engine  
  } else {  
    // reject request  
  }  
  // finish processing request  
} else {  
  // reject request  
}
```

**Serious trading is about timing.** Networks can be unstable and unreliable,
which can lead to requests taking varying amounts of time to reach the
servers. With `recvWindow`, you can specify that the request must be
processed within a certain number of milliseconds or be rejected by the
server.

**It is recommended to use a small `recvWindow` of 5000 or less!**

### SIGNED request example (HMAC)[​](/docs/binance-spot-api-docs/websocket-api/request-security#signed-request-example-hmac "Direct link to SIGNED request example (HMAC)")

Here is a step-by-step guide on how to sign requests using an HMAC secret key.

Example API key and secret key:

| Key | Value |
| --- | --- |
| `apiKey` | `vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A` |
| `secretKey` | `NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j` |

**WARNING: DO NOT SHARE YOUR API KEY AND SECRET KEY WITH ANYONE.**

The example keys are provided here only for illustrative purposes.

Example of request with a symbol name comprised entirely of ASCII characters:

```prism-code
{  
    "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
    "method": "order.place",  
    "params": {  
        "symbol": "BTCUSDT",  
        "side": "SELL",  
        "type": "LIMIT",  
        "timeInForce": "GTC",  
        "quantity": "0.01000000",  
        "price": "52000.00",  
        "recvWindow": 100,  
        "timestamp": 1645423376532,  
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",  
        "signature": "------ FILL ME ------"  
    }  
}
```

Example of a request with a symbol name containing non-ASCII characters:

```prism-code
{  
    "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
    "method": "order.place",  
    "params": {  
        "symbol": "１２３４５６",  
        "side": "BUY",  
        "type": "LIMIT",  
        "timeInForce": "GTC",  
        "quantity": "0.01000000",  
        "price": "0.10000000",  
        "recvWindow": 5000,  
        "timestamp": 1645423376532,  
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",  
        "signature": "------ FILL ME ------"  
    }  
}
```

As you can see, the `signature` parameter is currently missing.

**Step 1: Construct the signature payload**

Take all request `params` except `signature` and **sort them in alphabetical order by parameter name**:

For the first set of example parameters (ASCII only):

| Parameter | Value |
| --- | --- |
| `apiKey` | vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A |
| `price` | 52000.00 |
| `quantity` | 0.01000000 |
| `recvWindow` | 100 |
| `side` | SELL |
| `symbol` | BTCUSDT |
| `timeInForce` | GTC |
| `timestamp` | 1645423376532 |
| `type` | LIMIT |

For the second set of example parameters (some non-ASCII characters):

| Parameter | Value |
| --- | --- |
| `apiKey` | vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A |
| `price` | 0.10000000 |
| `quantity` | 1.00000000 |
| `recvWindow` | 5000 |
| `side` | BUY |
| `symbol` | １２３４５６ |
| `timeInForce` | GTC |
| `timestamp` | 1645423376532 |
| `type` | LIMIT |

Format parameters as `parameter=value` pairs separated by `&`. Values need to be encoded in UTF-8.

For the first set of example parameters (ASCII only), the signature payload should look like this:

```prism-code
apiKey=vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT
```

For the second set of example parameters (some non-ASCII characters), the signature payload should look like this:

```prism-code
apiKey=vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT
```

**Step 2: Compute the signature**

1. Use the `secretKey` of your API key as the signing key for the HMAC-SHA-256 algorithm.
2. Sign the UTF-8 bytes of the signature payload constructed in Step 1.
3. Encode the HMAC-SHA-256 output as a hex string.

Note that `apiKey`, `secretKey`, and the payload are **case-sensitive**, while the resulting signature value is case-insensitive.

You can cross-check your signature algorithm implementation with OpenSSL:

For the first set of example parameters (ASCII only):

```prism-code
$ echo -n 'apiKey=vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT' \  
  | openssl dgst -hex -sha256 -hmac 'NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j'  
  
aa1b5712c094bc4e57c05a1a5c1fd8d88dcd628338ea863fec7b88e59fe2db24
```

For the second set of example parameters (some non-ASCII characters):

```prism-code
$ echo -n 'apiKey=vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT' \  
  | openssl dgst -hex -sha256 -hmac 'NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j'  
  
b33892ae8e687c939f4468c6268ddd4c40ac1af18ad19a064864c47bae0752cd
```

**Step 3: Add `signature` to request `params`**

Complete the request by adding the `signature` parameter with the signature string.

For the first set of example parameters (ASCII only):

```prism-code
{  
    "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
    "method": "order.place",  
    "params": {  
        "symbol": "BTCUSDT",  
        "side": "SELL",  
        "type": "LIMIT",  
        "timeInForce": "GTC",  
        "quantity": "0.01000000",  
        "price": "52000.00",  
        "recvWindow": 100,  
        "timestamp": 1645423376532,  
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",  
        "signature": "aa1b5712c094bc4e57c05a1a5c1fd8d88dcd628338ea863fec7b88e59fe2db24"  
    }  
}
```

For the second set of example parameters (some non-ASCII characters):

```prism-code
{  
    "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
    "method": "order.place",  
    "params": {  
        "symbol": "１２３４５６",  
        "side": "BUY",  
        "type": "LIMIT",  
        "timeInForce": "GTC",  
        "quantity": "1.00000000",  
        "price": "0.10000000",  
        "recvWindow": 5000,  
        "timestamp": 1645423376532,  
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",  
        "signature": "b33892ae8e687c939f4468c6268ddd4c40ac1af18ad19a064864c47bae0752cd"  
    }  
}
```

### SIGNED request example (RSA)[​](/docs/binance-spot-api-docs/websocket-api/request-security#signed-request-example-rsa "Direct link to SIGNED request example (RSA)")

Here is a step-by-step guide on how to sign requests using an RSA private key.

| Key | Value |
| --- | --- |
| `apiKey` | `CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ` |

These examples assume the private key is stored in the file `test-rsa-prv.pem`.

**WARNING: DO NOT SHARE YOUR API KEY AND PRIVATE KEY WITH ANYONE.**

The example keys are provided here only for illustrative purposes.

Example of request with a symbol name comprised entirely of ASCII characters:

```prism-code
{  
    "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
    "method": "order.place",  
    "params": {  
        "symbol": "BTCUSDT",  
        "side": "SELL",  
        "type": "LIMIT",  
        "timeInForce": "GTC",  
        "quantity": "0.01000000",  
        "price": "52000.00",  
        "recvWindow": 100,  
        "timestamp": 1645423376532,  
        "apiKey": "CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ",  
        "signature": "------ FILL ME ------"  
    }  
}
```

Example of a request with a symbol name containing non-ASCII characters:

```prism-code
{  
    "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
    "method": "order.place",  
    "params": {  
        "symbol": "１２３４５６",  
        "side": "BUY",  
        "type": "LIMIT",  
        "timeInForce": "GTC",  
        "quantity": "0.01000000",  
        "price": "0.10000000",  
        "recvWindow": 5000,  
        "timestamp": 1645423376532,  
        "apiKey": "CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ",  
        "signature": "------ FILL ME ------"  
    }  
}
```

**Step 1: Construct the signature payload**

Take all request `params` except `signature` and **sort them in alphabetical order by parameter name**:

For the first set of example parameters (ASCII only):

| Parameter | Value |
| --- | --- |
| `apiKey` | CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ |
| `price` | 52000.00 |
| `quantity` | 0.01000000 |
| `recvWindow` | 100 |
| `side` | SELL |
| `symbol` | BTCUSDT |
| `timeInForce` | GTC |
| `timestamp` | 1645423376532 |
| `type` | LIMIT |

For the second set of example parameters (some non-ASCII characters):

| Parameter | Value |
| --- | --- |
| `apiKey` | CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ |
| `price` | 0.10000000 |
| `quantity` | 1.00000000 |
| `recvWindow` | 5000 |
| `side` | BUY |
| `symbol` | １２３４５６ |
| `timeInForce` | GTC |
| `timestamp` | 1645423376532 |
| `type` | LIMIT |

Format parameters as `parameter=value` pairs separated by `&`. Values need to be encoded in UTF-8.

For the first set of example parameters (ASCII only), the signature payload should look like this:

```prism-code
apiKey=CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT
```

For the second set of example parameters (some non-ASCII characters), the signature payload should look like this:

```prism-code
apiKey=CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT
```

**Step 2: Compute the signature**

1. Sign the UTF-8 bytes of the signature payload constructed in Step 1 using the RSASSA-PKCS1-v1\_5 algorithm with SHA-256 hash function.
2. Encode the output in base64.

Note that `apiKey`, the payload, and the resulting `signature` are **case-sensitive**.

You can cross-check your signature algorithm implementation with OpenSSL:

For the first set of example parameters (ASCII only):

```prism-code
$ echo -n 'apiKey=CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT' \  
  | openssl dgst -sha256 -sign test-rsa-prv.pem \  
  | openssl enc -base64 -A  
  
OJJaf8C/3VGrU4ATTR4GiUDqL2FboSE1Qw7UnnoYNfXTXHubIl1iaePGuGyfct4NPu5oVEZCH4Q6ZStfB1w4ssgu0uiB/Bg+fBrRFfVgVaLKBdYHMvT+ljUJzqVaeoThG9oXlduiw8PbS9U8DYAbDvWN3jqZLo4Z2YJbyovyDAvDTr/oC0+vssLqP7NmlNb3fF3Bj7StmOwJvQJTbRAtzxK5PP7OQe+0mbW+D7RqVkUiSswR8qJFWTeSe4nXXNIdZdueYhF/Xf25L+KitJS5IHdIHcKfEw3MQzHFb2ZsGWkjDQwxkwr7Noi0Zaa+gFtxCuatGFm9dFIyx217pmSHtA==
```

For the second set of example parameters (some non-ASCII characters):

```prism-code
$ echo -n 'apiKey=CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT' \  
  | openssl dgst -sha256 -sign test-rsa-prv.pem \  
  | openssl enc -base64 -A  
  
F3o/79Ttvl2cVYGPfBOF3oEOcm5QcYmTYWpdVIrKve5u+8paMNDAdUE+teqMxFM9HcquetGcfuFpLYtsQames5bDx/tskGM76TWW8HaM+6tuSYBSFLrKqChfA9hQGLYGjAiflf1YBnDhY+7vNbJFusUborNOloOj+ufzP5q42PvI3H0uNy3W5V3pyfXpDGCBtfCYYr9NAqA4d+AQfyllL/zkO9h9JSdozN49t0/hWGoD2dWgSO0Je6MytKEvD4DQXGeqNlBTB6tUXcWnRW+FcaKZ4KYqnxCtb1u8rFXUYgFykr2CbcJLSmw6ydEJ3EZ/NaZopRr+cU0W2m0HZ3qucw==
```

**Step 3: Add `signature` to request `params`**

Complete the request by adding the `signature` parameter with the signature string.

For the first set of example parameters (ASCII only):

```prism-code
{  
    "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
    "method": "order.place",  
    "params": {  
        "symbol": "BTCUSDT",  
        "side": "SELL",  
        "type": "LIMIT",  
        "timeInForce": "GTC",  
        "quantity": "0.01000000",  
        "price": "52000.00",  
        "newOrderRespType": "ACK",  
        "recvWindow": 100,  
        "timestamp": 1645423376532,  
        "apiKey": "CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ",  
        "signature": "OJJaf8C/3VGrU4ATTR4GiUDqL2FboSE1Qw7UnnoYNfXTXHubIl1iaePGuGyfct4NPu5oVEZCH4Q6ZStfB1w4ssgu0uiB/Bg+fBrRFfVgVaLKBdYHMvT+ljUJzqVaeoThG9oXlduiw8PbS9U8DYAbDvWN3jqZLo4Z2YJbyovyDAvDTr/oC0+vssLqP7NmlNb3fF3Bj7StmOwJvQJTbRAtzxK5PP7OQe+0mbW+D7RqVkUiSswR8qJFWTeSe4nXXNIdZdueYhF/Xf25L+KitJS5IHdIHcKfEw3MQzHFb2ZsGWkjDQwxkwr7Noi0Zaa+gFtxCuatGFm9dFIyx217pmSHtA=="  
    }  
}
```

For the second set of example parameters (some non-ASCII characters):

```prism-code
{  
    "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
    "method": "order.place",  
    "params": {  
        "symbol": "１２３４５６",  
        "side": "SELL",  
        "type": "LIMIT",  
        "timeInForce": "GTC",  
        "quantity": "1.00000000",  
        "price": "0.10000000",  
        "recvWindow": 5000,  
        "timestamp": 1645423376532,  
        "apiKey": "CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ",  
        "signature": "F3o/79Ttvl2cVYGPfBOF3oEOcm5QcYmTYWpdVIrKve5u+8paMNDAdUE+teqMxFM9HcquetGcfuFpLYtsQames5bDx/tskGM76TWW8HaM+6tuSYBSFLrKqChfA9hQGLYGjAiflf1YBnDhY+7vNbJFusUborNOloOj+ufzP5q42PvI3H0uNy3W5V3pyfXpDGCBtfCYYr9NAqA4d+AQfyllL/zkO9h9JSdozN49t0/hWGoD2dWgSO0Je6MytKEvD4DQXGeqNlBTB6tUXcWnRW+FcaKZ4KYqnxCtb1u8rFXUYgFykr2CbcJLSmw6ydEJ3EZ/NaZopRr+cU0W2m0HZ3qucw=="  
    }  
}
```

### SIGNED Request Example (Ed25519)[​](/docs/binance-spot-api-docs/websocket-api/request-security#signed-request-example-ed25519 "Direct link to SIGNED Request Example (Ed25519)")

**Note: It is highly recommended to use Ed25519 API keys as they will provide the best performance and security out of all supported key types.**

Here is a step-by-step guide on how to sign requests using an Ed25519 private key.

| Key | Value |
| --- | --- |
| `apiKey` | `4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO` |

These examples assume the private key is stored in the file `test-ed25519-prv.pem`.

**WARNING: DO NOT SHARE YOUR API KEY AND PRIVATE KEY WITH ANYONE.**

The example keys are provided here only for illustrative purposes.

Example of request with a symbol name comprised entirely of ASCII characters:

```prism-code
{  
    "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
    "method": "order.place",  
    "params": {  
        "symbol": "BTCUSDT",  
        "side": "SELL",  
        "type": "LIMIT",  
        "timeInForce": "GTC",  
        "quantity": "0.01000000",  
        "price": "52000.00",  
        "recvWindow": 100,  
        "timestamp": 1645423376532,  
        "apiKey": "4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO",  
        "signature": "------ FILL ME ------"  
    }  
}
```

Example of a request with a symbol name containing non-ASCII characters:

```prism-code
{  
    "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
    "method": "order.place",  
    "params": {  
        "symbol": "１２３４５６",  
        "side": "BUY",  
        "type": "LIMIT",  
        "timeInForce": "GTC",  
        "quantity": "0.01000000",  
        "price": "0.10000000",  
        "recvWindow": 5000,  
        "timestamp": 1645423376532,  
        "apiKey": "4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO",  
        "signature": "------ FILL ME ------"  
    }  
}
```

**Step 1: Construct the signature payload**

Take all request `params` except `signature` and **sort them in alphabetical order by parameter name**:

For the first set of example parameters (ASCII only):

| Parameter | Value |
| --- | --- |
| `apiKey` | 4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO |
| `price` | 52000.00 |
| `quantity` | 0.01000000 |
| `recvWindow` | 100 |
| `side` | SELL |
| `symbol` | BTCUSDT |
| `timeInForce` | GTC |
| `timestamp` | 1645423376532 |
| `type` | LIMIT |

For the second set of example parameters (some non-ASCII characters):

| Parameter | Value |
| --- | --- |
| `apiKey` | 4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO |
| `price` | 0.20000000 |
| `quantity` | 1.00000000 |
| `recvWindow` | 5000 |
| `side` | SELL |
| `symbol` | １２３４５６ |
| `timeInForce` | GTC |
| `timestamp` | 1668481559918 |
| `type` | LIMIT |

Format parameters as `parameter=value` pairs separated by `&`. Values need to be encoded in UTF-8.

For the first set of example parameters (ASCII only), the signature payload should look like this:

```prism-code
apiKey=4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT
```

For the second set of example parameters (some non-ASCII characters), the signature payload should look like this:

```prism-code
apiKey=4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT
```

**Step 2: Compute the signature**

1. Sign the UTF-8 bytes of your signature payload constructed in Step 1 using the Ed25519 private key.
2. Encode the output in base64.

Note that `apiKey`, the payload, and the resulting `signature` are **case-sensitive**.

You can cross-check your signature algorithm implementation with OpenSSL:

For the first set of example parameters (ASCII only):

```prism-code
echo -n "apiKey=4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT" \  
  | openssl dgst -sign ./test-ed25519-prv.pem \  
  | openssl enc -base64 -A  
  
EocljwPl29jDxWYaaRaOo4pJ9wEblFbklJvPugNscLLuKd5vHM2grWjn1z+rY0aJ7r/44enxHL6mOAJuJ1kqCg==
```

For the second set of example parameters (some non-ASCII characters):

```prism-code
echo -n "apiKey=4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT" \  
  | openssl dgst -sign ./test-ed25519-prv.pem \  
  | openssl enc -base64 -A  
  
dtNHJeyKry+cNjiGv+sv5kynO9S40tf8k7D5CfAEQAp0s2scunZj+ovJdz2OgW8XhkB9G3/HmASkA9uY9eyFCA==
```

**Step 3: Add the signature to request `params`**

For the first set of example parameters (ASCII only):

```prism-code
{  
    "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
    "method": "order.place",  
    "params": {  
        "symbol": "BTCUSDT",  
        "side": "SELL",  
        "type": "LIMIT",  
        "timeInForce": "GTC",  
        "quantity": "0.01000000",  
        "price": "52000.00",  
        "newOrderRespType": "ACK",  
        "recvWindow": 100,  
        "timestamp": 1645423376532,  
        "apiKey": "4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO",  
        "signature": "EocljwPl29jDxWYaaRaOo4pJ9wEblFbklJvPugNscLLuKd5vHM2grWjn1z+rY0aJ7r/44enxHL6mOAJuJ1kqCg=="  
    }  
}
```

For the second set of example parameters (some non-ASCII characters):

```prism-code
{  
    "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  
    "method": "order.place",  
    "params": {  
        "symbol": "１２３４５６",  
        "side": "SELL",  
        "type": "LIMIT",  
        "timeInForce": "GTC",  
        "quantity": "1.00000000",  
        "price": "0.10000000",  
        "recvWindow": 5000,  
        "timestamp": 1645423376532,  
        "apiKey": "4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO",  
        "signature": "dtNHJeyKry+cNjiGv+sv5kynO9S40tf8k7D5CfAEQAp0s2scunZj+ovJdz2OgW8XhkB9G3/HmASkA9uY9eyFCA=="  
    }  
}
```

Here is a sample Python script performing all the steps above:

```prism-code
#!/usr/bin/env python3  
  
import base64  
import time  
import json  
from cryptography.hazmat.primitives.serialization import load_pem_private_key  
from websocket import create_connection  
  
# Set up authentication  
API_KEY='put your own API Key here'  
PRIVATE_KEY_PATH='test-prv-key.pem'  
  
# Load the private key.  
# In this example the key is expected to be stored without encryption,  
# but we recommend using a strong password for improved security.  
with open(PRIVATE_KEY_PATH, 'rb') as f:  
  private_key = load_pem_private_key(data=f.read(), password=None)  
  
# Set up the request parameters  
params = {  
    'apiKey':       API_KEY,  
    'symbol':       '１２３４５６',  
    'side':         'SELL',  
    'type':         'LIMIT',  
    'timeInForce':  'GTC',  
    'quantity':     '1.0000000',  
    'price':        '0.10000000',  
    'recvWindow':   5000  
}  
  
# Timestamp the request  
timestamp = int(time.time() * 1000) # UNIX timestamp in milliseconds  
params['timestamp'] = timestamp  
  
# Sort parameters alphabetically by name  
params = dict(sorted(params.items()))  
  
# Compute the signature payload  
payload = '&'.join([f"{k}={v}" for k,v in params.items()]) # no percent encoding here!  
  
# Sign the request  
signature = base64.b64encode(private_key.sign(payload.encode('UTF-8')))  
params['signature'] = signature.decode('ASCII')  
  
# Send the request  
request = {  
    'id': 'my_new_order',  
    'method': 'order.place',  
    'params': params  
}  
  
ws = create_connection("wss://ws-api.binance.com:443/ws-api/v3")  
ws.send(json.dumps(request))  
result =  ws.recv()  
ws.close()  
  
print(result)
```