* The API system is asynchronous. Some delay in the response is normal and expected.
* Each method has a data source indicating where the data is coming from, and thus how up-to-date it is.

| Data Source | Latency | Description |
| --- | --- | --- |
| Matching Engine | lowest | The Matching Engine produces the response directly |
| Memory | low | Data is fetched from API server's local or external memory cache |
| Database | moderate | Data is retrieved from the database |

* Some methods have more than one data source (e.g., Memory => Database).

  This means that the API will look for the latest data in that order:
  first in the cache, then in the database.