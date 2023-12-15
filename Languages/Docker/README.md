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
- [Terminal Log](#terminal-log)

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

> The application folder and configuration files will be supressed in order to maintain the focus of the topic, which is Docker.

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
? What version of Python do you want to use? (3.10.7) 3.10.7
? What port do you want your app to listen on? (8000) 8000
? What is the command to run your app? (gunicorn '.venv.Lib.site-packages.asgiref.wsgi' --bind=0.0.0.0:8000) gunicorn 'setup.wsgi:application' --bind=0.0.0.0:8000

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

After that you can build the container (image) only using the following command:

```bash
docker compose up
```


> [!IMPORTANT]
> Remember to stop the Docker image after using it, otherwise it will keep running in the background.
> ```bash
> docker compose down
> ```

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

> [!INFO]
> **Docker Caching**
> Is a mechanism that allows Docker to reuse intermediate build steps from previous builds. This can significantly speed up builds, especially when you have a lot of dependencies to install.
>
> **Mounting Process**
> Is a process where you link a directory from your host machine to a directory inside a container. This allows data to persist outside the container and be shared between the host and the container. The `--mount` option in Docker is often used to achieve this.
>In your provided code, you have two `RUN` instructions in a Dockerfile. The first one installs system dependencies using `apt-get`, and the second one installs Python dependencies using `pip`.
>
> Why mounting is important in this context:
> Persistent Storage: The --mount option ensures that the data inside the specified host directory (/root/cache/pip) is persistent. If you don't use mounting, any data stored during the pip install process will be lost when the container is removed.
>
> Caching: Mounting a directory for the pip cache can significantly improve build times. Subsequent builds can reuse the cache stored on the host machine, avoiding the need to download and install dependencies again.
> 
> Separation of Concerns: Mounting allows you to separate the data that should persist (like cache) from the rest of the container filesystem. This can make it easier to manage and back up important data.

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

---

# Terminal Log

```bash
$ docker compose up
[+] Building 16.3s (14/14) FINISHED                      docker:default
 => [server internal] load .dockerignore                           0.1s
 => => transferring context: 680B                                  0.0s
 => [server internal] load build definition from Dockerfile        0.1s
 => => transferring dockerfile: 1.59kB                             0.0s
 => [server] resolve image config for docker.io/docker/dockerfile  2.1s
 => [server auth] docker/dockerfile:pull token for registry-1.doc  0.0s
 => CACHED [server] docker-image://docker.io/docker/dockerfile:1@  0.0s
 => [server internal] load metadata for docker.io/library/python:  1.3s
 => [server auth] library/python:pull token for registry-1.docker  0.0s
 => [server base 1/5] FROM docker.io/library/python:3.10.7-slim@s  4.7s
 => => resolve docker.io/library/python:3.10.7-slim@sha256:f2ee14  0.0s
 => => sha256:f2ee145f3bc4e061f8dfe7e6ebd427a4101 1.86kB / 1.86kB  0.0s
 => => sha256:f8fbb2370c6314c806b2ddbec8d94375987 1.37kB / 1.37kB  0.0s
 => => sha256:28358ad706063a4fab219d8bcb048124e6d 7.50kB / 7.50kB  0.0s
 => => sha256:bd159e379b3b1bc0134341e4ffdeab5f9 31.42MB / 31.42MB  1.3s
 => => sha256:de08aeb7fd50562d57cef1a49d6197d619d 1.08MB / 1.08MB  0.2s
 => => sha256:30527e10f55af538c1464ce755f9e9fce 12.11MB / 12.11MB  1.0s
 => => sha256:693e7a5ba2a8a42880d04042159d67aa9ebb2d6 234B / 234B  0.4s
 => => sha256:c7b6f7685fa51adb5da18c9a4fd647bc9cb 3.34MB / 3.34MB  1.1s
 => => extracting sha256:bd159e379b3b1bc0134341e4ffdeab5f966ec422  2.0s
 => => extracting sha256:de08aeb7fd50562d57cef1a49d6197d619df0b4c  0.1s
 => => extracting sha256:30527e10f55af538c1464ce755f9e9fceae68bb6  0.7s
 => => extracting sha256:693e7a5ba2a8a42880d04042159d67aa9ebb2d67  0.0s
 => => extracting sha256:c7b6f7685fa51adb5da18c9a4fd647bc9cb24af5  0.4s
 => [server internal] load build context                           0.7s
 => => transferring context: 138.09kB                              0.6s
 => [server base 2/5] WORKDIR /app                                 0.5s
 => [server base 3/5] RUN adduser     --disabled-password     --g  0.4s
 => [server base 4/5] RUN --mount=type=cache,target=/root/.cache/  6.1s
 => [server base 5/5] COPY . .                                     0.0s
 => [server] exporting to image                                    0.7s
 => => exporting layers                                            0.7s
 => => writing image sha256:b15750b7fe7ab06c01419167cc2e161d16b41  0.0s
 => => naming to docker.io/library/code-server                     0.0s
[+] Running 2/2
 ✔ Network code_default     Created                                0.2s 
 ✔ Container code-server-1  Created                                0.2s 
Attaching to code-server-1
code-server-1  | [2023-11-29 11:09:42 +0000] [7] [INFO] Starting gunicorn 21.2.0
code-server-1  | [2023-11-29 11:09:42 +0000] [7] [INFO] Listening at: http://0.0.0.0:8000 (7)
code-server-1  | [2023-11-29 11:09:42 +0000] [7] [INFO] Using worker: sync
code-server-1  | [2023-11-29 11:09:42 +0000] [8] [INFO] Booting worker with pid: 8
code-server-1  | Not Found: /favicon.ico
Gracefully stopping... (press Ctrl+C again to force)
Aborting on container exit...
[+] Stopping 1/1
 ✔ Container code-server-1  Stopped                               10.4s 
canceled
PS $ docker compose down
[+] Running 2/2
 ✔ Container code-server-1  Removed                                0.0s 
 ✔ Network code_default     Removed                                0.2s 
```