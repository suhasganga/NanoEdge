On this page

When troubleshooting or auditing your QuestDB configuration, it's useful to see which parameters have been changed from their defaults.

## Problem[​](#problem "Direct link to Problem")

You need to identify which configuration parameters have been explicitly set via the configuration file or environment variables, filtering out all parameters that are still using their default values.

## Solution[​](#solution "Direct link to Solution")

Query the `SHOW PARAMETERS` command and filter by `value_source` to exclude defaults:

Find which params where modified from default values[Demo this query](https://demo.questdb.io/?query=--%20Show%20all%20parameters%20modified%20from%20their%20defaults%2C%20via%20conf%20file%20or%20env%20variable%0A(SHOW%20PARAMETERS)%20WHERE%20value_source%20%3C%3E%20'default'%3B&executeQuery=true)

```prism-code
-- Show all parameters modified from their defaults, via conf file or env variable  
(SHOW PARAMETERS) WHERE value_source <> 'default';
```

This query returns only the parameters that have been explicitly configured, showing their current values and the source of the configuration (e.g., `conf` file or `env` variable).

Related Documentation

* [SHOW PARAMETERS reference](/docs/query/sql/show/#show-parameters)
* [Configuration reference](/docs/configuration/overview/)