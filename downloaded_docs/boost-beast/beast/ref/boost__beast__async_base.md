#### [async\_base](boost__beast__async_base.html "async_base")

Base class to assist writing composed operations.

##### [Synopsis](boost__beast__async_base.html#beast.ref.boost__beast__async_base.synopsis)

Defined in header `<boost/beast/core/async_base.hpp>`

```programlisting
template<
    class Handler,
    class Executor1,
    class Allocator = std::allocator<void>>
class async_base
```

##### [Types](boost__beast__async_base.html#beast.ref.boost__beast__async_base.types)

| Name | Description |
| --- | --- |
| **[allocator\_type](boost__beast__async_base/allocator_type.html "async_base::allocator_type")** | The type of allocator associated with this object. |
| **[cancellation\_slot\_type](boost__beast__async_base/cancellation_slot_type.html "async_base::cancellation_slot_type")** | The type of cancellation\_slot associated with this object. |
| **[executor\_type](boost__beast__async_base/executor_type.html "async_base::executor_type")** | The type of executor associated with this object. |
| **[immediate\_executor\_type](boost__beast__async_base/immediate_executor_type.html "async_base::immediate_executor_type")** | The type of the immediate executor associated with this object. |

##### [Member Functions](boost__beast__async_base.html#beast.ref.boost__beast__async_base.member_functions)

| Name | Description |
| --- | --- |
| **[async\_base](boost__beast__async_base/async_base.html "async_base::async_base") [constructor]** | Constructor.  — Move Constructor.  — |
| **[complete](boost__beast__async_base/complete.html "async_base::complete")** | Invoke the final completion handler, maybe using post. |
| **[complete\_now](boost__beast__async_base/complete_now.html "async_base::complete_now")** | Invoke the final completion handler. |
| **[get\_allocator](boost__beast__async_base/get_allocator.html "async_base::get_allocator")** | Returns the allocator associated with this object. |
| **[get\_cancellation\_slot](boost__beast__async_base/get_cancellation_slot.html "async_base::get_cancellation_slot")** | Returns the cancellation\_slot associated with this object. |
| **[get\_executor](boost__beast__async_base/get_executor.html "async_base::get_executor")** | Returns the executor associated with this object. |
| **[get\_immediate\_executor](boost__beast__async_base/get_immediate_executor.html "async_base::get_immediate_executor")** | Returns the immediate executor associated with this handler. |
| **[handler](boost__beast__async_base/handler.html "async_base::handler")** | Returns the handler associated with this object. |
| **[operator=](boost__beast__async_base/operator_eq_.html "async_base::operator=")** |  |
| **[release\_handler](boost__beast__async_base/release_handler.html "async_base::release_handler")** | Returns ownership of the handler associated with this object. |
| **[set\_allowed\_cancellation](boost__beast__async_base/set_allowed_cancellation.html "async_base::set_allowed_cancellation")** | Set the allowed cancellation types, default is `terminal`. |
| **[~async\_base](boost__beast__async_base/_dtor_async_base.html "async_base::~async_base") [destructor]** |  |

##### [Description](boost__beast__async_base.html#beast.ref.boost__beast__async_base.description)

A function object submitted to intermediate initiating functions during a
composed operation may derive from this type to inherit all of the boilerplate
to forward the executor, allocator, and legacy customization points associated
with the completion handler invoked at the end of the composed operation.

The composed operation must be typical; that is, associated with one executor
of an I/O object, and invoking a caller-provided completion handler when
the operation is finished. Classes derived from [`async_base`](boost__beast__async_base.html "async_base") will acquire these properties:

* Ownership of the final completion handler provided upon construction.
* If the final handler has an associated allocator, this allocator will
  be propagated to the composed operation subclass. Otherwise, the associated
  allocator will be the type specified in the allocator template parameter,
  or the default of `std::allocator<void>` if the parameter is omitted.
* If the final handler has an associated executor, then it will be used
  as the executor associated with the composed operation. Otherwise, the
  specified `Executor1` will
  be the type of executor associated with the composed operation.
* An instance of `net::executor_work_guard` for the instance
  of `Executor1` shall be
  maintained until either the final handler is invoked, or the operation
  base is destroyed, whichever comes first.
