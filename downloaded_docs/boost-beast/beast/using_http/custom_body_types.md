### [Custom Body Types](custom_body_types.html "Custom Body Types")

User-defined types are possible for the message body, where the type meets
the [*Body*](../concepts/Body.html "Body")
requirements. This simplified class declaration shows the customization points
available to user-defined body types:

```programlisting
/// Defines a Body type
struct body
{
    /// This determines the return type of the `message::body` member function
    using value_type = ...;

    /// An optional function, returns the body's payload size (which may be zero)
    static
    std::uint64_t
    size(value_type const& v);

    /// The algorithm used for extracting buffers
    class reader;

    /// The algorithm used for inserting buffers
    class writer;
}
```

The meaning of the nested types is as follows

**Table 1.29. Body Type Members**

| Name | Description |
| --- | --- |
| `value_type` | Determines the type of the [`message::body`](../ref/boost__beast__http__message/body.html "http::message::body") member. |
| `reader` | An optional nested type meeting the requirements of [*BodyReader*](../concepts/BodyReader.html "BodyReader"), which provides the algorithm for storing a forward range of buffer sequences in the body representation. If present, this body type may be used with a [`parser`](../ref/boost__beast__http__parser.html "http::parser"). |
| `writer` | An optional nested type meeting the requirements of [*BodyWriter*](../concepts/BodyWriter.html "BodyWriter"), which provides the algorithm for converting the body representation to a forward range of buffer sequences. If present this body type may be used with a [`serializer`](../ref/boost__beast__http__serializer.html "http::serializer"). |

  

##### [Value Type](custom_body_types.html#beast.using_http.custom_body_types.value_type)

