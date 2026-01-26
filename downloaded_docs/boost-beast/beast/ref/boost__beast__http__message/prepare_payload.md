##### [http::message::prepare\_payload](prepare_payload.html "http::message::prepare_payload")

Prepare the message payload fields for the body.

###### [Synopsis](prepare_payload.html#beast.ref.boost__beast__http__message.prepare_payload.synopsis)

```programlisting
void
prepare_payload();
```

###### [Description](prepare_payload.html#beast.ref.boost__beast__http__message.prepare_payload.description)

This function will adjust the Content-Length and Transfer-Encoding field
values based on the properties of the body.

###### [Example](prepare_payload.html#beast.ref.boost__beast__http__message.prepare_payload.example)

```programlisting
request<string_body> req{verb::post, "/" };
req.set(field::user_agent, "Beast" );
req.body() = "Hello, world!" ;
req.prepare_payload();
```

###### [Remarks](prepare_payload.html#beast.ref.boost__beast__http__message.prepare_payload.remarks)

This function is not necessary to call in the following situations:

* The request doesn't contain a body, such as in a GET or HEAD request.
* The Content-Length and Transfer-Encoding are set manually.