* Calls to the legacy customization point `asio_handler_is_continuation`
  which use argument-dependent lookup, will be forwarded to the legacy
  customization points associated with the handler.

##### [Example](boost__beast__async_base.html#beast.ref.boost__beast__async_base.example)

The following code demonstrates how [`async_base`](boost__beast__async_base.html "async_base") may be be used to assist
authoring an asynchronous initiating function, by providing all of the boilerplate
to manage the final completion handler in a way that maintains the allocator
and executor associations:

```programlisting
// Asynchronously read into a buffer until the buffer is full, or an error occurs
template < class AsyncReadStream, class ReadHandler>
typename net::async_result<ReadHandler, void(error_code, std::size_t)>::return_type
async_read(AsyncReadStream& stream, net::mutable_buffer buffer, ReadHandler&& handler)
{
    using handler_type = BOOST_ASIO_HANDLER_TYPE(ReadHandler, void (error_code, std::size_t));
    using base_type = async_base<handler_type, typename AsyncReadStream::executor_type>;

    struct op : base_type
    {
        AsyncReadStream& stream_;
        net::mutable_buffer buffer_;
        std::size_t total_bytes_transferred_;

        op(
            AsyncReadStream& stream,
            net::mutable_buffer buffer,
            handler_type& handler)
            : base_type(std::move(handler), stream.get_executor())
            , stream_(stream)
            , buffer_(buffer)
            , total_bytes_transferred_(0)
        {
            (*this)({}, 0, false ); // start the operation
        }

        void operator()(error_code ec, std::size_t bytes_transferred, bool is_continuation = true )
        {
            // Adjust the count of bytes and advance our buffer
            total_bytes_transferred_ += bytes_transferred;
            buffer_ = buffer_ + bytes_transferred;

            // Keep reading until buffer is full or an error occurs
            if (! ec && buffer_.size() > 0)
                return stream_.async_read_some(buffer_, std::move(* this ));

            // Call the completion handler with the result. If `is_continuation` is
            // false, which happens on the first time through this function, then
            // `net::post` will be used to call the completion handler, otherwise
            // the completion handler will be invoked directly.

            this->complete(is_continuation, ec, total_bytes_transferred_);
        }
    };

    net::async_completion<ReadHandler, void(error_code, std::size_t)> init{handler};
    op(stream, buffer, init.completion_handler);
    return init.result.get();
}
```

Data members of composed operations implemented as completion handlers do
not have stable addresses, as the composed operation object is move constructed
upon each call to an initiating function. For most operations this is not
a problem. For complex operations requiring stable temporary storage, the
class [`stable_async_base`](boost__beast__stable_async_base.html "stable_async_base") is provided which
offers additional functionality:

* The free function [`allocate_stable`](boost__beast__allocate_stable.html "allocate_stable") may be used
  to allocate one or more temporary objects associated with the composed
  operation.
* Memory for stable temporary objects is allocated using the allocator
  associated with the composed operation.
* Stable temporary objects are automatically destroyed, and the memory
  freed using the associated allocator, either before the final completion
  handler is invoked (a Networking requirement) or when the composed operation
  is destroyed, whichever occurs first.

##### [Temporary Storage Example](boost__beast__async_base.html#beast.ref.boost__beast__async_base.temporary_storage_example)

The following example demonstrates how a composed operation may store a temporary
object.

##### [Template Parameters](boost__beast__async_base.html#beast.ref.boost__beast__async_base.template_parameters)

| Type | Description |
| --- | --- |
| `Handler` | The type of the completion handler to store. This type must meet the requirements of *CompletionHandler*. |
| `Executor1` | The type of the executor used when the handler has no associated executor. An instance of this type must be provided upon construction. The implementation will maintain an executor work guard and a copy of this instance. |
| `Allocator` | The allocator type to use if the handler does not have an associated allocator. If this parameter is omitted, then `std::allocator<void>` will be used. If the specified allocator is not default constructible, an instance of the type must be provided upon construction. |

##### [See Also](boost__beast__async_base.html#beast.ref.boost__beast__async_base.see_also)

[`stable_async_base`](boost__beast__stable_async_base.html "stable_async_base")