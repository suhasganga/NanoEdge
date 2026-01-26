#### [http::status](boost__beast__http__status.html "http::status")

##### [Synopsis](boost__beast__http__status.html#beast.ref.boost__beast__http__status.synopsis)

Defined in header `<boost/beast/http/status.hpp>`

```programlisting
enum status
```

##### [Values](boost__beast__http__status.html#beast.ref.boost__beast__http__status.values)

| Name | Description |
| --- | --- |
| `unknown` | An unknown status-code.  This value indicates that the value for the status code is not in the list of commonly recognized status codes. Callers interested in the exactly value should use the interface which provides the raw integer. |
| `continue_` |  |
| `switching_protocols` | Switching Protocols.  This status indicates that a request to switch to a new protocol was accepted and applied by the server. A successful response to a WebSocket Upgrade HTTP request will have this code. |
| `processing` |  |
| `early_hints` |  |
| `ok` |  |
| `created` |  |
| `accepted` |  |
| `non_authoritative_information` |  |
| `no_content` |  |
| `reset_content` |  |
| `partial_content` |  |
| `multi_status` |  |
| `already_reported` |  |
| `im_used` |  |
| `multiple_choices` |  |
| `moved_permanently` |  |
| `found` |  |
| `see_other` |  |
| `not_modified` |  |
| `use_proxy` |  |
| `temporary_redirect` |  |
| `permanent_redirect` |  |
| `bad_request` |  |
| `unauthorized` |  |
| `payment_required` |  |
| `forbidden` |  |
| `not_found` |  |
| `method_not_allowed` |  |
| `not_acceptable` |  |
| `proxy_authentication_required` |  |
| `request_timeout` |  |
| `conflict` |  |
| `gone` |  |
| `length_required` |  |
| `precondition_failed` |  |
| `payload_too_large` |  |
| `uri_too_long` |  |
| `unsupported_media_type` |  |
| `range_not_satisfiable` |  |
| `expectation_failed` |  |
| `i_am_a_teapot` |  |
| `misdirected_request` |  |
| `unprocessable_entity` |  |
| `locked` |  |
| `failed_dependency` |  |
| `too_early` |  |
| `upgrade_required` |  |
| `precondition_required` |  |
| `too_many_requests` |  |
| `request_header_fields_too_large` |  |
| `unavailable_for_legal_reasons` |  |
| `internal_server_error` |  |
| `not_implemented` |  |
| `bad_gateway` |  |
| `service_unavailable` |  |
| `gateway_timeout` |  |
| `http_version_not_supported` |  |
| `variant_also_negotiates` |  |
| `insufficient_storage` |  |
| `loop_detected` |  |
| `not_extended` |  |
| `network_authentication_required` |  |