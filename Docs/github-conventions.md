---
title: GitHub Conventions
tags:
  - studies
  - programming
  - best_practices
use: Documentation, Conventions
languages: 
dependences: GitHub
---
<details> <summary>Table of Contents 🔖</summary>

- [#]()

</details>

---
- [i] #to_review : conectar com artigo de conceito, toc, tags
## GitHub Secrets naming convention

|Area|Prefix|Example secret name|Scope|
|---|---|---|---|
|Generic (any)|–|`DJANGO_SECRET_KEY`|**Repository Secret** (default)|
|Environment‑specific|`DEV_`, `STG_`, `PROD_`|`DEV_DB_PASSWORD`|**Environment Secret** (`development`, `staging`, `production`)|
|Third‑party|Tool name|`STRIPE_TEST_SECRET_KEY`|Repository or Environment|

**Why?**
- Upper‑snake‑case is required by GitHub.
- Prefixes (`DEV_`) avoid accidental cross‑environment use.
- Put _high‑risk_ keys (e.g., production payment keys) in an Environment called `production` with branch protection.

### Using the secrets in the workflow
A good example of `secrets` usage is loading them into the `env` context:

```yml
env:
      # Make secrets available to steps *and* to compose
      DJANGO_SECRET_KEY: ${{ secrets.DEV_DJANGO_SECRET_KEY }}
      DB_ENGINE:         ${{ secrets.DEV_DB_ENGINE }}
      DB_NAME:           ${{ secrets.DEV_DB_NAME }}
      DB_USER:           ${{ secrets.DEV_DB_USER }}
      DB_PASSWORD:       ${{ secrets.DEV_DB_PASSWORD }}
      DB_HOST:           ${{ secrets.DEV_DB_HOST }}
      DB_PORT:           ${{ secrets.DEV_DB_PORT }}
```

With this you may think **"but the secrets won't be exposed in the workflow run?"**

> [!NOTE]
> **TL/DR**
> The `env:` block *does* make each secret an **environment variable inside the job’s runner**, but it **doesn’t leak them outside** the job. GitHub Actions applies masking, so any value that exactly matches a secret is replaced with `***` in the logs. As long as you don’t deliberately print the variables (e.g. with `echo $DB_PASSWORD`), they remain private.

### What exactly happens?
1. **Job‑scope only** – Those variables live for the lifetime of the single job on the disposable VM. Parallel jobs or later workflows cannot read them.
2. **Automatic redaction** – If a secret’s literal value appears in stdout/stderr, GitHub substitutes `***`.  
   *Be careful*: tools run with `set -x` or verbose flags may still reveal data in derived forms (base64, JSON, etc.) that masking can’t detect.
3. **No exposure to pull‑requests from forks** – Environment secrets aren’t passed to PRs created from outside the repo unless you explicitly enable “Allow secrets in PRs from forks”.

### Good practices to minimise exposure

| What | Why | How |
|------|-----|-----|
| **Scope secrets to the few steps that need them** | Limits blast‑radius if a later step is compromised | Define `env:` at the *step* level instead of the *job* level. |
| **Never turn on `set -x` or `--debug` while secrets are in scope** | Prevents the shell from echoing commands + args that contain secret values | Use `set +x` before exporting or echoing secrets. |
| **Mask dynamic values** | GitHub masks only the stored secrets, not strings you build from them | `echo "::add-mask::$TOKEN_VALUE"` right after you generate a new token. |
| **Write secrets straight into a file without echoing them** | Avoids accidental log output | ```run: printf "%s\n" "DB_PASSWORD=$DB_PASSWORD" >> .env``` |
| **Tidy up** | Runner is ephemeral, but your remote server isn’t | After rsync/ssh, set restrictive perms (`chmod 600 .env`) or delete the file once Compose has started. |

### Example: tighter step‑level scoping

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: development
	
    steps:
      - uses: actions/checkout@v4
      # ...
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
      # ...
```

Now the secrets exist **only** during the “Generate .env” step and disappear as soon as that step finishes.

The original job‑level `env:` is safe for most internal repos, but scoping secrets narrowly and avoiding verbose command output provides an extra layer of assurance that nothing slips through your logs.

---
