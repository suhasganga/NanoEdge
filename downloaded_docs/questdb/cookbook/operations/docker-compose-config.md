On this page

You can override any QuestDB configuration parameter using environment variables in Docker Compose. This is useful for setting custom ports, authentication credentials, memory limits, and other operational settings without modifying configuration files.

## Environment variable format[​](#environment-variable-format "Direct link to Environment variable format")

To override configuration parameters via environment variables:

1. **Prefix with `QDB_`**: Add `QDB_` before the parameter name
2. **Capitalize**: Convert to uppercase
3. **Replace dots with underscores**: Change `.` to `_`

For example:

* `pg.user` becomes `QDB_PG_USER`
* `pg.password` becomes `QDB_PG_PASSWORD`
* `cairo.sql.copy.buffer.size` becomes `QDB_CAIRO_SQL_COPY_BUFFER_SIZE`

tip

Keep sensitive configuration like passwords in a `.env` file and reference them in `docker-compose.yml`:

```prism-code
environment:  
  - QDB_PG_PASSWORD=${QUESTDB_PASSWORD}
```

Then create a `.env` file:

```prism-code
QUESTDB_PASSWORD=your_secure_password
```

## Example: Custom PostgreSQL credentials[​](#example-custom-postgresql-credentials "Direct link to Example: Custom PostgreSQL credentials")

This Docker Compose file overrides the default PostgreSQL wire protocol credentials:

docker-compose.yml - Override pg.user and pg.password

```prism-code
version: "3.9"  
  
services:  
  questdb:  
    image: questdb/questdb  
    container_name: custom_questdb  
    restart: always  
    ports:  
      - "8812:8812"  
      - "9000:9000"  
      - "9009:9009"  
      - "9003:9003"  
    extra_hosts:  
      - "host.docker.internal:host-gateway"  
    environment:  
      - QDB_PG_USER=borat  
      - QDB_PG_PASSWORD=clever_password  
    volumes:  
      - ./questdb/questdb_root:/var/lib/questdb/
```

This configuration:

* Sets PostgreSQL wire protocol username to `borat`
* Sets password to `clever_password`
* Persists data to `./questdb/questdb_root` on the host machine
* Exposes all QuestDB ports (web console, HTTP, ILP, PostgreSQL wire)

Volume Permissions

If you encounter permission errors with mounted volumes, ensure the QuestDB container user has write access to the host directory. You may need to set ownership with `chown -R 1000:1000 ./questdb_root` or run the container with a specific user ID.

## Custom data directory permissions[​](#custom-data-directory-permissions "Direct link to Custom data directory permissions")

Run with specific user/group for volume permissions

```prism-code
services:  
  questdb:  
    image: questdb/questdb  
    user: "1000:1000"  
    environment:  
      - QDB_CAIRO_ROOT=/var/lib/questdb  
    volumes:  
      - ./questdb_data:/var/lib/questdb
```

## Complete configuration reference[​](#complete-configuration-reference "Direct link to Complete configuration reference")

For a full list of available configuration parameters, see:

* [Server Configuration Reference](/docs/configuration/overview/) - All configurable parameters with descriptions
* [Docker Deployment Guide](/docs/deployment/docker/) - Docker-specific setup instructions

Related Documentation

* [Server Configuration](/docs/configuration/overview/)
* [Docker Deployment Guide](/docs/deployment/docker/)
* [PostgreSQL Wire Protocol](/docs/query/pgwire/overview/)