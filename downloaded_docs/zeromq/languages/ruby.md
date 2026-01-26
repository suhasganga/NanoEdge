# Ruby

| Github | <https://github.com/zeromq/rbzmq> |
| --- | --- |
| gem | <https://rubygems.org/gems/zmq> |
| Docs | <http://zeromq.github.io/rbzmq/> |

## Installation

[Install libzmq](/download/).

```
gem install zmq
```

If the gem installation complains that it cannot find libzmq or headers, simply pass the location of your libzmq installation to the gem install command:

```
gem install zmq -- --with-zmq-dir=/opt/local
```

On Windows add a parameter for the libs. For example:

```
gem install zmq -- --with-zmq-dir=c:/src/zeromq-4.3.2 --with-zmq-lib=c:/src/zeromq-4.3.2/src/.libs
```

## Example

```
require "zmq"

context = ZMQ::Context.new(1)

puts "Opening connection for READ"
inbound = context.socket(ZMQ::UPSTREAM)
inbound.bind("tcp://127.0.0.1:9000")

outbound = context.socket(ZMQ::DOWNSTREAM)
outbound.connect("tcp://127.0.0.1:9000")
p outbound.send("Hello World!")
p outbound.send("QUIT")

loop do
  data = inbound.recv
  p data
  break if data == "QUIT"
end
```