#### [stable\_async\_base](boost__beast__stable_async_base.html "stable_async_base")

Base class to provide completion handler boilerplate for composed operations.

##### [Synopsis](boost__beast__stable_async_base.html#beast.ref.boost__beast__stable_async_base.synopsis)

Defined in header `<boost/beast/core/async_base.hpp>`

```programlisting
template<
    class Handler,
    class Executor1,
    class Allocator = std::allocator<void>>
class stable_async_base :
    public async_base< Handler, Executor1, std::allocator< void > >
```

##### [Types](boost__beast__stable_async_base.html#beast.ref.boost__beast__stable_async_base.types)

| Name | Description |
| --- | --- |
| **[allocator\_type](boost__beast__stable_async_base/allocator_type.html "stable_async_base::allocator_type")** | The type of allocator associated with this object. |
| **[cancellation\_slot\_type](boost__beast__stable_async_base/cancellation_slot_type.html "stable_async_base::cancellation_slot_type")** | The type of cancellation\_slot associated with this object. |
| **[executor\_type](boost__beast__stable_async_base/executor_type.html "stable_async_base::executor_type")** | The type of executor associated with this object. |
| **[immediate\_executor\_type](boost__beast__stable_async_base/immediate_executor_type.html "stable_async_base::immediate_executor_type")** | The type of the immediate executor associated with this object. |

##### [Member Functions](boost__beast__stable_async_base.html#beast.ref.boost__beast__stable_async_base.member_functions)

| Name | Description |
| --- | --- |
| **[complete](boost__beast__stable_async_base/complete.html "stable_async_base::complete")** | Invoke the final completion handler, maybe using post. |
| **[complete\_now](boost__beast__stable_async_base/complete_now.html "stable_async_base::complete_now")** | Invoke the final completion handler. |
| **[get\_allocator](boost__beast__stable_async_base/get_allocator.html "stable_async_base::get_allocator")** | Returns the allocator associated with this object. |
| **[get\_cancellation\_slot](boost__beast__stable_async_base/get_cancellation_slot.html "stable_async_base::get_cancellation_slot")** | Returns the cancellation\_slot associated with this object. |
| **[get\_executor](boost__beast__stable_async_base/get_executor.html "stable_async_base::get_executor")** | Returns the executor associated with this object. |
| **[get\_immediate\_executor](boost__beast__stable_async_base/get_immediate_executor.html "stable_async_base::get_immediate_executor")** | Returns the immediate executor associated with this handler. |
| **[handler](boost__beast__stable_async_base/handler.html "stable_async_base::handler")** | Returns the handler associated with this object. |
| **[release\_handler](boost__beast__stable_async_base/release_handler.html "stable_async_base::release_handler")** | Returns ownership of the handler associated with this object. |
| **[set\_allowed\_cancellation](boost__beast__stable_async_base/set_allowed_cancellation.html "stable_async_base::set_allowed_cancellation")** | Set the allowed cancellation types, default is `terminal`. |
| **[stable\_async\_base](boost__beast__stable_async_base/stable_async_base.html "stable_async_base::stable_async_base") [constructor]** | Constructor.  — Move Constructor. |
| **[~stable\_async\_base](boost__beast__stable_async_base/_dtor_stable_async_base.html "stable_async_base::~stable_async_base") [destructor]** | Destructor. |

##### [Friends](boost__beast__stable_async_base.html#beast.ref.boost__beast__stable_async_base.friends)

| Name | Description |
| --- | --- |
| **[allocate\_stable](boost__beast__stable_async_base/allocate_stable.html "stable_async_base::allocate_stable")** | Allocate a temporary object to hold operation state. |

##### [Description](boost__beast__stable_async_base.html#beast.ref.boost__beast__stable_async_base.description)

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

Data members of composed operations implemented as completion handlers do
not have stable addresses, as the composed operation object is move constructed
upon each call to an initiating function. For most operations this is not
a problem. For complex operations requiring stable temporary storage, the
class [`stable_async_base`](boost__beast__stable_async_base.html "stable_async_base") is provided which
offers additional functionality:

* The free function [`beast::allocate_stable`](boost__beast__allocate_stable.html "allocate_stable") may be used
  to allocate one or more temporary objects associated with the composed
  operation.
* Memory for stable temporary objects is allocated using the allocator
  associated with the composed operation.
* Stable temporary objects are automatically destroyed, and the memory
  freed using the associated allocator, either before the final completion
  handler is invoked (a Networking requirement) or when the composed operation
  is destroyed, whichever occurs first.

##### [Example](boost__beast__stable_async_base.html#beast.ref.boost__beast__stable_async_base.example)

