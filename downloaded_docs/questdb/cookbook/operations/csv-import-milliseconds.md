On this page

Import CSV files containing epoch timestamps in milliseconds into QuestDB.

## Problem[​](#problem "Direct link to Problem")

QuestDB expects either date/timestamp literals, or epochs in microseconds or nanoseconds.

## Solution options[​](#solution-options "Direct link to Solution options")

Here are the options available:

### Option 1: Pre-process the dataset[​](#option-1-pre-process-the-dataset "Direct link to Option 1: Pre-process the dataset")

Convert timestamps from milliseconds to microseconds before import. If importing lots of data, create Parquet files, copy them to the QuestDB import folder, and read them with `read_parquet('file.parquet')`. Then use `INSERT INTO SELECT` to copy to another table.

### Option 2: Staging table[​](#option-2-staging-table "Direct link to Option 2: Staging table")

Import into a non-partitioned table as DATE, then `INSERT INTO` a partitioned table as TIMESTAMP:

```prism-code
-- Create staging table  
CREATE TABLE trades_staging (  
  timestamp_ms LONG,  
  symbol SYMBOL,  
  price DOUBLE,  
  amount DOUBLE  
);  
  
-- Import CSV to staging table (via web console or REST API)  
  
-- Create final table  
CREATE TABLE trades (  
  timestamp TIMESTAMP,  
  symbol SYMBOL INDEX,  
  price DOUBLE,  
  amount DOUBLE  
) TIMESTAMP(timestamp) PARTITION BY DAY;  
  
-- Convert and insert  
INSERT INTO trades  
SELECT  
  cast(timestamp_ms * 1000 AS TIMESTAMP) as timestamp,  
  symbol,  
  price,  
  amount  
FROM trades_staging;  
  
-- Drop staging table  
DROP TABLE trades_staging;
```

You would be using twice the storage temporarily, but then you can drop the initial staging table.

### Option 3: ILP client[​](#option-3-ilp-client "Direct link to Option 3: ILP client")

Read the CSV line-by-line and convert, then send via the ILP client.

Related Documentation

* [CSV import](/docs/getting-started/web-console/import-csv/)
* [ILP ingestion](/docs/ingestion/overview/)
* [read\_parquet()](/docs/query/functions/parquet/)