On this page

This document outlines the IPv4 data type operators.

The IP addresses can be in the range of `0.0.0.1` - `255.255.255.255`.

The address: `0.0.0.0` is interpreted as `NULL`.

The following operators support `string` type arguments to permit the passing of
netmasks:

* `<<`
  [Strict IP address contained by](/docs/query/operators/ipv4/#-left-strict-ip-address-contained-by)
* `<<=`
  [IP address contained by or equal](/docs/query/operators/ipv4/#-left-ip-address-contained-by-or-equal)
* [rnd\_ipv4(string, int)](/docs/query/functions/random-value-generator/#rnd_ipv4string-int)
* [netmask()](/docs/query/operators/ipv4/#return-netmask---netmaskstring)

## `<` Less than[​](#-less-than "Direct link to -less-than")

Takes two IPv4 arguments.

Returns a boolean.

#### Examples[​](#examples "Direct link to Examples")

Use case: testing to see if one IP address is less than another.

```prism-code
ipv4 '33.1.8.43' < ipv4 '200.6.38.9' -> T
```

## `<=` Less than or equal[​](#-less-than-or-equal "Direct link to -less-than-or-equal")

Takes two IPv4 arguments.

Returns a boolean.

#### Examples[​](#examples-1 "Direct link to Examples")

Use case: testing to see if one IP address is less than or equal to another.

```prism-code
ipv4 '33.1.8.43' <= ipv4 '33.1.8.43' -> T
```

## `>` Greater than[​](#-greater-than "Direct link to -greater-than")

Takes two IPv4 arguments.

Returns a boolean.

#### Examples[​](#examples-2 "Direct link to Examples")

Use case: testing to see if one IP address is greater than another.

```prism-code
ipv4 '33.1.8.43' > ipv4 '200.6.38.9' -> F
```

## `>=` Greater than or equal[​](#-greater-than-or-equal "Direct link to -greater-than-or-equal")

Takes two IPv4 arguments.

Returns a boolean.

#### Examples[​](#examples-3 "Direct link to Examples")

Use case: testing to see if one IP address is greater than or equal to another.

```prism-code
ipv4 '33.1.8.43' >= ipv4 '200.6.38.9' -> F
```

## `=` Equals[​](#-equals "Direct link to -equals")

Takes two IPv4 arguments.

Returns a boolean.

#### Examples[​](#examples-4 "Direct link to Examples")

Use case: testing to see if one IP address is equal to another.

```prism-code
ipv4 '44.8.9.10' = ipv4 '6.2.90.1' -> F
```

## `!=` Does not equal[​](#-does-not-equal "Direct link to -does-not-equal")

Takes two IPv4 arguments.

Returns a boolean.

#### Examples[​](#examples-5 "Direct link to Examples")

Use case: testing to see if one IP address is not equal to another.

```prism-code
ipv4 '44.8.9.10' != ipv4 '6.2.90.1' -> T
```

## `<<` Left strict IP address contained by[​](#-left-strict-ip-address-contained-by "Direct link to -left-strict-ip-address-contained-by")

Takes one IPv4 argument and one string argument.

The string argument can accept IPv4 addresses with a subnet mask, the IPv4
argument cannot.

Returns a boolean.

#### Examples[​](#examples-6 "Direct link to Examples")

Use case: searching ip addresses by subnet

```prism-code
ipv4 '35.24.65.11' << '35.24.65.2/16' -> T  
ipv4 '35.24.65.11' << '35.24.65.2/32' -> F
```

## `>>` Right strict IP address contained by[​](#-right-strict-ip-address-contained-by "Direct link to -right-strict-ip-address-contained-by")

Takes one IPv4 argument and one string argument.

The string argument can accept IPv4 addresses with a subnet mask, the IPv4
argument cannot.

Returns a boolean.

#### Examples[​](#examples-7 "Direct link to Examples")

Use case: searching ip addresses by subnet

```prism-code
'35.24.65.2/16' >> ipv4 '35.24.65.11' -> T  
'35.24.65.2/32'  >> ipv4 '35.24.65.11' -> F
```

## `<<=` Left IP address contained by or equal[​](#-left-ip-address-contained-by-or-equal "Direct link to -left-ip-address-contained-by-or-equal")

Takes one IPv4 argument and one string argument

The string argument can accept IPv4 addresses with a subnet mask, the IPv4
argument cannot.

Returns a boolean.

#### Examples[​](#examples-8 "Direct link to Examples")

Use case: searching ip addresses by subnet

```prism-code
ipv4 '35.24.65.11' <<= '35.24.65.2/16' -> T  
ipv4 '35.24.65.11' <<= '35.24.65.2/32' -> T
```

## `<<=` Right IP address contained by or equal[​](#-right-ip-address-contained-by-or-equal "Direct link to -right-ip-address-contained-by-or-equal")

Takes one IPv4 argument and one string argument

The string argument can accept IPv4 addresses with a subnet mask, the IPv4
argument cannot.

Returns a boolean.

#### Examples[​](#examples-9 "Direct link to Examples")

Use case: searching ip addresses by subnet

```prism-code
'35.24.65.2/16' >>= ipv4 '35.24.65.11'  -> T  
'35.24.65.2/32' >>= ipv4 '35.24.65.11'  -> T
```

## `&` Bitwise AND[​](#-bitwise-and "Direct link to -bitwise-and")

Takes two IPv4 arguments.

Returns an IPv4 address.

#### Examples[​](#examples-10 "Direct link to Examples")

Use case: separating an ip address into its network and host portions

```prism-code
ipv4 '215.53.40.9' & ipv4 '255.255.0.0' -> 215.53.0.0  
ipv4 '99.8.63.41' & ipv4 '0.0.63.41' -> 0.0.63.41
```

## `~` Bitwise NOT[​](#-bitwise-not "Direct link to -bitwise-not")

Takes one IPv4 argument.

Returns an IPv4 address.

#### Examples[​](#examples-11 "Direct link to Examples")

Use case: computing broadcast address' bitmask from a netmask

```prism-code
~ ipv4 '255.255.0.0' -> 0.0.255.255
```

## `|` Bitwise OR[​](#-bitwise-or "Direct link to -bitwise-or")

Takes two IPv4 arguments.

Returns an IPv4 address.

#### Examples[​](#examples-12 "Direct link to Examples")

Use case: computing an ip address' broadcast address

```prism-code
ipv4 '92.11.8.40' | '0.0.255.255' -> 92.11.255.255
```

## `+` Add offset to an IP address[​](#-add-offset-to-an-ip-address "Direct link to -add-offset-to-an-ip-address")

Takes one IPv4 argument and one integer argument.

Returns an IPv4 address.

#### Examples[​](#examples-13 "Direct link to Examples")

Use case: altering an ip address

```prism-code
ipv4 '92.11.8.40' + 5 -> 92.11.8.45  
10 + ipv4 '2.6.43.8' -> 2.6.43.18
```

## `-` Subtract offset from IP address[​](#--subtract-offset-from-ip-address "Direct link to --subtract-offset-from-ip-address")

Takes one IPv4 argument and one integer argument.

Returns an IPv4 address.

#### Examples[​](#examples-14 "Direct link to Examples")

```prism-code
ipv4 '92.11.8.40' - 5 -> 92.11.8.35
```

## `-` Difference between two IP addresses[​](#--difference-between-two-ip-addresses "Direct link to --difference-between-two-ip-addresses")

Takes two IPv4 arguments.

Returns a long.

#### Examples[​](#examples-15 "Direct link to Examples")

Use case: calculating the range of unique addresses between two ip addresses

```prism-code
ipv4 '92.11.8.40' - ipv4 '92.11.8.0' -> 40
```

## Return netmask - netmask(string)[​](#return-netmask---netmaskstring "Direct link to Return netmask - netmask(string)")

Takes a `string` IPv4 argument as either:

* ipv4 address with a netmask `22.59.138.9/8`
* subnet with netmask: `2.2/16`

Returns an IPv4 addresses' netmask (`255.0.0.0`) in IPv4 format.

#### Examples[​](#examples-16 "Direct link to Examples")

Use case: Obtaining the broadcast bitmask for an ip address via performing
bitwise NOT on the netmask.

Apply a bitwise OR to this result to obtain the broadcast address of an ip
address.

```prism-code
~ netmask('68.11.9.2/8')) | ipv4 '68.11.9.2' -> 68.255.255.255
```