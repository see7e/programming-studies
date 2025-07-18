---
title: Logging in Django - An Overview
tags:
  - studies
  - programming
  - logging
  - django
use: Documentation, Error Handling
languages: Python
dependences: Django
---

<details> <summary>Table of Contents 🔖</summary>

- [Django Logging Overview](#django-logging-overview)
  - [Loggers](#loggers)
  - [Handlers](#handlers)
  - [Filters](#filters)
  - [Formatters](#formatters)

</details>

---

# Django Logging Overview

Django uses and extends Python’s built-in [`logging`](https://docs.python.org/3/library/logging.html#module-logging) module to perform system logging. This module is discussed in detail in Python’s own documentation; this section provides a quick overview.

The log messages are stored in a queue before being processed by the logger. This allows for asynchronous logging, where the log messages can be processed in the background without blocking the main application thread. The queue is implemented using the `queue.Queue` class from the Python standard library.

The Python module defines levels with increasing numeric values, from 0 to 50, but the effective elements can be listed as follows:
- `DEBUG`: Low level system information for debugging purposes, commonly has data about the system state.
- `INFO`: General system information, such as startup messages or successful operations, also filters HTTP requests.
- `WARNING`: Information describing a minor problem that has occurred which does not prevent the system from functioning.
- `ERROR`: Information describing a major problem that has occurred, which may prevent some functionality.
- `CRITICAL`: Information describing a critical problem that has occurred, which may prevent the system from functioning at all.

> [!NOTE]
> A log record can also contain useful metadata that describes the event that is being logged. This can include details such as a stack trace or an error code.

> [!WARNING]
> ## Concurrency
> The logging module is thread-safe, meaning that it can be used in multi-threaded applications without the need for additional synchronization. However, if you are using the logging module in a multi-threaded application, it is important to ensure that the log messages are processed in the correct order. This can be done by using a queue to store the log messages before they are processed by the logger.
> ## Security Considerations
> When using the logging module, it is important to ensure that sensitive information is not logged. [Here's](dj-logging_dive.md) another article that talks about these considerations.

The Logger module is divided into four components:
- **Logger**: The main interface for logging messages, which can be configured to log messages at different levels (described above).
- **Handler**: The component that sends the log messages to their final destination, such as a file or the console.
- **Filter**: A component that can be used to filter log messages based on certain criteria, such as the log level or the message content.
- **Formatter**: A component that formats the log messages before they are sent to their final destination, allowing customization of the output format.

## Loggers
Are the entry point entities, the logger is the main interface for capturing the messages. It is created using the `logging.getLogger(name)` function, where `name` is a string that identifies the logger. The name can be any string, but it is common to use the name of the module or application that is being logged.

Can be also configured to automatically retrieve the information at the `settings.py` file, using the constant `LOGGING`:
```python
LOG_FILE: str
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "simple": {
            "format": "[{levelname}] {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "file": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": LOG_FILE,
            "formatter": "verbose",
        },
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "file", "mail_admins"],
            "level": "DEBUG",
            "propagate": True,
        },
        "myapp": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "myapp.submodule": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}
```
> For a more in-depth explanation of the `LOGGING` dictionary, look [here](dj-logging_dive.md).

When a message is given to the logger, the log level of the message is compared to the log level of the logger. If the log level of the message meets or exceeds the log level of the logger itself, the message will undergo further processing. If it doesn’t, the message will be ignored.

## Handlers
They receive the log messages from the logger once the log level is met or exceeded, and send them to their final destination. Handlers can be configured to send log messages to different destinations, such as a file, the console, an email or a network socket.
Handlers can be configured in the `LOGGING` dictionary, as shown in the example above. Each handler has:
- a `level` attribute that determines the minimum log level for messages to be processed by that handler;
- the `class` attribute specifies the type of handler to use, such as `logging.StreamHandler` for console output or `logging.FileHandler` for file output;
- the `formatter` attribute specifies the formatter to use for formatting the log messages before they are sent to their final destination.

Handlers can also be added dynamically to the logger using the `addHandler()` method, allowing for more flexibility in configuring the logging system.

Having multiple handlers allows for different log messages to be sent to different destinations, even if they are generated by the same logger. For example, you can have one handler that sends all log messages to a file, and another handler that sends only error messages to an email address.

## Filters
Filters are optional components that can be used to create a triage system for log messages. They can be used to filter log messages based on certain criteria, such as the log level or the message content. Filters can be added to loggers and handlers, allowing for fine-grained control over which log messages are processed and sent to their final destination. A simple example of a filter that only allows log messages with a specific substring in the message content:
```python
class SubstringFilter(logging.Filter):
    def __init__(self, substring):
        super().__init__()
        self.substring = substring

    def filter(self, record):
        return self.substring in record.getMessage()
```
This filter can be added to a logger or handler using the `addFilter()` method, allowing only log messages that contain the specified substring to be processed.

Filters can also be used to modify the logging record prior to being emitted. For example, you could write a filter that downgrades ERROR log records to WARNING records if a particular set of criteria are met.

## Formatters
Formatters are used to format the log messages before they are sent to their final destination. They can be configured in the `LOGGING` dictionary, as shown in the example above. Each formatter has:
- a `format` attribute that specifies the format of the log message, using a string with placeholders for the log record attributes;
- a `datefmt` attribute that specifies the format of the date and time in the log message, using a string with placeholders for the date and time attributes;
> the rest of the attributes you can see at the [Python documentation](https://docs.python.org/3/library/logging.html#logrecord-attributes)

Note that the formatters must be specified as either `simple` or `verbose`.
