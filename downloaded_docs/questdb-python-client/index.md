[![QuestDB](_images/logo.svg)](https://questdb.com/)

# QuestDB Client Library for Python[¶](#questdb-client-library-for-python "Link to this heading")

This is the official Python client library for [QuestDB](https://questdb.com).

This client library implements QuestDB’s variant of the
[InfluxDB Line Protocol](https://questdb.com/docs/reference/api/ilp/overview/)
(ILP) over HTTP and TCP.

ILP provides the fastest way to insert data into QuestDB.

This implementation supports [authentication](https://py-questdb-client.readthedocs.io/en/latest/conf.html#authentication)
and full-connection encryption with
[TLS](https://py-questdb-client.readthedocs.io/en/latest/conf.html#tls).

## Install[¶](#install "Link to this heading")

The latest version of the library is 4.1.0 ([changelog](https://py-questdb-client.readthedocs.io/en/latest/changelog.html)).

```
python3 -m pip install -U questdb[dataframe]
```

## Quickstart[¶](#quickstart "Link to this heading")

Start by [setting up QuestDB](https://questdb.com/docs/quick-start/) .
Once set up, you can use this library to insert data.

The most common way to insert data is from a Pandas dataframe.

```
import pandas as pd
from questdb.ingress import Sender

df = pd.DataFrame({
    'symbol': pd.Categorical(['ETH-USD', 'BTC-USD']),
    'side': pd.Categorical(['sell', 'sell']),
    'price': [2615.54, 39269.98],
    'amount': [0.00044, 0.001],

    # NumPy float64 arrays are supported from v3.0.0rc1 onwards.
    # Note that requires QuestDB server >= 9.0.0 for array support
    'ord_book_bids': [
        np.array([2615.54, 2618.63]),
        np.array([39269.98, 39270.00])
    ],

    'timestamp': pd.to_datetime(['2021-01-01', '2021-01-02'])})

conf = f'http::addr=localhost:9000;'
with Sender.from_conf(conf) as sender:
    sender.dataframe(df, table_name='trades', at='timestamp')
```

You can also send individual rows. This only requires a more minimal installation:

```
python3 -m pip install -U questdb
```

```
from questdb.ingress import Sender, TimestampNanos

conf = f'http::addr=localhost:9000;'
with Sender.from_conf(conf) as sender:
    sender.row(
        'trades',
        symbols={'symbol': 'ETH-USD', 'side': 'sell'},
        columns={
            'price': 2615.54,
            'amount': 0.00044,

            # NumPy float64 arrays are supported from v3.0.0rc1 onwards.
            # Note that requires QuestDB server >= 9.0.0 for array support
            'ord_book_bids': np.array([2615.54, 2618.63]),
        },
        at=TimestampNanos.now())
    sender.flush()
```

To connect via the [older TCP protocol](https://py-questdb-client.readthedocs.io/en/latest/sender.html#ilp-tcp-or-ilp-http), set the
[configuration string](https://py-questdb-client.readthedocs.io/en/latest/conf.html) to:

```
conf = f'tcp::addr=localhost:9009;'
with Sender.from_conf(conf) as sender:
    ...
```

You can continue by reading the
[Sending Data Over ILP](https://py-questdb-client.readthedocs.io/en/latest/sender.html)
guide.

## Links[¶](#links "Link to this heading")

* [Core database documentation](https://questdb.com/docs/)
* [Python library documentation](https://py-questdb-client.readthedocs.io/)
* [GitHub repository](https://github.com/questdb/py-questdb-client)
* [Package on PyPI](https://pypi.org/project/questdb/)

## Community[¶](#community "Link to this heading")

Stop by our [Community Forum](https://community.questdb.com) to
chat with the QuestDB team.

You can also [sign up to our mailing list](https://questdb.com/contributors/)
to get notified of new releases.

## License[¶](#license "Link to this heading")

The code is released under the [Apache License 2.0](https://github.com/questdb/py-questdb-client/blob/main/LICENSE.txt).

## Contents[¶](#contents "Link to this heading")

* [Installation](installation.html)
* [Sending Data over ILP](sender.html)
* [Configuration](conf.html)
* [Examples](examples.html)
* [API Reference](api.html)
* [Troubleshooting](troubleshooting.html)
* [Community](community.html)
* [Changelog](changelog.html)

## Indices and tables[¶](#indices-and-tables "Link to this heading")

* [Index](genindex.html)
* [Module Index](py-modindex.html)
* [Search Page](search.html)