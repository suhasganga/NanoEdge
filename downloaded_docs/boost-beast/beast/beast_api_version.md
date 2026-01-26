## [Beast API Version](beast_api_version.html "Beast API Version")

Beast maintains it's own API version, which is more fine-grained than the boost
release.

It can be obtained as a string from the `BOOST_BEAST_VERSION`
macro or a string through `BOOST_BEAST_VERSION_STRING`.

```programlisting
/* Identifies the API version of Beast.

   This is a simple integer that is incremented by one every
   time a set of code changes is merged to the develop branch.
*/
#define BOOST_BEAST_VERSION 359

// A string describing BOOST_BEAST_VERSION, that can be used in http headers.
#define BOOST_BEAST_VERSION_STRING "Boost.Beast/" BOOST_STRINGIZE(BOOST_BEAST_VERSION)
```