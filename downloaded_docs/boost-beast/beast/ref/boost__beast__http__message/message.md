##### [http::message::message](message.html "http::message::message")

Constructor.

```programlisting
message();
  » more...

message(
    message&&);
  » more...

message(
    message const&);
  » more...

template<
    class... BodyArgs>
explicit
message(
    header_type&& h,
    BodyArgs&&... body_args);
  » more...

template<
    class... BodyArgs>
explicit
message(
    header_type const& h,
    BodyArgs&&... body_args);
  » more...

message(
    verb method,
    string_view target,
    unsigned version);
  » more...

template<
    class BodyArg>
message(
    verb method,
    string_view target,
    unsigned version,
    BodyArg&& body_arg);
  » more...

template<
    class BodyArg,
    class FieldsArg>
message(
    verb method,
    string_view target,
    unsigned version,
    BodyArg&& body_arg,
    FieldsArg&& fields_arg);
  » more...

message(
    status result,
    unsigned version);
  » more...

template<
    class BodyArg>
message(
    status result,
    unsigned version,
    BodyArg&& body_arg);
  » more...

template<
    class BodyArg,
    class FieldsArg>
message(
    status result,
    unsigned version,
    BodyArg&& body_arg,
    FieldsArg&& fields_arg);
  » more...

explicit
message(
    std::piecewise_construct_t);
  » more...
```

Construct a message.

```programlisting
template<
    class... BodyArgs>
message(
    std::piecewise_construct_t,
    std::tuple< BodyArgs... > body_args);
  » more...

template<
    class... BodyArgs,
    class... FieldsArgs>
message(
    std::piecewise_construct_t,
    std::tuple< BodyArgs... > body_args,
    std::tuple< FieldsArgs... > fields_args);
  » more...
```