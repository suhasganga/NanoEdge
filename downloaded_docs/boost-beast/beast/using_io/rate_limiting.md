### [Rate Limiting 💡](rate_limiting.html "Rate Limiting 💡")

The [`basic_stream`](../ref/boost__beast__basic_stream.html "basic_stream")
class template supports an additional `RatePolicy`
template parameter. Objects of this type must meet the requirements of [*RatePolicy*](../concepts/RatePolicy.html "RatePolicy").
They are used to implement rate limiting or bandwidth management. The default
policy for `basic_stream` and
`tcp_stream` is [`unlimited_rate_policy`](../ref/boost__beast__unlimited_rate_policy.html "unlimited_rate_policy"), which places
no limits on reading and writing. The library comes with the [`simple_rate_policy`](../ref/boost__beast__simple_rate_policy.html "simple_rate_policy"), allowing for
independent control of read and write limits expressed in terms of bytes
per second. The follow code creates an instance of the basic stream with
a simple rate policy, and sets the read and write limits:

```programlisting
// To declare a stream with a rate policy, it is necessary to
// write out all of the template parameter types.
//
// `simple_rate_policy` is default constructible, but
// if the choice of RatePolicy is not DefaultConstructible,
// an instance of the type may be passed to the constructor.

basic_stream<net::ip::tcp, net::any_io_executor, simple_rate_policy> stream(ioc);

// The policy object, which is default constructed, or
// decay-copied upon construction, is attached to the stream
// and may be accessed through the function `rate_policy`.
//
// Here we set individual rate limits for reading and writing

stream.rate_policy().read_limit(10000); // bytes per second

stream.rate_policy().write_limit(850000); // bytes per second
```

More sophisticated rate policies can be implemented as user-defined types
which meet the requirements of [*RatePolicy*](../concepts/RatePolicy.html "RatePolicy").
Here, we develop a rate policy that measures the instantaneous throughput
of reads and writes. First we write a small utility class that applies an
exponential smoothing function to a series of discrete rate samples, to calculate
instantaneous throughput.

```programlisting
class window
{
    std::size_t value_ = 0;

    // The size of the exponential window, in seconds.
    // This should be a power of two.

    static std::size_t constexpr Window = 4;

public:
    /** Returns the number of elapsed seconds since the given time, and adjusts the time.

        This function returns the number of elapsed seconds since the
        specified time point, rounding down. It also moves the specified
        time point forward by the number of elapsed seconds.

        @param since The time point from which to calculate elapsed time.
        The function will modify the value, by adding the number of elapsed
        seconds to it.

        @return The number of elapsed seconds.
    */
    template<class Clock, class Duration>
    static
    std::chrono::seconds
    get_elapsed(std::chrono::time_point<Clock, Duration>& since) noexcept
    {
        auto const elapsed = std::chrono::duration_cast<
            std::chrono::seconds>(Clock::now() - since);
        since += elapsed;
        return elapsed;
    }

    /// Returns the current value, after adding the given sample.
    std::size_t
    update(std::size_t sample, std::chrono::seconds elapsed) noexcept
    {
        // Apply exponential decay.
        //
        // This formula is fast (no division or multiplication) but inaccurate.
        // It overshoots by `n*(1-a)/(1-a^n), where a=(window-1)/window`.
        // Could be good enough for a rough approximation, but if relying
        // on this for production please perform tests!

        auto count = elapsed.count();
        while(count--)
            value_ -= (value_ + Window - 1) / Window;
        value_ += sample;
        return value_ / Window;
    }
    /// Returns the current value
    std::size_t
    value() const noexcept
    {
        return value_ / Window;
    }
};
```

Then we define our rate policy object. We friend the type [`rate_policy_access`](../ref/boost__beast__rate_policy_access.html "rate_policy_access") to allow our
implementation to be private, but still allow the `basic_stream`
access to call the required functions. This lets us avoid having to write
a cumbersome friend declaration for the `basic_stream`
class template. Public members of rate policy objects become part of the
stream object's interface, through a call to `rate_policy`.

```programlisting
/** A RatePolicy to measure instantaneous throughput.

    This measures the rate of transfer for reading and writing
    using a simple exponential decay function.
*/
class rate_gauge
{
    // The clock used to measure elapsed time
    using clock_type = std::chrono::steady_clock;

    // This implements an exponential smoothing window function.
    // The value `Seconds` is the size of the window in seconds.

    clock_type::time_point when_;
    std::size_t read_bytes_ = 0;
    std::size_t write_bytes_ = 0;
    window read_window_;
    window write_window_;

    // Friending this type allows us to mark the
    // member functions required by RatePolicy as private.
    friend class rate_policy_access;

    // Returns the number of bytes available to read currently
    // Required by RatePolicy
    std::size_t
    available_read_bytes() const noexcept
    {
        // no limit
        return (std::numeric_limits<std::size_t>::max)();
    }

    // Returns the number of bytes available to write currently
    // Required by RatePolicy
    std::size_t
    available_write_bytes() const noexcept
    {
        // no limit
        return (std::numeric_limits<std::size_t>::max)();
    }

    // Called every time bytes are read
    // Required by RatePolicy
    void
    transfer_read_bytes(std::size_t n) noexcept
    {
        // Add this to our running total of bytes read
        read_bytes_ += n;
    }

    // Called every time bytes are written
    // Required by RatePolicy
    void
    transfer_write_bytes(std::size_t n) noexcept
    {
        // Add this to our running total of bytes written
        write_bytes_ += n;
    }

    // Called approximately once per second
    // Required by RatePolicy
    void
    on_timer()
    {
        // Calculate elapsed time in seconds, and adjust our time point
        auto const elapsed = window::get_elapsed(when_);

        // Skip the update when elapsed==0,
        // otherwise the measurement will have jitter
        if(elapsed.count() == 0)
            return;

        // Add our samples and apply exponential decay
        read_window_.update(read_bytes_, elapsed);
        write_window_.update(write_bytes_, elapsed);

        // Reset our counts of bytes transferred
        read_bytes_ = 0;
        write_bytes_ = 0;
    }

public:
    rate_gauge()
        : when_(clock_type::now())
    {
    }

    /// Returns the current rate of reading in bytes per second
    std::size_t
    read_bytes_per_second() const noexcept
    {
        return read_window_.value();
    }

    /// Returns the current rate of writing in bytes per second
    std::size_t
    write_bytes_per_second() const noexcept
    {
        return write_window_.value();
    }
};
```

To use our new policy we declare an instance of the stream, and then use
it with stream algorithms as usual. At any time, we can determine the current
read or write rates by calling into the policy.

```programlisting
// This stream will use our new rate_gauge policy
basic_stream<net::ip::tcp, net::any_io_executor, rate_gauge> stream(ioc);

//...

// Print the current rates
std::cout <<
    stream.rate_policy().read_bytes_per_second() << " bytes/second read\n" <<
    stream.rate_policy().write_bytes_per_second() << " bytes/second written\n";
```