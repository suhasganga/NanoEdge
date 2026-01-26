On this page

The Web Console provides an interactive interface for creating new tables through the "Create table" tab that can be opened from the right-hand side bar.

![Screenshot of the create table tab](/docs/images/docs/console/create-table-tab.webp)

The Create table tab allows you to define the table structure, partition settings, WAL configuration, and add columns using an intuitive UI.

![Screenshot of the create table panel](/docs/images/docs/console/create-table.webp)

## Actions[​](#actions "Direct link to Actions")

* **Remove column**: Removes the last focused column from the schema
* **Insert column above**: Inserts a new column above the last focused column
* **Insert column below**: Inserts a new column below the last focused column
* **Create**: Creates the table with the specified storage details and columns

## Table settings[​](#table-settings "Direct link to Table settings")

You can set the table name from the name input, select the partitioning type, and specify whether WAL is enabled using the respective dropdowns.

See [WAL](/docs/concepts/write-ahead-log/) and [Partitions](/docs/concepts/partitions/) concepts for more details.

## Column settings[​](#column-settings "Direct link to Column settings")

You can specify the name and [data type](/docs/query/datatypes/overview/) for a column.

* For columns with type `timestamp`, you can specify if the column will be the designated timestamp.
* For columns with type `geohash`, you can specify the [precision](/docs/query/datatypes/geohashes/#specifying-geohash-precision) of the column.