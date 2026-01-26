## Chapter 1. Boost.Beast

### Vinnie Falco

Copyright © 2016-2019 Vinnie
Falco

Distributed under the Boost Software License, Version 1.0. (See accompanying
file LICENSE\_1\_0.txt or copy at <http://www.boost.org/LICENSE_1_0.txt>)

**Table of Contents**

[Reference](beast/quickref.html)

[Release Notes](beast/release_notes.html)

[Beast API Version](beast/beast_api_version.html)

[Introduction](beast/introduction.html)
:   [Requirements](beast/introduction.html#beast.introduction.requirements)

    [Reporting Bugs](beast/introduction.html#beast.introduction.reporting_bugs)

    [Credits](beast/introduction.html#beast.introduction.credits)

[Quick Look](beast/quick_start.html)
:   [Simple HTTP Client 💡](beast/quick_start/http_client.html)

    [Simple WebSocket Client 💡](beast/quick_start/websocket_client.html)

    [Security Review (Bishop Fox) 🎦](beast/quick_start/security_review_bishop_fox.html)

    [WebSocket (Autobahn|Testsuite)](beast/quick_start/websocket_autobahn_testsuite.html)

[Examples](beast/examples.html)
:   [Clients](beast/examples.html#beast.examples.clients)

    [Servers](beast/examples.html#beast.examples.servers)

    [Servers (Advanced)](beast/examples.html#beast.examples.servers_advanced)

    [Chat Server 🎦](beast/examples.html#beast.examples.chat_server)

[Networking](beast/using_io.html)
:   [Refresher](beast/using_io/asio_refresher.html)

    [Streams](beast/using_io/stream_types.html)

    [Timeouts 💡](beast/using_io/timeouts.html)

    [Rate Limiting 💡](beast/using_io/rate_limiting.html)

    [Layered Streams](beast/using_io/layered_streams.html)
    :   [Counted Stream 💡](beast/using_io/layered_streams/counted_stream_example.html)

    [Buffer Types](beast/using_io/buffer_types.html)

    [Files](beast/using_io/files.html)

    [Writing Composed Operations](beast/using_io/writing_composed_operations.html)
    :   [Echo 💡](beast/using_io/writing_composed_operations/echo.html)

        [Detect SSL 💡](beast/using_io/writing_composed_operations/detect_ssl.html)

    [SSL/TLS Certificate](beast/using_io/ssl_tls_certificate.html)

    [SSL/TLS Shutdown](beast/using_io/ssl_tls_shutdown.html)
    :   [error::stream\_truncated](beast/using_io/ssl_tls_shutdown.html#beast.using_io.ssl_tls_shutdown.error_stream_truncated)

[Configuration](beast/config.html)
:   [Configuration Preprocessor Definitions](beast/config/configuration_preprocessor_defin.html)

[HTTP](beast/using_http.html)
:   [Protocol Primer](beast/using_http/protocol_primer.html)

    [Message Containers](beast/using_http/message_containers.html)

    [Message Stream Operations](beast/using_http/message_stream_operations.html)

    [Serializer Stream Operations](beast/using_http/serializer_stream_operations.html)

    [Parser Stream Operations](beast/using_http/parser_stream_operations.html)
    :   [Incremental Read 💡](beast/using_http/parser_stream_operations/incremental_read.html)

        [Reading large response body 💡](beast/using_http/parser_stream_operations/read_large_response_body.html)

    [Buffer-Oriented Serializing](beast/using_http/buffer_oriented_serializing.html)
    :   [Write To std::ostream 💡](beast/using_http/buffer_oriented_serializing.html#beast.using_http.buffer_oriented_serializing.write_to_std_ostream)

    [Buffer-Oriented Parsing](beast/using_http/buffer_oriented_parsing.html)
    :   [Read From std::istream 💡](beast/using_http/buffer_oriented_parsing.html#beast.using_http.buffer_oriented_parsing.read_from_std_istream)

    [Chunked Encoding](beast/using_http/chunked_encoding.html)

    [Custom Body Types](beast/using_http/custom_body_types.html)
    :   [File Body 💡](beast/using_http/custom_body_types.html#beast.using_http.custom_body_types.file_body)

    [Custom Parsers](beast/using_http/custom_parsers.html)

[HTTP Examples](beast/more_examples.html)
:   [Change Body Type 💡](beast/more_examples/change_body_type.html)

    [Expect 100-continue (Client) 💡](beast/more_examples/expect_100_continue_client.html)

    [Expect 100-continue (Server) 💡](beast/more_examples/expect_100_continue_server.html)

    [HEAD request (Client) 💡](beast/more_examples/head_request_client.html)

    [HEAD response (Server) 💡](beast/more_examples/head_response_server.html)

    [HTTP Relay 💡](beast/more_examples/http_relay.html)

    [Send Child Process Output 💡](beast/more_examples/send_child_process_output.html)

[WebSocket](beast/using_websocket.html)
:   [Connecting](beast/using_websocket/establishing_connections.html)

    [Handshaking](beast/using_websocket/handshaking.html)

    [Decorator](beast/using_websocket/decorator.html)

    [Messages](beast/using_websocket/messages.html)

    [Control Frames](beast/using_websocket/control_frames.html)

    [Timeouts](beast/using_websocket/timeouts.html)

    [Teardown](beast/using_websocket/teardown.html)

    [Notes](beast/using_websocket/notes.html)

[Concepts](beast/concepts.html)
:   [Body](beast/concepts/Body.html)

    [BodyReader](beast/concepts/BodyReader.html)

    [BodyWriter](beast/concepts/BodyWriter.html)

    [BufferSequence](beast/concepts/BufferSequence.html)

    [BuffersGenerator](beast/concepts/BuffersGenerator.html)

    [DynamicBuffer](beast/concepts/DynamicBuffer.html)

    [Fields](beast/concepts/Fields.html)

    [FieldsWriter](beast/concepts/FieldsWriter.html)

    [File](beast/concepts/File.html)

    [RatePolicy](beast/concepts/RatePolicy.html)

    [Streams](beast/concepts/streams.html)

[Design Choices](beast/design_choices.html)
:   [HTTP Message Container 🎦](beast/design_choices/http_message_container.html)

    [HTTP Comparison to Other Libraries](beast/design_choices/http_comparison_to_other_librari.html)

    [Comparison to Zaphoyd Studios WebSocket++](beast/design_choices/comparison_to_zaphoyd_studios_we.html)

    [FAQ](beast/design_choices/faq.html)

[Index](beast/index.html)

★ indicates a new or updated section in
this version.

💡 contains example source code.

🎦 contains video presentation content

## [Documentation](index.html#beast.documentation)

Visit <https://boost.org/libs/beast>
for complete documentation.