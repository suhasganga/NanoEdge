On this page

QuestDB provides a simple [HTTP API](/docs/query/rest-api/) that allows you to interact with the database using SQL queries.
This API can be leveraged for automation using Bash scripts and scheduled execution via cron jobs. This is a lightweight
approach that requires minimal dependencies.

For a more robust approach, you might want to explore the integration with workflow orchestrators such as
[Apache Airflow](/docs/integrations/orchestration/airflow/) or [Dagster](/docs/integrations/orchestration/dagster/).

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* QuestDB running locally or on a server
* `curl` installed (pre-installed on most Linux/macOS systems)
* Basic knowledge of Bash or similar scripting language

## Example: Running a Scheduled Query[​](#example-running-a-scheduled-query "Direct link to Example: Running a Scheduled Query")

The following example demonstrates how to execute a query using the HTTP API:

drop-partitions.sh

```prism-code
#!/bin/bash  
  
# QuestDB API URL  
QUESTDB_URL="http://localhost:9000/exec"  
  
# Query: Drop partitions older than 30 days  
QUERY="ALTER TABLE my_table DROP PARTITION WHERE timestamp < dateadd('d', -30, now());"  
  
# Execute the query  
curl -G "$QUESTDB_URL" --data-urlencode "query=$QUERY"
```

## Automating with Cron[​](#automating-with-cron "Direct link to Automating with Cron")

To execute this script daily at midnight, add the following line to your crontab:

```prism-code
0 0 * * * /path/to/script.sh
```

## Pros & Cons[​](#pros--cons "Direct link to Pros & Cons")

✅ Simple to implement   
✅ No external dependencies   
✅ Works on any Unix-like system \

❌ No monitoring or logging   
❌ No built-in error handling   
❌ No backfilling support

## Next Steps[​](#next-steps "Direct link to Next Steps")

For more advanced automation, consider using a workflow orchestrator like [**Dagster**](/docs/integrations/orchestration/dagster/) or
[**Apache Airflow**](/docs/integrations/orchestration/airflow/).

* **Full Example Repository**: <https://github.com/questdb/data-orchestration-and-scheduling-samples>