On this page

Querying - as a base action - is performed in three primary ways:

1. Query via the
   [QuestDB Web Console](/docs/query/overview/#questdb-web-console)
2. Query via [PostgreSQL](/docs/query/overview/#postgresql)
3. Query via [REST HTTP API](/docs/query/overview/#rest-http-api)
4. Query via [Apache Parquet](/docs/query/overview/#apache-parquet)

For efficient and clear querying, QuestDB provides SQL with enhanced time series
extensions. This makes analyzing, downsampling, processing and reading time
series data an intuitive and flexible experience.

Queries can be written into many applications using existing drivers and clients
of the PostgreSQL or REST-ful ecosystems. However, querying is also leveraged
heavily by third-party tools to provide visualizations, such as within
[Grafana](/docs/integrations/visualization/grafana/), or for data analysis with dataframe
libraries like [Polars](/docs/integrations/data-processing/polars/).

> Need to ingest data first? Checkout our
> [Ingestion overview](/docs/ingestion/overview/).

## QuestDB Web Console[​](#questdb-web-console "Direct link to QuestDB Web Console")

The Web Console is available by default at
`http://localhost:9000`. The GUI makes it easy to write, return
and chart queries. There is autocomplete, syntax highlighting, errors, and more.
If you want to test a query or interact direclty with your data in the cleanest
and simplest way, apply queries via the [Web Console](/docs/getting-started/web-console/overview/).

![A shot of the Web Console, showing auto complete and a colourful returned table.](/docs/images/docs/console/overview.webp)

Click to zoom

For an example, click *Demo this query* in the below snippet. This will run a
query within our public demo instance and [Web Console](/docs/getting-started/web-console/overview/):

Navigate time with SQL[Demo this query](https://demo.questdb.io/?query=SELECT%0A%20%20%20%20timestamp%2C%20symbol%2C%0A%20%20%20%20first(price)%20AS%20open%2C%0A%20%20%20%20last(price)%20AS%20close%2C%0A%20%20%20%20min(price)%2C%0A%20%20%20%20max(price)%2C%0A%20%20%20%20sum(amount)%20AS%20volume%0AFROM%20trades%0AWHERE%20%20timestamp%20%3E%20dateadd('d'%2C%20-1%2C%20now())%0ASAMPLE%20BY%2015m%3B&executeQuery=true)

```prism-code
SELECT  
    timestamp, symbol,  
    first(price) AS open,  
    last(price) AS close,  
    min(price),  
    max(price),  
    sum(amount) AS volume  
FROM trades  
WHERE  timestamp > dateadd('d', -1, now())  
SAMPLE BY 15m;
```

If you see *Demo this query* on other snippets in this docs, they can be run
against the demo instance.

## PostgreSQL[​](#postgresql "Direct link to PostgreSQL")

Query QuestDB using the PostgreSQL endpoint via the default port `8812`.

See [PGWire Client overview](/docs/query/pgwire/overview/) for details on how to
connect to QuestDB using PostgreSQL clients.

Brief examples in multiple languages are shown below.

* Python
* Java
* NodeJS
* Go
* C#
* C
* Ruby
* PHP

```prism-code
import psycopg as pg  
import time  
  
# Connect to an existing QuestDB instance  
  
conn_str = 'user=admin password=quest host=127.0.0.1 port=8812 dbname=qdb'  
with pg.connect(conn_str, autocommit=True) as connection:  
  
    # Open a cursor to perform database operations  
  
    with connection.cursor() as cur:  
  
        #Query the database and obtain data as Python objects.  
  
        cur.execute('SELECT * FROM trades_pg;')  
        records = cur.fetchall()  
        for row in records:  
            print(row)  
  
# the connection is now closed
```

```prism-code
package com.myco;  
  
import java.sql.*;  
import java.util.Properties;  
  
public class App {  
    public static void main(String[] args) throws SQLException {  
        Properties properties = new Properties();  
        properties.setProperty("user", "admin");  
        properties.setProperty("password", "quest");  
        properties.setProperty("sslmode", "disable");  
  
        final Connection connection = DriverManager.getConnection(  
            "jdbc:postgresql://localhost:8812/qdb", properties);  
        try (PreparedStatement preparedStatement = connection.prepareStatement(  
                "SELECT x FROM long_sequence(5);")) {  
            try (ResultSet rs = preparedStatement.executeQuery()) {  
                while (rs.next()) {  
                    System.out.println(rs.getLong(1));  
                }  
            }  
        }  
        connection.close();  
    }  
}
```

```prism-code
"use strict"  
  
const { Client } = require("pg")  
  
const start = async () => {  
  const client = new Client({  
    database: "qdb",  
    host: "127.0.0.1",  
    password: "quest",  
    port: 8812,  
    user: "admin",  
  })  
  await client.connect()  
  
  const res = await client.query("SELECT x FROM long_sequence(5);")  
  
  console.log(res.rows)  
  
  await client.end()  
}  
  
start().catch(console.error)
```

```prism-code
package main  
  
import (  
  "database/sql"  
  "fmt"  
  
  _ "github.com/lib/pq"  
)  
  
const (  
  host     = "localhost"  
  port     = 8812  
  user     = "admin"  
  password = "quest"  
  dbname   = "qdb"  
)  
  
func main() {  
  connStr := fmt.Sprintf(  
    "host=%s port=%d user=%s password=%s dbname=%s sslmode=disable",  
    host, port, user, password, dbname)  
  db, err := sql.Open("postgres", connStr)  
  checkErr(err)  
  defer db.Close()  
  
  stmt, err := db.Prepare("SELECT x FROM long_sequence(5);")  
  checkErr(err)  
  defer stmt.Close()  
  
  rows, err := stmt.Query()  
  checkErr(err)  
  defer rows.Close()  
  
  var num string  
  for rows.Next() {  
    err = rows.Scan(&num)  
    checkErr(err)  
    fmt.Println(num)  
  }  
  
  err = rows.Err()  
  checkErr(err)  
}  
  
func checkErr(err error) {  
  if err != nil {  
    panic(err)  
  }  
}
```

```prism-code
// compile with  
// g++ libpq_example.c -o libpq_example.exe  -I pgsql\include -L dev\pgsql\lib  
// -std=c++17  -lpthread -lpq  
#include <libpq-fe.h>  
#include <stdio.h>  
#include <stdlib.h>  
  
void do_exit(PGconn *conn) {  
  PQfinish(conn);  
  exit(1);  
}  
  
int main() {  
  PGconn *conn = PQconnectdb(  
      "host=localhost user=admin password=quest port=8812 dbname=testdb");  
  if (PQstatus(conn) == CONNECTION_BAD) {  
    fprintf(stderr, "Connection to database failed: %s\n",  
            PQerrorMessage(conn));  
    do_exit(conn);  
  }  
  PGresult *res = PQexec(conn, "SELECT x FROM long_sequence(5);");  
  if (PQresultStatus(res) != PGRES_TUPLES_OK) {  
    printf("No data retrieved\n");  
    PQclear(res);  
    do_exit(conn);  
  }  
  int rows = PQntuples(res);  
  for (int i = 0; i < rows; i++) {  
    printf("%s\n", PQgetvalue(res, i, 0));  
  }  
  PQclear(res);  
  PQfinish(conn);  
  return 0;  
}
```

```prism-code
using Npgsql;  
string username = "admin";  
string password = "quest";  
string database = "qdb";  
int port = 8812;  
var connectionString = $@"host=localhost;port={port};username={username};password={password};  
database={database};ServerCompatibilityMode=NoTypeLoading;";  
await using NpgsqlConnection connection = new NpgsqlConnection(connectionString);  
await connection.OpenAsync();  
  
var sql = "SELECT x FROM long_sequence(5);";  
  
await using NpgsqlCommand command = new NpgsqlCommand(sql, connection);  
await using (var reader = await command.ExecuteReaderAsync()) {  
    while (await reader.ReadAsync())  
    {  
        var x = reader.GetInt64(0);  
    }  
}
```

```prism-code
require 'pg'  
begin  
    conn =PG.connect( host: "127.0.0.1", port: 8812, dbname: 'qdb',  
                      user: 'admin', password: 'quest' )  
    rows = conn.exec 'SELECT x FROM long_sequence(5);'  
    rows.each do |row|  
        puts row  
    end  
rescue PG::Error => e  
     puts e.message  
ensure  
    conn.close if conn  
end
```

```prism-code
<?php  
  
function exceptions_error_handler($severity, $message, $filename, $lineno) {  
    throw new ErrorException($message, 0, $severity, $filename, $lineno);  
}  
  
set_error_handler('exceptions_error_handler');  
$db_conn = null;  
  
try {  
        $db_conn = pg_connect(" host = 'localhost' port=8812 dbname = 'qdb' user = 'admin'  password = 'quest' ");  
        $result = pg_query($db_conn, 'SELECT x FROM long_sequence(5);' );  
        while ($row = pg_fetch_assoc($result) ){  
                print_r($row);  
                }  
        pg_free_result($result);  
} catch (Exception $e) {  
    echo 'Caught exception: ',  $e->getMessage(), "\n";  
} finally {  
        if (!is_null($db_conn)) {  
                pg_close($db_conn);  
        }  
}  
  
?>
```

#### Further Reading[​](#further-reading "Direct link to Further Reading")

See the [PGWire Client overview](/docs/query/pgwire/overview/) for more details on how to use PostgreSQL
clients to connect to QuestDB.

## REST HTTP API[​](#rest-http-api "Direct link to REST HTTP API")

QuestDB exposes a REST API for compatibility with a wide range of libraries and
tools.

The REST API is accessible on port `9000` and has the following query-capable
entrypoints:

For details such as content type, query parameters and more, refer to the
[REST HTTP API](/docs/query/rest-api/) reference.

| Entrypoint | HTTP Method | Description | REST HTTP API Reference |
| --- | --- | --- | --- |
| [`/exp?query=..`](#exp-sql-query-to-csv) | GET | Export SQL Query as CSV | [Reference](/docs/query/rest-api/#exp---export-data) |
| [`/exec?query=..`](#exec-sql-query-to-json) | GET | Run SQL Query returning JSON result set | [Reference](/docs/query/rest-api/#exec---execute-queries) |

#### `/exp`: SQL Query to CSV[​](#exp-sql-query-to-csv "Direct link to exp-sql-query-to-csv")

The `/exp` entrypoint allows querying the database with a SQL select query and
obtaining the results as CSV.

For obtaining results in JSON, use `/exec` instead, documented next.

* cURL
* Python

```prism-code
curl -G --data-urlencode \  
    "query=SELECT * FROM example_table2 LIMIT 3" \  
    http://localhost:9000/exp
```

```prism-code
"col1","col2","col3"  
"a",10.5,true  
"b",100.0,false  
"c",,true
```

```prism-code
import requests  
  
resp = requests.get(  
    'http://localhost:9000/exp',  
    {  
        'query': 'SELECT * FROM example_table2',  
        'limit': '3,6'   # Rows 3, 4, 5  
    })  
print(resp.text)
```

```prism-code
"col1","col2","col3"  
"d",20.5,true  
"e",200.0,false  
"f",,true
```

#### `/exec`: SQL Query to JSON[​](#exec-sql-query-to-json "Direct link to exec-sql-query-to-json")

The `/exec` entrypoint takes a SQL query and returns results as JSON.

This is similar to the `/exp` entry point which returns results as CSV.

##### Querying Data[​](#querying-data "Direct link to Querying Data")

* cURL
* Python
* NodeJS
* Go

```prism-code
curl -G \  
  --data-urlencode "query=SELECT x FROM long_sequence(5);" \  
  http://localhost:9000/exec
```

The JSON response contains the original query, a `"columns"` key with the schema
of the results, a `"count"` number of rows and a `"dataset"` with the results.

```prism-code
{  
  "query": "SELECT x FROM long_sequence(5);",  
  "columns": [{ "name": "x", "type": "LONG" }],  
  "dataset": [[1], [2], [3], [4], [5]],  
  "count": 5  
}
```

```prism-code
import sys  
import requests  
  
host = 'http://localhost:9000'  
  
sql_query = "select * from long_sequence(10)"  
  
try:  
    response = requests.get(  
        host + '/exec',  
        params={'query': sql_query}).json()  
    for row in response['dataset']:  
        print(row[0])  
except requests.exceptions.RequestException as e:  
    print(f'Error: {e}', file=sys.stderr)
```

```prism-code
const fetch = require("node-fetch")  
  
const HOST = "http://localhost:9000"  
  
async function run() {  
  try {  
    const query = "SELECT x FROM long_sequence(5);"  
  
    const response = await fetch(  
      `${HOST}/exec?query=${encodeURIComponent(query)}`,  
    )  
    const json = await response.json()  
  
    console.log(json)  
  } catch (error) {  
    console.log(error)  
  }  
}  
  
run()
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
  params.Add("query", "SELECT x FROM long_sequence(5);")  
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

Alternatively, the `/exec` endpoint can be used to create a table and the
`INSERT` statement can be used to populate it with values:

* cURL
* NodeJS
* Python

```prism-code
# Create Table  
curl -G \  
  --data-urlencode "query=CREATE TABLE IF NOT EXISTS trades(name VARCHAR, value INT)" \  
  http://localhost:9000/exec  
  
# Insert a row  
curl -G \  
  --data-urlencode "query=INSERT INTO trades VALUES('abc', 123456)" \  
  http://localhost:9000/exec  
  
# Update a row  
curl -G \  
  --data-urlencode "query=UPDATE trades SET value = 9876 WHERE name = 'abc'" \  
  http://localhost:9000/exec
```

The `node-fetch` package can be installed using `npm i node-fetch`.

```prism-code
const fetch = require("node-fetch");  
  
const HOST = "http://localhost:9000";  
  
async function createTable() {  
  try {  
    const query = "CREATE TABLE IF NOT EXISTS trades (name VARCHAR, value INT)";  
  
    const response = await fetch(  
      `${HOST}/exec?query=${encodeURIComponent(query)}`,  
    );  
    const json = await response.json();  
  
    console.log(json);  
  } catch (error) {  
    console.log(error);  
  }  
}  
  
async function insertData() {  
  try {  
    const query = "INSERT INTO trades VALUES('abc', 123456)";  
  
    const response = await fetch(  
      `${HOST}/exec?query=${encodeURIComponent(query)}`,  
    );  
    const json = await response.json();  
  
    console.log(json);  
  } catch (error) {  
    console.log(error);  
  }  
}  
  
async function updateData() {  
  try {  
    const query = "UPDATE trades SET value = 9876 WHERE name = 'abc'";  
  
    const response = await fetch(  
      `${HOST}/exec?query=${encodeURIComponent(query)}`,  
    );  
    const json = await response.json();  
  
    console.log(json);  
  } catch (error) {  
    console.log(error);  
  }  
}  
  
createTable().then(insertData).then(updateData);
```

```prism-code
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
    print("Error: %s" % (e))  
  
# create table  
run_query("CREATE TABLE IF NOT EXISTS trades (name VARCHAR, value INT)")  
# insert row  
run_query("INSERT INTO trades VALUES('abc', 123456)")  
# update row  
run_query("UPDATE trades SET value = 9876 WHERE name = 'abc'")
```

## Apache Parquet[​](#apache-parquet "Direct link to Apache Parquet")

info

Apache Parquet support is in **beta**. It may not be fit for production use.

Please let us know if you run into issues. Either:

1. Email us at [support@questdb.io](mailto:support@questdb.io)
2. Join our [public Slack](https://slack.questdb.com/)
3. Post on our [Discourse community](https://community.questdb.com/)

Parquet files can be read and thus queried by QuestDB.

QuestDB is shipped with a demo Parquet file, `trades.parquet`, which can be
queried using the `read_parquet` function.

Example:

read\_parquet example

```prism-code
SELECT  
  *  
FROM  
  read_parquet('trades.parquet')  
WHERE  
  side = 'buy';
```

The trades.parquet file is located in the `import` subdirectory inside the
QuestDB root directory. Drop your own Parquet files to the import directory and
query them using the `read_parquet()` function.

You can change the allowed directory by setting the `cairo.sql.copy.root`
configuration key.

For more information, see the
[Parquet documentation](/docs/query/functions/parquet/).

## What's next?[​](#whats-next "Direct link to What's next?")

Now... SQL! It's query time.

Whether you want to use the [Web Console](/docs/getting-started/web-console/overview/), PostgreSQL or REST HTTP (or both),
query construction is rich.

To brush up and learn what's unique in QuestDB, consider the following:

* [Data types](/docs/query/datatypes/overview/)
* [SQL execution order](/docs/query/sql-execution-order/)

And to learn about some of our favourite, most powerful syntax:

* [Window functions](/docs/query/functions/window-functions/overview/) are a powerful analysis
  tool
* [Aggregate functions](/docs/query/functions/aggregation/) - aggregations
  are key!
* [Date & time operators](/docs/query/operators/date-time/) to learn about
  date and time
* [`SAMPLE BY`](/docs/query/sql/sample-by/) to summarize data into chunks
  based on a specified time interval, from a year to a microsecond
* [`WHERE IN`](/docs/query/sql/where/#time-range-where-in) to compress time ranges
  into concise intervals
* [`LATEST ON`](/docs/query/sql/latest-on/) for latest values within
  multiple series within a table
* [`ASOF JOIN`](/docs/query/sql/asof-join/) to associate timestamps between
  a series based on proximity; no extra indices required
* [Materialized Views](/docs/concepts/materialized-views/) to pre-compute complex queries
  for optimal performance

Looking for visuals?

* Explore [Grafana](/docs/integrations/visualization/grafana/)
* Jump quickly into the [Web Console](/docs/getting-started/web-console/overview/)