---
title: Docker image on branch creation
tags:
  - studies
  - common_core
  - programação
use: DevOps, GitHub Actions, Docker, Dockerfile, GitHub, GitHub Actions
languages: Yamel, Dockerfile, Shell
dependences: GitHub, Docker, GitHub Actions
---

# Initializing a Docker image on brach creation

You can use the following steps to achieve this:

1. Create a new Codespace configuration file in your repository. You can name it `.devcontainer.json` and place it in the root of your repository.

2. In the `.devcontainer.json` file, specify the Docker image you want to use as the environment. To install packages from given URLs in the `.devcontainer.json` file, you can use the `postCreateCommand` property to run a command after the Codespace is created. 

    Here's an example of how you can install two packages from given URLs:

    ```json
    {
    "name": "My Codespace",
    "dockerFile": "Dockerfile",
    "extensions": [
        "ms-vscode-remote.remote-containers"
    ],
    "postCreateCommand": "curl -L https://github.com/42School/norminette/archive/master.tar.gz | tar xz -C /usr/local --strip-components=1 && curl -L https://github.com/xicodomingues/francinette/archive/master.tar.gz | tar xz -C /usr/local --strip-components=1"
    }
    ```

   This configuration specifies that the Codespace should use the Dockerfile in the root of the repository to build the environment, and that the Codespace should have the "Remote - Containers" extension installed.

3. In your GitHub Actions workflow file, you can add a step to create a Codespace when the `42` branch is created. You can use the following configuration:

   ```yaml
   name: Create Codespace on 42 branch creation

   on:
     create:
       branches:
         - '42'

   jobs:
     create-codespace:
       runs-on: ubuntu-latest
       steps:
         - name: Create Codespace
           uses: microsoft/create-codespace-action@v1
           with:
             token: ${{ secrets.GITHUB_TOKEN }}
             config: .devcontainer.json
   ```

   This configuration specifies that a Codespace should be created when the `42` branch is created, using the `.devcontainer.json` configuration file and the `microsoft/create-codespace-action` action.

When the `42` branch is created, the GitHub Actions workflow will trigger and create a Codespace using the Docker image specified in the `.devcontainer.json` file.

## Using only the docker file

1. Create a new directory and place the Dockerfile in it.

    ```docker
    # Dockerfile
    FROM ubuntu:latest

    RUN apt-get update && apt-get install -y \
        build-essential \
        curl \
        git \
        libssl-dev \
        pkg-config \
        && rm -rf /var/lib/apt/lists/*

    # install norminette (https://github.com/42School/norminette)
    RUN curl -L  | tar xz -C /usr/local --strip-components=1

    # install francinette (https://github.com/xicodomingues/francinette)
    RUN curl -L  | tar xz -C /usr/local --strip-components=1
    ```

2. Open a terminal and navigate to the directory where the Dockerfile is located.
3. Build the Docker image using the following command: 

   ```bash
   docker build -t my-app .
   ```

   This will create a Docker image with the tag "my-app".

4. Run the Docker container using the following command:

   ```bash
   docker run -it my-app
   ```

   This will start a new container from the "my-app" image and drop you into a shell inside the container.


# FAQ

## What is a YAML file?

YAML is a human-readable data serialization format that is often used for configuration files. It is similar to JSON, but is designed to be more readable and easier to write.

## What is a JSON file?

JSON is a lightweight data interchange format that is often used for web APIs and configuration files. It is designed to be easy for humans to read and write, and easy for machines to parse and generate.

## What is a Dockerfile?

A Dockerfile is a text file that contains instructions for building a Docker image. It specifies the base image to use, any additional packages or dependencies to install, and any commands to run when the container is started.

## What is a Codespace?

A Codespace is a cloud-hosted development environment that is provided by GitHub. It allows developers to work on their code from anywhere, using a web-based editor or their own local editor.

## What is the `.devcontainer.json` file?

The `.devcontainer.json` file is a configuration file that is used to specify the environment for a Codespace. It can be used to specify the Docker image to use, any extensions to install, and any post-create commands to run.

## What is the `microsoft/create-codespace-action` action?

The `microsoft/create-codespace-action` action is a GitHub Actions action that can be used to create a Codespace. It takes a configuration file as input, and uses that file to create a Codespace with the specified environment.

## What is token: ${{ secrets.GITHUB_TOKEN }}?

`token: ${{ secrets.GITHUB_TOKEN }}` is a YAML key-value pair that specifies a GitHub personal access token. 

`${{ secrets.GITHUB_TOKEN }}` is a GitHub Actions secret that is automatically created for each repository. It is a token that can be used to authenticate with the GitHub API and perform actions on behalf of the repository. 

In the context of the YAML file you provided, the `token` key is used to specify the GitHub personal access token that will be used to authenticate with the GitHub API when running the GitHub Actions workflow. 

By using `${{ secrets.GITHUB_TOKEN }}`, the workflow will automatically use the token associated with the repository, without the need to manually specify the token.

## What are the `steps -uses:` possibles?

The `steps -uses:` possibles are the GitHub Actions actions that can be used in a GitHub Actions workflow. Here some examples:

- `actions/create-codespace@v1`, which is used to create a Codespace.
- `actions/codespace/`
- `actions/cehcout@v2`, which is used to check out the repository.
- `actions/setup-node@v2`, which is used to set up a Node.js environment.
- `actions/setup-python@v2`, which is used to set up a Python environment.
- `actions/create-release@v1`, which is used to create a GitHub release.

Find more actions in the [GitHub Marketplace](https://github.com/marketplace?type=actions) or even better in [Awesome Actions](https://github.com/sdras/awesome-actions).

# TODO (future)

- Add to routine a pipeline to verify the code using the `~/francinette/tester.sh` outputs.