The `value_type` nested type
allows the body to define the declaration of the body type as it appears
in the message. This can be any type. For example, a body's value type may
specify `std::vector<char>` or
`std::list<std::string>`. A custom body may even set the value
type to something that is not a container for body octets, such as a [`boost::filesystem::path`](../../../../../../libs/filesystem/doc/reference.html#class-path). Or, a more structured container
may be chosen. This declares a body's value type as a JSON tree structure
produced from a [`boost::json::stream_parser`](../../../../../../doc/html/json/input_output.html#json.input_output.parsing.streaming_parser):

```programlisting
#include <boost/json/stream_parser.hpp>

struct Body
{
    using value_type = boost::json::value;

    class reader;
    class writer;
};
```

As long as a suitable reader or writer is available to provide the algorithm
for transferring buffers in and out of the value type, those bodies may be
parsed or serialized.

#### [File Body 💡](custom_body_types.html#beast.using_http.custom_body_types.file_body "File Body 💡")

Use of the flexible [*Body*](../concepts/Body.html "Body")
concept customization point enables authors to preserve the self-contained
nature of the [`message`](../ref/boost__beast__http__message.html "http::message") object while allowing
domain specific behaviors. Common operations for HTTP servers include sending
responses which deliver file contents, and allowing for file uploads. In
this example we build the [`basic_file_body`](../ref/boost__beast__http__basic_file_body.html "http::basic_file_body") type which supports
both reading and writing to a file on the file system. The interface is
a class templated on the type of file used to access the file system, which
must meet the requirements of [*File*](../concepts/File.html "File").

First we declare the type with its nested types:

```programlisting
/** A message body represented by a file on the filesystem.

    Messages with this type have bodies represented by a
    file on the file system. When parsing a message using
    this body type, the data is stored in the file pointed
    to by the path, which must be writable. When serializing,
    the implementation will read the file and present those
    octets as the body content. This may be used to serve
    content from a directory as part of a web service.

    @tparam File The implementation to use for accessing files.
    This type must meet the requirements of <em>File</em>.
*/
template<class File>
struct basic_file_body
{
    // Make sure the type meets the requirements
    static_assert(is_file<File>::value,
        "File type requirements not met");

    /// The type of File this body uses
    using file_type = File;

    // Algorithm for storing buffers when parsing.
    class reader;

    // Algorithm for retrieving buffers when serializing.
    class writer;

    // The type of the @ref message::body member.
    class value_type;

    /** Returns the size of the body

        @param body The file body to use
    */
    static
    std::uint64_t
    size(value_type const& body);
};
```

We will start with the definition of the `value_type`.
Our strategy will be to store the file object directly in the message container
through the `value_type`
field. To use this body it will be necessary to call `msg.body.file().open()` first with the required information such
as the path and open mode. This ensures that the file exists throughout
the operation and prevent the race condition where the file is removed
from the file system in between calls.

```programlisting
/** The type of the @ref message::body member.

    Messages declared using `basic_file_body` will have this type for
    the body member. This rich class interface allow the file to be
    opened with the file handle maintained directly in the object,
    which is attached to the message.
*/
template<class File>
class basic_file_body<File>::value_type
{
    // This body container holds a handle to the file
    // when it is open, and also caches the size when set.

#ifndef BOOST_BEAST_DOXYGEN
    friend class reader;
    friend class writer;
    friend struct basic_file_body;
#endif

    // This represents the open file
    File file_;

    // The cached file size
    std::uint64_t file_size_ = 0;

public:
    /** Destructor.

        If the file is open, it is closed first.
    */
    ~value_type() = default;

    /// Constructor
    value_type() = default;

    /// Constructor
    value_type(value_type&& other) = default;

    /// Move assignment
    value_type& operator=(value_type&& other) = default;

    /// Return the file
    File& file()
    {
        return file_;
    }

    /// Returns `true` if the file is open
    bool
    is_open() const
    {
        return file_.is_open();
    }

    /// Returns the size of the file if open
    std::uint64_t
    size() const
    {
        return file_size_;
    }

    /// Close the file if open
    void
    close();

    /** Open a file at the given path with the specified mode

        @param path The utf-8 encoded path to the file

        @param mode The file mode to use

        @param ec Set to the error, if any occurred
    */
    void
    open(char const* path, file_mode mode, error_code& ec);

    /** Set the open file

        This function is used to set the open file. Any previously
        set file will be closed.

        @param file The file to set. The file must be open or else
        an error occurs

        @param ec Set to the error, if any occurred
    */
    void
    reset(File&& file, error_code& ec);

    /** Set the cursor position of the file.

        This function can be used to move the cursor of the file ahead
        so that only a part gets read. This file will also adjust the
        value_type, in case the file is already part of a body.

        @param offset The offset in bytes from the beginning of the file

        @param ec Set to the error, if any occurred
    */

    void seek(std::uint64_t offset, error_code& ec);
};

template<class File>
void
basic_file_body<File>::
value_type::
close()
{
    error_code ignored;
    file_.close(ignored);
}

template<class File>
void
basic_file_body<File>::
value_type::
open(char const* path, file_mode mode, error_code& ec)
{
    // Open the file
    file_.open(path, mode, ec);
    if(ec)
        return;

    // Cache the size
    file_size_ = file_.size(ec);
    if(ec)
    {
        close();
        return;
    }
}

template<class File>
void
basic_file_body<File>::
value_type::
reset(File&& file, error_code& ec)
{
    // First close the file if open
    if(file_.is_open())
    {
        error_code ignored;
        file_.close(ignored);
    }

    // Take ownership of the new file
    file_ = std::move(file);

    // Cache the size
    file_size_ = file_.size(ec);

    // Consider the offset
    if (!ec)
        file_size_ -= file_.pos(ec);
}

template<class File>
void
basic_file_body<File>::
value_type::
seek(std::uint64_t offset, error_code& ec)
{
    file_.seek(offset, ec);
    // Cache the size
    if (!ec)
        file_size_ = file_.size(ec);

    // Consider the offset
    if (!ec)
        file_size_ -= file_.pos(ec);
}

// This is called from message::payload_size
template<class File>
std::uint64_t
basic_file_body<File>::
size(value_type const& body)
{
    // Forward the call to the body
    return body.size();
}
```

Our implementation of [*BodyWriter*](../concepts/BodyWriter.html "BodyWriter")
will contain a small buffer from which the file contents are read. The
buffer is provided to the implementation on each call until everything
has been read in.

```programlisting
/** Algorithm for retrieving buffers when serializing.

    Objects of this type are created during serialization
    to extract the buffers representing the body.
*/
template<class File>
class basic_file_body<File>::writer
{
    value_type& body_;                       // The body we are reading from
    std::uint64_t remain_;                   // The number of unread bytes
    char buf_[BOOST_BEAST_FILE_BUFFER_SIZE]; // Small buffer for reading

public:
    // The type of buffer sequence returned by `get`.
    //
    using const_buffers_type =
        net::const_buffer;

    // Constructor.
    //
    // `h` holds the headers of the message we are
    // serializing, while `b` holds the body.
    //
    // Note that the message is passed by non-const reference.
    // This is intentional, because reading from the file
    // changes its "current position" which counts makes the
    // operation logically not-const (although it is bitwise
    // const).
    //
    // The BodyWriter concept allows the writer to choose
    // whether to take the message by const reference or
    // non-const reference. Depending on the choice, a
    // serializer constructed using that body type will
    // require the same const or non-const reference to
    // construct.
    //
    // Readers which accept const messages usually allow
    // the same body to be serialized by multiple threads
    // concurrently, while readers accepting non-const
    // messages may only be serialized by one thread at
    // a time.
    //
    template<bool isRequest, class Fields>
    writer(header<isRequest, Fields>& h, value_type& b);

    // Initializer
    //
    // This is called before the body is serialized and
    // gives the writer a chance to do something that might
    // need to return an error code.
    //
    void
    init(error_code& ec);

    // This function is called zero or more times to
    // retrieve buffers. A return value of `boost::none`
    // means there are no more buffers. Otherwise,
    // the contained pair will have the next buffer
    // to serialize, and a `bool` indicating whether
    // or not there may be additional buffers.
    boost::optional<std::pair<const_buffers_type, bool>>
    get(error_code& ec);
};
```

And here are the definitions for the functions we have declared:

```programlisting
// Here we just stash a reference to the path for later.
// Rather than dealing with messy constructor exceptions,
// we save the things that might fail for the call to `init`.
//
template<class File>
template<bool isRequest, class Fields>
basic_file_body<File>::
writer::
writer(header<isRequest, Fields>& h, value_type& b)
    : body_(b)
{
    boost::ignore_unused(h);

    // The file must already be open
    BOOST_ASSERT(body_.file_.is_open());

    // Get the size of the file
    remain_ = body_.file_size_;
}

// Initializer
template<class File>
void
basic_file_body<File>::
writer::
init(error_code& ec)
{
    // The error_code specification requires that we
    // either set the error to some value, or set it
    // to indicate no error.
    //
    // We don't do anything fancy so set "no error"
    ec = {};
}

// This function is called repeatedly by the serializer to
// retrieve the buffers representing the body. Our strategy
// is to read into our buffer and return it until we have
// read through the whole file.
//
template<class File>
auto
basic_file_body<File>::
writer::
get(error_code& ec) ->
    boost::optional<std::pair<const_buffers_type, bool>>
{
    // Calculate the smaller of our buffer size,
    // or the amount of unread data in the file.
    auto const amount =  remain_ > sizeof(buf_) ?
        sizeof(buf_) : static_cast<std::size_t>(remain_);

    // Handle the case where the file is zero length
    if(amount == 0)
    {
        // Modify the error code to indicate success
        // This is required by the error_code specification.
        //
        // NOTE We use the existing category instead of calling
        //      into the library to get the generic category because
        //      that saves us a possibly expensive atomic operation.
        //
        ec = {};
        return boost::none;
    }

    // Now read the next buffer
    auto const nread = body_.file_.read(buf_, amount, ec);
    if(ec)
        return boost::none;

    if (nread == 0)
    {
        BOOST_BEAST_ASSIGN_EC(ec, error::short_read);
        return boost::none;
    }

    // Make sure there is forward progress
    BOOST_ASSERT(nread != 0);
    BOOST_ASSERT(nread <= remain_);

    // Update the amount remaining based on what we got
    remain_ -= nread;

    // Return the buffer to the caller.
    //
    // The second element of the pair indicates whether or
    // not there is more data. As long as there is some
    // unread bytes, there will be more data. Otherwise,
    // we set this bool to `false` so we will not be called
    // again.
    //
    ec = {};
    return {{
        const_buffers_type{buf_, nread},    // buffer to return.
        remain_ > 0                         // `true` if there are more buffers.
        }};
}
```

Files can be read now, and the next step is to allow writing to files by
implementing the [*BodyReader*](../concepts/BodyReader.html "BodyReader").
The style is similar to the writer, except that buffers are incoming instead
of outgoing. Here's the declaration:

```programlisting
/** Algorithm for storing buffers when parsing.

    Objects of this type are created during parsing
    to store incoming buffers representing the body.
*/
template<class File>
class basic_file_body<File>::reader
{
    value_type& body_;  // The body we are writing to

public:
    // Constructor.
    //
    // This is called after the header is parsed and
    // indicates that a non-zero sized body may be present.
    // `h` holds the received message headers.
    // `b` is an instance of `basic_file_body`.
    //
    template<bool isRequest, class Fields>
    explicit
    reader(header<isRequest, Fields>&h, value_type& b);

    // Initializer
    //
    // This is called before the body is parsed and
    // gives the reader a chance to do something that might
    // need to return an error code. It informs us of
    // the payload size (`content_length`) which we can
    // optionally use for optimization.
    //
    void
    init(boost::optional<std::uint64_t> const&, error_code& ec);

    // This function is called one or more times to store
    // buffer sequences corresponding to the incoming body.
    //
    template<class ConstBufferSequence>
    std::size_t
    put(ConstBufferSequence const& buffers,
        error_code& ec);

    // This function is called when writing is complete.
    // It is an opportunity to perform any final actions
    // which might fail, in order to return an error code.
    // Operations that might fail should not be attempted in
    // destructors, since an exception thrown from there
    // would terminate the program.
    //
    void
    finish(error_code& ec);
};
```

Finally, here is the implementation of the reader member functions:

```programlisting
// We don't do much in the reader constructor since the
// file is already open.
//
template<class File>
template<bool isRequest, class Fields>
basic_file_body<File>::
reader::
reader(header<isRequest, Fields>& h, value_type& body)
    : body_(body)
{
    boost::ignore_unused(h);
}

template<class File>
void
basic_file_body<File>::
reader::
init(
    boost::optional<std::uint64_t> const& content_length,
    error_code& ec)
{
    // The file must already be open for writing
    BOOST_ASSERT(body_.file_.is_open());

    // We don't do anything with this but a sophisticated
    // application might check available space on the device
    // to see if there is enough room to store the body.
    boost::ignore_unused(content_length);

    // The error_code specification requires that we
    // either set the error to some value, or set it
    // to indicate no error.
    //
    // We don't do anything fancy so set "no error"
    ec = {};
}

// This will get called one or more times with body buffers
//
template<class File>
template<class ConstBufferSequence>
std::size_t
basic_file_body<File>::
reader::
put(ConstBufferSequence const& buffers, error_code& ec)
{
    // This function must return the total number of
    // bytes transferred from the input buffers.
    std::size_t nwritten = 0;

    // Loop over all the buffers in the sequence,
    // and write each one to the file.
    for(auto it = net::buffer_sequence_begin(buffers);
        it != net::buffer_sequence_end(buffers); ++it)
    {
        // Write this buffer to the file
        net::const_buffer buffer = *it;
        nwritten += body_.file_.write(
            buffer.data(), buffer.size(), ec);
        if(ec)
            return nwritten;
    }

    // Indicate success
    // This is required by the error_code specification
    ec = {};

    return nwritten;
}

// Called after writing is done when there's no error.
template<class File>
void
basic_file_body<File>::
reader::
finish(error_code& ec)
{
    // This has to be cleared before returning, to
    // indicate no error. The specification requires it.
    ec = {};
}
```

We have created a full featured body type capable of reading and writing
files on the filesystem, integrating seamlessly with the HTTP algorithms
and message container. The body type works with any file implementation
meeting the requirements of [*File*](../concepts/File.html "File")
so it may be transparently used with solutions optimized for particular
platforms. Example HTTP servers which use file bodies are available in
the example directory.