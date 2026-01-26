On this page

## Observability & diagnostics[​](#observability--diagnostics "Direct link to Observability & diagnostics")

QuestDB provides real-time metrics, a health check endpoint, and logging to monitor performance and simplify troubleshooting.

* **Metrics:**
  QuestDB exposes detailed [metrics in Prometheus format](/docs/operations/logging-metrics/#metrics), including query
  statistics, memory usage, and I/O details.
* **Health check:**
  A [minimal HTTP server](/docs/operations/logging-metrics/#minimal-http-server) monitors system health.
* **Metadata tables:**
  The engine provides [metadata tables](/docs/query/functions/meta/) to query
  table status, partition status, query execution, and latency.
* **Extensive logging:**
  [Logging](/docs/operations/logging-metrics/) covers SQL parsing, execution, background processing, and runtime exceptions. The framework minimizes performance impact.
* **Real-time metric dashboards:**
  The web console lets you create dashboards that display per-table metrics.

![Metric dashboard at the QuestDB Console](/docs/images/guides/questdb-internals/telemetry.webp)

Metric dashboard at the QuestDB Console

## Next up[​](#next-up "Direct link to Next up")

Back to [Architecture Overview](/docs/architecture/questdb-architecture/) or continue to [Configuration](/docs/configuration/overview/).