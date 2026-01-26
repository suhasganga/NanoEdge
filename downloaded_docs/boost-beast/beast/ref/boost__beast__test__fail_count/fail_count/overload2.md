###### [test::fail\_count::fail\_count (2 of 2 overloads)](overload2.html "test::fail_count::fail_count (2 of 2 overloads)")

Construct a counter.

###### [Synopsis](overload2.html#beast.ref.boost__beast__test__fail_count.fail_count.overload2.synopsis)

```programlisting
fail_count(
    std::size_t n,
    error_code ev = error::test_failure);
```

###### [Parameters](overload2.html#beast.ref.boost__beast__test__fail_count.fail_count.overload2.parameters)

| Name | Description |
| --- | --- |
| `n` | The 0-based index of the operation to fail on or after |
| `ev` | An optional error code to use when generating a simulated failure |