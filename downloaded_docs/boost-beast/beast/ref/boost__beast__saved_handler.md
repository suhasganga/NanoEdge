#### [saved\_handler](boost__beast__saved_handler.html "saved_handler")

An invocable, nullary function object which holds a completion handler.

##### [Synopsis](boost__beast__saved_handler.html#beast.ref.boost__beast__saved_handler.synopsis)

Defined in header `<boost/beast/core/saved_handler.hpp>`

```programlisting
class saved_handler
```

##### [Member Functions](boost__beast__saved_handler.html#beast.ref.boost__beast__saved_handler.member_functions)

| Name | Description |
| --- | --- |
| **[emplace](boost__beast__saved_handler/emplace.html "saved_handler::emplace")** | Store a completion handler in the container. |
| **[has\_value](boost__beast__saved_handler/has_value.html "saved_handler::has_value")** | Returns `true` if `*this` contains a completion handler. |
| **[invoke](boost__beast__saved_handler/invoke.html "saved_handler::invoke")** | Unconditionally invoke the stored completion handler. |
| **[maybe\_invoke](boost__beast__saved_handler/maybe_invoke.html "saved_handler::maybe_invoke")** | Conditionally invoke the stored completion handler. |
| **[operator=](boost__beast__saved_handler/operator_eq_.html "saved_handler::operator=")** | Copy Assignment (deleted)  — Move Assignment. |
| **[reset](boost__beast__saved_handler/reset.html "saved_handler::reset")** | Discard the saved handler, if one exists. |
| **[saved\_handler](boost__beast__saved_handler/saved_handler.html "saved_handler::saved_handler") [constructor]** | Default Constructor.  — Copy Constructor (deleted)  — Move Constructor. |
| **[~saved\_handler](boost__beast__saved_handler/_dtor_saved_handler.html "saved_handler::~saved_handler") [destructor]** | Destructor. |

##### [Description](boost__beast__saved_handler.html#beast.ref.boost__beast__saved_handler.description)

This container can hold a type-erased instance of any completion handler,
or it can be empty. When the container holds a value, the implementation
maintains an instance of `net::executor_work_guard`
for the handler's associated executor. Memory is dynamically allocated to
store the completion handler, and the allocator may optionally be specified.
Otherwise, the implementation uses the handler's associated allocator.