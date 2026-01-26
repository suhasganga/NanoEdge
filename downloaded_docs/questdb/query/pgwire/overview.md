On this page

QuestDB implements the PostgreSQL wire protocol (PGWire), allowing you to
connect using standard PostgreSQL client libraries. This is the recommended way
to **query data** from QuestDB, as you can use existing PostgreSQL clients and
tools.

PGWire also supports [INSERT statements](#insert-examples) for lower-volume data
ingestion. For high-throughput ingestion, use the
[QuestDB clients](/docs/ingestion/overview/) instead.

## Query examples[​](#query-examples "Direct link to Query examples")

### .NET

Query QuestDB using Npgsql or other .NET PostgreSQL drivers.

[Read more](/docs/query/pgwire/dotnet/)

![.NET logo](/docs/images/logos/dotnet.svg)

### Go

Query QuestDB using pgx or other Go PostgreSQL drivers.

[Read more](/docs/query/pgwire/go/)

![Go logo](/docs/images/logos/go.svg)

### Java

Query QuestDB using JDBC with any PostgreSQL-compatible driver.

[Read more](/docs/query/pgwire/java/)

![Java logo](/docs/images/logos/java.svg)

### Node.js

Query QuestDB using pg or other Node.js PostgreSQL clients.

[Read more](/docs/query/pgwire/nodejs/)

![Node.js logo](/docs/images/logos/nodejs-light.svg)

### Python

Query QuestDB using psycopg, asyncpg, or other Python drivers.

[Read more](/docs/query/pgwire/python/)

![Python logo](/docs/images/logos/python.svg)

### Rust

Query QuestDB using tokio-postgres or other Rust PostgreSQL crates.

[Read more](/docs/query/pgwire/rust/)

![Rust logo](/docs/images/logos/rust.svg)

### PHP

Query QuestDB using PDO or other PHP PostgreSQL extensions.

[Read more](/docs/query/pgwire/php/)

![PHP logo](/docs/images/logos/php.svg)

### R

Query QuestDB using RPostgres or other R database packages.

[Read more](/docs/query/pgwire/r/)

![R logo](/docs/images/logos/r.svg)

## Compatibility[​](#compatibility "Direct link to Compatibility")

### Supported features[​](#supported-features "Direct link to Supported features")

* Querying (all types except `BLOB`)
* Prepared statements with bind parameters
* `INSERT` statements with bind parameters
* `UPDATE` statements with bind parameters
* DDL execution
* Batch inserts
* Plain authentication

### Unsupported features[​](#unsupported-features "Direct link to Unsupported features")

* SSL
* Remote file upload (`COPY` from `stdin`)
* `DELETE` statements
* `BLOB` transfer

### Connection properties[​](#connection-properties "Direct link to Connection properties")

| Name | Example | Description |
| --- | --- | --- |
| `database` | qdb | Can be set to any value (e.g., `qdb`). Database name is ignored; QuestDB does not have database instance names. |
| `user` | admin | User name configured in `pg.user` or `pg.readonly.user` property in `server.conf`. Default: `admin` |
| `password` | quest | Password from `pg.password` or `pg.readonly.password` property in `server.conf`. Default: `quest` |
| `options` | -c statement\_timeout=60000 | The only supported option is `statement_timeout`, which specifies maximum execution time in milliseconds for SELECT or UPDATE statements. |

## Important considerations[​](#important-considerations "Direct link to Important considerations")

### Large result sets[​](#large-result-sets "Direct link to Large result sets")

When querying large datasets, most PostgreSQL drivers load the entire result
set into memory before returning rows. This causes out-of-memory errors and
slow performance.

**Solution:** Use cursor-based fetching to retrieve rows in batches.

See [Handling Large Result Sets](/docs/query/pgwire/large-result-sets/) for
per-language examples.

### Timestamp handling[​](#timestamp-handling "Direct link to Timestamp handling")

QuestDB stores all timestamps internally in
[UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). However, when
transmitting timestamps over the PGWire protocol, QuestDB represents them as
`TIMESTAMP WITHOUT TIMEZONE`. This can lead to client libraries interpreting
these timestamps in their local timezone by default, potentially causing
confusion or incorrect data representation.

Our language-specific guides provide detailed examples on how to configure your
client to correctly interpret these timestamps as UTC.

We recommend setting the timezone in your client library to UTC to ensure
consistent handling of timestamps.

### SQL dialect differences[​](#sql-dialect-differences "Direct link to SQL dialect differences")

While QuestDB supports the PGWire protocol for communication, its SQL dialect
and feature set are not identical to PostgreSQL. QuestDB is a specialized
time-series database and does not support all SQL features, functions, or data
types that a standard PostgreSQL server does.

Always refer to the [QuestDB SQL documentation](/docs/query/overview/)
for supported operations.

### Forward-only cursors[​](#forward-only-cursors "Direct link to Forward-only cursors")

QuestDB's cursors are forward-only, differing from PostgreSQL's support for
scrollable cursors (which allow bidirectional navigation and arbitrary row
access). With QuestDB, you can iterate through query results sequentially from
start to finish, but you cannot move backward or jump to specific rows.

Explicit `DECLARE CURSOR` statements for scrollable types, or operations like
fetching in reverse (e.g., `FETCH BACKWARD`), are not supported.

This limitation can impact client libraries that rely on scrollable cursor
features. For example, Python's psycopg2 driver might encounter issues if
attempting such operations. For optimal compatibility, choose drivers or
configure existing ones to use forward-only cursors, such as Python's asyncpg
driver.

### Protocol flavors and encoding[​](#protocol-flavors-and-encoding "Direct link to Protocol flavors and encoding")

The PostgreSQL wire protocol has different implementations and options. When
your client library allows:

* Prefer the **Extended Query Protocol** over the Simple Query Protocol
* Choose clients that support **BINARY encoding** for data transfer over TEXT
  encoding for optimal performance and type fidelity

The specifics of how to configure this will vary by client library.

## Highly-available reads (Enterprise)[​](#highly-available-reads-enterprise "Direct link to Highly-available reads (Enterprise)")

QuestDB Enterprise supports running
[multiple replicas](/docs/high-availability/setup/) to serve queries. Many client
libraries allow specifying **multiple hosts** in the connection string. This
ensures that initial connections succeed even if a node is unavailable. If the
connected node fails later, the application should catch the error, reconnect to
another host, and retry the read.

For background and code samples in multiple languages, see:

* Blog: [Highly-available reads with QuestDB](https://questdb.com/blog/highly-available-reads-with-questdb/)
* Examples: [questdb/questdb-ha-reads](https://github.com/questdb/questdb-ha-reads)

## INSERT examples[​](#insert-examples "Direct link to INSERT examples")

PGWire supports INSERT statements for lower-volume ingestion use cases.

* psql
* Python
* Java
* NodeJS
* Go
* Rust

Create the table:

```prism-code
psql -h localhost -p 8812 -U admin -d qdb \  
    -c "CREATE TABLE IF NOT EXISTS t1 (name STRING, value INT);"
```

Insert row:

```prism-code
psql -h localhost -p 8812 -U admin -d qdb -c "INSERT INTO t1 VALUES('a', 42)"
```

Query back:

```prism-code
psql -h localhost -p 8812 -U admin -d qdb -c "SELECT * FROM t1"
```

Note that you can also run `psql` from Docker without installing the client
locally:

```prism-code
docker run -it --rm --network=host -e PGPASSWORD=quest \  
    postgres psql ....
```

This example uses the [psycopg3](https://www.psycopg.org/psycopg3/docs/)
adapter.

To [install](https://www.psycopg.org/psycopg3/docs/basic/install.html) the
client library, use `pip`:

```prism-code
python3 -m pip install "psycopg[binary]"
```

```prism-code
import psycopg as pg  
import time  
  
# Connect to an existing QuestDB instance  
  
conn_str = 'user=admin password=quest host=127.0.0.1 port=8812 dbname=qdb'  
with pg.connect(conn_str, autocommit=True) as connection:  
  
    # Open a cursor to perform database operations  
  
    with connection.cursor() as cur:  
  
        # Execute a command: this creates a new table  
  
        cur.execute('''  
          CREATE TABLE IF NOT EXISTS test_pg (  
              ts TIMESTAMP,  
              name STRING,  
              value INT  
          ) timestamp(ts);  
          ''')  
  
        print('Table created.')  
  
        # Insert data into the table.  
  
        for x in range(10):  
  
            # Converting datetime into millisecond for QuestDB  
  
            timestamp = time.time_ns() // 1000  
  
            cur.execute('''  
                INSERT INTO test_pg  
                    VALUES (%s, %s, %s);  
                ''',  
                (timestamp, 'python example', x))  
  
        print('Rows inserted.')  
  
        #Query the database and obtain data as Python objects.  
  
        cur.execute('SELECT * FROM test_pg;')  
        records = cur.fetchall()  
        for row in records:  
            print(row)  
  
# the connection is now closed
```

```prism-code
package com.myco;  
  
import java.sql.*;  
import java.util.Properties;  
  
class App {  
  public static void main(String[] args) throws SQLException {  
    Properties properties = new Properties();  
    properties.setProperty("user", "admin");  
    properties.setProperty("password", "quest");  
    properties.setProperty("sslmode", "disable");  
  
    final Connection connection = DriverManager.getConnection(  
      "jdbc:postgresql://localhost:8812/qdb", properties);  
    connection.setAutoCommit(false);  
  
    final PreparedStatement statement = connection.prepareStatement(  
      "CREATE TABLE IF NOT EXISTS trades (" +  
      "    ts TIMESTAMP, date DATE, name STRING, value INT" +  
      ") timestamp(ts);");  
    statement.execute();  
  
    try (PreparedStatement preparedStatement = connection.prepareStatement(  
        "INSERT INTO TRADES  VALUES (?, ?, ?, ?)")) {  
      preparedStatement.setTimestamp(  
        1,  
        new Timestamp(io.questdb.std.Os.currentTimeMicros()));  
      preparedStatement.setDate(2, new Date(System.currentTimeMillis()));  
      preparedStatement.setString(3, "abc");  
      preparedStatement.setInt(4, 123);  
      preparedStatement.execute();  
    }  
    System.out.println("Done");  
    connection.close();  
  }  
}
```

This example uses the [`pg` package](https://www.npmjs.com/package/pg) which
allows for quickly building queries using Postgres wire protocol. Details on the
use of this package can be found on the
[node-postgres documentation](https://node-postgres.com/).

This example uses naive `Date.now() * 1000` inserts for Timestamp types in
microsecond resolution. For accurate microsecond timestamps, the
[process.hrtime.bigint()](https://nodejs.org/api/process.html#processhrtimebigint)
call can be used.

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
  
  const createTable = await client.query(  
    "CREATE TABLE IF NOT EXISTS trades (" +  
      "    ts TIMESTAMP, date DATE, name STRING, value INT" +  
      ") timestamp(ts);",  
  )  
  console.log(createTable)  
  
  let now = new Date().toISOString()  
  const insertData = await client.query(  
    "INSERT INTO trades VALUES($1, $2, $3, $4);",  
    [now, now, "node pg example", 123],  
  )  
  await client.query("COMMIT")  
  
  console.log(insertData)  
  
  for (let rows = 0; rows < 10; rows++) {  
    // Providing a 'name' field allows for prepared statements / bind variables  
    now = new Date().toISOString()  
    const query = {  
      name: "insert-values",  
      text: "INSERT INTO trades VALUES($1, $2, $3, $4);",  
      values: [now, now, "node pg prep statement", rows],  
    }  
    await client.query(query)  
  }  
  await client.query("COMMIT")  
  
  const readAll = await client.query("SELECT * FROM trades")  
  console.log(readAll.rows)  
  
  await client.end()  
}  
  
start()  
  .then(() => console.log("Done"))  
  .catch(console.error)
```

This example uses the [pgx](https://github.com/jackc/pgx) driver and toolkit for
PostgreSQL in Go. More details on the use of this toolkit can be found on the
[GitHub repository for pgx](https://github.com/jackc/pgx/wiki/Getting-started-with-pgx).

```prism-code
package main  
  
import (  
  "context"  
  "fmt"  
  "log"  
  "time"  
  
  "github.com/jackc/pgx/v4"  
)  
  
var conn *pgx.Conn  
var err error  
  
func main() {  
  ctx := context.Background()  
  conn, _ = pgx.Connect(ctx, "postgresql://admin:quest@localhost:8812/qdb")  
  defer conn.Close(ctx)  
  
  // text-based query  
  _, err := conn.Exec(ctx,  
    ("CREATE TABLE IF NOT EXISTS trades (" +  
     "    ts TIMESTAMP, date DATE, name STRING, value INT" +  
     ") timestamp(ts);"))  
  if err != nil {  
    log.Fatalln(err)  
  }  
  
  // Prepared statement given the name 'ps1'  
  _, err = conn.Prepare(ctx, "ps1", "INSERT INTO trades VALUES($1,$2,$3,$4)")  
  if err != nil {  
    log.Fatalln(err)  
  }  
  
  // Insert all rows in a single commit  
  tx, err := conn.Begin(ctx)  
  if err != nil {  
    log.Fatalln(err)  
  }  
  
  for i := 0; i < 10; i++ {  
    // Execute 'ps1' statement with a string and the loop iterator value  
    _, err = conn.Exec(  
      ctx,  
      "ps1",  
      time.Now(),  
      time.Now().Round(time.Millisecond),  
      "go prepared statement",  
      i + 1)  
    if err != nil {  
      log.Fatalln(err)  
    }  
  }  
  
  // Commit the transaction  
  err = tx.Commit(ctx)  
  if err != nil {  
    log.Fatalln(err)  
  }  
  
  // Read all rows from table  
  rows, err := conn.Query(ctx, "SELECT * FROM trades")  
  fmt.Println("Reading from trades table:")  
  for rows.Next() {  
    var name string  
    var value int64  
    var ts time.Time  
    var date time.Time  
    err = rows.Scan(&ts, &date, &name, &value)  
    fmt.Println(ts, date, name, value)  
  }  
  
  err = conn.Close(ctx)  
}
```

The following example shows how to use parameterized queries and prepared
statements using the [rust-postgres](https://docs.rs/postgres/0.19.0/postgres/)
client.

```prism-code
use postgres::{Client, NoTls, Error};  
use chrono::{Utc};  
use std::time::SystemTime;  
  
fn main() -> Result<(), Error> {  
    let mut client = Client::connect("postgresql://admin:quest@localhost:8812/qdb", NoTls)?;  
  
    // Basic query  
    client.batch_execute(  
      "CREATE TABLE IF NOT EXISTS trades ( \  
          ts TIMESTAMP, date DATE, name STRING, value INT \  
      ) timestamp(ts);")?;  
  
    // Parameterized query  
    let name: &str = "rust example";  
    let val: i32 = 123;  
    let utc = Utc::now();  
    let sys_time = SystemTime::now();  
    client.execute(  
        "INSERT INTO trades VALUES($1,$2,$3,$4)",  
        &[&utc.naive_local(), &sys_time, &name, &val],  
    )?;  
  
    // Prepared statement  
    let mut txn = client.transaction()?;  
    let statement = txn.prepare("INSERT INTO trades VALUES ($1,$2,$3,$4)")?;  
    for value in 0..10 {  
        let utc = Utc::now();  
        let sys_time = SystemTime::now();  
        txn.execute(&statement, &[&utc.naive_local(), &sys_time, &name, &value])?;  
    }  
    txn.commit()?;  
  
    println!("import finished");  
    Ok(())  
}
```

### Decimal values[​](#decimal-values "Direct link to Decimal values")

To insert `decimal` values via PGWire, you must either use the `m` suffix to
indicate that the value is a decimal literal or cast the value to `decimal`:

```prism-code
INSERT INTO my_table (decimal_column) VALUES (123.45m);                        -- Using 'm' suffix  
INSERT INTO my_table (decimal_column) VALUES (CAST($1 AS DECIMAL(18, 3)));     -- Using CAST over bind parameter
```

In the text format, PostgreSQL clients send decimal values as strings.
Currently, QuestDB parses these strings as `double` values and doesn't
implicitly convert them to `decimal` to avoid unintended precision loss. You
must explicitly cast `double` values to `decimal` in your SQL queries when
inserting into `decimal` columns.