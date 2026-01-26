On this page

The QuestDB REST API is based on standard HTTP features and is understood by
off-the-shelf HTTP clients. It provides a simple way to interact with QuestDB
and is compatible with most programming languages. API functions are fully keyed
on the URL and they use query parameters as their arguments.

The [Web Console](/docs/getting-started/web-console/overview/) is the official Web client for QuestDB, that relies on the REST API.

**Available methods**

* [`/imp`](#imp---import-data) for importing data from `.CSV` files
* [`/exec`](#exec---execute-queries) to execute a SQL statement
* [`/exp`](#exp---export-data) to export data

## Examples[​](#examples "Direct link to Examples")

QuestDB exposes a REST API for compatibility with a wide range of libraries and
tools. The REST API is accessible on port `9000` and has the following
insert-capable entrypoints:

| Entrypoint | HTTP Method | Description | API Docs |
| --- | --- | --- | --- |
| [`/imp`](#imp-uploading-tabular-data) | POST | Import CSV data | [Reference](/docs/query/rest-api/#imp---import-data) |
| [`/exec?query=..`](#exec-sql-insert-query) | GET | Run SQL Query returning JSON result set | [Reference](/docs/query/rest-api/#exec---execute-queries) |

For details such as content type, query parameters and more, refer to the
[REST API](/docs/query/rest-api/) docs.

### `/imp`: Uploading Tabular Data[​](#imp-uploading-tabular-data "Direct link to imp-uploading-tabular-data")

Let's assume you want to upload the following data via the `/imp` entrypoint:

* CSV
* Table

```prism-code
col1,col2,col3  
a,10.5,True  
b,100,False  
c,,True
```

| col1 | col2 | col3 |
| --- | --- | --- |
| a | 10.5 | *true* |
| b | 100 | *false* |
| c | *NULL* | *true* |

You can do so via the command line using `cURL` or programmatically via HTTP
APIs in your scripts and applications.

By default, the response is designed to be human-readable. Use the `fmt=json`
query argument to obtain a response in JSON. You can also specify the schema
explicitly. See the second example in Python for these features.

* cURL
* Python
* NodeJS
* Go

This example imports a CSV file with automatic schema detection.

Basic import with table name

```prism-code
curl -F data=@data.csv http://localhost:9000/imp?name=table_name
```

This example overwrites an existing table and specifies a timestamp format and a
designated timestamp column. For more information on the optional parameters to
specify timestamp formats, partitioning and renaming tables, see the
[REST API documentation](/docs/query/rest-api/#examples).

Providing a user-defined schema

```prism-code
curl \  
-F schema='[{"name":"ts", "type": "TIMESTAMP", "pattern": "yyyy-MM-dd - HH:mm:ss"}]' \  
-F data=@weather.csv 'http://localhost:9000/imp?overwrite=true&timestamp=ts'
```

This first example shows uploading the `data.csv` file with automatic schema
detection.

```prism-code
import sys  
import requests  
  
csv = {'data': ('my_table', open('./data.csv', 'r'))}  
host = 'http://localhost:9000'  
  
try:  
    response = requests.post(host + '/imp', files=csv)  
    print(response.text)  
except requests.exceptions.RequestException as e:  
    print(f'Error: {e}', file=sys.stderr)
```

The second example creates a CSV buffer from Python objects and uploads them
with a custom schema. Note UTF-8 encoding.

The `fmt=json` parameter allows us to obtain a parsable response, rather than a
tabular response designed for human consumption.

```prism-code
import io  
import csv  
import requests  
import pprint  
import json  
  
  
def to_csv_str(table):  
    output = io.StringIO()  
    csv.writer(output, dialect='excel').writerows(table)  
    return output.getvalue().encode('utf-8')  
  
  
def main():  
    table_name = 'example_table2'  
    table = [  
        ['col1', 'col2', 'col3'],  
        ['a',    10.5,   True],  
        ['b',    100,    False],  
        ['c',    None,   True]]  
  
    table_csv = to_csv_str(table)  
    print(table_csv)  
    schema = json.dumps([  
        {'name': 'col1', 'type': 'SYMBOL'},  
        {'name': 'col2', 'type': 'DOUBLE'},  
        {'name': 'col3', 'type': 'BOOLEAN'}])  
    response = requests.post(  
        'http://localhost:9000/imp',  
        params={'fmt': 'json'},  
        files={  
            'schema': schema,  
            'data': (table_name, table_csv)}).json()  
  
    # You can parse the `status` field and `error` fields  
    # of individual columns. See Reference/API/REST docs for details.  
    pprint.pprint(response)  
  
  
if __name__ == '__main__':  
    main()
```

```prism-code
const fetch = require("node-fetch")  
const FormData = require("form-data")  
const fs = require("fs")  
  
const HOST = "http://127.0.0.1:9000"  
  
async function run() {  
  const form = new FormData()  
  
  form.append("data", fs.readFileSync(__dirname + "/data.csv"), {  
    filename: "data.csv",  
    contentType: "application/octet-stream",  
  })  
  
  try {  
    const r = await fetch(`${HOST}/imp`, {  
      method: "POST",  
      body: form,  
      headers: form.getHeaders(),  
    })  
  
    console.log(r)  
  } catch (e) {  
    console.error(e)  
  }  
}  
  
run()
```

```prism-code
package main  
  
import (  
  "bytes"  
  "fmt"  
  "io"  
  "io/ioutil"  
  "log"  
  "mime/multipart"  
  "net/http"  
  "net/url"  
  "os"  
)  
  
func main() {  
  u, err := url.Parse("http://localhost:9000")  
  checkErr(err)  
  u.Path += "imp"  
  url := fmt.Sprintf("%v", u)  
  fileName := "/path/to/data.csv"  
  file, err := os.Open(fileName)  
  checkErr(err)  
  
  defer file.Close()  
  
  buf := new(bytes.Buffer)  
  writer := multipart.NewWriter(buf)  
  uploadFile, _ := writer.CreateFormFile("data", "data.csv")  
  _, err = io.Copy(uploadFile, file)  
  checkErr(err)  
  writer.Close()  
  
  req, err := http.NewRequest(http.MethodPut, url, buf)  
  checkErr(err)  
  req.Header.Add("Content-Type", writer.FormDataContentType())  
  
  client := &http.Client{}  
  res, err := client.Do(req)  
  checkErr(err)  
  
  defer res.Body.Close()  
  
  body, err := ioutil.ReadAll(res.Body)  
  checkErr(err)  
  
  log.Println(string(body))  
}  
  
func checkErr(err error) {  
  if err != nil {  
    panic(err)  
  }  
}
```

### `/exec`: SQL `INSERT` Query[​](#exec-sql-insert-query "Direct link to exec-sql-insert-query")

The `/exec` entrypoint takes a SQL query and returns results as JSON.

We can use this for quick SQL inserts too, but note that there's no support for
parameterized queries that are necessary to avoid SQL injection issues. Prefer
[InfluxDB Line Protocol](/docs/configuration/overview/#influxdb-line-protocol-ilp) if you
need high-performance inserts.

* cURL
* Python
* NodeJS
* Go

```prism-code
# Create Table  
curl -G \  
  --data-urlencode "query=CREATE TABLE IF NOT EXISTS trades(name STRING, value INT)" \  
  http://localhost:9000/exec  
  
# Insert a row  
curl -G \  
  --data-urlencode "query=INSERT INTO trades VALUES('abc', 123456)" \  
  http://localhost:9000/exec
```

```prism-code
import sys  
import requests  
import json  
  
host = 'http://localhost:9000'  
  
def run_query(sql_query):  
    query_params = {'query': sql_query, 'fmt' : 'json'}  
    try:  
        response = requests.get(host + '/exec', params=query_params)  
        json_response = json.loads(response.text)  
        print(json_response)  
    except requests.exceptions.RequestException as e:  
        print(f'Error: {e}', file=sys.stderr)  
  
# create table  
run_query("CREATE TABLE IF NOT EXISTS trades (name STRING, value INT)")  
# insert row  
run_query("INSERT INTO trades VALUES('abc', 123456)")
```

The `node-fetch` package can be installed using `npm i node-fetch`.

```prism-code
const fetch = require("node-fetch")  
  
const HOST = "http://127.0.0.1:9000"  
  
async function createTable() {  
  try {  
    const query = "CREATE TABLE IF NOT EXISTS trades (name STRING, value INT)"  
  
    const response = await fetch(  
      `${HOST}/exec?query=${encodeURIComponent(query)}`,  
    )  
    const json = await response.json()  
  
    console.log(json)  
  } catch (error) {  
    console.log(error)  
  }  
}  
  
async function insertData() {  
  try {  
    const query = "INSERT INTO trades VALUES('abc', 123456)"  
  
    const response = await fetch(  
      `${HOST}/exec?query=${encodeURIComponent(query)}`,  
    )  
    const json = await response.json()  
  
    console.log(json)  
  } catch (error) {  
    console.log(error)  
  }  
}  
  
createTable().then(insertData)
```

```prism-code
package main  
  
import (  
  "fmt"  
  "io/ioutil"  
  "log"  
  "net/http"  
  "net/url"  
)  
  
func main() {  
  u, err := url.Parse("http://localhost:9000")  
  checkErr(err)  
  
  u.Path += "exec"  
  params := url.Values{}  
  params.Add("query", `  
    CREATE TABLE IF NOT EXISTS  
      trades (name STRING, value INT);  
    INSERT INTO  
      trades  
    VALUES(  
      "abc",  
      123456  
    );  
  `)  
  u.RawQuery = params.Encode()  
  url := fmt.Sprintf("%v", u)  
  
  res, err := http.Get(url)  
  checkErr(err)  
  
  defer res.Body.Close()  
  
  body, err := ioutil.ReadAll(res.Body)  
  checkErr(err)  
  
  log.Println(string(body))  
}  
  
func checkErr(err error) {  
  if err != nil {  
    panic(err)  
  }  
}
```

## /imp - Import data[​](#imp---import-data "Direct link to /imp - Import data")

tip

For a complete guide including text loader configuration and troubleshooting,
see [CSV Import](/docs/ingestion/import-csv/#import-csv-via-rest).

`/imp` streams tabular text data directly into a table. It supports CSV, TAB and
pipe (`|`) delimited inputs with optional headers. There are no restrictions on
data size. Data types and structures are detected automatically, without
additional configuration. In some cases, additional configuration can be
provided to improve the automatic detection as described in
[user-defined schema](#user-defined-schema).

note

The structure detection algorithm analyses the chunk in the beginning of the
file and relies on relative uniformity of data. When the first chunk is
non-representative of the rest of the data, automatic imports can yield errors.

If the data follows a uniform pattern, the number of lines which are analyzed
for schema detection can be reduced to improve performance during uploads using
the `http.text.analysis.max.lines` key. Usage of this setting is described in
the [HTTP server configuration](/docs/configuration/overview/#http-server) documentation.

### URL parameters[​](#url-parameters "Direct link to URL parameters")

`/imp` is expecting an HTTP POST request using the `multipart/form-data`
Content-Type with following optional URL parameters which must be URL encoded:

| Parameter | Required | Default | Description |
| --- | --- | --- | --- |
| `atomicity` | No | `skipCol` | `abort`, `skipRow` or `skipCol`. Behaviour when an error is detected in the data. `abort`: the entire file will be skipped. `skipRow`: the row is skipped. `skipCol`: the column is skipped. |
| `delimiter` | No |  | URL encoded delimiter character. When set, import will try to detect the delimiter automatically. Since automatic delimiter detection requires at least two lines (rows) to be present in the file, this parameter may be used to allow single line file import. |
| `fmt` | No | `tabular` | Can be set to `json` to get the response formatted as such. |
| `forceHeader` | No | `false` | `true` or `false`. When `false`, QuestDB will try to infer if the first line of the file is the header line. When set to `true`, QuestDB will expect that line to be the header line. |
| `name` | No | Name of the file | Name of the table to create, [see below](/docs/query/rest-api/#names). |
| `overwrite` | No | `false` | `true` or `false`. When set to true, any existing data or structure will be overwritten. |
| `partitionBy` | No | `NONE` | See [partitions](/docs/concepts/partitions/#properties). |
| `o3MaxLag` | No |  | Sets upper limit on the created table to be used for the in-memory out-of-order buffer. Can be also set globally via the `cairo.o3.max.lag` configuration property. |
| `maxUncommittedRows` | No |  | Maximum number of uncommitted rows to be set for the created table. When the number of pending rows reaches this parameter on a table, a commit will be issued. Can be also set globally via the `cairo.max.uncommitted.rows` configuration property. |
| `skipLev` | No | `false` | `true` or `false`. Skip “Line Extra Values”, when set to true, the parser will ignore those extra values rather than ignoring entire line. An extra value is something in addition to what is defined by the header. |
| `timestamp` | No |  | Name of the column that will be used as a [designated timestamp](/docs/concepts/designated-timestamp/). |
| `create` | No | `true` | `true` or `false`. When set to `false`, QuestDB will not automatically create a table '`name`' if one does not exist, and will return an error instead. |

tip

If you experience large latencies when importing big CSV files with out-of-order
timestamps, try increasing `maxUncommittedRows` parameter from the default
`500,000` value.

Example usage

```prism-code
curl -F data=@weather.csv \  
'http://localhost:9000/imp?overwrite=true&name=new_table&timestamp=ts&partitionBy=MONTH'
```

Further example queries with context on the source CSV file contents relative
and the generated tables are provided in the [examples section](#examples-1)
below.

### Names[​](#names "Direct link to Names")

Table and column names are subject to restrictions, the following list of
characters are automatically removed:

```prism-code
[whitespace]  
.  
?  
,  
:  
\  
/  
\\  
\0  
)  
(  
_  
+  
-  
*  
~  
%
```

When the header row is missing, column names are generated automatically.

### Consistency guarantees[​](#consistency-guarantees "Direct link to Consistency guarantees")

`/imp` benefits from the properties of the QuestDB
[storage engine](/docs/architecture/storage-engine/#durability),
although Atomicity and Durability can be relaxed to meet convenience and
performance demands.

#### Atomicity[​](#atomicity "Direct link to Atomicity")

QuestDB is fully insured against any connection problems. If the server detects
closed socket(s), the entire request is rolled back instantly and transparently
for any existing readers. The only time data can be partially imported is when
atomicity is in `relaxed` mode and data cannot be converted to column type. In
this scenario, any "defective" row of data is discarded and `/imp` continues to
stream request data into table.

#### Consistency[​](#consistency "Direct link to Consistency")

This property is guaranteed by consistency of append transactions against
QuestDB storage engine.

#### Isolation[​](#isolation "Direct link to Isolation")

Data is committed to QuestDB storage engine at end of request. Uncommitted
transactions are not visible to readers.

#### Durability[​](#durability "Direct link to Durability")

`/imp` streams data from network socket buffer directly into memory mapped
files. At this point data is handed over to the OS and is resilient against
QuestDB internal errors and unlikely but hypothetically possible crashes. This
is default method of appending data and it is chosen for its performance
characteristics.

### Examples[​](#examples-1 "Direct link to Examples")

#### Automatic schema detection[​](#automatic-schema-detection "Direct link to Automatic schema detection")

The following example uploads a file `ratings.csv` which has the following
contents:

| ts | visMiles | tempF | dewpF |
| --- | --- | --- | --- |
| 2010-01-01T00:00:00.000000Z | 8.8 | 34 | 30 |
| 2010-01-01T00:51:00.000000Z | 9.100000000000 | 34 | 30 |
| 2010-01-01T01:36:00.000000Z | 8.0 | 34 | 30 |
| ... | ... | ... | ... |

An import can be performed with automatic schema detection with the following
request:

```prism-code
curl -F data=@weather.csv 'http://localhost:9000/imp'
```

A HTTP status code of `200` will be returned and the response will be:

```prism-code
+-------------------------------------------------------------------------------+  
|      Location:  |     weather.csv  |        Pattern  | Locale  |      Errors  |  
|   Partition by  |            NONE  |                 |         |              |  
|      Timestamp  |            NONE  |                 |         |              |  
+-------------------------------------------------------------------------------+  
|   Rows handled  |           49976  |                 |         |              |  
|  Rows imported  |           49976  |                 |         |              |  
+-------------------------------------------------------------------------------+  
|              0  |              ts  |                TIMESTAMP  |           0  |  
|              1  |        visMiles  |                   DOUBLE  |           0  |  
|              2  |           tempF  |                      INT  |           0  |  
|              3  |           dewpF  |                      INT  |           0  |  
+-------------------------------------------------------------------------------+
```

#### User-defined schema[​](#user-defined-schema "Direct link to User-defined schema")

To specify the schema of a table, a schema object can be provided:

```prism-code
curl \  
-F schema='[{"name":"dewpF", "type": "STRING"}]' \  
-F data=@weather.csv 'http://localhost:9000/imp'
```

Response

```prism-code
+------------------------------------------------------------------------------+  
|      Location:  |    weather.csv  |        Pattern  | Locale  |      Errors  |  
|   Partition by  |           NONE  |                 |         |              |  
|      Timestamp  |           NONE  |                 |         |              |  
+------------------------------------------------------------------------------+  
|   Rows handled  |          49976  |                 |         |              |  
|  Rows imported  |          49976  |                 |         |              |  
+------------------------------------------------------------------------------+  
|              0  |             ts  |                TIMESTAMP  |           0  |  
|              1  |       visMiles  |                   DOUBLE  |           0  |  
|              2  |          tempF  |                      INT  |           0  |  
|              3  |          dewpF  |                   STRING  |           0  |  
+------------------------------------------------------------------------------+
```

**Non-standard timestamp formats**

Given a file `weather.csv` with the following contents which contains a
timestamp with a non-standard format:

| ts | visMiles | tempF | dewpF |
| --- | --- | --- | --- |
| 2010-01-01 - 00:00:00 | 8.8 | 34 | 30 |
| 2010-01-01 - 00:51:00 | 9.100000000000 | 34 | 30 |
| 2010-01-01 - 01:36:00 | 8.0 | 34 | 30 |
| ... | ... | ... | ... |

The file can be imported as usual with the following request:

Importing CSV with non-standard timestamp

```prism-code
curl -F data=@weather.csv 'http://localhost:9000/imp'
```

A HTTP status code of `200` will be returned and the import will be successful,
but the timestamp column is detected as a `VARCHAR` type:

Response with timestamp as VARCHAR type

```prism-code
+-------------------------------------------------------------------------------+  
|      Location:  |     weather.csv  |        Pattern  | Locale  |      Errors  |  
|   Partition by  |            NONE  |                 |         |              |  
|      Timestamp  |            NONE  |                 |         |              |  
+-------------------------------------------------------------------------------+  
|   Rows handled  |           49976  |                 |         |              |  
|  Rows imported  |           49976  |                 |         |              |  
+-------------------------------------------------------------------------------+  
|              0  |              ts  |                  VARCHAR  |           0  |  
|              1  |        visMiles  |                   DOUBLE  |           0  |  
|              2  |           tempF  |                      INT  |           0  |  
|              3  |           dewpF  |                      INT  |           0  |  
+-------------------------------------------------------------------------------+
```

To amend the timestamp column type, this example curl can be used which has a
`schema` JSON object to specify that the `ts` column is of `TIMESTAMP` type with
the pattern `yyyy-MM-dd - HH:mm:ss`

Additionally, URL parameters are provided:

* `overwrite=true` to overwrite the existing table
* `timestamp=ts` to specify that the `ts` column is the designated timestamp
  column for this table
* `partitionBy=MONTH` to set a
  [partitioning strategy](/docs/operations/data-retention/) on the table by
  `MONTH`

Providing a user-defined schema

```prism-code
curl \  
-F schema='[{"name":"ts", "type": "TIMESTAMP", "pattern": "yyyy-MM-dd - HH:mm:ss"}]' \  
-F data=@weather.csv \  
'http://localhost:9000/imp?overwrite=true&timestamp=ts&partitionBy=MONTH'
```

The HTTP status code will be set to `200` and the response will show `0` errors
parsing the timestamp column:

```prism-code
+------------------------------------------------------------------------------+  
|      Location:  |    weather.csv  |        Pattern  | Locale  |      Errors  |  
|   Partition by  |          MONTH  |                 |         |              |  
|      Timestamp  |             ts  |                 |         |              |  
+------------------------------------------------------------------------------+  
|   Rows handled  |          49976  |                 |         |              |  
|  Rows imported  |          49976  |                 |         |              |  
+------------------------------------------------------------------------------+  
|              0  |             ts  |                TIMESTAMP  |           0  |  
|              1  |       visMiles  |                   DOUBLE  |           0  |  
|              2  |          tempF  |                      INT  |           0  |  
|              3  |          dewpF  |                      INT  |           0  |  
+------------------------------------------------------------------------------+
```

#### JSON response[​](#json-response "Direct link to JSON response")

If you intend to upload CSV programmatically, it's easier to parse the response
as JSON. Set `fmt=json` query argument on the request.

Here's an example of a successful response:

```prism-code
{  
  "status": "OK",  
  "location": "example_table",  
  "rowsRejected": 0,  
  "rowsImported": 3,  
  "header": false,  
  "columns": [  
    { "name": "col1", "type": "SYMBOL", "size": 4, "errors": 0 },  
    { "name": "col2", "type": "DOUBLE", "size": 8, "errors": 0 },  
    { "name": "col3", "type": "BOOLEAN", "size": 1, "errors": 0 }  
  ]  
}
```

Here is an example with request-level errors:

```prism-code
{  
  "status": "not enough lines [table=example_table]"  
}
```

Here is an example with column-level errors due to unsuccessful casts:

```prism-code
{  
  "status": "OK",  
  "location": "example_table2",  
  "rowsRejected": 0,  
  "rowsImported": 3,  
  "header": false,  
  "columns": [  
    { "name": "col1", "type": "DOUBLE", "size": 8, "errors": 3 },  
    { "name": "col2", "type": "SYMBOL", "size": 4, "errors": 0 },  
    { "name": "col3", "type": "BOOLEAN", "size": 1, "errors": 0 }  
  ]  
}
```

## /exec - Execute queries[​](#exec---execute-queries "Direct link to /exec - Execute queries")

`/exec` compiles and executes the SQL query supplied as a parameter and returns
a JSON response.

note

The query execution terminates automatically when the socket connection is
closed.

### Overview[​](#overview "Direct link to Overview")

#### Parameters[​](#parameters "Direct link to Parameters")

`/exec` is expecting an HTTP GET request with following query parameters:

| Parameter | Required | Default | Description |
| --- | --- | --- | --- |
| `count` | No | `false` | `true` or `false`. Counts the number of rows and returns this value. |
| `limit` | No |  | Allows limiting the number of rows to return. `limit=10` will return the first 10 rows (equivalent to `limit=1,10`), `limit=10,20` will return row numbers 10 through to 20 inclusive. |
| `nm` | No | `false` | `true` or `false`. Skips the metadata section of the response when set to `true`. |
| `query` | Yes |  | URL encoded query text. It can be multi-line. |
| `timings` | No | `false` | `true` or `false`. When set to `true`, QuestDB will also include a `timings` property in the response which gives details about the execution times. |
| `explain` | No | `false` | `true` or `false`. When set to `true`, QuestDB will also include an `explain` property in the response which gives details about the execution plan. |
| `quoteLargeNum` | No | `false` | `true` or `false`. When set to `true`, QuestDB will surround `LONG` type numbers with double quotation marks that will make them parsed as strings. |

The parameters must be URL encoded.

#### Headers[​](#headers "Direct link to Headers")

Supported HTTP headers:

| Header | Required | Description |
| --- | --- | --- |
| `Statement-Timeout` | No | Query timeout in milliseconds, overrides default timeout from server.conf |

### Examples[​](#examples-2 "Direct link to Examples")

#### SELECT query example:[​](#select-query-example "Direct link to SELECT query example:")

```prism-code
curl -G \  
  --data-urlencode "query=SELECT timestamp, price FROM trades LIMIT 2;" \  
  --data-urlencode "count=true" \  
  http://localhost:9000/exec
```

A HTTP status code of `200` is returned with the following response body:

```prism-code
{  
  "query": "SELECT timestamp, price FROM trades LIMIT 2;",  
  "columns": [  
    {  
      "name": "timestamp",  
      "type": "TIMESTAMP"  
    },  
    {  
      "name": "price",  
      "type": "DOUBLE"  
    }  
  ],  
  "timestamp": 0  
  "dataset": [  
    ["2024-01-01T00:00:00.000000Z", 142.50],  
    ["2024-01-01T00:00:01.000000Z", 142.75]  
  ],  
  "count": 2  
}
```

SELECT query returns response in the following format:

```prism-code
{  
  "query": string,  
  "columns": Array<{ "name": string, "type": string }>  
  "dataset": Array<Array<Value for Column1, Value for Column2>>,  
  "timestamp": number,  
  "count": Optional<number>,  
  "timings": Optional<{ compiler: number, count: number, execute: number }>,  
  "explain": Optional<{ jitCompiled: boolean }>  
}
```

You can find the exact list of column types in the
[dedicated page](/docs/query/datatypes/overview/).

The `timestamp` field indicates which of the columns in the result set is the
designated timestamp, or -1 if there isn't one.

#### UPDATE query example:[​](#update-query-example "Direct link to UPDATE query example:")

This request executes an update of table `weather` setting 2 minutes query
timeout

```prism-code
curl -G \  
  -H "Statement-Timeout: 120000" \  
  --data-urlencode "query=UPDATE weather SET tempF = tempF + 0.12 WHERE tempF > 60" \  
  http://localhost:9000/exec
```

A HTTP status code of `200` is returned with the following response body:

```prism-code
{  
  "ddl": "OK",  
  "updated": 34  
}
```

#### CREATE TABLE query example:[​](#create-table-query-example "Direct link to CREATE TABLE query example:")

This request creates a basic table, with a designated timestamp.

```prism-code
curl -G \  
  -H "Statement-Timeout: 120000" \  
  --data-urlencode "query=CREATE TABLE foo ( a INT, ts TIMESTAMP) timestamp(ts)" \  
  http://localhost:9000/exec
```

A HTTP status code of `200` is returned with the following response body:

```prism-code
{  
  "ddl": "OK"  
}
```

## /exp - Export data[​](#exp---export-data "Direct link to /exp - Export data")

This endpoint allows you to pass url-encoded queries but the request body is
returned in a tabular form to be saved and reused as opposed to JSON.

### Overview[​](#overview-1 "Direct link to Overview")

`/exp` is expecting an HTTP GET request with following parameters:

| Parameter | Required | Description |
| --- | --- | --- |
| `query` | Yes | URL encoded query text. It can be multi-line. |
| `limit` | No | Paging opp parameter. For example, `limit=10,20` will return row numbers 10 through to 20 inclusive and `limit=20` will return first 20 rows, which is equivalent to `limit=0,20`. `limit=-20` will return the last 20 rows. |
| `nm` | No | `true` or `false`. Skips the metadata section of the response when set to `true`. |
| `fmt` | No | Export format. Valid values: `parquet`, `csv`. When set to `parquet`, exports data in Parquet format instead of CSV. |

#### Parquet Export Parameters[​](#parquet-export-parameters "Direct link to Parquet Export Parameters")

warning

Parquet exports currently require writing interim data to disk, and therefore must be run on **read-write instances only**.

This limitation will be removed in future.

When `fmt=parquet`, the following additional parameters are supported:

| Parameter | Required | Default | Description |
| --- | --- | --- | --- |
| `partition_by` | No | `NONE` | Partition unit: `NONE`, `HOUR`, `DAY`, `WEEK`, `MONTH`, or `YEAR`. |
| `compression_codec` | No | `ZSTD` | Compression algorithm: `UNCOMPRESSED`, `SNAPPY`, `GZIP`, `LZ4`, `ZSTD`, `LZ4_RAW`, `BROTLI`, `LZO`. |
| `compression_level` | No | `9` | Compression level (codec-specific). Higher values = better compression but slower. |
| `row_group_size` | No | `100000` | Number of rows per Parquet row group. |
| `data_page_size` | No | `1048576` | Size of data pages in bytes (default 1MB). |
| `statistics_enabled` | No | `true` | Enable Parquet column statistics: `true` or `false`. |
| `parquet_version` | No | `2` | Parquet format version: `1` (v1.0) or `2` (v2.0). |
| `raw_array_encoding` | No | `false` | Use raw encoding for arrays: `true` (lighter-weight, less compatible) or `false` (heavier-weight, more compatible) |

The parameters must be URL encoded.

### Examples[​](#examples-3 "Direct link to Examples")

#### CSV Export (default)[​](#csv-export-default "Direct link to CSV Export (default)")

Considering the query:

```prism-code
curl -G \  
  --data-urlencode "query=SELECT AccidentIndex2, Date, Time FROM 'Accidents0514.csv'" \  
  --data-urlencode "limit=5" \  
  http://localhost:9000/exp
```

A HTTP status code of `200` is returned with the following response body:

```prism-code
"AccidentIndex","Date","Time"  
200501BS00001,"2005-01-04T00:00:00.000Z",17:42  
200501BS00002,"2005-01-05T00:00:00.000Z",17:36  
200501BS00003,"2005-01-06T00:00:00.000Z",00:15  
200501BS00004,"2005-01-07T00:00:00.000Z",10:35  
200501BS00005,"2005-01-10T00:00:00.000Z",21:13
```

#### Parquet Export[​](#parquet-export "Direct link to Parquet Export")

Export query results to Parquet format:

```prism-code
curl -G \  
  --data-urlencode "query=SELECT * FROM trades WHERE timestamp IN today()" \  
  --data-urlencode "fmt=parquet" \  
  http://localhost:9000/exp > trades_today.parquet
```

#### Parquet Export with Custom Options[​](#parquet-export-with-custom-options "Direct link to Parquet Export with Custom Options")

Export with custom compression and partitioning:

```prism-code
curl -G \  
  --data-urlencode "query=SELECT * FROM trades" \  
  --data-urlencode "fmt=parquet" \  
  --data-urlencode "partition_by=DAY" \  
  --data-urlencode "compression_codec=ZSTD" \  
  --data-urlencode "compression_level=9" \  
  --data-urlencode "row_group_size=1000000" \  
  http://localhost:9000/exp > trades.parquet
```

#### Parquet Export with LZ4 Compression[​](#parquet-export-with-lz4-compression "Direct link to Parquet Export with LZ4 Compression")

Export with LZ4\_RAW compression for faster export:

```prism-code
curl -G \  
  --data-urlencode "query=SELECT symbol, price, amount FROM trades WHERE timestamp > dateadd('h', -1, now())" \  
  --data-urlencode "fmt=parquet" \  
  --data-urlencode "compression_codec=LZ4_RAW" \  
  http://localhost:9000/exp > recent_trades.parquet
```

## Error responses[​](#error-responses "Direct link to Error responses")

### Malformed queries[​](#malformed-queries "Direct link to Malformed queries")

A successful call to `/exec` or `/exp` which also contains a malformed query
will return response bodies with the following format:

```prism-code
{  
  "query": string,  
  "error": string,  
  "position": number  
}
```

The `position` field is the character number from the beginning of the string
where the error was found.

Considering the query:

```prism-code
curl -G \  
  --data-urlencode "query=SELECT * FROM table;" \  
  http://localhost:9000/exp
```

A HTTP status code of `400` is returned with the following response body:

```prism-code
{  
  "query": "SELECT * FROM table;",  
  "error": "function, literal or constant is expected",  
  "position": 8  
}
```

## Authentication (RBAC)[​](#authentication-rbac "Direct link to Authentication (RBAC)")

note

Role-based Access Control (RBAC) is available in
[QuestDB Enterprise](https://questdb.com/enterprise/). See the next paragraph for authentication in
QuestDB Open Source.

REST API supports two authentication types:

* HTTP basic authentication
* Token-based authentication

The first authentication type is mainly supported by web browsers. But you can
also apply user credentials programmatically in a `Authorization: Basic` header.
This example `curl` command that executes a `SELECT 1;` query along with the
`Authorization: Basic` header:

```prism-code
curl -G --data-urlencode "query=SELECT 1;" \  
    -u "my_user:my_password" \  
    http://localhost:9000/exec
```

The second authentication type requires a REST API token to be specified in a
`Authorization: Bearer` header:

```prism-code
curl -G --data-urlencode "query=SELECT 1;" \  
    -H "Authorization: Bearer qt1cNK6s2t79f76GmTBN9k7XTWm5wwOtF7C0UBxiHGPn44" \  
    http://localhost:9000/exec
```

Refer to the [user management](/docs/security/rbac/#user-management) page to
learn more on how to generate a REST API token.

## Authentication in QuestDB open source[​](#authentication-in-questdb-open-source "Direct link to Authentication in QuestDB open source")

QuestDB Open Source supports HTTP basic authentication. To enable it, set the
configuration options `http.user` and `http.password` in `server.conf`.

The following example shows how to enable HTTP basic authentication in QuestDB
open source:

```prism-code
http.user=my_user  
http.password=my_password
```

Then this `curl` command executes a `SELECT 1;` query:

```prism-code
curl -G --data-urlencode "query=SELECT 1;" \  
    -u "my_user:my_password" \  
    http://localhost:9000/exec
```