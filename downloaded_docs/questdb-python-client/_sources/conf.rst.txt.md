.. \_sender\_conf:
=============
Configuration
=============
When constructing a :ref:`sender ` you can pass a configuration string
to the :func:`Sender.from\_conf ` method.
.. code-block:: python
from questdb.ingress import Sender
conf = "http::addr=localhost:9009;username=admin;password=quest;"
with Sender.from\_conf(conf) as sender:
...
The format of the configuration string is::
::=;=;...;
.. note::
The keys are case-sensitive.
The valid protocols are:
\* ``tcp``: ILP/TCP
\* ``tcps``: ILP/TCP with TLS
\* ``http``: ILP/HTTP
\* ``https``: ILP/HTTP with TLS
If you're unsure which protocol to use, see :ref:`sender\_which\_protocol`.
Only the ``addr=host:port`` key is mandatory. It specifies the hostname and port
of the QuestDB server.
The same configuration string can also be loaded from the ``QDB\_CLIENT\_CONF``
environment variable. This is useful for keeping sensitive information out of
your code.
.. code-block:: bash
export QDB\_CLIENT\_CONF="http::addr=localhost:9009;username=admin;password=quest;"
.. code-block:: python
from questdb.ingress import Sender
with Sender.from\_env() as sender:
...
Connection
==========
\* ``addr`` - ``str``: The address of the server in the form of
``host:port``.
This key-value pair is mandatory, but the port can be defaulted.
If omitted, the port will be defaulted to 9009 for TCP(s)
and 9000 for HTTP(s).
\* ``bind\_interface`` - TCP-only, ``str``: Network interface to bind from.
Useful if you have an accelerated network interface (e.g. Solarflare) and
want to use it.
The default is ``0.0.0.0``.
.. \_sender\_conf\_auth:
Authentication
==============
If you're using QuestDB enterprise you can read up on creating and permissioning
users in the `Enterprise quickstart `\_
and the `role-based access control `\_ guides.
HTTP Bearer Token
-----------------
\* ``token`` - ``str``: Bearer token for HTTP authentication.
HTTP Basic Auth
---------------
\* ``username`` - ``str``: Username for HTTP basic authentication.
\* ``password`` - ``str``: Password for HTTP basic authentication.
TCP Auth
--------
\* ``username`` - ``str``: Username for TCP authentication (A.K.A. \*kid\*).
\* ``token`` - ``str``: Token for TCP authentication (A.K.A. \*d\*).
\* ``token\_x`` - ``str``: Token X for TCP authentication (A.K.A. \*x\*).
\* ``token\_y`` - ``str``: Token Y for TCP authentication (A.K.A. \*y\*).
You can additionally set the ``auth\_timeout`` parameter (milliseconds) to
control how long the client will wait for a response from the server during
the authentication process. The default is 15 seconds.
See the :ref:`auth\_and\_tls\_example` example for more details.
.. \_sender\_conf\_tls:
TLS
===
TLS in enabled by selecting the ``tcps`` or ``https`` protocol.
See the `QuestDB enterprise TLS documentation `\_
on how to enable this feature in the server.
Open source QuestDB does not offer TLS support out of the box, but you can
still use TLS by setting up a proxy in front of QuestDB, such as
`HAProxy `.
\* ``tls\_ca`` - The remote server's certificate authority verification mechamism.
\* ``'webpki\_roots'``: Use the
`webpki-roots `\_ Rust crate to
recognize certificates.
\* ``'os\_roots'``: Use the OS-provided certificate store.
\* ``'webpki\_and\_os\_roots'``: Use both the
`webpki-roots `\_ Rust crate and
the OS-provided certificate store to recognize certificates.
\* ``pem\_file``: Path to a PEM-encoded certificate authority file.
This is useful for testing with self-signed certificates.
The default is: ``'webpki\_and\_os\_roots'``.
\* ``tls\_roots`` - ``str``: Path to a PEM-encoded certificate authority file.
When used it defaults the ``tls\_ca`` to ``'pem\_file'``.
\* ``tls\_verify`` - ``'on'`` | ``'unsafe\_off'``: Whether to verify the server's
certificate. This should only be used for testing as a last resort and never
used in production as it makes the connection vulnerable to man-in-the-middle
attacks.
The default is: ``'on'``.
As an example, if you are in a corporate environment and need to use the OS
certificate store, you can use the following configuration string::
https::addr=localhost:9009;tls\_ca=os\_roots;
Alternatively, if you are testing with a self-signed certificate, you can use
the following configuration string::
https::addr=localhost:9009;tls\_roots=/path/to/cert.pem;
For more details on using self-signed test certificates, see:
\* For Open Source QuestDB: https://github.com/questdb/c-questdb-client/blob/main/tls\_certs/README.md#self-signed-certificates
\* For QuestDB Enterprise: https://questdb.com/docs/operations/tls/#demo-certificates
.. \_sender\_conf\_auto\_flush:
Auto-flushing
=============
The following parameters control the :ref:`sender\_auto\_flush` behavior.
\* ``auto\_flush`` - ``'on'`` | ``'off'``: Global switch for the auto-flushing
behavior.
Default: ``'on'``.
\* ``auto\_flush\_rows`` - ``int > 0`` | ``'off'``: The number of rows that will
trigger a flush. Set to ``'off'`` to disable.
\*Default: 75000 (HTTP) | 600 (TCP).\*
\* ``auto\_flush\_bytes`` - ``int > 0`` | ``'off'``: The number of bytes that will
trigger a flush. Set to ``'off'`` to disable.
Default: ``'off'``.
\* ``auto\_flush\_interval`` - ``int > 0`` | ``'off'``: The time in milliseconds
that will trigger a flush. Set to ``'off'`` to disable.
Default: 1000 (millis).
.. \_sender\_conf\_auto\_flush\_interval:
``auto\_flush\_interval``
-----------------------
The `auto\_flush\_interval` parameter controls how long the sender's buffer can be
left unflushed for after appending a new row via the
:func:`Sender.row ` or the
:func:`Sender.dataframe ` methods.
It is defined in milliseconds.
Note that this parameter does \*not\* create a timer that counts down
each time data is added. Instead, the client checks the time elapsed since the
last flush each time new data is added. If the elapsed time exceeds the
specified ``auto\_flush\_interval``, the client automatically flushes the current
buffer to the database.
Consider the following example:
.. code-block:: python
from questdb.ingress import Sender, TimestampNanos
import time
conf = "http::addr=localhost:9009;auto\_flush\_interval=1000;"
with Sender.from\_conf(conf) as sender:
# row 1
sender.row('table1', columns={'val': 1}, at=TimestampNanos.now())
time.sleep(60) # sleep for 1 minute
# row 2
sender.row('table2', columns={'val': 2}, at=TimestampNanos.now())
In this example above, "row 1" will not be flushed for a whole minute, until
"row 2" is added and the ``auto\_flush\_interval`` limit of 1 second is exceeded,
causing both "row 1" and "row 2" to be flushed together.
If you need consistent flushing at specific intervals, you should set
``auto\_flush\_interval=off`` and implement your own timer-based logic.
The :ref:`sender\_advanced` documentation should help you.
.. \_sender\_conf\_protocol\_version:
Protocol Version
================
Specifies the version of InfluxDB Line Protocol to use.
Here is a configuration string with ``protocol\_version=2`` for ``TCP``::
tcp::addr=localhost:9000;protocol\_version=2;
Valid options are:
\* ``1`` - Text-based format compatible with InfluxDB database when used over HTTP.
\* ``2`` - Array support and binary format serialization for 64-bit floats (version specific to QuestDB).
\* ``3`` - Decimal type support (requires QuestDB 9.2.0+). Also includes all features from version 2.
\* ``auto`` (default) - Automatic version selection based on protocol type.
HTTP/HTTPS: Auto-detects server capability during handshake (supports version negotiation)
TCP/TCPS: Defaults to version 1 for compatibility
.. note::
Protocol version ``2`` requires QuestDB server version 9.0.0 or higher.
Protocol version ``3`` requires QuestDB server version 9.2.0 or higher and
is needed for ingesting data into ``DECIMAL`` columns.
.. \_sender\_conf\_buffer:
Buffer
======
\* ``protocol\_version`` - ``int (1, 2)``: Buffer protocol version.
\* ``init\_buf\_size`` - ``int > 0``: Initial buffer capacity.
Default: 65536 (64KiB).
\* ``max\_buf\_size`` - ``int > 0``: Maximum flushable buffer capacity.
Default: 104857600 (100MiB).
\* ``max\_name\_len`` - ``int > 0``: Maximum length of a table or column name.
Default: 127.
.. \_sender\_conf\_request:
HTTP Request
============
The following parameters control the HTTP request behavior.
\* ``retry\_timeout`` - ``int > 0``: The time in milliseconds to continue retrying
after a failed HTTP request. The interval between retries is an exponential
backoff starting at 10ms and doubling after each failed attempt up to a
maximum of 1 second.
Default: 10000 (10 seconds).
\* ``request\_timeout`` - ``int > 0``: The time in milliseconds to wait for a
response from the server. This is in addition to the calculation derived from
the ``request\_min\_throughput`` parameter.
Default: 10000 (10 seconds).
\* ``request\_min\_throughput`` - ``int > 0``: Minimum expected throughput in
bytes per second for HTTP requests. If the throughput is lower than this
value, the connection will time out.
This is used to calculate an additional timeout on top of ``request\_timeout``.
This is useful for large requests.
You can set this value to ``0`` to disable this logic.
Default: 102400 (100 KiB/s).
The final request timeout calculation is::
request\_timeout + (buffer\_size / request\_min\_throughput)