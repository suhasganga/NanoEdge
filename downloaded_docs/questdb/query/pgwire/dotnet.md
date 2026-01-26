On this page

QuestDB is tested with the following C# client:

* [Npgsql](https://www.npgsql.org/)

Other .NET clients that are compatible with the PostgreSQL wire protocol
should also work with QuestDB, but we do not test them. If you find a client that
does not work, please [open an issue](https://github.com/questdb/questdb/issues/new?template=bug_report.yaml).

### Performance Considerations[​](#performance-considerations "Direct link to Performance Considerations")

QuestDB is a high-performance database. The PGWire protocol has many
flavors, and some of them are not optimized for performance. For best performance when querying data from QuestDB with
C#, we recommend using Npgsql with connection pooling.

tip

For data ingestion, we recommend using QuestDB's first-party clients with the [InfluxDB Line Protocol (ILP)](/docs/ingestion/overview/)
instead of PGWire. PGWire should primarily be used for querying data in QuestDB. QuestDB provides an
official [.NET client](https://questdb.com/docs/ingestion/clients/dotnet/) for data ingestion using ILP.

## Introduction to PGWire in QuestDB[​](#introduction-to-pgwire-in-questdb "Direct link to Introduction to PGWire in QuestDB")

QuestDB supports the PostgreSQL Wire Protocol (PGWire) for querying data. This compatibility allows you to use standard
.NET PostgreSQL clients with QuestDB's high-performance time-series database.

It's important to note that QuestDB's underlying storage model differs from PostgreSQL's, which means some PostgreSQL
features may not be available in QuestDB.

## Connection Parameters[​](#connection-parameters "Direct link to Connection Parameters")

The Npgsql client needs the following connection parameters to connect to QuestDB:

* **Host**: The hostname or IP address of the QuestDB server (default: `localhost`)
* **Port**: The PostgreSQL wire protocol port (default: `8812`)
* **Username**: The username for authentication (default: `admin`)
* **Password**: The password for authentication (default: `quest`)
* **Database**: The database name (default: `qdb`)
* **ServerCompatibilityMode**: This should be set to `NoTypeLoading` for QuestDB

## Npgsql[​](#npgsql "Direct link to Npgsql")

[Npgsql](https://www.npgsql.org/) is an open-source ADO.NET Data Provider for PostgreSQL. It enables .NET applications to
connect to and interact with PostgreSQL databases, including QuestDB.

### Features[​](#features "Direct link to Features")

* Full ADO.NET implementation
* Connection pooling
* Prepared statements
* Support for asynchronous operations
* Batch operations

### Installation[​](#installation "Direct link to Installation")

To use Npgsql in your project, add the following NuGet package:

#### Using the .NET CLI[​](#using-the-net-cli "Direct link to Using the .NET CLI")

```prism-code
dotnet add package Npgsql
```

#### Using the Package Manager Console[​](#using-the-package-manager-console "Direct link to Using the Package Manager Console")

```prism-code
Install-Package Npgsql
```

#### Using the PackageReference in .csproj[​](#using-the-packagereference-in-csproj "Direct link to Using the PackageReference in .csproj")

```prism-code
<ItemGroup>  
    <PackageReference Include="Npgsql" Version="9.0.3"/>  
</ItemGroup>
```

### Basic Connection[​](#basic-connection "Direct link to Basic Connection")

```prism-code
using Npgsql;  
  
namespace QuestDBExample  
{  
    class Program  
    {  
        static async Task Main(string[] args)  
        {  
            AppContext.SetSwitch("Npgsql.EnableLegacyTimestampBehavior", true);  
            // Connection string with required ServerCompatibilityMode=NoTypeLoading  
            string connectionString =  
                "Host=localhost;Port=8812;Username=admin;Password=quest;Database=qdb;" +  
                "ServerCompatibilityMode=NoTypeLoading;";  
            try  
            {  
                await using var connection = new NpgsqlConnection(connectionString);  
                await connection.OpenAsync();  
  
                Console.WriteLine("Connected to QuestDB successfully!");  
  
                await connection.CloseAsync();  
            }  
            catch (Exception ex)  
            {  
                Console.WriteLine($"Error connecting to QuestDB: {ex.Message}");  
            }  
        }  
    }  
}
```

> **Important**: Always include `ServerCompatibilityMode=NoTypeLoading` in your connection string when connecting to
> QuestDB. This is necessary because QuestDB's type system differs from PostgreSQL's, and this setting prevents Npgsql
> from attempting to load PostgreSQL-specific types that aren't supported by QuestDB.

The `AppContext.SetSwitch("Npgsql.EnableLegacyTimestampBehavior", true)` setting is required because
QuestDB handles timestamps differently than PostgreSQL. While QuestDB timestamps are always stored in UTC, they are
transmitted over PGWire protocol as 'TIMESTAMP WITHOUT TIMEZONE' for legacy compatibility reasons. This setting
ensures Npgsql properly handles these timestamps as DateTime values rather than attempting timezone conversions.

### Querying Data[​](#querying-data "Direct link to Querying Data")

```prism-code
using Npgsql;  
  
namespace QuestDBExample  
{  
    class Program  
    {  
        static async Task Main(string[] args)  
        {  
            AppContext.SetSwitch("Npgsql.EnableLegacyTimestampBehavior", true);  
            string connectionString =  
               "Host=localhost;Port=8812;Username=admin;Password=quest;Database=qdb;" +  
               "ServerCompatibilityMode=NoTypeLoading;";  
  
            try  
            {  
                await using var connection = new NpgsqlConnection(connectionString);  
                await connection.OpenAsync();  
  
  
                string sql = "SELECT symbol, price, amount, timestamp FROM trades LIMIT 10";  
                await using var command = new NpgsqlCommand(sql, connection);  
  
                await using var reader = await command.ExecuteReaderAsync();  
  
                var columns = new string[reader.FieldCount];  
                for (int i = 0; i < reader.FieldCount; i++)  
                {  
                    columns[i] = reader.GetName(i);  
                    Console.Write($"{columns[i]}\t");  
                }  
                Console.WriteLine();  
  
                while (await reader.ReadAsync())  
                {  
  
                    var symbol = reader.GetString(0);  
                    var price = reader.GetDouble(1);  
                    var amount = reader.GetDouble(2);  
                    // Get the DateTime and specify it as UTC since we know QuestDB timestamps are in UTC  
                    DateTime dateTime = DateTime.SpecifyKind(reader.GetDateTime(3), DateTimeKind.Utc);  
  
                    Console.Write($"{symbol}\t{price}\t{amount}\t{dateTime}\t\n");  
                }  
            }  
            catch (Exception ex)  
            {  
                Console.WriteLine($"Error executing query: {ex.Message}");  
            }  
        }  
    }  
}
```

### Parameterized Queries[​](#parameterized-queries "Direct link to Parameterized Queries")

Using parameterized queries with Npgsql provides protection against SQL injection and can improve performance when
executing similar queries repeatedly:

```prism-code
using Npgsql;  
  
namespace QuestDBExample  
{  
    class Program  
    {  
        static async Task Main(string[] args)  
        {  
            AppContext.SetSwitch("Npgsql.EnableLegacyTimestampBehavior", true);  
            string connectionString =  
                "Host=localhost;Port=8812;Username=admin;Password=quest;Database=qdb;" +  
                "ServerCompatibilityMode=NoTypeLoading;";  
  
            try  
            {  
                await using var connection = new NpgsqlConnection(connectionString);  
                await connection.OpenAsync();  
  
                string symbol = "BTC-USD";  
                DateTime startTime = DateTime.UtcNow.AddDays(-7000); // 7 days ago  
  
                string sql = @"  
                    SELECT *  
                    FROM trades  
                    WHERE symbol = @symbol AND timestamp >= @startTime  
                    ORDER BY timestamp DESC  
                    LIMIT 10";  
  
                await using var command = new NpgsqlCommand(sql, connection);  
  
                command.Parameters.AddWithValue("@symbol", symbol);  
                command.Parameters.AddWithValue("@startTime", startTime);  
  
                await using var reader = await command.ExecuteReaderAsync();  
  
                while (await reader.ReadAsync())  
                {  
                    DateTime timestamp = (DateTime)reader["timestamp"];  
                    timestamp = DateTime.SpecifyKind(timestamp, DateTimeKind.Utc);  
  
                    string tradingSymbol = reader["symbol"].ToString();  
                    double price = reader.GetDouble(reader.GetOrdinal("price"));  
  
                    Console.WriteLine($"Timestamp: {timestamp}, Symbol: {tradingSymbol}, Price: {price:F2}");  
                }  
            }  
            catch (Exception ex)  
            {  
                Console.WriteLine($"Error executing parameterized query: {ex.Message}");  
            }  
        }  
    }  
}
```

### Connection Pooling[​](#connection-pooling "Direct link to Connection Pooling")

Npgsql includes built-in connection pooling to efficiently manage database connections. Connection pooling is enabled by
default, but you can configure various pooling settings in the connection string:

```prism-code
using Npgsql;  
  
namespace QuestDBExample  
{  
    class Program  
    {  
        static async Task Main(string[] args)  
        {  
            AppContext.SetSwitch("Npgsql.EnableLegacyTimestampBehavior", true);  
            string connectionString =  
                "Host=localhost;Port=8812;Username=admin;Password=quest;Database=qdb;" +  
                "ServerCompatibilityMode=NoTypeLoading;" +  
                "Maximum Pool Size=20;Minimum Pool Size=1;Connection Lifetime=15;";  
  
            try  
            {  
                // Simulate multiple concurrent connections  
                var tasks = new Task[10];  
                for (int i = 0; i < 10; i++)  
                {  
                    int connectionId = i;  
                    tasks[i] = Task.Run(async () =>  
                    {  
                        await using var connection = new NpgsqlConnection(connectionString);  
                        await connection.OpenAsync();  
  
                        Console.WriteLine($"Connection {connectionId} opened");  
  
                        // Simulate some work  
                        await Task.Delay(1000);  
  
                        await using var cmd = new NpgsqlCommand("SELECT 1", connection);  
                        int result = (int)await cmd.ExecuteScalarAsync();  
  
                        Console.WriteLine($"Connection {connectionId} executed query with result: {result}");  
                    });  
                }  
  
                await Task.WhenAll(tasks);  
                Console.WriteLine("All connections have been processed");  
            }  
            catch (Exception ex)  
            {  
                Console.WriteLine($"Error: {ex.Message}");  
            }  
        }  
    }  
}
```

### Handling QuestDB-Specific Time-Series Queries[​](#handling-questdb-specific-time-series-queries "Direct link to Handling QuestDB-Specific Time-Series Queries")

QuestDB provides specialized time-series functions that can be used with Npgsql:

```prism-code
using Npgsql;  
  
namespace QuestDBExample  
{  
    class Program  
    {  
        static async Task Main(string[] args)  
        {  
            AppContext.SetSwitch("Npgsql.EnableLegacyTimestampBehavior", true);  
            string connectionString =  
                "Host=localhost;Port=8812;Username=admin;Password=quest;Database=qdb;" +  
                "ServerCompatibilityMode=NoTypeLoading;";  
  
            try  
            {  
                await using var connection = new NpgsqlConnection(connectionString);  
                await connection.OpenAsync();  
  
                // SAMPLE BY query (time-based downsampling)  
                string sampleByQuery = @"  
                    SELECT  
                        timestamp,  
                        symbol,  
                        avg(price) as avg_price,  
                        min(price) as min_price,  
                        max(price) as max_price  
                    FROM trades  
                    WHERE timestamp >= dateadd('d', -7000, now())  
                    SAMPLE BY 1h";  
  
                Console.WriteLine("Executing SAMPLE BY query...");  
                await using (var cmd1 = new NpgsqlCommand(sampleByQuery, connection))  
                {  
                    await using var reader = await cmd1.ExecuteReaderAsync();  
  
                    while (await reader.ReadAsync())  
                    {  
                        Console.WriteLine($"Time: {reader["timestamp"]}, " +  
                                         $"Symbol: {reader["symbol"]}, " +  
                                         $"Avg Price: {reader.GetDouble(reader.GetOrdinal("avg_price")):F2}, " +  
                                         $"Range: {reader.GetDouble(reader.GetOrdinal("min_price")):F2} - " +  
                                         $"{reader.GetDouble(reader.GetOrdinal("max_price")):F2}");  
                    }  
                }  
  
                // LATEST ON query (last value per group)  
                string latestByQuery = "SELECT * FROM trades LATEST ON timestamp PARTITION BY symbol";  
                Console.WriteLine("\nExecuting LATEST ON query...");  
                await using (var cmd2 = new NpgsqlCommand(latestByQuery, connection))  
                {  
                    await using var reader = await cmd2.ExecuteReaderAsync();  
  
                    while (await reader.ReadAsync())  
                    {  
                        Console.WriteLine($"Symbol: {reader["symbol"]}, " +  
                                         $"Latest Price: {reader.GetDouble(reader.GetOrdinal("price")):F2} " +  
                                         $"at {reader["timestamp"]}");  
                    }  
                }  
            }  
            catch (Exception ex)  
            {  
                Console.WriteLine($"Error executing time-series query: {ex.Message}");  
            }  
        }  
    }  
}
```

### Using ASP.NET Core[​](#using-aspnet-core "Direct link to Using ASP.NET Core")

Here's an example of integrating QuestDB with an ASP.NET Core web application using direct Npgsql access:

```prism-code
using Microsoft.AspNetCore.Mvc;  
using Npgsql;  
  
namespace QuestDBAspNetCoreExample  
{  
    public class Trade  
    {  
        public DateTime Timestamp { get; set; }  
        public string Symbol { get; set; }  
        public double Price { get; set; }  
        public double Amount { get; set; }  
    }  
  
    public class QuestDBService  
    {  
        private readonly string _connectionString;  
  
        public QuestDBService(IConfiguration configuration)  
        {  
            _connectionString = configuration.GetConnectionString("QuestDB");  
        }  
  
        public async Task<IEnumerable<Trade>> GetRecentTradesAsync(string symbol = null, int limit = 10)  
        {  
            var trades = new List<Trade>();  
  
            await using var connection = new NpgsqlConnection(_connectionString);  
            await connection.OpenAsync();  
  
            string sql;  
            NpgsqlCommand command;  
  
            if (string.IsNullOrEmpty(symbol))  
            {  
                sql = "SELECT timestamp, symbol, price, amount FROM trades ORDER BY timestamp DESC LIMIT @limit";  
                command = new NpgsqlCommand(sql, connection);  
                command.Parameters.AddWithValue("@limit", limit);  
            }  
            else  
            {  
                sql = "SELECT timestamp, symbol, price, amount FROM trades WHERE symbol = @symbol ORDER BY timestamp DESC LIMIT @limit";  
                command = new NpgsqlCommand(sql, connection);  
                command.Parameters.AddWithValue("@symbol", symbol);  
                command.Parameters.AddWithValue("@limit", limit);  
            }  
  
            await using var reader = await command.ExecuteReaderAsync();  
            while (await reader.ReadAsync())  
            {  
                trades.Add(new Trade  
                {  
                    Timestamp = DateTime.SpecifyKind(reader.GetDateTime(0), DateTimeKind.Utc),  
                    Symbol = reader.GetString(1),  
                    Price = reader.GetDouble(2),  
                    Amount = reader.GetDouble(3)  
                });  
            }  
  
            return trades;  
        }  
  
        public async Task<IEnumerable<Trade>> GetLatestTradesAsync()  
        {  
            var trades = new List<Trade>();  
  
            await using var connection = new NpgsqlConnection(_connectionString);  
            await connection.OpenAsync();  
  
            string sql = "SELECT * FROM trades LATEST ON timestamp PARTITION BY symbol";  
            await using var command = new NpgsqlCommand(sql, connection);  
  
            await using var reader = await command.ExecuteReaderAsync();  
            while (await reader.ReadAsync())  
            {  
                trades.Add(new Trade  
                {  
                    Timestamp = DateTime.SpecifyKind(reader.GetDateTime(reader.GetOrdinal("timestamp")), DateTimeKind.Utc),  
                    Symbol = reader.GetString(reader.GetOrdinal("symbol")),  
                    Price = reader.GetDouble(reader.GetOrdinal("price")),  
                    Amount = reader.GetDouble(reader.GetOrdinal("amount"))  
                });  
            }  
  
            return trades;  
        }  
  
        public async Task<IEnumerable<dynamic>> GetTradeStatsAsync(int days = 7)  
        {  
            var stats = new List<dynamic>();  
  
            await using var connection = new NpgsqlConnection(_connectionString);  
            await connection.OpenAsync();  
  
            string sql = @"  
                SELECT  
                    symbol,  
                    count(*) as trade_count,  
                    avg(price) as avg_price,  
                    min(price) as min_price,  
                    max(price) as max_price,  
                    sum(amount) as total_volume  
                FROM trades  
                WHERE timestamp >= dateadd('d', @days, now())  
                GROUP BY symbol  
                ORDER BY total_volume DESC";  
  
            await using var command = new NpgsqlCommand(sql, connection);  
            command.Parameters.AddWithValue("@days", -days);  
  
            await using var reader = await command.ExecuteReaderAsync();  
            while (await reader.ReadAsync())  
            {  
                stats.Add(new  
                {  
                    Symbol = reader.GetString(0),  
                    TradeCount = reader.GetInt64(1),  
                    AvgPrice = reader.GetDouble(2),  
                    MinPrice = reader.GetDouble(3),  
                    MaxPrice = reader.GetDouble(4),  
                    TotalVolume = reader.GetDouble(5)  
                });  
            }  
  
            return stats;  
        }  
    }  
  
    public class Startup  
    {  
        public Startup(IConfiguration configuration)  
        {  
            Configuration = configuration;  
        }  
  
        public IConfiguration Configuration { get; }  
  
        public void ConfigureServices(IServiceCollection services)  
        {  
            services.AddSingleton<QuestDBService>();  
  
            services.AddControllers();  
            services.AddSwaggerGen();  
        }  
  
        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)  
        {  
            if (env.IsDevelopment())  
            {  
                app.UseDeveloperExceptionPage();  
                app.UseSwagger();  
                app.UseSwaggerUI();  
            }  
  
            app.UseRouting();  
            app.UseEndpoints(endpoints =>  
            {  
                endpoints.MapControllers();  
            });  
        }  
    }  
  
    [ApiController]  
    [Route("api/[controller]")]  
    public class TradesController : ControllerBase  
    {  
        private readonly QuestDBService _questDBService;  
  
        public TradesController(QuestDBService questDBService)  
        {  
            _questDBService = questDBService;  
        }  
  
        [HttpGet]  
        public async Task<ActionResult<IEnumerable<Trade>>> GetRecentTrades([FromQuery] string symbol = null, [FromQuery] int limit = 10)  
        {  
            var trades = await _questDBService.GetRecentTradesAsync(symbol, limit);  
            return Ok(trades);  
        }  
  
        [HttpGet("latest")]  
        public async Task<ActionResult<IEnumerable<Trade>>> GetLatestTrades()  
        {  
            var trades = await _questDBService.GetLatestTradesAsync();  
            return Ok(trades);  
        }  
  
        [HttpGet("stats")]  
        public async Task<ActionResult> GetTradeStats([FromQuery] int days = 7)  
        {  
            var stats = await _questDBService.GetTradeStatsAsync(days);  
            return Ok(stats);  
        }  
    }  
  
    public class Program  
    {  
        public static void Main(string[] args)  
        {  
            AppContext.SetSwitch("Npgsql.EnableLegacyTimestampBehavior", true);  
            CreateHostBuilder(args).Build().Run();  
        }  
  
        public static IHostBuilder CreateHostBuilder(string[] args) =>  
            Host.CreateDefaultBuilder(args)  
                .ConfigureWebHostDefaults(webBuilder =>  
                {  
                    webBuilder.UseStartup<Startup>();  
                });  
    }  
}
```

Add the following to `appsettings.json`:

```prism-code
{  
  "ConnectionStrings": {  
    "QuestDB": "Host=localhost;Port=8812;Username=admin;Password=quest;Database=qdb;ServerCompatibilityMode=NoTypeLoading;"  
  },  
  "Logging": {  
    "LogLevel": {  
      "Default": "Information",  
      "Microsoft": "Warning",  
      "Microsoft.Hosting.Lifetime": "Information"  
    }  
  },  
  "AllowedHosts": "*"  
}
```

### Working with Dapper[​](#working-with-dapper "Direct link to Working with Dapper")

[Dapper](https://github.com/DapperLib/Dapper) is a popular micro-ORM that works well with Npgsql and QuestDB. It
provides a lightweight alternative to full ORMs like Entity Framework Core while still offering object mapping
capabilities.

First, add the Dapper NuGet package:

```prism-code
dotnet add package Dapper
```

Here's an example of using Dapper with QuestDB:

```prism-code
using Dapper;  
using Npgsql;  
  
namespace QuestDBDapperExample  
{  
    public class Trade  
    {  
        private DateTime _timestamp;  
        public DateTime Timestamp  
        {  
            get => _timestamp;  
            set => _timestamp = DateTime.SpecifyKind(value, DateTimeKind.Utc);  
        }  
        public string Symbol { get; set; }  
        public double Price { get; set; }  
        public double Amount { get; set; }  
    }  
  
    public class TimeSeriesPoint  
    {  
        private DateTime _timestamp;  
        public DateTime Timestamp  
        {  
            get => _timestamp;  
            set => _timestamp = DateTime.SpecifyKind(value, DateTimeKind.Utc);  
        }  
        public string Symbol { get; set; }  
        public double AvgPrice { get; set; }  
        public double MinPrice { get; set; }  
        public double MaxPrice { get; set; }  
    }  
  
    class Program  
    {  
        static async Task Main(string[] args)  
        {  
            AppContext.SetSwitch("Npgsql.EnableLegacyTimestampBehavior", true);  
            string connectionString =  
                "Host=localhost;Port=8812;Username=admin;Password=quest;Database=qdb;" +  
                "ServerCompatibilityMode=NoTypeLoading;";  
  
            try  
            {  
                await using var connection = new NpgsqlConnection(connectionString);  
                await connection.OpenAsync();  
  
                // Basic query with Dapper  
                var trades = await connection.QueryAsync<Trade>(  
                    "SELECT timestamp AS Timestamp, symbol AS Symbol, price AS Price, amount AS Amount " +  
                    "FROM trades LIMIT 10");  
  
                Console.WriteLine($"Retrieved {trades.Count()} trades:");  
                foreach (var trade in trades)  
                {  
                    Console.WriteLine($"Timestamp: {trade.Timestamp}, " +  
                                     $"Symbol: {trade.Symbol}, " +  
                                     $"Price: {trade.Price:F2}, " +  
                                     $"Amount: {trade.Amount:F4}");  
                }  
  
                // Parameterized query  
                string symbol = "BTC-USD";  
                DateTime startTime = DateTime.UtcNow.AddDays(-7000);  
  
                var filteredTrades = await connection.QueryAsync<Trade>(  
                    "SELECT timestamp AS Timestamp, symbol AS Symbol, price AS Price, amount AS Amount " +  
                    "FROM trades " +  
                    "WHERE symbol = @Symbol AND timestamp >= @StartTime " +  
                    "ORDER BY timestamp DESC " +  
                    "LIMIT 10",  
                    new { Symbol = symbol, StartTime = startTime });  
  
                Console.WriteLine($"\nRetrieved {filteredTrades.Count()} filtered trades for {symbol}:");  
                foreach (var trade in filteredTrades)  
                {  
                    Console.WriteLine($"Timestamp: {trade.Timestamp}, " +  
                                     $"Price: {trade.Price:F2}, " +  
                                     $"Amount: {trade.Amount:F4}");  
                }  
  
                // Time-series query with SAMPLE BY  
                var timeSeriesData = await connection.QueryAsync<TimeSeriesPoint>(  
                    "SELECT " +  
                    "   timestamp AS Timestamp, " +  
                    "   symbol AS Symbol, " +  
                    "   avg(price) AS AvgPrice, " +  
                    "   min(price) AS MinPrice, " +  
                    "   max(price) AS MaxPrice " +  
                    "FROM trades " +  
                    "WHERE timestamp >= dateadd('d', -10000, now()) " +  
                    "SAMPLE BY 1h");  
  
                Console.WriteLine($"\nRetrieved {timeSeriesData.Count()} time series points:");  
                foreach (var point in timeSeriesData)  
                {  
                    Console.WriteLine($"Time: {point.Timestamp}, " +  
                                     $"Symbol: {point.Symbol}, " +  
                                     $"Avg Price: {point.AvgPrice:F2}, " +  
                                     $"Range: {point.MinPrice:F2} - {point.MaxPrice:F2}");  
                }  
            }  
            catch (Exception ex)  
            {  
                Console.WriteLine($"Error: {ex.Message}");  
            }  
        }  
    }  
}
```

### Known Limitations with QuestDB[​](#known-limitations-with-questdb "Direct link to Known Limitations with QuestDB")

When using Npgsql with QuestDB, be aware of these limitations:

1. **Type System Differences**: QuestDB's type system differs from PostgreSQL's. Always use
   `ServerCompatibilityMode=NoTypeLoading` to avoid issues.
2. **Cursor Support**: QuestDB does not support scrollable cursors that require explicit creation and management through
   `DECLARE CURSOR` and subsequent operations.
3. **Transaction Semantics**: QuestDB has different transaction semantics compared to traditional RDBMS.
4. **Schema Management**: QuestDB's table creation and schema modification capabilities differ from PostgreSQL.
5. **Extensions**: PostgreSQL-specific extensions are not available in QuestDB.

### Performance Tips[​](#performance-tips "Direct link to Performance Tips")

1. **Connection Pooling**: Use Npgsql's built-in connection pooling for better performance in multi-threaded
   applications.
2. **Prepared Statements**: Use prepared statements for frequently executed queries to improve performance.
3. **Batch Operations**: When possible, batch multiple operations together to reduce network overhead.
4. **Query Optimization**: Take advantage of QuestDB's time-series functions like `SAMPLE BY` and `LATEST ON` for
   efficient queries.
5. **Limit Result Sets**: When dealing with large time-series datasets, use `LIMIT` clauses to avoid retrieving too much
   data at once.

## QuestDB Time Series Features[​](#questdb-time-series-features "Direct link to QuestDB Time Series Features")

QuestDB provides specialized time-series functions that can be used with Npgsql:

### SAMPLE BY Queries[​](#sample-by-queries "Direct link to SAMPLE BY Queries")

SAMPLE BY is used for time-based downsampling:

Sample By 1 Hour[Demo this query](https://demo.questdb.io/?query=SELECT%20timestamp%2C%0A%20%20%20%20%20%20%20symbol%2C%0A%20%20%20%20%20%20%20avg(price)%20as%20avg_price%2C%0A%20%20%20%20%20%20%20min(price)%20as%20min_price%2C%0A%20%20%20%20%20%20%20max(price)%20as%20max_price%0AFROM%20trades%0AWHERE%20timestamp%20%3E%3D%20dateadd('d'%2C%20-7%2C%20now())%20SAMPLE%20BY%201h%3B&executeQuery=true)

```prism-code
SELECT timestamp,  
       symbol,  
       avg(price) as avg_price,  
       min(price) as min_price,  
       max(price) as max_price  
FROM trades  
WHERE timestamp >= dateadd('d', -7, now()) SAMPLE BY 1h;
```

### LATEST ON Queries[​](#latest-on-queries "Direct link to LATEST ON Queries")

LATEST ON is an efficient way to get the most recent values:

LATEST Rows Per Symbol[Demo this query](https://demo.questdb.io/?query=SELECT%20*%0AFROM%20trades%0AWHERE%20timestamp%20IN%20today()%0ALATEST%20ON%20timestamp%20PARTITION%20BY%20symbol%3B&executeQuery=true)

```prism-code
SELECT *  
FROM trades  
WHERE timestamp IN today()  
LATEST ON timestamp PARTITION BY symbol;
```

## Highly-Available Reads with QuestDB Enterprise[​](#highly-available-reads-with-questdb-enterprise "Direct link to Highly-Available Reads with QuestDB Enterprise")

QuestDB Enterprise supports running [multiple replicas](https://questdb.com/docs/high-availability/setup/) to serve queries.
Client applications can specify **multiple hosts** in the connection string. This ensures that initial connections
succeed even if a node is down. If the connected node fails later, the application should catch the error, reconnect to
another host, and retry the read.

See our blog post for background and the companion repository for a minimal example:

* Blog: [Highly-available reads with QuestDB](https://questdb.com/blog/highly-available-reads-with-questdb/)
* Example: [questdb/questdb-ha-reads](https://github.com/questdb/questdb-ha-reads)

## PGWire Known Limitations with QuestDB[​](#pgwire-known-limitations-with-questdb "Direct link to PGWire Known Limitations with QuestDB")

* Some PostgreSQL-specific features (complex transaction semantics, exotic data types, certain metadata calls) may not be fully supported.
* Cursors/scrollable result sets and some ORM expectations may behave differently than in PostgreSQL.
* Prefer **querying** via PGWire and **ingestion** via ILP for best throughput.

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### Connection issues[​](#connection-issues "Direct link to Connection issues")

1. Verify QuestDB is running and listening on port **8812**.
2. Check credentials and network access.
3. Try a minimal query: `SELECT 1`.
4. Inspect QuestDB server logs for connection or auth errors.

### Query Errors[​](#query-errors "Direct link to Query Errors")

For query-related errors:

1. Verify that the table you're querying exists
2. Check the syntax of your SQL query
3. Ensure that you're using the correct data types for parameters
4. Look for any unsupported PostgreSQL features that might be causing issues

### Timestamp confusion[​](#timestamp-confusion "Direct link to Timestamp confusion")

* Remember: **QuestDB stores and encodes timestamps always as UTC**.

## Conclusion[​](#conclusion "Direct link to Conclusion")

Npgsql provides a robust way to connect C# applications to QuestDB through the PostgreSQL Wire Protocol. By following
the guidelines in this documentation, you can effectively query time-series data from QuestDB and integrate it with
various .NET applications.

For data ingestion, remember that QuestDB provides an
official [.NET client](https://questdb.com/docs/ingestion/clients/dotnet/) that uses the InfluxDB Line Protocol (ILP) for
high-throughput data insertion. For optimal performance, use this client for data ingestion and Npgsql for querying.

QuestDB's SQL extensions for time-series data, such as `SAMPLE BY` and `LATEST ON`, provide powerful tools for analyzing
time-series data that can be easily accessed through Npgsql.

For production applications, consider using direct Npgsql queries, as they offer more direct
control over queries and better compatibility with QuestDB's time-series model than higher-level ORMs like Entity
Framework Core, which are better suited for traditional OLTP databases.