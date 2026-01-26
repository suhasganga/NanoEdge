### [Buffer Types](buffer_types.html "Buffer Types")

To facilitate working with instances of the [*ConstBufferSequence*](../../../../../../doc/html/boost_asio/reference/ConstBufferSequence.html)
and [*MutableBufferSequence*](../../../../../../doc/html/boost_asio/reference/MutableBufferSequence.html)
concepts introduced in [Boost.Asio](../../../../../../libs/asio/index.html),
Beast treats those sequences as a special type of range. The following algorithms
and wrappers are provided which transform these ranges efficiently using
lazy evaluation. No memory allocations are used in the transformations; instead,
they create lightweight iterators over the existing, unmodified memory buffers.
Control of buffers is retained by the caller; ownership is not transferred.

**Table 1.7. Buffer Algorithms and Types**

| Name | Description |
| --- | --- |
| [`buffer_bytes`](../ref/boost__beast__buffer_bytes.html "buffer_bytes") | This is a more reliable version of [`net::buffer_size`](../../../../../../doc/html/boost_asio/reference/buffer_size.html) which is easier to use and also works for types which are convertible to `net::const_buffer` or `net::mutable_buffer`. |
| [`buffers_cat`](../ref/boost__beast__buffers_cat.html "buffers_cat") | This functions returns a new buffer sequence which, when iterated, traverses the sequence which would be formed if all of the input buffer sequences were concatenated. With this routine, multiple calls to a stream's `write_some` function may be combined into one, eliminating expensive system calls. |
| [`buffers_cat_view`](../ref/boost__beast__buffers_cat_view.html "buffers_cat_view") | This class represents the buffer sequence formed by concatenating two or more buffer sequences. This is type of object returned by [`buffers_cat`](../ref/boost__beast__buffers_cat.html "buffers_cat"). |
| [`buffers_front`](../ref/boost__beast__buffers_front.html "buffers_front") | This function returns the first buffer in a buffer sequence, or a buffer of size zero if the buffer sequence has no elements. |
| [`buffers_prefix`](../ref/boost__beast__buffers_prefix.html "buffers_prefix") | This function returns a new buffer or buffer sequence which represents a prefix of the original buffers. |
| [`buffers_prefix_view`](../ref/boost__beast__buffers_prefix_view.html "buffers_prefix_view") | This class represents the buffer sequence formed from a prefix of an existing buffer sequence. This is the type of buffer returned by [`buffers_prefix`](../ref/boost__beast__buffers_prefix.html "buffers_prefix"). |
| [`buffers_range`](../ref/boost__beast__buffers_range.html "buffers_range") [`buffers_range_ref`](../ref/boost__beast__buffers_range_ref.html "buffers_range_ref") | This function returns an iterable range representing the passed buffer sequence. The values obtained when iterating the range will always be a constant buffer, unless the underlying buffer sequence is mutable, in which case the value obtained when iterating will be a mutable buffer. It is intended as a notational convenience when writing a *range-for* statement over a buffer sequence.  The function [`buffers_range`](../ref/boost__beast__buffers_range_ref.html "buffers_range_ref") maintains a copy of the buffer sequence, while [`buffers_range_ref`](../ref/boost__beast__buffers_range_ref.html "buffers_range_ref") maintains a reference (in this case, the caller must ensure that the lifetime of the referenced buffer sequence extends until the range object is destroyed). |
| [`buffers_suffix`](../ref/boost__beast__buffers_suffix.html "buffers_suffix") | This class wraps the underlying memory of an existing buffer sequence and presents a suffix of the original sequence. The length of the suffix may be progressively shortened. This lets callers work with sequential increments of a buffer sequence. |
| [`buffers_to_string`](../ref/boost__beast__buffers_to_string.html "buffers_to_string") | This function converts a buffer sequence to a `std::string`. It can be used for diagnostic purposes and tests. |
| [`buffer_ref`](../ref/boost__beast__buffer_ref.html "buffer_ref") [`ref`](../ref/boost__beast__ref.html "ref") | This function converts a beast buffer, that is to be passed by reference, into a buffer reference, that can be passed by value into asio functions.  It implements the [*DynamicBuffer\_v2'*](../../../../../../doc/html/boost_asio/reference/DynamicBuffer_v2.html) concept. |

  

The [*DynamicBuffer*](../concepts/DynamicBuffer.html "DynamicBuffer")
concept introduced in [Boost.Asio](../../../../../../libs/asio/index.html)
models a buffer sequence which supports an owning, resizable range. Beast
provides this set of additional implementations of the dynamic buffer concept:

**Table 1.8. Dynamic Buffer Implementations**

| Name | Description |
| --- | --- |
| [`buffers_adaptor`](../ref/boost__beast__buffers_adaptor.html "buffers_adaptor") | This wrapper adapts any [*MutableBufferSequence*](../../../../../../doc/html/boost_asio/reference/MutableBufferSequence.html) into a [*DynamicBuffer*](../concepts/DynamicBuffer.html "DynamicBuffer") with an upper limit on the total size of the input and output areas equal to the size of the underlying mutable buffer sequence. The implementation does not perform heap allocations. |
| [`flat_buffer`](../ref/boost__beast__flat_buffer.html "flat_buffer") [`basic_flat_buffer`](../ref/boost__beast__basic_flat_buffer.html "basic_flat_buffer") | Guarantees that input and output areas are buffer sequences with length one. Upon construction an optional upper limit to the total size of the input and output areas may be set. The basic container is an [**AllocatorAwareContainer**](https://en.cppreference.com/w/cpp/named_req/AllocatorAwareContainer). |
| [`multi_buffer`](../ref/boost__beast__multi_buffer.html "multi_buffer") [`basic_multi_buffer`](../ref/boost__beast__basic_multi_buffer.html "basic_multi_buffer") | Uses a sequence of one or more character arrays of varying sizes. Additional character array objects are appended to the sequence to accommodate changes in the size of the character sequence. The basic container is an [**AllocatorAwareContainer**](https://en.cppreference.com/w/cpp/named_req/AllocatorAwareContainer). |
| [`flat_static_buffer`](../ref/boost__beast__flat_static_buffer.html "flat_static_buffer") [`flat_static_buffer_base`](../ref/boost__beast__flat_static_buffer_base.html "flat_static_buffer_base") | Guarantees that input and output areas are buffer sequences with length one. Provides the facilities of a dynamic buffer, subject to an upper limit placed on the total size of the input and output areas defined by a constexpr template parameter. The storage for the sequences are kept in the class; the implementation does not perform heap allocations. |
| [`static_buffer`](../ref/boost__beast__static_buffer.html "static_buffer") [`static_buffer_base`](../ref/boost__beast__static_buffer_base.html "static_buffer_base") | Provides the facilities of a circular dynamic buffer. subject to an upper limit placed on the total size of the input and output areas defined by a constexpr template parameter. The implementation never moves memory during buffer operations. The storage for the sequences are kept in the class; the implementation does not perform heap allocations. |

  

The buffers provide different guarantees regarding the allocated memory;
stable means that existing mutable and const\_buffers obtained by calling
`data` or `prepare`,
will remain valid.

Note that copies always requires a new call to `data`
and `prepare`.`

**Table 1.9. Memory stability**

| Name | Allocation | buffer sequence length | Max Size | Movable | prepare/commit | consume |
| --- | --- | --- | --- | --- | --- | --- |
| [`flat_buffer`](../ref/boost__beast__flat_buffer.html "flat_buffer") | dynamic | 1 | dynamic | yes | invalidating | invalidating |
| [`multi_buffer`](../ref/boost__beast__multi_buffer.html "multi_buffer") | dynamic | dynamic | stable | yes | invalidating |
| [`flat_static_buffer`](../ref/boost__beast__flat_static_buffer.html "flat_static_buffer") | static | 1 | static | no | invalidating |
| [`static_buffer`](../ref/boost__beast__static_buffer.html "static_buffer") | static | 1-2 | static | no | may invalidate |

  

These two functions facilitate buffer interoperability with standard output
streams.

**Table 1.10. Buffer Output Streams**

| Name | Description |
| --- | --- |
| [`make_printable`](../ref/boost__beast__make_printable.html "make_printable") | This function wraps a [*ConstBufferSequence*](../../../../../../doc/html/boost_asio/reference/ConstBufferSequence.html) so it may be used with `operator<<` and `std::ostream`. |
| [`ostream`](../ref/boost__beast__ostream.html "ostream") | This function returns a `std::ostream` which wraps a dynamic buffer. Characters sent to the stream using `operator<<` are stored in the dynamic buffer. |

  

These type traits are provided to facilitate writing compile-time metafunctions
which operate on buffers:

**Table 1.11. Buffer Algorithms and Types**

| Name | Description |
| --- | --- |
| [`buffers_iterator_type`](../ref/boost__beast__buffers_iterator_type.html "buffers_iterator_type") | This metafunction is used to determine the type of iterator used by a particular buffer sequence. |
| [`buffers_type`](../ref/boost__beast__buffers_type.html "buffers_type") | This metafunction is used to determine the underlying buffer type for a list of buffer sequence. The equivalent type of the alias will vary depending on the template type argument. |
| [`is_const_buffer_sequence`](../ref/boost__beast__is_const_buffer_sequence.html "is_const_buffer_sequence") | This metafunction is used to determine if all of the specified types meet the requirements of [*ConstBufferSequence*](../../../../../../doc/html/boost_asio/reference/ConstBufferSequence.html). This type alias will be `std::true_type` if each specified type meets the requirements, otherwise, this type alias will be `std::false_type`. |
| [`is_mutable_buffer_sequence`](../ref/boost__beast__is_mutable_buffer_sequence.html "is_mutable_buffer_sequence") | This metafunction is used to determine if all of the specified types meet the requirements of [*MutableBufferSequence*](../../../../../../doc/html/boost_asio/reference/MutableBufferSequence.html). This type alias will be `std::true_type` if each specified type meets the requirements, otherwise, this type alias will be `std::false_type`. |