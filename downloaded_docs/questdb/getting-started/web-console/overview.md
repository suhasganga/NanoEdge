On this page

Web Console is a client that allows you to interact with QuestDB. It
provides UI tools to query and explore the data, visualize the results in a table or plot.

![Screenshot of the Web Console](/docs/images/docs/console/overview.webp)

### Accessing the Web Console[​](#accessing-the-web-console "Direct link to Accessing the Web Console")

Web Console will be available at `http://[server-address]:9000`. When
running locally, this will be `http://localhost:9000`.

### Layout[​](#layout "Direct link to Layout")

![Preview of the different sections in the Web Console](/docs/images/docs/console/layout.webp)

The Web Console is organized into the following main sections that work together to provide a complete workflow:

### Code Editor[​](#code-editor "Direct link to Code Editor")

The **Code Editor** is where you write and execute SQL queries with features like syntax highlighting, auto-completion, and error tracing. It supports executing queries by selection, multiple query execution, and query planning.

[Learn more about Code Editor →](/docs/getting-started/web-console/code-editor/)

### AI Assistant[​](#ai-assistant "Direct link to AI Assistant")

The **AI Assistant** provides intelligent query assistance directly in the Web Console using AI-powered explanations and suggestions. It helps you write, understand, and fix SQL queries while maintaining complete control over your data and API keys through a Bring Your Own Key (BYOK) model.

[Learn more about AI Assistant →](/docs/getting-started/web-console/questdb-ai/)

### Metrics View[​](#metrics-view "Direct link to Metrics View")

The **Metrics View** provides real-time monitoring and telemetry capabilities for your QuestDB instance. It displays interactive charts and widgets to track database performance, WAL operations, and table-specific metrics.

[Learn more about Metrics View →](/docs/getting-started/web-console/metrics-view/)

### Schema Explorer[​](#schema-explorer "Direct link to Schema Explorer")

The **Schema Explorer** is the navigation hub for exploring tables and materialized views. It provides detailed information about each database object including columns with data types, storage configuration (partitioning and WAL status), and for materialized views, their base tables.

[Learn more about Schema Explorer →](/docs/getting-started/web-console/schema-explorer/)

### Result Grid[​](#result-grid "Direct link to Result Grid")

The **Result Grid** displays your query results in an interactive table format with features for data navigation, export, and visualization.

[Learn more about Result Grid →](/docs/getting-started/web-console/result-grid/)

### Query Log[​](#query-log "Direct link to Query Log")

The **Query Log** monitors query execution status and performance metrics, providing real-time feedback and maintaining a history of recent operations. It shows execution times, row counts, and detailed error information to help optimize your queries.

[Learn more about Query Log →](/docs/getting-started/web-console/query-log/)

### Import CSV[​](#import-csv "Direct link to Import CSV")

The **Import CSV** interface allows you to upload and import CSV files into QuestDB with automatic schema detection, flexible configuration options, and detailed progress tracking. You can create new tables or append to existing ones with full control over the import process.

[Learn more about Import CSV →](/docs/getting-started/web-console/import-csv/)

### Right Sidebar[​](#right-sidebar "Direct link to Right Sidebar")

The **Right Sidebar** provides quick access to essential tools and information:

* **Help**: Access quick links and contact options through a convenient help menu
* **QuestDB News**: Stay up-to-date with the latest QuestDB announcements and updates
* **Create Table**: Build new tables visually using an intuitive interface. Define table structure, configure partitioning, enable WAL, and add columns with their data types—all without writing SQL code. [Learn more about Create Table →](/docs/getting-started/web-console/create-table/)

### Instance Naming[​](#instance-naming "Direct link to Instance Naming")

Web Console allows you to set the instance name, type, and color. This functionality is particularly useful for production users who manage multiple deployments and frequently navigate between them. This feature makes it easier to keep track of instance information and label instances with meaningful names for their users.  
The instance name, instance type, and description are displayed when hovering over the icon in the instance information badge.

Instance information can be modified through the dialog that opens when clicking the edit icon:

![Instance information edit popper in Web Console](/docs/images/docs/console/instance-naming.webp)

info

If `http.settings.readonly` configuration is set to true, instance information is not editable.

info

When using QuestDB Enterprise with Role-Based Access Control (RBAC), only the users with `SETTINGS` or `DATABASE ADMIN` permission can edit the instance information. See [Database Permissions](/docs/security/rbac/#database-permissions) for more details.