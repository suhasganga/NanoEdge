On this page

Dagster is a modern data orchestrator that enables structured and scalable workflow automation. With Dagster, you can automate tasks such as executing SQL queries on QuestDB and managing data pipelines with built-in monitoring and logging.

Alternatively, checkout our [Automating QuestDB Tasks](/docs/operations/task-automation/) guide for a scripted approach.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* Python 3.9 or later
* QuestDB running locally or remotely
* `psycopg` library for PostgreSQL interaction
* Dagster installed

## Installation[​](#installation "Direct link to Installation")

To install Dagster and the required dependencies, run:

```prism-code
pip install dagster dagster-webserver psycopg
```

Please refer to the [Dagster Docs](https://docs.dagster.io/getting-started/installation) for other options.

## Basic integration[​](#basic-integration "Direct link to Basic integration")

On Dagster you write your automation either using a dependency graph approach, similar to Apache Airflow, or following
a data resource model. Whichever approach you take, the automation is written in Python and the easiest way to automate
QuestDB tasks is by using `Psycopg`.

## Example: Running a Query on QuestDB[​](#example-running-a-query-on-questdb "Direct link to Example: Running a Query on QuestDB")

The following example defines a Dagster operation (`op`) to execute a SQL query on QuestDB:

```prism-code
from dagster import op, job  
import psycopg  
  
@op  
def execute_query():  
    conn = psycopg.connect("postgresql://admin:quest@localhost:8812/qdb")  
    with conn.cursor() as cursor:  
        cursor.execute("ALTER TABLE my_table DROP PARTITION WHERE timestamp < dateadd('d', -30, now());")  
    conn.commit()  
  
@job  
def questdb_cleanup_job():  
    execute_query()
```

## Running the Dagster Job[​](#running-the-dagster-job "Direct link to Running the Dagster Job")

1. Start the Dagster UI:

   ```prism-code
   dagster dev
   ```
2. Open `http://localhost:3000` and trigger the `questdb_cleanup_job` manually.

## Scheduling the Job[​](#scheduling-the-job "Direct link to Scheduling the Job")

To schedule the job to run daily at midnight:

```prism-code
from dagster import schedule  
  
@schedule(cron_schedule="0 0 * * *", job=questdb_cleanup_job, execution_timezone="UTC")  
def daily_questdb_cleanup_schedule():  
    return {}
```

## Next Steps[​](#next-steps "Direct link to Next Steps")

For further details and resources, refer to the following links:

* **Dagster Documentation**: <https://docs.dagster.io/>
* **Full Example Repository**: <https://github.com/questdb/data-orchestration-and-scheduling-samples>