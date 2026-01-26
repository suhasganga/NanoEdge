### [RatePolicy](RatePolicy.html "RatePolicy")

An instance of **RatePolicy** is associated
with a [`basic_stream`](../ref/boost__beast__basic_stream.html "basic_stream"), and controls the rate
at which bytes may be independently sent and received. This may be used to
achieve fine-grained bandwidth management and flow control.

##### [Associated Types](RatePolicy.html#beast.concepts.RatePolicy.associated_types)

* [`rate_policy_access`](../ref/boost__beast__rate_policy_access.html "rate_policy_access")

|  |  |
| --- | --- |
| [Warning] | Warning |
| These requirements may undergo non-backward compatible changes in subsequent versions. |

##### [Requirements](RatePolicy.html#beast.concepts.RatePolicy.requirements)

In this table:

* `P` denotes a type that
  meets the requirements of **RatePolicy**.
* `x` denotes an xvalue of
  type `P`
* `a` denotes a value of
  type `P`.
* `n` denotes a value of
  type `std::size_t`

**Table 1.46. Valid expressions**

| Expression | Type | Semantics, Pre/Post-conditions |
| --- | --- | --- |
| `P a(x)` |  | Requires *MoveConstructible*. |
| `friend rate_policy_access` |  | The member functions required in `P` should be private. [`rate_policy_access`](../ref/boost__beast__rate_policy_access.html "rate_policy_access") must be a friend of `P` for the implementation to gain access to the required member functions. |
| `a.available_read_bytes()` | `std::size_t` | This function is called by the implementation to determine the maximum number of allowed bytes to be transferred in the next read operation. The actual number of bytes subsequently transferred may be less than this number.  If the policy returns a value of zero, the read operation will asynchronously wait until the next timer interval before retrying. When the retry occurs, this function will be called again. |
| `a.available_write_bytes()` | `std::size_t` | This function is called by the implementation to determine the maximum number of allowed bytes to be transferred in the next write operation. The actual number of bytes subsequently transferred may be less than this number.  If the policy returns a value of zero, the read operation will asynchronously wait until the next timer interval before retrying. When the retry occurs, this function will be called again. |
| `a.transfer_read_bytes(n)` |  | The implementation calls this function to inform the policy that `n` bytes were successfully transferred in the most recent read operation. The policy object may optionally use this information to calculate throughputs and/or inform the algorithm used to determine subsequently queried transfer maximums. |
| `a.transfer_write_bytes(n)` |  | The implementation calls this function to inform the policy that `n` bytes were successfully transferred in the most recent write operation. The policy object may optionally use this information to calculate throughputs and/or inform the algorithm used to determine subsequently queried transfer limits. |
| `a.on_timer()` |  | The implementation calls this function every time the internal timer expires. The policy object may optionally use this opportunity to calculate elapsed time and throughput, and/or inform the algorithm used to determine subsequently queried transfer limits. |

  

##### [Exemplar](RatePolicy.html#beast.concepts.RatePolicy.exemplar)

```programlisting
class RatePolicy
{
    friend class rate_policy_access;

    std::size_t
    available_read_bytes();

    std::size_t
    available_write_bytes();

    void
    transfer_read_bytes(std::size_t);

    void
    transfer_write_bytes(std::size_t);

    void
    on_timer();
};
```

##### [Models](RatePolicy.html#beast.concepts.RatePolicy.models)

* [`simple_rate_policy`](../ref/boost__beast__simple_rate_policy.html "simple_rate_policy")
* [`unlimited_rate_policy`](../ref/boost__beast__unlimited_rate_policy.html "unlimited_rate_policy")