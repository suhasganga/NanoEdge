### [Writing Composed Operations](writing_composed_operations.html "Writing Composed Operations")

Asynchronous operations are started by calling a free function or member
function known as an asynchronous *[initiating
function](../../../../../../doc/html/boost_asio/reference/asynchronous_operations.html)*. This function accepts parameters specific to
the operation as well as a [*CompletionToken*](../../../../../../doc/html/boost_asio/reference/asynchronous_operations.html#boost_asio.reference.asynchronous_operations.completion_tokens_and_handlers).
The token is either a completion handler, or a type defining how the caller
is informed of the asynchronous operation result. Networking provides the
special tokens [`net::use_future`](../../../../../../doc/html/boost_asio/reference/use_future_t.html)
and [`net::yield_context`](../../../../../../doc/html/boost_asio/reference/yield_context.html)
for using futures and coroutines respectively. This system of customizing
the return value and method of completion notification is known as the *Universal
Asynchronous Model* described in [**N3747**](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2013/n3747.pdf), and a built in to [Networking
TS](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2018/n4771.pdf). Here is an example of an initiating function which reads a line
from the stream and echoes it back. This function is developed further in
the next section:

```programlisting
template<
    class AsyncStream,
    class DynamicBuffer,
    class CompletionToken>
auto
async_echo (AsyncStream& stream, DynamicBuffer& buffer, CompletionToken&& token)
```

|  |  |
| --- | --- |
| [Tip] | Tip |
| This initiating function receives the dynamic buffer by lvalue-reference, instead of by rvalue-reference as specified in networking. An explanation for this difference may be found in [[P1100R0] Efficient composition with DynamicBuffer](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2018/p1100r0.html). |

Authors using Beast can reuse the library's primitives to create their own
initiating functions for performing a series of other, intermediate asynchronous
operations before invoking a final completion handler. The set of intermediate
actions produced by an initiating function is known as a [*composed
operation*](http://blog.think-async.com/2009/08/composed-operations-coroutines-and-code.html). To ensure full interoperability and well-defined
behavior, [Boost.Asio](../../../../../../libs/asio/index.html) imposes
requirements on the implementation of composed operations. These classes
and functions make it easier to develop initiating functions and their composed
operations:

**Table 1.13. Asynchronous Helpers**

| Name | Description |
| --- | --- |
| [`async_base`](../ref/boost__beast__async_base.html "async_base") [`stable_async_base`](../ref/boost__beast__stable_async_base.html "stable_async_base") | This class is designed to be used as a base class when authoring composed asynchronous operations expressed as an intermediate completion handler. This eliminates the need for the extensive boilerplate to propagate the associated executor and the associated allocator. |
| [`allocate_stable`](../ref/boost__beast__allocate_stable.html "allocate_stable") | For composed operation algorithms which need stable storage for temporary objects, this function may be used. Memory for the stable storage is allocated using the allocator associated with the final completion handler. The implementation automatically destroys the temporary object before the final completion handler is invoked, or when the intermediate completion handler is destroyed. |
| [`bind_handler`](../ref/boost__beast__bind_handler.html "bind_handler") | This function creates a new handler which, when invoked, calls the original handler with the list of bound arguments. Any parameters passed in the invocation will be substituted for placeholders present in the list of bound arguments. Parameters which are not matched to placeholders are silently discarded.  The passed handler and arguments are forwarded into the returned handler, whose associated allocator and associated executor will be the same as those of the original handler. |
| [`bind_front_handler`](../ref/boost__beast__bind_front_handler.html "bind_front_handler") | This function creates a new handler which, when invoked, calls the original handler with the list of bound arguments, along with the list of invoked arguments at either the front or the back of the argument list. Placeholders are not supported.  The passed handler and arguments are forwarded into the returned handler, whose associated allocator and associated executor will will be the same as those of the original handler. |
| [`saved_handler`](../ref/boost__beast__saved_handler.html "saved_handler") | This wrapper safely stores a completion handler so it may be invoked later, allowing an implementation to "pause" an operation until some condition is met. |