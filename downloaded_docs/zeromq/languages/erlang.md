# Erlang

* [erlzmq\_dnif](#erlzmq_dnif)
* [Chumak](#chumak)
* [ezmq](#ezmq)
* [erlang-czmq](#erlang-czmq)
* [erlzmq2](#erlzmq2)
* [erlzmq2 - esl fork](#erlzmq2---esl-fork)
* [erlzmq](#erlzmq)

## erlzmq\_dnif

| Github | <http://github.com/lukaszsamson/erlzmq> |
| --- | --- |
| Hex | <https://hex.pm/packages/erlzmq_dnif> |

Fork of erlzmq2 using dirty NIFs for blocking IO calls and dedicated threads for safely handling sockets.
Compatible with zmq 4.x
Supports macos and \*nix
Supports CurveZMQ

## Chumak

|  |  |
| --- | --- |
| Github | https://github.com/zeromq/chumak |
| Hex | https://hex.pm/packages/chumak |

Pure Erlang implementation of ZeroMQ Message Transport Protocol.

## ezmq

|  |  |
| --- | --- |
| Github | https://github.com/zeromq/ezmq |

ezmq implements the ØMQ protocol in 100% pure Erlang.

## erlang-czmq

|  |  |
| --- | --- |
| Github | https://github.com/gar1t/erlang-czmq |

erlang-czmq is an Erlang port wrote on top of czmq. The API mirrors that of CZMQ with all functions being available through the czmqmodule.

## erlzmq2

|  |  |
| --- | --- |
| Github | http://github.com/zeromq/erlzmq2 |

erlzmq2 is NIF based binding.
Not maintained
Warning: unstable (leaks file descriptors, memory, threads, has race conditions, can deadlock beam and crashes due to accessing zmq sockets from multiple beam threads)

## erlzmq2 - esl fork

|  |  |
| --- | --- |
| Github | http://github.com/esl/erlzmq |
| Hex | https://hex.pm/packages/erlzmq |

Fork of erlzmq2 published on hex.pm.
Compatible with zmq 4.x
Supports macos and \*nix
Warning: unstable (leaks file descriptors, memory, threads, has race conditions, can deadlock beam and crashes due to accessing zmq sockets from multiple beam threads)

## erlzmq

|  |  |
| --- | --- |
| Github | http://github.com/zeromq/erlzmq |

erlzmq is port based binding. Compatible with zmq 2.x
Not maintained