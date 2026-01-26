# Installation[¶](#installation "Link to this heading")

## Dependency[¶](#dependency "Link to this heading")

The Python QuestDB client does not have any additional run-time dependencies and
will run on any version of Python >= 3.9 on most platforms and architectures.

From version 3.0.0, this library depends on `numpy>=1.21.0`.

### Optional Dependencies[¶](#optional-dependencies "Link to this heading")

Ingesting dataframes also require the following
dependencies to be installed:

* `pandas`
* `pyarrow`

These are bundled as the `dataframe` extra.

Without this option, you may still ingest data row-by-row.

### PIP[¶](#pip "Link to this heading")

You can install it (or update it) globally by running:

```
python3 -m pip install -U questdb[dataframe]
```

Or, from within a virtual environment:

```
pip install -U questdb[dataframe]
```

If you don’t need to work with dataframes:

```
python3 -m pip install -U questdb
```

### Poetry[¶](#poetry "Link to this heading")

If you’re using poetry, you can add `questdb` as a dependency:

```
poetry add questdb[dataframe]
```

Similarly, if you don’t need to work with dataframes:

```
poetry add questdb
```

or to update the dependency:

```
poetry update questdb
```

## Verifying the Installation[¶](#verifying-the-installation "Link to this heading")

If you want to check that you’ve installed the wheel correctly, you can run the
following statements from a `python3` interactive shell:

```
>>> import questdb.ingress
>>> buf = questdb.ingress.Buffer()
>>> buf.row('test', symbols={'a': 'b'})
<questdb.ingress.Buffer object at 0x104b68240>
>>> str(buf)
'test,a=b\n'
```

If you also want to if check you can serialize from Pandas
(which requires additional dependencies):

```
>>> import questdb.ingress
>>> import pandas as pd
>>> df = pd.DataFrame({'a': [1, 2]})
>>> buf = questdb.ingress.Buffer()
>>> buf.dataframe(df, table_name='test')
>>> str(buf)
'test a=1i\ntest a=2i\n'
```