The following code demonstrates how [`stable_async_base`](boost__beast__stable_async_base.html "stable_async_base") may be be used
to assist authoring an asynchronous initiating function, by providing all
of the boilerplate to manage the final completion handler in a way that maintains
the allocator and executor associations. Furthermore, the operation shown
allocates temporary memory using [`beast::allocate_stable`](boost__beast__allocate_stable.html "allocate_stable") for the timer and
message, whose addresses must not change between intermediate operations:

```programlisting
// Asynchronously send a message multiple times, once per second
template < class AsyncWriteStream, class T, class WriteHandler>
auto async_write_messages(
    AsyncWriteStream& stream,
    T const & message,
    std::size_t repeat_count,
    WriteHandler&& handler) ->
        typename net::async_result<
            typename std::decay<WriteHandler>::type,
            void(error_code)>::return_type
{
    using handler_type = typename net::async_completion<WriteHandler, void(error_code)>::completion_handler_type;
    using base_type = stable_async_base<handler_type, typename AsyncWriteStream::executor_type>;

    struct op : base_type, boost::asio::coroutine
    {
        // This object must have a stable address
        struct temporary_data
        {
            // Although std::string is in theory movable, most implementations
            // use a "small buffer optimization" which means that we might
            // be submitting a buffer to the write operation and then
            // moving the string, invalidating the buffer. To prevent
            // undefined behavior we store the string object itself at
            // a stable location.
            std::string const message;

            net::steady_timer timer;

            temporary_data(std::string message_, net::io_context& ctx)
                : message(std::move(message_))
                , timer(ctx)
            {
            }
        };

        AsyncWriteStream& stream_;
        std::size_t repeats_;
        temporary_data& data_;

        op(AsyncWriteStream& stream, std::size_t repeats, std::string message, handler_type& handler)
            : base_type(std::move(handler), stream.get_executor())
            , stream_(stream)
            , repeats_(repeats)
            , data_(allocate_stable<temporary_data>(*this, std::move(message), stream.get_executor().context()))
        {
            (*this)(); // start the operation
        }

        // Including this file provides the keywords for macro-based coroutines
        #include <boost/asio/yield.hpp>

        void operator()(error_code ec = {}, std::size_t = 0)
        {
            reenter(* this )
            {
                // If repeats starts at 0 then we must complete immediately. But
                // we can't call the final handler from inside the initiating
                // function, so we post our intermediate handler first. We use
                // net::async_write with an empty buffer instead of calling
                // net::post to avoid an extra function template instantiation, to
                // keep compile times lower and make the resulting executable smaller.
                yield net::async_write(stream_, net::const_buffer{}, std::move(* this ));
                while (! ec && repeats_-- > 0)
                {
                    // Send the string. We construct a `const_buffer` here to guarantee
                    // that we do not create an additional function template instantation
                    // of net::async_write, since we already instantiated it above for
                    // net::const_buffer.

                    yield net::async_write(stream_,
                        net::const_buffer(net::buffer(data_.message)), std::move(* this ));
                    if (ec)
                        break ;

                    // Set the timer and wait
                    data_.timer.expires_after(std::chrono::seconds(1));
                    yield data_.timer.async_wait(std::move(* this ));
                }
            }

            // The base class destroys the temporary data automatically,
            // before invoking the final completion handler
            this->complete_now(ec);
        }

        // Including this file undefines the macros for the coroutines
        #include <boost/asio/unyield.hpp>
    };

    net::async_completion<WriteHandler, void(error_code)> completion(handler);
    std::ostringstream os;
    os << message;
    op(stream, repeat_count, os.str(), completion.completion_handler);
    return completion.result.get();
}
```

##### [Template Parameters](boost__beast__stable_async_base.html#beast.ref.boost__beast__stable_async_base.template_parameters)

| Type | Description |
| --- | --- |
| `Handler` | The type of the completion handler to store. This type must meet the requirements of *CompletionHandler*. |
| `Executor1` | The type of the executor used when the handler has no associated executor. An instance of this type must be provided upon construction. The implementation will maintain an executor work guard and a copy of this instance. |
| `Allocator` | The allocator type to use if the handler does not have an associated allocator. If this parameter is omitted, then `std::allocator<void>` will be used. If the specified allocator is not default constructible, an instance of the type must be provided upon construction. |

##### [See Also](boost__beast__stable_async_base.html#beast.ref.boost__beast__stable_async_base.see_also)

[`allocate_stable`](boost__beast__stable_async_base/allocate_stable.html "stable_async_base::allocate_stable"), [`async_base`](boost__beast__async_base.html "async_base")