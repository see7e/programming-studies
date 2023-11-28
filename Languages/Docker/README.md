---
title: Docker - Basics
tags: studies, programação
use: Documentation
languages: Docker, yaml
dependences: NULL
---

<details> <summary>Table of Contents 🔖</summary>

- [Docker](#docker)
  - [Step 1: Project Structure](#step-1-project-structure)
  - [Step 2: Initialise Docker](#step-2-initialise-docker)
- [`Dockerfile`](#dockerfile)
  - [1. **Base Image Selection:**](#1-base-image-selection)
  - [2. **Environment Configuration:**](#2-environment-configuration)
  - [3. **Working Directory:**](#3-working-directory)
  - [4. **User Creation:**](#4-user-creation)
  - [5. **Dependency Installation:**](#5-dependency-installation)
  - [6. **User Switching:**](#6-user-switching)
  - [7. **Source Code Copying:**](#7-source-code-copying)
  - [8. **Port Exposure:**](#8-port-exposure)
  - [9. **Application Run Command:**](#9-application-run-command)
  - [Future Expansion:](#future-expansion)
- [`compose.yaml`](#composeyaml)
  - [1. **Service Definition:**](#1-service-definition)
  - [2. **Service Build Context:**](#2-service-build-context)
  - [3. **Port Mapping:**](#3-port-mapping)
  - [4. **PostgreSQL Database (Commented Section):**](#4-postgresql-database-commented-section)
  - [5. **Database Service Configuration (Inside Commented Section):**](#5-database-service-configuration-inside-commented-section)
  - [6. **Volumes and Secrets (Inside Commented Section):**](#6-volumes-and-secrets-inside-commented-section)
  - [Future Expansion:](#future-expansion-1)

</details>

---

# Docker

Docker is a powerful tool for containerization, which allows you to package your application and its dependencies into a single container, making it easy to deploy and run consistently across different environments. Here, I'll guide you through creating a basic Docker configuration for a simple Django server.

> Remember to adapt these suggestions based on the specific requirements and architecture of your application.

## Step 1: Project Structure

Assuming you have a Django project, let's say named "", your project structure might look like this:

> [!IMPORTANT]
> To fultill the purpose of this documentation, the project structure will be created following the code below (use `source .venv/bin/activate` for Linux and `source .venv/Scripts/activate` for Windows):
>
> ```bash
> python -m venv .venv
> # activate  # the python virtual environment
> pip install django
> python -m django startproject setup .
> python manage.py startapp myapp
> python manage.py migrate
> python manage.py runserver # only to test
> ```

```
..
|-- manage.py
|-- setup/
    |-- ...
|-- myapp/
    |-- ...
|-- Dockerfile
|-- requirements.txt
|-- compose.yaml
```

> The application folder and configuration files will be supressed in order to maintain the focus of the topic, wich is Docker.

## Step 2: Initialise Docker

```bash
$ docker init

Welcome to the Docker Init CLI!

This utility will walk you through creating the following files with sensible defaults for your project:
  - .dockerignore
  - Dockerfile
  - compose.yaml

Let's get started!

? What application platform does your project use? Python
? What version of Python do you want to use? (3.10.7) 
? What version of Python do you want to use? 3.10.7

? What port do you want your app to listen on? (8000)
? What port do you want your app to listen on? 8000

? What is the command to run your app? (gunicorn '.venv.Lib.site-packages.asgiref.wsgi' --bind=0.0.0.0:8000) 
? What is the command to run your app? gunicorn 'setup.wsgi:application' --bind=0.0.0.0:8000

CREATED: .dockerignore
CREATED: Dockerfile
CREATED: compose.yaml

✔ Your Docker files are ready!

Take a moment to review them and tailor them to your application.

WARNING: Be sure your requirements.txt contains an entry for the gunicorn 
package, which is required to run your application.

When you're ready, start your application by running: docker compose up --build

Your application will be available at http://localhost:8000
```


# `Dockerfile`

This Dockerfile is for building a Python application container using Docker. Let's break down the different sections to understand what each part does.

## 1. **Base Image Selection:**

```dockerfile
ARG PYTHON_VERSION=3.10.7
FROM python:${PYTHON_VERSION}-slim as base
```

- This sets the Python version to be used in the image. It starts with a slim base image of Python, which is a minimalistic version suitable for production.

## 2. **Environment Configuration:**

```dockerfile
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
```

- These environment variables configure Python to not write bytecode files and to not buffer the output, which is good for Docker containers.

## 3. **Working Directory:**

```dockerfile
WORKDIR /app
```

- This sets the working directory inside the container to `/app`.

## 4. **User Creation:**

```dockerfile
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser
```

- It creates a non-privileged user (`appuser`) with a specified UID. This is a security best practice to avoid running the application as the root user.

## 5. **Dependency Installation:**

```dockerfile
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt
```

- This installs the Python dependencies listed in the `requirements.txt` file. It takes advantage of Docker's caching mechanism to speed up builds.

## 6. **User Switching:**

```dockerfile
USER appuser
```

- This switches to the non-privileged user (`appuser`) for running the application.

## 7. **Source Code Copying:**

```dockerfile
COPY . .
```

- This copies the source code from the local directory into the container's `/app` directory.

## 8. **Port Exposure:**

```dockerfile
EXPOSE 8000
```

- This exposes port 8000, which is the port that the application inside the container is expected to listen on.

## 9. **Application Run Command:**

```dockerfile
CMD gunicorn 'setup.wsgi:application' --bind=0.0.0.0:8000
```

- This is the command that will be executed when the container starts. It runs the Gunicorn server to serve the application, binding it to all available interfaces on port 8000.

## Future Expansion:

To expand on this in the future, you might consider the following:

1. **Optimization:** Depending on your application, you might need to optimize the Dockerfile for better performance or security.

2. **Multi-stage builds:** If your application has multiple stages (e.g., building assets, compiling code), consider using multi-stage builds to reduce the final image size.

3. **Logging and Monitoring:** Incorporate logging mechanisms and monitoring tools into your container to better manage and debug your application in production.

4. **Security Scanning:** Integrate security scanning tools to ensure that your container images are free from vulnerabilities.

5. **CI/CD Pipeline:** Set up a continuous integration and deployment pipeline to automate the build and deployment process.

6. **Environment Variables:** Use environment variables for configuration, allowing flexibility without modifying the Dockerfile.


# `compose.yaml`

## 1. **Service Definition:**

```yaml
services:
  server:
    build:
      context: .
    ports:
      - 8000:8000
```

- This defines a service named "server." It uses the Dockerfile in the current directory for building the service. The service exposes port 8000, mapping it to the same port on the host.

## 2. **Service Build Context:**

```yaml
    build:
      context: .
```

- This specifies the build context for the service. In this case, it's set to the current directory, meaning it will use the Dockerfile in the current directory for building the Docker image.

## 3. **Port Mapping:**

```yaml
    ports:
      - 8000:8000
```

- This maps port 8000 on the host to port 8000 on the service. This allows external access to the application running inside the Docker container.

## 4. **PostgreSQL Database (Commented Section):**

```yaml
# The commented out section below is an example of how to define a PostgreSQL
# database that your application can use.
# ...
```

- This section provides an example of how to define a PostgreSQL database service for your application. It includes details such as image, restart policy, user, secrets, volumes, environment variables, exposure of port 5432, and a health check.

## 5. **Database Service Configuration (Inside Commented Section):**

```yaml
#   db:
#     image: postgres
#     restart: always
#     user: postgres
#     secrets:
#       - db-password
#     volumes:
#       - db-data:/var/lib/postgresql/data
#     environment:
#       - POSTGRES_DB=example
#       - POSTGRES_PASSWORD_FILE=/run/secrets/db-password
#     expose:
#       - 5432
#     healthcheck:
#       test: [ "CMD", "pg_isready" ]
#       interval: 10s
#       timeout: 5s
#       retries: 5
```

- This section defines a PostgreSQL database service named "db." It includes details like the Docker image to use, restart policy, user, secrets for passwords, volumes for data persistence, environment variables, port exposure, and a health check to ensure the database is ready.

## 6. **Volumes and Secrets (Inside Commented Section):**

```yaml
# volumes:
#   db-data:
# secrets:
#   db-password:
#     file: db/password.txt
```

- These sections define volumes (`db-data`) and secrets (`db-password`). Volumes are used to persist database data, and secrets are used to securely store sensitive information like the database password.

## Future Expansion:

To expand on this in the future:

1. **Environment Variables:** Consider using environment variables for configuration settings in your services.

2. **Networks:** Define custom networks for better isolation and communication between services.

3. **Scaling:** If needed, configure service scaling to run multiple instances of the same service.

4. **Logging and Monitoring:** Integrate logging and monitoring solutions for better visibility into the health and performance of your services.

5. **Service Dependencies:** If your application grows, you might need to define dependencies between services more explicitly.

6. **Security:** Implement security best practices, especially if dealing with sensitive data.

7. **Versioning:** Keep an eye on Docker Compose updates and consider versioning your Docker Compose file accordingly.


> [!TIP]
> **Scaling in a Distributed System**
> 
> For a distributed system, consider using container orchestration tools like Kubernetes. You would create Kubernetes deployment files, services, and possibly use tools like Helm for managing configurations.
> 
> This example is a basic setup. In a real professional project, you would need to address security concerns, use production-ready web servers (e.g., Gunicorn), handle static files and database connections properly, and configure your Django settings for production.
> 
> Remember to follow best practices, such as not using the development server in a production environment and securing sensitive information in your Docker images and environment variables.