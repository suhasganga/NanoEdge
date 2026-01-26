On this page

QuestDB may be started, stopped and passed configuration options from the
command line. On Windows, the QuestDB server can also start an
[interactive session](#interactive-session-windows).

## Options[​](#options "Direct link to Options")

The following sections describe the options that may be passed to QuestDB when
starting the server from the command line.

* Linux
* macOS (Homebrew)
* Windows

```prism-code
./questdb.sh [start|stop|status] [-d dir] [-f] [-n] [-t tag]
```

```prism-code
questdb [start|stop|status] [-d dir] [-f] [-n] [-t tag]
```

```prism-code
questdb.exe [start|stop|status|install|remove] \  
  [-d dir] [-f] [-j JAVA_HOME] [-t tag]
```

### Start[​](#start "Direct link to Start")

`start` - starts QuestDB as a service.

| Option | Description |
| --- | --- |
| `-d` | Expects a `dir` directory value which is a folder that will be used as QuestDB's root directory. For more information and the default values, see the [default root](#default-root-directory-1) section below. |
| `-t` | Expects a `tag` string value which will be as a tag for the service. This option allows users to run several QuestDB services and manage them separately. If this option is omitted, the default tag will be `questdb`. |
| `-f` | Force re-deploying the [Web Console](/docs/getting-started/web-console/overview/). Without this option, the [Web Console](/docs/getting-started/web-console/overview/) is cached and deployed only when missing. |
| `-n` | Do not respond to the HUP signal. This keeps QuestDB alive after you close the terminal window where you started it. |
| `-j` | **Windows only!** This option allows to specify a path to `JAVA_HOME`. |

note

* When running multiple QuestDB services, a tag must be used to disambiguate
  between services for `start` and `stop` commands. There will be conflicting
  ports and root directories if only the tag flag is specified when starting
  multiple services. Each new service should have its own config file or should
  be started with separate port and root directory options.
* When running QuestDB as Windows service you can check status in both:

  + Windows Event Viewer - look for events with "QuestDB" source in Windows Logs
    | Application .
  + service log file - `$dataDir\log\service-%Y-%m-%dT%H-%M-%S.txt` (default is
    `C:\Windows\System32\qdbroot\log\service-%Y-%m-%dT%H-%M-%S.txt` )

* Linux
* macOS (Homebrew)
* Windows

```prism-code
./questdb.sh start [-d dir] [-f] [-n] [-t tag]
```

```prism-code
questdb start [-d dir] [-f] [-n] [-t tag]
```

```prism-code
questdb.exe start [-d dir] [-f] [-j JAVA_HOME] [-t tag]
```

#### Default root directory[​](#default-root-directory "Direct link to Default root directory")

By default, QuestDB's [root directory](/docs/concepts/deep-dive/root-directory-structure/)
will be the following:

* Linux
* macOS (Homebrew)
* Windows

```prism-code
$HOME/.questdb
```

Path on Macs with Apple Silicon (M1 or M2) chip:

```prism-code
/opt/homebrew/var/questdb
```

Path on Macs with Intel chip:

```prism-code
/usr/local/var/questdb
```

```prism-code
C:\Windows\System32\qdbroot
```

### Stop[​](#stop "Direct link to Stop")

`stop` - stops a service.

| Option | Description |
| --- | --- |
| `-t` | Expects a `tag` string value which to stop a service by tag. If this is omitted, the default tag will be `questdb` |

* Linux
* macOS (Homebrew)
* Windows

```prism-code
./questdb.sh stop
```

```prism-code
questdb stop
```

```prism-code
questdb.exe stop
```

### Status[​](#status "Direct link to Status")

`status` - shows the status for a service.

| Option | Description |
| --- | --- |
| `-t` | Expects a `tag` string value which to stop a service by tag. If this is omitted, the default will be `questdb` |

* Linux
* macOS (Homebrew)
* Windows

```prism-code
./questdb.sh status
```

```prism-code
questdb status
```

```prism-code
questdb.exe status
```

### Install (Windows)[​](#install-windows "Direct link to Install (Windows)")

`install` - installs the Windows QuestDB service. The service will start
automatically at startup.

```prism-code
questdb.exe install
```

### Remove (Windows)[​](#remove-windows "Direct link to Remove (Windows)")

`remove` - removes the Windows QuestDB service. It will no longer start at
startup.

```prism-code
questdb.exe remove
```

## Interactive session (Windows)[​](#interactive-session-windows "Direct link to Interactive session (Windows)")

You can start QuestDB interactively by running `questdb.exe`. This will launch
QuestDB interactively in the active `Shell` window. QuestDB will be stopped when
the Shell is closed.

### Default root directory[​](#default-root-directory-1 "Direct link to Default root directory")

When started interactively, QuestDB's root directory defaults to the `current`
directory.

### Stop[​](#stop-1 "Direct link to Stop")

To stop, press `Ctrl`+`C` in the terminal or close it
directly.