---
title: Deploying on Development
tags:
  - studies
  - programming
  - deploy
  - CI/CD
use: Documentation
languages: Docker, yaml
dependences: GitHub, GitHub Actions
---

<details> <summary>Table of Contents 🔖</summary>

- [Intro](#intro)
- [Containers!](#containers)
  - [Secrets you’ll need in **Environment ➜ development**](#secrets-youll-need-in-environment-development)
  - [`.env` file](#env-file)
  - [Docker/compose files](#dockercompose-files)
  - [Remote helper script (lives in your repo)](#remote-helper-script-lives-in-your-repo)
  - [GitHub Actions workflows](#githubactions-workflows)
    - [`dev.yml`](#devyml)
    - [`deploy_dev.yml`](#deploy_devyml)
      - [What this does](#what-this-does)
      - [Server prerequisites](#server-prerequisites)
      - [Why the workflow used `rsync`?](#why-the-workflow-usedrsync)
    - [Considerations on Nginx](#considerations-on-nginx)
      - [Option A – Put Nginx only on the *dev‑server compose*](#optiona--put-nginx-only-on-the-devserver-compose)
      - [Option B – Separate override file](#optionb--separate-override-file)

</details>

---
# Intro
Sometimes we want to test the application in a more effective way than running automated tests (see here for [Django's tests](../Languages/Python/Django/dj-tests.md)). Or we just want to present for the QA, Testing or Client a brief example of a safe and running environment.

As my previous experience, I've been working with GitHub Actions for creating and managing CI/CD pipelines, with various contexts (one already mentioned above).
In this article we'll see a brief endeavour regarding a deployment pipeline for a Development environment.

---
# Containers!
A safer approach is to create containers for all the elements used, this helps when checking the logs, or some other Docker-usage benefit.

We'll use a small script to safely redeploys **only** the *web* container whenever someone pushes to the `dev` branch (or triggers the workflow manually). The database stays up; the app image and container are rebuilt, pruned, and restarted.

## Secrets you’ll need in **Environment ➜ development**

| Secret name              | Purpose                               |
| ------------------------ | ------------------------------------- |
| `DEV_SSH_HOST`           | IP/hostname of the dev server         |
| `DEV_SSH_USER`           | SSH user that can run Docker          |
| `DEV_SSH_KEY`            | Private key (PEM) for that user       |
| `DEV_WORKDIR` (optional) | Path on server; default `/srv/webapp` |
*(These names follow the “DEV_” prefix rule from the [GitHub Conventions](github-conventions.md).)*

## `.env` file
This will serve as a placeholder for some of the variables that will be loaded from the GH Secrets.

```dotenv
# ─── Django ────────────────────────────────────────────────────────────────
DJANGO_SETTINGS_MODULE=setup.settings
DJANGO_SECRET_KEY=

# ─── PostgreSQL ────────────────────────────────────────────────────────────
DB_ENGINE=django.db.backends.postgresql        # rarely changes, still helpful
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=db                                     # “db” matches docker‑compose
DB_PORT=5432

# ─── Misc / 3rd‑party (add as needed) ──────────────────────────────────────
SMTP_HOST=
SMTP_USER=
SMTP_PASSWORD=
STRIPE_TEST_SECRET_KEY=
```

> [!TIP]
> Use empty values so `grep -v '=' .env.example` stays clean in diffs.

## Docker/compose files

```yaml
---

services:
  web:
    build: .
    env_file:
      - .env  # will be created in CI below
    ports:
      - "8000:8000"
    depends_on:
      db:
        condition: service_healthy
	
  db:
    image: postgres:latest
    env_file:
      - .env  # so Postgres picks up DB_* vars
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U $${DB_USER} -d $${DB_NAME}"]
      interval: 10s
      timeout: 5s
      retries: 5
  nginx:
    image: nginx:latest
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - web
volumes:
  pgdata:  # named volume lives under /var/lib/docker/volumes

```

This way no secrets appear in the image layers and the same compose file works locally.

## Remote helper script (lives in your repo)
`scripts/deploy_dev_remote.sh` — keep it small and explicit:

```bash
#!/usr/bin/env bash
# Rebuild & restart ONLY the web service.
set -euo pipefail

echo "▶ Cleaning up old 'web' container…"
docker compose stop web || true
docker compose rm -f web || true

echo "▶ Building new image…"
docker compose build web

echo "▶ Starting fresh 'web' container…"
docker compose up -d web

echo "▶ Pruning dangling images…"
docker image prune -f --filter "label=stage=development"

echo "✅ Deploy complete."
```

> [!TIP]
> *Make it executable: `chmod +x .github/scripts/deploy_dev_remote.sh`*

## GitHub Actions workflows
You'll have two GitHub‑Actions workflows:

|Workflow file|Purpose|Runs containers?|
|---|---|---|
|`.github/workflows/dev.yml`|CI / tests on the GitHub runner|Yes – `docker compose up` locally on the runner|
|`.github/workflows/deploy‑dev.yml`|Push to the _remote_ dev server via SSH + `docker compose`|Yes – but only **web** (plus DB already running)|

### `dev.yml`

```yml
name: CI (dev)

on: [push, pull_request]

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: development
    steps:
      - uses: actions/checkout@v4
      # add SSH key (doesn't need DB secrets)
      - name: Add SSH key
        uses: webfactory/ssh-agent@v0.9.0
        with:
          ssh-private-key: ${{ secrets.DEV_SSH_KEY }}
      # Create .env – only this step needs DB_* vars
      - name: Generate .env for compose
        env:
          DJANGO_SECRET_KEY: ${{ secrets.DEV_DJANGO_SECRET_KEY }}
          DB_ENGINE:         ${{ secrets.DEV_DB_ENGINE }}
          DB_NAME:           ${{ secrets.DEV_DB_NAME }}
          DB_USER:           ${{ secrets.DEV_DB_USER }}
          DB_PASSWORD:       ${{ secrets.DEV_DB_PASSWORD }}
          DB_HOST:           ${{ secrets.DEV_DB_HOST }}
          DB_PORT:           ${{ secrets.DEV_DB_PORT }}
        run: |
          {
            echo "DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY"
            echo "DB_ENGINE=$DB_ENGINE"
            echo "DB_NAME=$DB_NAME"
            echo "DB_USER=$DB_USER"
            echo "DB_PASSWORD=$DB_PASSWORD"
            echo "DB_HOST=$DB_HOST"
            echo "DB_PORT=$DB_PORT"
          } > .env
          chmod 600 .env
      - name: Run tests
        run: |
          docker compose up --build -d
          docker compose exec -T web pytest
```
> The runner has the secret values; it writes a throw‑away `.env` used only for that job.

### `deploy_dev.yml`
#### What this does
1. **Rsync** keeps the code on the server in sync with the `dev` branch (no Docker context upload). [Why use?](#why)
2. **Remote script**:
   * *Stops* and removes the current `web` container.  
   * *Builds* the new image (`docker compose build web`).  
   * *Starts* a fresh `web` container (`docker compose up -d web`).  
   * *Prunes* dangling images to save disk space.  
3. **Database** (`db` service) never stops, so data persists.

#### Server prerequisites
* Docker Engine + the v2 Compose plugin (`docker compose`)  
* The directory referenced by `DEV_WORKDIR` already exists and contains your initial clone (or the first workflow run will create it via `rsync`)  
* SSH user is in the `docker` group or can run Docker with `sudo` (adjust the script if you need `sudo docker …`)  

```yaml
---
name: Deploy to Dev

# Trigger on pushes to dev *or* manual dispatch
on:
  push:
    branches: [dev]
  workflow_dispatch:

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: development          # ties to the env‑scoped secrets above
    concurrency: dev_deploy           # prevents overlapping runs
    steps:
      # 1. Checkout code
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      # 2. Start an SSH agent and add the private key
      - name: Add SSH key
        uses: webfactory/ssh-agent@v0.9.0
        with:
          ssh-private-key: ${{ secrets.DEV_SSH_KEY }}
      # 3. Sync project to the dev server (fast incremental deploy)
      - name: Rsync source to server
        run: |
          rsync -az --delete \
            --exclude='.git' \
            --exclude='__pycache__' \
            -e "ssh -o StrictHostKeyChecking=no" \
            ./ ${{ secrets.DEV_SSH_USER }}@${{ secrets.DEV_SSH_HOST }}:${{ secrets.DEV_WORKDIR:-/srv/webapp }}
      # 4. Execute the remote deploy script
      - name: Run remote deploy
        run: |
          ssh -o StrictHostKeyChecking=no \
              ${{ secrets.DEV_SSH_USER }}@${{ secrets.DEV_SSH_HOST }} \
              "cd ${DEV_WORKDIR:-/srv/webapp} && ./scripts/deploy_dev_remote.sh"
```

#### Why the workflow used `rsync`?

| Step                         | Where the code lives        | Notes                                           |
| ---------------------------- | --------------------------- | ----------------------------------------------- |
| `actions/checkout@v4`        | **GitHub runner** workspace | Free, happens automatically                     |
| `rsync … server:/srv/webapp` | **Dev server**              | Copies only changed files, deletes removed ones |

Here're some alternatives (pick the style you like):

|Approach|How it works|Pros|Cons|
|---|---|---|---|
|**Git pull over SSH**|Run `ssh devserver "cd /srv/webapp && git pull"`|No file copy; Git handles diffs|Requires a clone & deploy key on the server; leaves a full Git repo (sometimes unwanted)|
|**Docker image registry**|`docker buildx build --push … my-registry/web:dev` on runner → `ssh` → `docker compose pull web` on server|No source code on server, just images; mirrors prod flow|Need a registry (GHCR, DockerHub); larger network transfer; runner must wait for build & push|
|**`scp` everything**|`scp -r . devserver:/srv/webapp`|Simple|Always copies _all_ files—slow for big repos|
|**`rsync` (current)**|`rsync -az --delete …`|Fast; deletes stale files; no Git repo left behind|Extra dependency (but pre‑installed on most Linux distros)|

So **you can absolutely swap `rsync` out** for a `git pull`, `scp`, or an image‑registry workflow. Pick whichever best matches your infrastructure and comfort level:

```yaml
# Example: replace the rsync step with a simple git pull
- name: Git pull on server
  run: |
    ssh -o StrictHostKeyChecking=no \
        ${{ secrets.DEV_SSH_USER }}@${{ secrets.DEV_SSH_HOST }} \
        "cd ${DEV_WORKDIR:-/srv/webapp} && git pull --ff-only"
```

Just make sure that whatever you choose leaves the up‑to‑date application code (or image) on the development server **before** the remote `docker compose build/up` commands run.

### Considerations on Nginx

#### Option A – Put Nginx only on the *dev‑server compose*
* **Why**: You don’t need Nginx for unit/pytest runs; Django’s test client is enough.  
* **How**: Add the `nginx:` service to the *same* `docker‑compose.yml`, but don’t start or rebuild it in normal deploys unless its config changes.

```yaml
services:
  nginx:
    image: nginx:latest
    ports: ["80:80"]
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - web
```

*Deploy script stays the same* (`docker compose up -d web`).  
If you tweak `nginx.conf`, run `docker compose up -d nginx web` once.

> [!NOTE]
> I'll go with this option just to avoid the unnecessary reload of Ngix when there's no config change.

#### Option B – Separate override file
Keep the base file minimal (`web` + `db`) and create `docker-compose.devserver.yml` containing only Nginx (and maybe tweaks like `restart: always`). On the server:

```bash
docker compose -f docker-compose.yml -f docker-compose.devserver.yml up -d
```

Your **CI workflow** still uses only the base file, so no wasteful Nginx container inside the runner.

If you decide to rebuild/reload Nginx automatically, edit the remote helper script:

```bash
#!/usr/bin/env bash
set -euo pipefail

docker compose stop web                 # leave nginx + db alone
docker compose rm -f web
docker compose build web

# Re‑up both so nginx picks up the new upstream container ID
docker compose up -d web nginx

docker image prune -f --filter "label=stage=development"
echo "✅ Deploy complete."
```

---
